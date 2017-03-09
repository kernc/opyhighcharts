#!/usr/bin/env python3

from setuptools import find_packages, setup

VERSION = '0.1.0'


def _discover_tests():
    import unittest
    return unittest.defaultTestLoader.discover('opyhighcharts.tests',
                                               pattern='test_*.py',
                                               top_level_dir='.')


if __name__ == '__main__':
    setup(
        name='opyhighcharts',
        version=VERSION,
        description='A thin wrapper for Highcharts JS',
        long_description=
            'A thin Qt WebKit/WebEngine wrapper for Highcharts JS. '
            'In addition to the specified requirements, it depends also on '
            'the interface as provided by '
            '`Orange.widgets.utils.webview.WebviewWidget` available to import'
            'from `__opyhighcharts_interfaces.WebviewWidget`.',
        author='Michael Jackson',
        url='https://github.com/biolab/opyhighcharts',
        license='CC-BY-NC-3.0',
        setup_requires=[
            'setuptools_git >= 0.3',
        ],
        install_requires=[
            'AnyQt',
            'numpy',
        ],
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        test_suite='setup._discover_tests',
        keywords=[
            'visualization',
            'javascript',
            'charts',
            'scatter plot',
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Programming Language :: Python',
            'Programming Language :: JavaScript',
            'License :: Free for non-commercial use'
            'Topic :: Scientific/Engineering :: Visualization',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
        ],
    )
