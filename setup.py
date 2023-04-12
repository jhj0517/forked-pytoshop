#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from setuptools.extension import Extension

requirements = [
    'cython==0.28.5',
    'numpy',
]

test_requirements = [
    'pytest'
]


try:
    from Cython.Build import cythonize
except ImportError:
    extensions = []
else:
    extensions = cythonize([
        Extension(
            "pytoshop.packbits",
            ["pytoshop/packbits.pyx"]
        )
    ])


setup(
    name='pytoshop',
    version='1.1.0',
    description="A Python-based library to write Photoshop PSD files",
    long_description="",
    author="Michael Droettboom",
    author_email='mdboom@gmail.com',
    url='https://github.com/mdboom/pytoshop',
    packages=[
        'pytoshop',
        'pytoshop.user'
    ],
    package_dir={'pytoshop':
                 'pytoshop'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='pytoshop',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    ext_modules=extensions
)
