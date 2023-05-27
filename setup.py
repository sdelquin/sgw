# read the contents of your README file
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

REQUIREMENTS = (
    'sendgrid==5.3.0',
    'markdown==3.4.3',
)

setup(
    name='sgw',
    version='1.2.2',
    url='https://github.com/sdelquin/sgw.git',
    author='Sergio Delgado Quintero',
    author_email='sdelquin@gmail.com',
    description='Wrapper made in Python for sendgrid',
    packages=['sgw'],
    install_requires=REQUIREMENTS,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
