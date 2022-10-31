from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_image_processing_DiO",
    version="0.0.1",
    author="Vitor Souza",
    author_email="vitorugo_kta@hotmail.com",
    description="Test version Image processing package using skimage. This project belongs to Karina Tiemi Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitorhssouza/package_image_processing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.3',
)