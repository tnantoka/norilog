import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
    name='norilog',
    version='1.0.0',
    long_description=read_file('README.rst'),
    packages=find_packages(),
    author='tnantoka',
    author_email='tnantoka@bornneet.com',
    url='https://github.com/tnantoka/norilog',
    include_package_data=True,
    install_requires=[
        'Flask'
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """
)
