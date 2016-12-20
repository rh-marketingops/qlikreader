from __future__ import print_function

from setuptools import setup, Extension

import qlikreader

setup(

    name='qlikreader',
    version=qlikreader.__version__,
    author='Pramod Toraskar',
    author_email='',
    url='https://github.com/rh-marketingops/qlikreader',

    install_requires=[
        'retrying==1.3.3',
        'selenium==2.53.6',
        'six==1.10.0'
    ],

    packages=['qlikreader'],

    package_dir={'xvfb': ''},

    #ext_modules=[Extension('xvfb', ['Xvfb.x'])],

    include_package_data=True,

    license='GNU General Public License',

    platforms='any',

    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 0 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
        ],

    keywords='marketing automation data qlikview',

    zip_safe=False
)
