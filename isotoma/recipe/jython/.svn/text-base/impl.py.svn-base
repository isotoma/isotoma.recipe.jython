# encoding: utf-8
#
# sk.recipe.jython implementation
# 
# Copyright 2010 Sean Kelly and contributors.
# This is licensed software. Please see the LICENSE.txt file for details.

'''Jython installer recipe for Buildout: implementation.'''

import logging, os, os.path, zc.buildout, subprocess
from zc.buildout.download import Download

_defaultURL = 'http://sourceforge.net/projects/jython/files/jython/jython_installer-2.5.1.jar'
_defaultMD5 = '2ee978eff4306b23753b3fe9d7af5b37'

class Recipe(object):
    '''This is a Buildout recipe that automates the installation of Jython.'''
    def __init__(self, buildout, name, options):
        '''Initialize the recipe.'''
        self.buildout, self.name, self.options = buildout, name, options

        # Check options: if neither md5sum or url are given, we use default values for both.
        # However, if only md5sum is given, that's nonsensical; insist on having the URL as well.
        # Lastly, if only url is given, don't fall back to our default MD5, which is valid
        # only for our default Jython installer.
        if 'md5sum' in options and 'url' not in options:
            raise zc.buildout.UserError('You must specify the "url" to a Jython installer when specifying the "md5sum" of it.')
        if 'md5sum' not in options and 'url' in options:
            defaultMD5 = ''
        else:
            defaultMD5 = _defaultMD5

        # Set up options and export our "location" and "executable".
        options['location']   = os.path.join(buildout['buildout']['parts-directory'], name)
        options['executable'] = os.path.join(options['location'], 'bin', 'jython')
        options['url']        = options.get('url', _defaultURL).strip()
        options['md5sum']     = options.get('md5sum', defaultMD5).strip()
        options['java']       = options.get('java', 'java').strip()
        options['jre']        = options.get('jre', '').strip()

        # The include-parts option supports multiple values.
        self.parts = []
        for i in options.get('include-parts', '').splitlines():
            if i.strip():
                self.parts.append(i)
    def install(self):
        '''Install Jython.'''
        logger = logging.getLogger(self.name)
        downloader = Download(self.buildout['buildout'], namespace='sk.recipe.jython', logger=logger)
        url, md5sum = self.options['url'], self.options['md5sum']
        if len(md5sum) == 0:
            md5sum = None
        installerPath, isInstallerTemporary = downloader(url, md5sum)
        java, jre, destination = self.options['java'], self.options['jre'], self.options['location']
        if not os.path.isdir(destination):
            os.makedirs(destination)
        args = [java, '-jar', installerPath, '--silent', '--directory', destination]
        if jre:
            args.extend(['--jre', jre])
        if len(self.parts) > 0:
            args.append('--include')
            args.extend(self.parts)
        rc = subprocess.call(args)
        if rc != 0:
            raise SystemError('Jython installer return nonzero (%d) status; invoked with %r' % (rc, args))
        return destination
    def update(self):
        '''Update Jython. No update facility is provided, though.'''
        pass
    # No custom uninstall required
