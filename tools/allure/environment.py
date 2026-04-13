import sys
import platform

from config import settings


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    os_info = [f'os_info={platform.system()}, {platform.release()}']
    python_version = [f'python_version={sys.version}']

    properties = '\n'.join([*items, *os_info, *python_version])

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)

