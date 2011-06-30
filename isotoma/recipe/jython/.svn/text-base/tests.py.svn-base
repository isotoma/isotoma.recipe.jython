# encoding: utf-8
#
# Tests for sk.recipe.jython
# 
# Copyright 2010 Sean Kelly and contributors.
# This is licensed software. Please see the LICENSE.txt file for details.

from zope.testing import doctest, renormalizing
import unittest, zc.buildout.tests, zc.buildout.testing, re

_optionFlags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.REPORT_ONLY_FIRST_FAILURE)

def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)
    zc.buildout.testing.install_develop('sk.recipe.jython', test)

def test_suite():
    suite = unittest.TestSuite((
        doctest.DocFileSuite(
            'README.txt',
            setUp=setUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags=_optionFlags,
            checker=renormalizing.RENormalizing([
                (re.compile('--prefix=\S+sample-buildout'), '--prefix=/sample_buildout'),
                (re.compile('\s/\S+sample-buildout'), ' /sample_buildout'),
                zc.buildout.testing.normalize_path,
            ]),
        ),
    ))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
