from setuptools import setup

setup(
    name="sgw",
    version="1.0.1",
    url="https://github.com/sdelquin/sgw.git",
    author="Sergio Delgado Quintero",
    author_email="sdelquin@gmail.com",
    description="Wrapper made in Python for sendgrid",
    packages=["sgw"],
    install_requires=["sendgrid"],
)
