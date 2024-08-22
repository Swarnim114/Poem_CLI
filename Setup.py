from setuptools import setup, find_packages

setup(
    name="poemcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "poemcli=poemcli.main:main",
        ],
    },
)
