from setuptools import setup, find_packages

setup(
    name="ascibar",
    version="0.1.0",
    packages=find_packages(),
    description="A Lightweight Python library for creating customizable ASCII-based progress bars in terminal applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="mouhamaddev",
    author_email="mouhamaddev04@gmail.com",
    url="https://github.com/mouhamaddev/ascibar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
