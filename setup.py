from setuptools import setup, find_packages

setup(
    name="st-repeating-field-group",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Streamlit plugin for creating repeating field groups",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/st-repeating-field-group",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="streamlit plugin repeating field group",
    install_requires=[
        "streamlit>=0.80.0",
    ],
    python_requires=">=3.7",
)