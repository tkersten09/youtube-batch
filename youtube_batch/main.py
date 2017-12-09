#!/usr/bin/env python
# 
# Upload videos to Youtube from the command-line using APIv3.
#
# Author: Arnau Sanchez <pyarnau@gmail.com>
# Project: https://github.com/tokland/youtube-upload
"""
Upload all videos in given folder to Youtube from the command-line which.

    $ youtube-batch --endingse="mp4, mpg" \
                     --description="Anne Sophie Mutter plays Beethoven" \
                     --category=Music \
                     --tags="mutter, beethoven" \
                     anne_sophie_mutter.flv
"""

import os
import sys
from pathlib import Path
import optparse
from youtube_upload import lib

class OptionsError(Exception): pass

EXIT_CODES = {
    OptionsError: 2,
    NotImplementedError: 5,
}


def upload_files(path, options):
    """Upload all files in the folders given by using tokland/youtube-upload script."""
    endings = [str(s.strip()) for s in (options.endings or "").split(",")]
    for end in endings:
        p = Path(path).glob('*.'+ end)
        for file in sorted(p):
            #Using the youtube-upload. And an example of the used command line is:
            # youtube-upload --title="Anne Sophie Mutter plays Beethoven" --chunksize="65536" "Anne Sophie Mutter plays Beethoven.mp4"
            string = 'youtube-upload --title="' + str(file.stem) + '" --chunksize="'+ str(options.chunksize) +'" "' + str(file)  + '"'
            #print(string)
            os.system(string)
        
def parse_options_error(parser, options):
    """Check errors in options."""
    required_options = []
    missing = [opt for opt in required_options if not getattr(options, opt)]
    if missing:
        parser.print_usage()
        msg = "Some required option are missing: {0}".format(", ".join(missing))
        raise OptionsError(msg)
        
        
def run_main(parser, options, args, output=sys.stdout):
    """Run the main scripts from the parsed options/args.
       And checks if the given folders exists beforehand."""
    parse_options_error(parser, options)
    #args = [r'E:\Digitalisierte Videos\convert\uploadTest']
    #print("args: {}".format(args))
    
    #Checks if all folders exists
    for index, path in enumerate(args):
        p = Path(path)
        if not p.exists():
            raise OptionsError("{0} does not exists".format(path))
            
    for index, path in enumerate(args):
            #print(path)
            upload_files(path, options)
            
def main(arguments):
    """Define the usage and the options. And then parses the given options/args and give this to run_main()."""
    
    usage = """Usage: %prog [OPTIONS] FOLDER [FOLDER2 ...]

    Uploads all videos in the folders to Youtube."""
    parser = optparse.OptionParser(usage=usage)
    
    #Additional options
    parser.add_option('-e', '--endings', dest='endings', type="string",  default = "mp4",
        help='Video File Endings (separated by commas: "mp4, m4v,...")')
    parser.add_option('', '--chunksize', dest='chunksize', type="int", 
        default = 1024*256, help='Update file chunksize')
    
    #Fixes bug for the .exe in windows: The help will be displayed, when no arguments are given.
    if len(arguments) == 0:
        parser.print_help()
        return 0
    
    options, args = parser.parse_args(arguments)
    
    #print(options)
    
    run_main(parser, options, args)


def run():
    sys.exit(lib.catch_exceptions(EXIT_CODES, main, sys.argv[1:]))
  
if __name__ == '__main__':
    run()
