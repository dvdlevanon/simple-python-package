from setuptools import setup

setup(
    name='simple-python-package',
    version='0.0.2',
    packages=['examplepackage'],
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
)
