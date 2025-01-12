from setuptools import setup, find_packages

setup(
    name="weird-stories",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas==2.2.3',
        'PyYAML==6.0.2',
        'pytest==8.3.4',
        'black==24.10.0',
        'mkdocs==1.6.1',
        'networkx==3.2.1',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive database and analysis tool for weird fiction stories",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/weird-stories",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)