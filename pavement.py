from paver.defaults import *

import paver.doctools
import paver.virtual
import paver.setuputils

options(
    setup=Bunch(
	    name='PackageManager',
	    version="0.0.1",
	    description='Package Manager',
	    author='Bertrand Cachet',
	    author_email='bertrand.cachet@gmail.com',
	    url='http://code.google.com/p/winlibre',
	    packages=['pacman'],
	    install_requires=[],
	    test_suite='nose.collector',
	    zip_safe=False,
    ),

    sphinx=Bunch(
        builddir="build",
        sourcedir="source"
    ),
    
	virtualenv=Bunch(
		packages_to_install=['virtualenv', 'elementtree', 'elements', 'sphinx', 'nose', 'pylint', 'django'],
		install_paver=False,
		script_name='bootstrap.py',
		paver_command_line=None
    ),

)

if paver.virtual.has_virtualenv:
    @task
    def bootstrap():
        """Build a virtualenv bootstrap for developing paver."""
        paver.virtual._create_bootstrap(options.script_name,
										options.packages_to_install,
										options.paver_command_line,
#										options.install_paver
										)

import os
def rm_files(arg, dirname, names):
    for filename in names:
        filename = os.path.join(dirname,filename)
        if os.path.isfile(filename):
            if os.path.splitext(filename)[1] in arg:
                os.remove(filename)

@task
def clean():
    path("build").rmtree()
    import os
    for package in options.setup.packages:
        dir = package.replace('.', os.path.sep)
        os.path.walk(dir, rm_files, ['.pyc'])
        os.path.walk(dir, rm_files, ['.py~'])
    os.path.walk('tests', rm_files, ['.pyc'])
    os.path.walk('tests', rm_files, ['.py~'])

@task
def doc_clean():
    """Cleans up generated documentation. Remove the docs/build directory."""
    docdir = path("docs") / "build"
    docdir.rmtree()
    docdir = path("docs") / ".build"
    docdir.rmtree()
    docdir = path(options.setup.name) / "docs"
    docdir.rmtree()

@task
@needs(["clean", "doc_clean"])
def dist_clean():
    """Cleans up this paver directory. Removes the virtualenv traces, build directory and generated docs"""
    path(".Python").remove()
    path(".coverage").remove()
    path("%s.egg-info" % options.setup.name).rmtree()
    path("bin").rmtree()
    path("lib").rmtree()
    path("include").rmtree()
