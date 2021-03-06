import setuptools

metadata = {
    "name": "hugebrain16",
    "version": "1.2.1",
    "author": "HugeBrain16",
    "author_email": "joshtuck373@gmail.com",
    "url": "https://github.com/hugebrain16-pack",
    "description": "my personal packages",
    "long_description": open("README.md", "r", encoding="UTF-8").read(),
    "long_description_content_type": "text/markdown",
    "license": "MIT",
    "packages": setuptools.find_packages(),
}

setuptools.setup(**metadata)
