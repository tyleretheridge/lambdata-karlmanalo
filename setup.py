# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-karlmanalo", # the name that you will install via pip
    version="1.4",
    author="Karl Manalo",
    author_email="karlmanalo@comcast.net",
    description="Practice package index",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/karlmanalo/lambdata-karlmanalo",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)