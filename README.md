# dynpaper

1. [About](#about)
2. [How it works](#how-it-works)
3. [Features](#features)
4. [Installation](#installation)
5. [Running](#running)
6. [Contributing](#contributing)
7. [Todo](#to-do)
8. [Acknowledgements](#acknowledgements)

## About  
This project has been inspired by MacOS Mojave's dynamic wallpaper. It has been built with modularity in mind making the addition of desktop environments or wallpaper managers easy. It has been tested on Ubuntu 18.04 on Gnome.

## How it works  
The application calculates the duration of the day and night by finding the time difference between dawn and dusk. Then \'splits\' the time into intervals and assigns a new wallpaper when the intervals have passed. It uses the time provided by the Operating System.

## Features
Compared to the previous iteration, the app does __not__ use ip to find the coordinates and then the dawn and dusk, but relies on the user input, making the app usable both online and offline.  
The app, if the user provides the necessary flags, adds a call to itself to the user provided(or the default) shell configuration file, allowing it to run automatically on login. For reference, the default file is ~/.bashrc and the app will add the following two lines


```sh
#dynpaper
dynpaper  <arguments> &

```

Currently supports:

* Gnome  
* Nitrogen  
* feh


## Installation

```sh
git clone https://github.com/oddProton/dynpaper  
cd dynpaper  
./setup.py install  
```

Download the MacOS Mojave wallpapers and extract them to any folder you'd like.  

## Running
```
usage: dynpaper [-h] [-a] [-f FILE_TEMPLATE] [-s SHELL_CONF] [-r DAWN]
                [-d DUSK] -e {gnome,budgie,nitrogen,feh} [-i INTERVAL]
                [-g FILE_RANGE]

optional arguments:
  -h, --help            show this help message and exit
  -a, --auto-run        Turn flag on to add shell command in your shell config
                        file, default is ~/.bashrc, provide specific with -s
  -f FILE_TEMPLATE, --file-template FILE_TEMPLATE
                        File template for the wallpapers, ex.
                        '~/Pictures/Wallpapers/mojave_dynamic_{}.png', use
                        '{}' to replace the number.
  -s SHELL_CONF, --shell-conf SHELL_CONF
                        The config of the shell you are using, ~/.bash_profile
                        for bash, ~/.zprofile for zsh etc.
  -r DAWN, --dawn DAWN  Dawn/sunrise time, ex. 06:23
  -d DUSK, --dusk DUSK  Dusk/sunset time, ex. 20:23
  -e {gnome,budgie,nitrogen,feh}, --env {gnome,budgie,nitrogen,feh}
                        Your current desktop environment/wallpaper manager.
  -i INTERVAL, --interval INTERVAL
                        Refresh interval in minutes, default = 5.
  -g FILE_RANGE, --file-range FILE_RANGE
                        File index range. Ex (13,17) indicates the files
                        [1,12] inclusive are split throughout the day and the
                        files[13, 16] inclusive are split throughout the
                        night.If you are using apple's wallpapers, don't set
                        it.

```

Most of these are __optional__ arguments and only -e/--env and -f/--file-template, are required.

```sh
dynpaper -f PATH_TO_FILE_WITHOUT_NUMBER -e gnome
```
Example:
```sh
dynpaper -a -f ~/Pictures/Wallpapers/mojave_dynamic_{}.png -s ~/.zprofile -e gnome
```
* `-a` Will add the current configuration to the provided shell config file.  
* `-f` Points to the file with the number replaced by `{}`.  
* `-s` Points to the shell configuration file.  
* `-e` Defines which environment to use to set the wallpaper.  

Now, .zprofile contains the following:

```sh
#dynpaper
dynpaper -f ~/Pictures/Wallpapers/mojave_dynamic_{}.png -e gnome &
```

__Note__: In order to autorun, please point to the appropriate configuration file, `.profile`/`.bash_profile` for bash and `.zprofile` for zsh. 

Dawn and Dusk information are __not__ required. They have default values 06:00 and 20:00 respectively and serve to better integrade with the user's timezone.

## Contributing

* If you have found a bug, simply write an issue, explaining the bug and add the error that occured if possible.
* If you want to include another desktop environment, edit the `PROCESS_CALLS` variable, add a key, to identify the environment and as value add the equivalent call that would set the wallpaper. Replace the file on the call with `{}`.
* If you wish to add some other feature, simply write it and open a pull request.

## To-do

- [ ] Close the subprocess call.
- [ ] Keep only one process running.
- [ ] Expand it so it works with more combinations of wallpapers besides apple's.

## Acknowledgements

Acknowledging Apple for the idea for time based wallpapers.
