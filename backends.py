# Funcions interacting with other miscellaneous parts of the system


PROCESS_CALLS = {
    'gnome': "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{}",
    'budgie': "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{}",
    'nitrogen': "nitrogen --set-auto {}",
    'feh': "feh --bg-scale {}",
}



def add_to_shell(args, argv):

    argv = [x for x in argv[1:] if x not in {
        '-s', '--shell-conf', args.shell_conf, '-a', '--auto-run'}]

    runf = "dynpaper "
    for arg in argv:
        runf = runf+' {}'.format(arg)
    runf = runf + ' &\n'

    with open(args.shell_conf, 'r') as fp:
        content = fp.readlines()
        fp.close()

    if '#dynpaper\n' in content:
        index = content.index('#dynpaper\n')
        if index == len(content):
            content.append(runf)
        else:
            content[index + 1] = runf
    else:
        content.append('#dynpaper\n')
        content.append(runf)

    with open(args.shell_conf, 'w') as fp:
        fp.writelines(content)
        fp.close()

    return
