Supported Options
=================

The ``sk.recipe.jython`` recipe supports the following options:

``url``
    (Optional.) URL to a release of Jython.  If not given, defaults to the URL to the
    2.5.1 release_ of Jython.  This URL must point to a Jython installer jar
    file.
``md5sum``
    (Optional.) MD5 hash of the Jython installer mentioned by ``url``.  If
    specified, the downloaded Jython release will be checked against this hash
    and installation will *not* proceed if there's a mismatch.  If both
    ``md5sum`` and ``url`` are missing, then the recipe will check the 2.5.1
    release for its proper MD5 hash, 2ee978eff4306b23753b3fe9d7af5b37.
``java``
    (Optional.) Full path to a Java virtual machine executable.  If not
    specified, the recipe will find one by shell path.  This ``java``
    executable will be invoked to *install* Jython only, not for Jython's
    runtime. Example: ``/usr/java/j2sdk/bin/java``.
``jre``
    (Optional.) Home directory of a Java runtime or development kit used to
    *run* Jython.  Specify this if you wish to have Jython use a separate
    runtime from that of the installer.  Unlike the ``java`` option above, the
    ``jre`` option expects the home directory of a Java runtime; i.e., there
    will be ``bin``, ``lib``, etc., directories in the directory named by this
    option.  Exampe: ``/System/Library/Frameworks/JavaVM.framework/Home``.
``include-parts``
    (Optional.) List of parts to install.  See "Installable Parts" below.  If
    not specified, you'll get a minimal Jython installation, which is more
    than likely what you'll want if you're developing Jython-based
    applications.

All options are optional.  Really.  By default the recipe makes a complete
Jython installation in the Buildout's ``parts/jython`` directory (you can
override the parts directory in the ``[buildout]`` itself).  That means your
recipe can be as simple as::

    [jython]
    recipe = sk.recipe.jython

This recipe exports two values that are handy in other recipes:

``location``
    This exported option identifies where the recipe installed Jython.  You
    can use its value as the JYTHON_HOME environment variable.
``executable``
    This exported option names the path of the ``jython`` executable.  You can
    use this as a Python interpreter, for example with the ``zc.recipe.egg``
    collection of recipes.


Installable Parts
-----------------

Jython consists of a number of parts that comprises an installation.  The
``include-parts`` option specifies which extra parts to include in an
installation (by default, *no* additional parts are installed).  The
additional parts are:

* ``mod``: Library modules.
* ``demo``: Demonstrations and example code.
* ``doc``: Documentation.
* ``src``: Source code to Jython.


Example Usage
=============

For this demonstration, we'll use a fanciful Jython installer jar (actually an
empty file) and Java virtual machine (written in Python) to mimic what the
actual an Jython installer does.  In actuality, it merely echoes the options
given to it.  These files are in the ``testdata`` directory::

    >>> import os.path
    >>> testdata = join(os.path.dirname(__file__), 'testdata')

The file ``java`` is actually an executable Python script, while
``jython-fake.jar`` is an empty file.

Let's create a buildout to build and install Jython::

    >>> write(sample_buildout, 'buildout.cfg', '''
    ... [buildout]
    ... parts = jython
    ...
    ... [jython]
    ... recipe = sk.recipe.jython
    ... java = %(testdata)s/java
    ... url = file://%(testdata)s/jython-fake.jar
    ... ''' % dict(testdata=testdata))

This will "download" the fake Jython installer and install it with all parts.
Running the buildout::

    >>> print system(buildout)
    Installing jython.
    "JVM": Jython installer in file ".../jython-fake.jar"
    "JVM": Installer options: ['--silent', '--directory', '/sample-buildout/parts/jython']
    
And the parts directory should now have Jython installed::

    >>> ls(sample_buildout, 'parts')
    d jython


Using Additional Options
------------------------

Let's exercise the ``jre`` and ``include-parts`` options, specifying a
mythical JRE at ``/usr/mythical/java/j3sdk`` and asking for the documentation
(``doc``) and source code (``src``) to be installed::

    >>> write(sample_buildout, 'buildout.cfg', '''
    ... [buildout]
    ... parts = jython
    ...
    ... [jython]
    ... recipe = sk.recipe.jython
    ... java = %(testdata)s/java
    ... jre = /usr/mythical/java/j3sdk
    ... include-parts =
    ...     doc
    ...     src
    ... url = file://%(testdata)s/jython-fake.jar
    ... ''' % dict(testdata=testdata))

Re-running the buildout now gives us::

    >>> print system(buildout)
    Uninstalling jython.
    Installing jython.
    "JVM": Jython installer in file ".../jython-fake.jar"
    "JVM": Installer options: ['--silent', '--directory', '/sample-buildout/parts/jython', '--jre', '/usr/mythical/java/j3sdk', '--include', 'doc', 'src']

Perfect.


MD5 Hashes
----------

Let's re-write the buildout but inject an error: an incorrect MD5 hash::

    >>> write(sample_buildout, 'buildout.cfg',
    ... '''
    ... [buildout]
    ... parts = jython
    ...
    ... [jython]
    ... recipe = sk.recipe.jython
    ... java = %(testdata)s/java
    ... md5sum = c120503f1e327388bd0b6bbdee530733
    ... url = file://%(testdata)s/jython-fake.jar
    ... ''' % dict(testdata=testdata))

The hash shown above is *not* the correct MD5 for an empty file (which is what
``jython-fake.jar`` is).  Running the buildout should bail::

    >>> print system(buildout)
    Uninstalling jython.
    Installing jython.
    While:
      Installing jython.
    Error: MD5 checksum mismatch...

Specifying the correct MD5::

    >>> write(sample_buildout, 'buildout.cfg',
    ... '''
    ... [buildout]
    ... parts = jython
    ...
    ... [jython]
    ... recipe = sk.recipe.jython
    ... java = %(testdata)s/java
    ... md5sum = d41d8cd98f00b204e9800998ecf8427e
    ... url = file://%(testdata)s/jython-fake.jar
    ... ''' % dict(testdata=testdata))

Makes the problem go away::

    >>> print system(buildout)
    Installing jython.
    "JVM": Jython installer in file ".../jython-fake.jar"
    "JVM": Installer options: ['--silent', '--directory', '/sample-buildout/parts/jython']

That's pretty much it.


.. References:
.. _release: http://sourceforge.net/projects/jython/files/jython/jython_installer-2.5.1.jar
