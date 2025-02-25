import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
__version__ ="0.1.0"

REPO_NAME = "TextInsight"
AUTHOR_USER_NAME = "tanvibalsara18"
SRC_REPO = "TextInsight"
AUTHOR_EMAIL = "tanvibalsara18@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=requirements,  
    python_requires=">=3.7"    
)
