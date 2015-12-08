from os.path import expanduser
import argparse


class Launcher(object):
    
    def __init__(self, name, icon, bin_file, file_name):
        """
        Constructor
        """
        self.name      = name
        self.icon      = icon
        self.bin_file   = bin_file
        self.file_name  = file_name
                
    def create_file(self):
        """
        Create a file on directory
        ~/.local/share/applications
        """
        user_home = expanduser("~")
        file_path = "%s/.local/share/applications/%s.desktop" % (user_home, self.file_name)
        my_file = open(file_path, 'w')
        
        content = """
#!/usr/bin/env xdg-open

[Desktop Entry]

Version=1.0

Type=Application

Terminal=false

StartupNotify=true

Icon=%s

Name=%s

Exec=env UBUNTU_MENUPROXY=0 %s
""" % (self.icon, self.name, self.bin_file)
        
        my_file.write(content)
        my_file.close()
        
        print(content)
        
"""
Get args and create a launcher
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Testing args')

    parser.add_argument('--name', action = 'store', dest = 'name',
                        default = 'No name', required = True,
                        help = 'Program description')

    parser.add_argument('--icon', action = 'store', dest = 'icon',
                        default = '', required = True,
                        help = 'Path to icon')

    parser.add_argument('--bin', action = 'store', dest = 'bin',
                        default = '', required = True,
                        help = 'Path to executable file')

    parser.add_argument('--file', action = 'store', dest = 'file',
                        default = '', required = True,
                        help = 'File file_name.desktop to create')

    args = parser.parse_args()

    name = args.name
    icon = args.icon
    bin_file = args.bin
    file_name = args.file

    l = Launcher(name, icon, bin_file, file_name)
    l.create_file()
