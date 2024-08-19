import sys

from setuptools import find_packages, setup

NAME = "llm_server"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="FastAPI",
    author_email="",
    url="",
    keywords=["OpenAPI", "FastAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"": ["openapi/openapi.yaml"]},
    include_package_data=True,
    entry_points={"console_scripts": ["llm_server=llm_server.__main__:main"]},
    long_description="A server that performs queries on LLMs.",
)
