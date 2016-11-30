from __future__ import print_function

from setuptools import setup

import qlikreader

setup(
    name='qlikreader',
    version=qlikreader.__version__,
    url='https://github.com/rh-marketingops/qlikreader',
    license='GNU General Public License',
    author='Pramod Toraskar',
    #tests_require=[],
    #install_requires=[],
    author_email='',
    description='',
    #long_description=readme(),
    packages=['qlikreader'],
    include_package_data=True,
    package_dir={'':'qlikreader'},
    platforms='any',
    #test_suite = 'nose.collector',
    install_requires=[
        'retrying==1.3.3',
        'selenium==2.53.6',
        'six==1.10.0'
    ],
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