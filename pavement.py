from paver.easy import *
import paver.doctools
from paver.setuputils import setup
from pathlib import Path


setup(
    name="youtube-batch",
    packages=['youtube_batch/',],
    version="0.1.0",
    author="Thomas Kersten",
    author_email="tkersten09@gmail.com",
    install_requires=[
        'youtube_upload',
        'google-api-python-client',
        'progressbar2'
        ],
    scripts= ["bin/youtube-batch"],
    entry_points={
        'console_scripts': [
            'youtube-batch = youtube_batch.main:run'
        ],
    },
)

@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    #eggdir = Path('THz.egg-info')
    #eggdir.rmtree()
    
    pass


# the pass that follows is to work around a weird bug. It looks like
# you can't compile a Python module that ends in a comment.
pass

