import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'appfigures_api',
    version = '0.0.4',
    author = 'Huang Yi-Ming',
    author_email = 'ymhuang@fmbase.tw',
    description = ('A Python API client for AppFigures'),
    license = 'MIT',
    keywords = 'appfigures api',
    url = 'http://packages.python.org/appfigures_api',
    packages=['appfigures_api', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'License :: OSI Approved :: MIT License',
    ],
)