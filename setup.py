import setuptools

setuptools.setup(
    name='pyvjoy',
    version='1.0.1',
    description='Python bindings for vJoy',
    url='https://github.com/maxofbritton/pyvjoy',
    author='Maximilian Britton',
    author_email='maximilian.briton@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    packages=setuptools.find_packages(),
    package_data={'': ['utils/*/*.dll']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pyvjoy=vjoyvevice.__main__:main",
        ]
    }
)