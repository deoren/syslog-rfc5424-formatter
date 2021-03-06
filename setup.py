#!/usr/bin/env python

from setuptools import setup


setup(
    name="syslog-rfc5424-formatter",
    version="1.0.0",
    author="EasyPost",
    author_email="oss@easypost.com",
    url="https://github.com/easypost/syslog-rfc5424-formatter",
    license="ISC",
    py_modules=['syslog_rfc5424_formatter'],
    keywords=["logging"],
    description="Logging formatter which produces well-formatted RFC5424 Syslog Protocol messages",
    long_description=open('README.md', 'r').read(),
    entry_points={
        'console_scripts': [
            'stdin2epilog = epilog_client.stdin:main',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Topic :: System :: Logging",
    ]
)
