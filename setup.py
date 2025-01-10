#whenever we bwant to create a package and host it on the pypi website 
#we need to have all the following set up code 

import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
__version__="0.0.0"

REPO_NAME=" Chicken-Disease-Classification-"
AUTHOR_USER_NAME="Nilayaa11"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="nilayahuddar@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN App",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
