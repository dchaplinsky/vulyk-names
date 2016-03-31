#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pip.req import parse_requirements

with open('README.rst') as readme_file:
    readme = readme_file.read()

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = requirements


setup(
    name='vulyk_names',
    version='0.1.0',
    description="Vulyk names plugin",
    long_description=readme,
    author="Dmitry Chaplinsky",
    author_email='chaplinsky.dmitry@gmail.com',
    url='https://github.com/dchaplinsky/vulyk-names',
    packages=[
        'vulyk_names',
        'vulyk_names.models',
        'vulyk_names.static',
        'vulyk_names.views'
    ],
    package_dir={'vulyk_names':
                 'vulyk_names'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='vulyk_names',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
