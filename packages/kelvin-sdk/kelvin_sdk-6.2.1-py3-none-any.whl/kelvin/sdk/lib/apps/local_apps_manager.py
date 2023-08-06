"""
Copyright 2021 Kelvin Inc.

Licensed under the Kelvin Inc. Developer SDK License Agreement (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

http://www.kelvininc.com/developer-sdk-license

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
"""

from typing import Optional

from click import Abort

from kelvin.sdk.lib.apps.apps_migration_manager import migrate_app_configuration
from kelvin.sdk.lib.configs.internal.docker_configs import DockerConfigs
from kelvin.sdk.lib.configs.internal.general_configs import GeneralConfigs
from kelvin.sdk.lib.datatypes.datatypes_manager import setup_datatypes
from kelvin.sdk.lib.models.apps.kelvin_app import ApplicationLanguage
from kelvin.sdk.lib.models.apps.ksdk_app_configuration import ApplicationFlavour, ProjectType
from kelvin.sdk.lib.models.apps.ksdk_app_setup import (
    BridgeAppBuildingObject,
    DockerAppBuildingObject,
    KelvinAppBuildingObject,
    ProjectCreationParametersObject,
)
from kelvin.sdk.lib.models.factories.app_setup_configuration_objects_factory import (
    get_bridge_app_building_object,
    get_kelvin_app_building_object,
    get_project_building_object,
)
from kelvin.sdk.lib.models.factories.docker_manager_factory import get_docker_manager
from kelvin.sdk.lib.models.factories.project.factory import ProjectFactory
from kelvin.sdk.lib.models.generic import KPath, NameWithVersion
from kelvin.sdk.lib.models.ksdk_docker import DockerImageNameDetails
from kelvin.sdk.lib.models.operation import OperationResponse
from kelvin.sdk.lib.models.types import EmbeddedFiles
from kelvin.sdk.lib.schema.schema_manager import validate_app_schema_from_app_config_file
from kelvin.sdk.lib.templates.templates_manager import get_embedded_file
from kelvin.sdk.lib.utils.application_utils import check_if_app_name_is_valid, check_if_app_name_with_version_is_valid
from kelvin.sdk.lib.utils.logger_utils import logger
from kelvin.sdk.lib.utils.version_utils import assess_docker_image_version


# 1 - entrypoint functions
def app_create_from_wizard() -> OperationResponse:
    """
    The entry point for the creation of an application. (WizardTree)

    Usually initiated when no parameters are provided.

    - Creates the directory that will contain the app app.
    - Creates all necessary base files for the development of the app.

    Returns
    -------
    OperationResponse
        an OperationResponse object wrapping the result of the creation of the application.

    """
    from kelvin.sdk.lib.utils.cli_wizard_utils import start_app_creation_wizard

    try:
        project_creation_parameters = start_app_creation_wizard()
        return project_create(project_creation_parameters=project_creation_parameters)
    except Abort:
        error_message = "Application Wizard cancelled"
        logger.warning(error_message)
        return OperationResponse(success=True, log=error_message)
    except Exception as exc:
        error_message = f"Error processing wizard input parameters: {str(exc)}"
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


def app_create_from_parameters(
    app_dir: str,
    app_name: Optional[str],
    app_description: Optional[str],
    app_type: Optional[ProjectType],
    app_flavour: Optional[ApplicationFlavour],
    kelvin_app_lang: Optional[ApplicationLanguage],
) -> OperationResponse:
    """
    The entry point for the creation of an application. (Parameters)

    - Creates the directory that will contain the app app.
    - Creates all necessary base files for the development of the app.

    Parameters
    ----------
    app_dir: str
        the app's targeted dir. Will contain all the application files.
    app_name: str, optional
        the name of the new app.
    app_description: str, optional
        the description of the new app.
    app_type: ProjectType, optional
        the type of the new application. # E.g. 'docker', 'kelvin'.
    app_flavour: ApplicationFlavour, optional
        the flavour of the new application. # E.g. 'default', 'injector', 'extractor'.
    kelvin_app_lang: ApplicationLanguage, optional
        the language the new app will be written on. For kelvin apps only. # E.g. python.

    Returns
    ----------
    OperationResponse
        an OperationResponse object wrapping the result of the creation of the application.
    """
    from kelvin.sdk.lib.models.apps.ksdk_app_setup import ProjectCreationParametersObject

    try:
        project_creation_parameters = ProjectCreationParametersObject(
            app_dir=app_dir,
            app_name=app_name,
            app_description=app_description,
            app_type=app_type,
            app_flavour=app_flavour,
            kelvin_app_lang=kelvin_app_lang,
        )
        return project_create(project_creation_parameters=project_creation_parameters)
    except Exception as exc:
        app_creation_error_parsing_parameters: str = f"""{str(exc)}.
                \n
                Proceeding with wizard.
        """
        logger.exception(app_creation_error_parsing_parameters)
        return app_create_from_wizard()


