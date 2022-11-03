from setuptools import find_packages,setup

setup(
    name='Sensor',
    version="0.0.1",
    author='Ruchi Yadav',
    author_email='Ruchii22yadav22@gmail.com',
    packages=find_packages(),
    install_requires=["pymongo== 4.2.0"],
)