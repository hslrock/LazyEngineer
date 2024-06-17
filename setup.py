from setuptools import find_packages
from setuptools import setup

setup(
    name="lazyengineer",
    version="0.1.0",
    description="",
    author="LEE HYUN SEUNG",
    author_email="hslrock@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "setuptools>=70.0.0",
        "black>=24.4.2",
        "isort>=5.13.2",
        "flake8>=7.1.0",
        "pre-commit>=3.7.1",
        "mypy>=1.10.0",
        "flake8-pyproject>=1.2.3",
        "requests>=2.32.3",
        "openai>=1.34.0",
        "google-cloud-aiplatform>=1.55.0",
        "pydantic>=2.7.4",
        "pydantic-settings>=2.3.3",
        "google-generativeai>=0.6.0",
        "jinja2>=3.1.4",
    ],
    entry_points={
        "console_scripts": [
            "lazyengineer=src.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
