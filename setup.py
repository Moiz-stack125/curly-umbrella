from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
# IMPORTANT,DO SOME RESEARCH ABOUT THESE THINGS SEEMS IMPORTANT
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements = [requirement.strip() for requirement in file_obj]

    return [
        requirement
        for requirement in requirements
        if requirement and requirement != HYPEN_E_DOT
    ]

setup(
    name="mlProject",
    version="0.0.1",
    author="Moiz",
    author_email="mohdmoiz@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
