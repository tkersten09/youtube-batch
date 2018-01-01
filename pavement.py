from paver.easy import *

from paver.setuputils import setup

setup(
    name="youtube-batch",
    packages=['youtube_batch/'],
    version="0.2.0",
    author="Thomas Kersten",
    author_email="tkersten09@gmail.com",
    url="https://github.com/tkersten09/youtube-batch",
    license="GNU Public License v3.0",
    install_requires=[
        'youtube-upload', 'google-api-python-client', 'progressbar2'
    ],
    scripts=["bin/youtube-batch"],
    entry_points={
        'console_scripts': ['youtube-batch = youtube_batch.main:run'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=True,
)


@task
@needs('generate_setup', 'minilib')
def build():
    """Build the release"""

    sh('paver bdist_egg')
    sh('paver sdist')

    # Delete temporary directories of the Build
    eggdir = path('.').glob('*.egg-info')
    for p in eggdir:
        p.rmtree()
    path('build').rmtree()

    pass


@task
@needs('generate_setup', 'minilib')
def dev():
    """Install the package in dev mode.

    This means that it installs this package while it stayes in the current
    folder. This way editing code and testing is a lot faster."""

    sh('python setup.py develop')
    pass


# the pass that follows is to work around a weird bug. It looks like
# you can't compile a Python module that ends in a comment.
pass

# the pass that follows is to work around a weird bug. It looks like
# you can't compile a Python module that ends in a comment.
pass