def project_create(project_creation_parameters: ProjectCreationParametersObject) -> OperationResponse:
    """
    The entry point for the creation of an application. (Parameters)

    - Creates the directory that will contain the app app.
    - Creates all necessary base files for the development of the app.

    Parameters
    ----------
    project_creation_parameters: ProjectCreationParametersObject
        the object containing all the required variables for App creation.

    Returns
    ----------
    OperationResponse
        an OperationResponse object wrapping the result of the creation of the application.
    """
    try:
        check_if_app_name_is_valid(app_name=project_creation_parameters.app_name)

        from kelvin.sdk.lib.session.session_manager import session_manager

        session_manager.login_client_on_current_url()
        project_class_name: str = project_creation_parameters.app_type.project_class_name()

        logger.info(f'Creating new {project_class_name} "{project_creation_parameters.app_name}"')

        # 1 - Create the base directory and app creation object
        project = ProjectFactory.create_project(project_creation_parameters=project_creation_parameters)
        project.create_dirs_and_files()

        app_creation_success_message: str = (
            f'Successfully created new {project_class_name}: "{project_creation_parameters.app_name}".'
        )
        if project_creation_parameters.app_type == ProjectType.kelvin:
            app_creation_success_message = f"""{app_creation_success_message}

            Continue its configuration using \"studio\". Refer to \"kelvin studio --help\" for more information."""
        logger.relevant(app_creation_success_message)

        return OperationResponse(success=True, log=app_creation_success_message)
    except Exception as exc:
        error_message = ""
        if project_creation_parameters:
            app_name = project_creation_parameters.app_name
            error_message = f'Error creating "{app_name}" project: {str(exc)}'
            logger.exception(error_message)
            if project_creation_parameters.app_dir and app_name:
                app_complete_directory = KPath(project_creation_parameters.app_dir) / app_name
                app_complete_directory.delete_dir()
        return OperationResponse(success=False, log=error_message)


def project_build(
    app_dir: str, fresh_build: bool = False, build_for_upload: bool = False, upload_datatypes: bool = False
) -> OperationResponse:
    """
    The entry point for the building of an application.

    Attempts to read the application content

    Parameters
    ----------
    app_dir : str
        the path where the application is hosted.
    fresh_build : bool
        If specified will remove any cache and rebuild the application from scratch.
    build_for_upload : bool
        indicates whether or the package object aims for an upload.
    upload_datatypes : bool
        If specified, will upload locally defined datatypes.

    Returns
    -------
    OperationResponse
        an OperationResponse object wrapping the result of the application build process.

    """
    try:
        from kelvin.sdk.lib.session.session_manager import session_manager

        session_manager.login_client_on_current_url()

        base_app_building_object = get_project_building_object(app_dir=app_dir, fresh_build=fresh_build)

        app_type = base_app_building_object.app_config_model.app.type
        app_name = base_app_building_object.app_config_model.info.name

        logger.info(f"Assessing basic {app_type.project_class_name()} info..")

        validate_app_schema_from_app_config_file(app_config=base_app_building_object.app_config_raw)

        if app_type == ProjectType.kelvin:
            logger.info(f'Building "Kelvin type" application "{app_name}"')
            kelvin_app_building_object = get_kelvin_app_building_object(
                app_dir=app_dir,
                app_config_raw=base_app_building_object.app_config_raw,
                build_for_upload=build_for_upload,
                upload_datatypes=upload_datatypes,
                fresh_build=fresh_build,
            )
            return _build_kelvin_app(kelvin_app_building_object=kelvin_app_building_object)

        elif app_type == ProjectType.bridge:
            logger.info(f'Building "Bridge type" application "{app_name}"')
            bridge_app_building_object = get_bridge_app_building_object(
                app_dir=app_dir,
                app_config_raw=base_app_building_object.app_config_raw,
                build_for_upload=build_for_upload,
                upload_datatypes=upload_datatypes,
                fresh_build=fresh_build,
            )
            return _build_kelvin_app(kelvin_app_building_object=bridge_app_building_object)

        elif app_type == ProjectType.docker:
            logger.info(f'Building "Docker type" application "{app_name}"')
            docker_app_building_object = DockerAppBuildingObject(**base_app_building_object.dict())
            return _build_docker_app(docker_app_building_object=docker_app_building_object)

        return OperationResponse(success=True, log=f"Project {app_name} successfully built")
    except Exception as exc:
        error_message = f"""Error building application: {str(exc)}

            Consider building the app in verbose mode to retrieve more information: --verbose
        """
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


