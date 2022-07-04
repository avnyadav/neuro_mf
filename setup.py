import os

from setuptools import setup, find_packages
from pathlib import Path
from typing import List

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

PROJECT_NAME = "model_factory"
VERSION = "0.0.1"
AUTHOR = "Avnish Yadav"
DESCRIPTION = """
    Model Factory helps us to generate model training and grid search code automatically based 
    on configuration provided.
    """
REQUIREMENT_FILE_NAME = os.path.join(this_directory,"requirements.txt")
HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    print(os.listdir("."))
    print(f"{os.getcwd()}Is file available->{os.path.exists(REQUIREMENT_FILE_NAME)}")
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=get_requirements_list(),
    long_description=long_description,
    long_description_content_type='text/markdown',
)
