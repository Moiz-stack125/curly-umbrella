from pathlib import Path
from typing import List

from setuptools import find_packages, setup

EDITABLE_INSTALL = '-e .'


def get_requirements(file_path: str | Path) -> List[str]:
    with open(file_path, encoding='utf-8') as file_obj:
        requirements = [requirement.strip() for requirement in file_obj]

    return [
        requirement
        for requirement in requirements
        if requirement and requirement != EDITABLE_INSTALL
    ]


project_root = Path(__file__).resolve().parent

setup(
    name="mlproject",
    version="0.0.1",
    author="Moiz",
    author_email="mohdmoiz@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(project_root / 'requirements.txt'),
)
