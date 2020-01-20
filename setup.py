from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE.md") as f:
    license = f.read()

setup(
    name="pygti",
    version="0.1.0",
    description="access public transport information in hamburg, germany.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tom Schneider",
    author_email="mail@vigonotion.com",
    url="https://github.com/vigonotion/pygti",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
