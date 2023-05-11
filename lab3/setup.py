from setuptools import setup

setup(
    name="json_xml_serializer",
    version="0.1.1",
    description="Library for python (de)serialization in Json and Xml",
    url="https://github.com/panton8/igi-labs/tree/lab3",
    author="Anton Padvalnikau",
    author_email="podvalnikov0@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers"],
    include_package_data=True,
    install_requires=["regex"]
)