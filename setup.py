from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='imcsv',
    packages=find_packages(include=['imcsv']),
    version='0.0.1',
    description='In-Memory CSV file creator',
    author='Kwabena Asante',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaypee90/imcsv",
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)