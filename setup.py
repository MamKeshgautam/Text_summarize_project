import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__= "0.0.0"
AUTHOR_NAME= "MAMKESH GAUTAM"
AUTHOR_EMAIL='keshgautam25@gmail.com'
SRC_REPO="textSummarizer"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)