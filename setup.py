# Setup code for git auto-commit and auto pr message generator

from setuptools import find_packages
from setuptools import setup

setup(
    name="git-auto-post",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "pygithub"],
    entry_points={
        "console_scripts": [
            "git-auto-post = src.main:main",
        ],
    },
)
