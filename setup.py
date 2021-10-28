import io
import setuptools

with io.open("README.md", mode="r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="syllab",
    version="0.0.4",
    author="Roman Inozemtsev",
    author_email="dao@mir.one",
    description="Simple Python package for breaking Russian words into syllables",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/mir-one/syllab",
    packages=setuptools.find_packages(),
)
