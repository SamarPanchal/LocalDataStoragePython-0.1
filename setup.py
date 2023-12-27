import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "LocalDataStorage",
    version = "0.1",
    author = "Samar Panchal",
    author_email = "123samarpanchal@gmail.com",
    description = "This Python package creates a file locally in the user's device more easily.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6"
)
