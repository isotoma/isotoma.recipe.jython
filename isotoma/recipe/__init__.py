# encoding: utf-8
# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
#
# sk.recipe namespace declarartion for sk.recipe.jython
# 
# Copyright 2010 Sean Kelly and contributors.
# This is licensed software. Please see the LICENSE.txt file for details.

'''Namespace ``recipe`` for recipes for Buildout.'''

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