def app_migrate(app_dir: str) -> OperationResponse:
    """
    Migrate the application configuration to the new schema version.

    Parameters
    ----------
    app_dir: str
        the path to the application that requires migrate.

    Returns
    ----------
    OperationResponse
        an OperationResponse object wrapping the result of the application migration process.

    """
    try:
        logger.info("Migrating application configuration to the latest version.")

        output_file_path = KPath(app_dir) / GeneralConfigs.default_migrated_app_config_file

        migrate_app_configuration(app_dir_path=app_dir, output_file_path=output_file_path)

        app_migrate_success: str = f"""Application successfully migrated.
            New configuration successfully output to:
                {output_file_path}
        """
        logger.relevant(app_migrate_success)
        return OperationResponse(success=True, log=app_migrate_success)

    except Exception as exc:
        error_message = f"Error migrating application: {str(exc)}"
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


def app_image_unpack(
    app_name_with_version: str,
    output_dir: str,
    container_app_dir: str = DockerConfigs.container_app_dir_path,
    clean_dir: bool = True,
) -> OperationResponse:
    """
    Extract the content of an application from its built image.

    Parameters
    ----------
    app_name_with_version: str
        the name of the image to unpack the app from.
    output_dir: str
        the output directory to output the application content.
    container_app_dir: str
        the directory from which to extract the application content.
    clean_dir: str
        clean the directory before extracting into it.

    Returns
    ----------
    OperationResponse
        an OperationResponse object wrapping the result of the application image unpack operation.

    """
    try:
        # 1 - Build the DockerImageNameDetails object for the application
        docker_manager = get_docker_manager()
        docker_image_name_details: DockerImageNameDetails = DockerImageNameDetails(
            docker_image_name=app_name_with_version, registry_url=docker_manager.logged_registry_url
        )

        # 2 - Find the provided application. If it does not exist, attempt to retrieve the registry's counterpart
        application_name: str = docker_manager.assess_docker_image_name(
            docker_image_name_details=docker_image_name_details, is_external_app=False
        )

        logger.info(f'Unpacking application "{application_name}" to directory "{output_dir}"')

        app_was_unpacked = docker_manager.unpack_app_from_docker_image(
            app_name=application_name,
            output_dir=output_dir,
            container_app_dir=container_app_dir,
            clean_dir=clean_dir,
        )

        success_message: str = ""
        if app_was_unpacked:
            success_message = f'Application "{application_name}" successfully unpacked to "{output_dir}"'
            logger.relevant(success_message)

        return OperationResponse(success=True, log=success_message)

    except Exception as exc:
        error_message = f"Error unpacking application: {str(exc)}"
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


def app_image_remove(app_name_with_version: str) -> OperationResponse:
    """
    Remove the specified application from the existing image list (in the docker instance).

    Parameters
    ----------
    app_name_with_version: str
        the app to be removed. Must include the version.

    Returns
    ----------
    OperationResponse
        an OperationResponse object wrapping the result of the application image removal operation.

    """
    try:
        check_if_app_name_with_version_is_valid(app_name_with_version=app_name_with_version)

        application_name = NameWithVersion(name=app_name_with_version)

        logger.info(f'Removing packaged application "{application_name.full_name}"')

        docker_manager = get_docker_manager()
        docker_manager.remove_docker_image(docker_image_name=application_name.full_name)

        success_message = f'Successfully removed application: "{application_name.full_name}"'
        logger.relevant(success_message)

        return OperationResponse(success=True, log=success_message)

    except Exception as exc:
        error_message = f"Error removing application: {str(exc)}"
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


def app_image_config(
    app_name_with_version: str, output_dir: str, image_dir: str = DockerConfigs.container_app_config_file_path
) -> OperationResponse:
    """
    Extract the app configuration file (app.yaml) from a built image into a specific directory.

    Parameters
    ----------
    app_name_with_version: str
        the name of the image to unpack the app configuration file from.
    output_dir: str
        the output directory to output the app configuration file.
    image_dir: str
        the directory from which to extract the application configuration file.

    Returns
    --------
    OperationResponse
        an OperationResponse object wrapping the result of the application configuration extraction operation.

    """
    try:
        # 1 - Build the DockerImageNameDetails object for the application
        docker_manager = get_docker_manager()
        docker_image_name_details = DockerImageNameDetails(
            docker_image_name=app_name_with_version, registry_url=docker_manager.logged_registry_url
        )

        # 2 - Find the provided application. If it does not exist, attempt to retrieve the registry's counterpart
        application_name: str = docker_manager.assess_docker_image_name(
            docker_image_name_details=docker_image_name_details, is_external_app=False
        )

        logger.info(f'Extracting "{application_name}"\'s configuration file to directory "{output_dir}"')

        app_config_was_unpacked = docker_manager.unpack_app_from_docker_image(
            app_name=application_name, output_dir=output_dir, container_app_dir=image_dir
        )

        success_message: str = ""
        if app_config_was_unpacked:
            success_message = f'Configuration file of "{application_name}" successfully extracted to "{output_dir}"'
            logger.relevant(success_message)

        return OperationResponse(success=True, log=success_message)

    except Exception as exc:
        error_message = f"Error extracting application configuration: {str(exc)}"
        logger.exception(error_message)
        return OperationResponse(success=False, log=error_message)


