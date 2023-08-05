#!/usr/bin/env python3

from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py3d",
    version="0.0.9",
    description="a 3d library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tumiz",
    author_email="hh11698@163.com",
    python_requires=">=3.5.0",
    url="https://github.com/Tumiz/scenario",
    install_requires=["numpy","tornado"],
    packages=find_packages(),
    py_modules=["py3d","server"],
    data_files=[
        ("/py3d/static",["static/logo.png","static/bundle.js"]),
        ("/py3d",["viewer.html"])
        ],
    license="GPL-3.0 License"
)
