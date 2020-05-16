#! /usr/bin/env python
from setuptools import setup
import os

if __name__ == "__main__":
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    setup(
        name='kirpputori',
        maintainer='Marijn van Vliet',
        maintainer_email='w.m.vanvliet@gmail.com',
        description='A random collection of algorithms.',
        license='BSD-3',
        url='https://github.com/wmvanvliet/kirpputori',
        version='0.1.dev0',
        download_url='https://github.com/wmvanvliet/kirpputori/archive/master.zip',
        long_description=open('README.rst').read(),
        classifiers=['Intended Audience :: Science/Research',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved',
                     'Programming Language :: Python',
                     'Topic :: Software Development',
                     'Topic :: Scientific/Engineering',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
        platforms='any',
        packages=['kirpputori'],
        install_requires=['numpy', 'scipy'],
    )