# 2 - internal, utils methods
def _build_docker_app(docker_app_building_object: DockerAppBuildingObject) -> OperationResponse:
    """
    The entry point for the building of a 'Docker' type application.

    Parameters
    ----------
    docker_app_building_object : DockerAppBuildingObject
        the ProjectBuildingObject that contains all necessary variables to build a docker app.

    Returns
    -------
    OperationResponse
        an OperationResponse object wrapping the result of whether the Docker application was successfully built.

    """
    docker_manager = get_docker_manager()

    app_name = docker_app_building_object.app_config_model.info.name

    build_result = docker_manager.build_docker_app_image(docker_build_object=docker_app_building_object)
    result_message = f'Image successfully built: "{app_name}"'
    logger.relevant(result_message)

    return OperationResponse(success=build_result, log=result_message)


def _build_kelvin_app(kelvin_app_building_object: KelvinAppBuildingObject) -> OperationResponse:
    """
    The entry point for the building of a kelvin-type application.

    Package the kelvin application using a KelvinAppBuildingObject, thus building a valid docker image.

    Parameters
    ----------
    kelvin_app_building_object : KelvinAppBuildingObject
        the object that contains all the required variables to build an app.

    Returns
    -------
    OperationResponse
        an OperationResponse object wrapping the result of whether the kelvin application was successfully built.

    """
    docker_manager = get_docker_manager()

    # 1 - Retrieve the variables necessary to build the application
    app_name = kelvin_app_building_object.full_docker_image_name
    app_build_dir_path = kelvin_app_building_object.app_build_dir_path
    app_config_file_path = kelvin_app_building_object.app_config_file_path
    app_dir_path = kelvin_app_building_object.app_dir_path
    app_build_dir_path.delete_dir().create_dir()

    # 2 - Setup the application datatypes (if there are any)
    datatype_dir_path = setup_datatypes(kelvin_app_building_object=kelvin_app_building_object)
    kelvin_app_building_object.app_datatype_dir_path = datatype_dir_path
    kelvin_app_building_object.build_for_datatype_compilation = bool(datatype_dir_path)

    logger.debug(f'Provided configuration file path: "{app_config_file_path}"')
    logger.debug(f'Provided application directory: "{app_dir_path}"')

    # 3 - Build the dockerfile and proceed to build the image
    docker_manager.build_kelvin_app_dockerfile(kelvin_app_building_object=kelvin_app_building_object)
    # 3.1 - Setup the broker configuration
    if not kelvin_app_building_object.build_for_upload:
        docker_manager.setup_kelvin_broker_configuration(
            app_name=kelvin_app_building_object.app_config_model.info.name,
            target_output_directory=app_build_dir_path,
            app_config_file_path=app_config_file_path,
            project_type=kelvin_app_building_object.app_config_model.app.type,
        )
    # 3.2 - Override the .dockerignore file. May be removed by August 2021
    dockerignore_contents = get_embedded_file(embedded_file=EmbeddedFiles.DOCKERIGNORE).render()
    dockerignore_file_path = KPath(app_dir_path / GeneralConfigs.default_dockerignore_file).expanduser().resolve()
    dockerignore_file_path.write_content(content=dockerignore_contents)

    # 3.3 - Finally, build the image
    success_build = docker_manager.build_kelvin_app_docker_image(kelvin_app_building_object=kelvin_app_building_object)
    logger.relevant(f'Image successfully built: "{app_name}"')

    # 4 - Once built, access whether the application base image is compliant with the latest version and warn the user.
    kelvin_app = kelvin_app_building_object.app_config_model.app.app_type_configuration
    app_lang = kelvin_app.language.type if kelvin_app else None

    assess_docker_image_version(
        current_docker_image=kelvin_app_building_object.kelvin_app_runner_image,
        app_lang=ApplicationLanguage(app_lang),
        reduced_size=kelvin_app_building_object.reduced_size_kelvin_app_runner_image,
    )
    return OperationResponse(success=success_build)
