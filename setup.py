"""Drone Designer module set up."""

from pathlib import Path

from setuptools import find_packages, setup

_root = Path(__file__).parent

setup(
    name="dronedesigner",
    version="0.1.0",
    url="https://github.com/b-r-y/dronedesigner",
    author="b-r-y",
    description="Python toy tool for drone design.",
    packages=find_packages(include=["dronedesigner", "dronedesigner.*"]),
    install_requires=[
        "ipywidgets >= 8.1.5",
        "ipykernel >= 6.29.5",
        "ruamel.yaml >= 0.18.10",
        "sphinx_rtd_theme >= 3.0.1",
    ],
)
