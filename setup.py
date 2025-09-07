from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='devangm2005-jpg',
    author_email='devangm2005@gmail.com',
    packages=find_packages(where="src"),  # 👈 tell setuptools to look inside src
    package_dir={"": "src"},              # 👈 root package dir is src/
    install_requires=get_requirements('requirements.txt')
)