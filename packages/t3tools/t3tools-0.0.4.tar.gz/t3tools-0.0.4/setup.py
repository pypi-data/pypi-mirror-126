#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='t3tools',
    version='0.0.4',
    description=(
        '实用工具 from 唐峰2098'
    ),
    # long_description=open('README.rst').read(),
    long_description='common tools from tangfeng2098.',
    author='唐峰',
    author_email='tangfeng2098@outlook.com',
    maintainer='唐峰',
    maintainer_email='tangfeng2098@outlook.com',
    license='MIT License',
    # packages=find_packages(),
    packages=['common'],
    platforms=["all"],
    url='http://null.null.null',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
