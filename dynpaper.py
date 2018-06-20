#!/usr/bin/env python3

import argparse
import subprocess
import os.path
import time
from sys import argv
import datetime
import socket
import wallpaper
import indexer
import timing
import backends


VERSION = '1.2.1'

def get_version():
    return VERSION


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--auto-run',
                        default=False, action='store_const', const=True, help='Turn flag on to add\
                         shell command in your shell config file, default is ~/.profile, provide specific with -s')
    parser.add_argument('-f', '--file-template',
                        action='store', type=str, help='File template for the wallpapers,\
                         ex. \'~/Pictures/Wallpapers/mojave_dynamic_{}.png\', use \'{}\' to replace the number.')
    parser.add_argument('-s', '--shell-conf', action='store', default='~/.profile',
                        help='The config of the shell you are using, ~/.profile for bash, ~/.zprofile for zsh etc.')
    parser.add_argument('-r', '--dawn', action='store',
                        default='06:00', help='Dawn/sunrise time, ex. 06:23')
    parser.add_argument('-d', '--dusk', action='store',
                        default='20:00', help='Dusk/sunset time, ex. 20:23')
    parser.add_argument(
        '-e', '--env', choices=backends.PROCESS_CALLS.keys(), required=True, help='Your current desktop environment/wallpaper manager.')
    parser.add_argument('-i', '--interval', action='store', type=int,
                        default=5, help='Refresh interval in minutes, default = 5.')

    parser.add_argument(
        '-g', '--file-range', action='store', default='(13,17)', help='File index range. Ex (13,17) indicates the files [1,12]\
         inclusive are split throughout the day and the files[13, 16] inclusive are split throughout the night.If you are using\
          apple\'s wallpapers, don\'t set it.')

    args = parser.parse_args(argv[1:])

    err_range(args)
    err_dusk_dawn(args)
    err_set_auto(args)
    err_wallpapers(args)
    err_interval(args)

    return args


def err_interval(args):
    try:
        if not isinstance(args.interval, int):
            raise ValueError
        if args.interval < 1:
            raise ValueError
    except:
        print('Interval needs to be an integer greater than 1')


def err_range(args):
    try:
        args.file_range = eval(args.file_range)
        if not isinstance(args.file_range, tuple):
            raise ValueError
        if args.file_range[0] > args.file_range[1]:
            raise ValueError
        if not isinstance(args.file_range[0], int):
            raise ValueError
        if not isinstance(args.file_range[1], int):
            raise ValueError
    except:
        print(
            'Invalid format specified, please use x,y or (x,y) where x<y, x,y are integers.')
        exit(-1)


def err_wallpapers(args):
    for i in range(1, args.file_range[1]):
        file = args.file_template.format(i)
        if not os.path.isfile(file):
            print('File:{} does not exist.'.format(file))
            exit(-1)


def err_set_auto(args):
    if not args.auto_run:
        return

    if not os.path.isfile(args.shell_conf):
        print('Shell config file:{} doesn\'t exist.'.format(args.shell_conf))
        exit(-1)


def err_dusk_dawn(args):

    dawn_time = timing.time_string_to_float(args.dawn)
    if isinstance(dawn_time, str):
        print('Dawn time is invalid, err: {}'.format(dawn_time))
        exit(-1)

    dusk_time = timing.time_string_to_float(args.dusk)
    if isinstance(dusk_time, str):
        print('Dusk time is invalid, err: {}'.format(dusk_time))
        exit(-1)

    if timing.time_string_to_float(args.dawn) > timing.time_string_to_float(args.dusk):
        print('Dawn can\'t be after dusk.')
        exit(-1)

def acquire_lock():
    __socket = socket.socket(
        socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        __socket.bind('\0'+'dynpaper')
    except socket.error:
        print('Already running.')
        exit(-1)
    return __socket


def main():
    __socket = acquire_lock()
    args = arguments()
    if args.auto_run:
        backends.add_to_shell(args, argv)

    args.dawn = timing.time_string_to_float(args.dawn)
    args.dusk = timing.time_string_to_float(args.dusk)

    index = indexer.get_index(args)

    while True:
        wallpaper.set_wallpaper(args)
        while index == indexer.get_index(args):
            time.sleep(60 * args.interval)
        index = indexer.get_index(args)


if __name__ == '__main__':
    main()
