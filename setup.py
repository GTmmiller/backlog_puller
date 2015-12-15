# Based off the setup.py from https://github.com/pypa/sampleproject

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='backlog_puller',
    version='1.0.0',

    description='A python module for pulling data from a backloggery account in a variety of different formats',
    long_description=long_description,

    url='https://github.com/GTmmiller/backloggery-puller',

    author='Steven Miller',
    author_email='msm@gatech.edu',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',

        'Topic :: Games/Entertainment',
        'Topic :: Internet'
    ],

    keywords='video games backlog puller',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'backlog_pull=backlog_puller.__main__:main',
        ],
    },
)
