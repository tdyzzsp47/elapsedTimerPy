import setuptools

setuptools.setup(
    name="elapsedTimerPy",
    version="0.0.1",
    author="tdyzzsp47",
    author_email="tdyzzsp47@gmail.com",
    description="elapsedTimerPy is a package that measures the execution time of a python program",
    long_description="elapsedTimerPy is a package that measures the execution time of a python program",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
