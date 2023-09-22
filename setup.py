from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='0.0.1',
    description='A Python package for customized Encoder/Decoder',
    author='Yijia Ma',
    packages=find_packages(
        where='src',
        include=['jsonapi']
    ),
    package_dir={"": "src"},
    install_requires=[
        'importlib-metadata; python_version == "3.9"',
    ],
)