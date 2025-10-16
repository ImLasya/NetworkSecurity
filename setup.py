'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''


from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Reads the requirements.txt file and returns a list of dependencies."""
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="lasya",
    author_email="lasyapriyaneelisetty0310@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
                