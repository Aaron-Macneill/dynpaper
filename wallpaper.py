# Functions dealing with wallpapers


import subprocess
from indexer import get_index
from backends import PROCESS_CALLS

def set_wallpaper(args):
    index = get_index(args)
    subprocess.Popen(PROCESS_CALLS[args.env].format(
        args.file_template.format(index)), shell=True)
