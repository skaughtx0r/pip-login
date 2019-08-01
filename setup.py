import json
from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="pip_login",
    version="0.0.1",
    py_modules=["pip_login"],
    short_description="Utility to log into private pypi repositories",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=["keyring", "prompt_toolkit", "pip>=19.2.1"],
    entry_points={"console_scripts": ["pip-login = pip_login:main"]},
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
