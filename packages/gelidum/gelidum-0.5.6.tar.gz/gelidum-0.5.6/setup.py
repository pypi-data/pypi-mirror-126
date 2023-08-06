import os
from setuptools import setup, find_packages

root_dir_path = os.path.dirname(os.path.abspath(__file__))

long_description = open(os.path.join(root_dir_path, "README.md")).read()
version = open(os.path.join(root_dir_path, "version.txt")).read()

requirements_path = os.path.join(root_dir_path, "requirements.txt")
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="gelidum",
    version=version,
    author="Diego J. Romero López",
    author_email="diegojromerolopez@gmail.com",
    description="Freeze your python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=requirements,
    license="MIT",
    keywords="freeze python object",
    url="https://github.com/diegojromerolopez/gelidum",
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    scripts=[]
)
