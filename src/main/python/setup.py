from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))

setup(
name='hokiegeek2',

version='0.0.1',

description='collection of raspberrypi applications',

author='hokiegeek2',

author_email='hokiegeek2@gmail',

url='https://github.com/hokiegeek2/raspberrypi-projects',

packages=find_packages(exclude=['contrib', 'docs', 'tests']),

install_requires=['RPi.GPIO']
)
