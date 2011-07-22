# encoding: utf-8
#
# Distribute metadata for sk.recipe.jython
# 
# Copyright 2010 Sean Kelly and contributors.
# This is licensed software. Please see the LICENSE.txt file for details.

from setuptools import setup, find_packages
import os.path

_name = 'isotoma.recipe.jython'
_desc = 'A recipe for Buildout (zc.buildout) to install Jython'
_version = '0.0.7'
_keywords = 'buildout jython installation automation'
_url, _downloadURL = 'http://github.com/isotoma/isotoma.recipe.jython', ''
_author, _authorEmail = 'Tom Wardill', 'tom.wardill@isotoma.com'
_license = 'BSD'
_namespaces = ['isotoma', 'isotoma.recipe']
_entryPoints = {
    'zc.buildout': [
        'default = %s:Recipe' % _name,
        'install = %s:Recipe' % _name,
    ]
}
_zipSafe = True
_testSuite = '%s.tests.test_suite' % _name
_requirements = [
    'setuptools',
    'zc.buildout >=1.2.0',
]
_testRequirements = [
    'zope.testing',
]
_classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Framework :: Buildout',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Libraries :: Java Libraries',
]

def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDesc = '\n\n'.join([
    _header,
    _read('README.txt'),
    _read('docs', 'INSTALL.txt'),
    _read('isotoma', 'recipe', 'jython', 'README.txt'),
    _read('docs', 'HISTORY.txt'),
])
open('doc.txt', 'w').write(_longDesc)

setup(
    author=_author,
    author_email=_authorEmail,
    classifiers=_classifiers,
    description=_desc,
    download_url=_downloadURL,
    entry_points=_entryPoints,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_longDesc,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages(exclude=['ez_setup']),
    tests_require=_testRequirements,
    test_suite=_testSuite,
    url=_url,
    version=_version,
    zip_safe=_zipSafe,
)
