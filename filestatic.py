#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Static - simple file event-action script.
# Copyright (C) 2017  Ranx

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import configparser
from time import sleep
import filecmp
import shutil
import shlex
try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

CONFIG_FILE_NAME = 'filestatic.ini'


def main():
    config = configparser.RawConfigParser(allow_no_value=True)
    if os.path.isfile(CONFIG_FILE_NAME):
        config.read(CONFIG_FILE_NAME)
    else:
        # Default config
        config['Detection'] = {'files': '',
                               'additional_files': '',
                               'event_type': '',
                               'action': '',
                               'delay': '',
                               'loop': ''}

        with open(CONFIG_FILE_NAME, 'w') as f:
            config.write(f)

        print('Configuration file was created! Configure "%s" and run the program again!' % CONFIG_FILE_NAME)
        any_key()

    files = shlex.split(config.get('Detection', 'files'))
    additional_files = shlex.split(config.get('Detection', 'additional_files'))
    event_type = config.get('Detection', 'event_type')
    action = config.get('Detection', 'action')
    delay = config.getfloat('Detection', 'delay')
    loop = config.getboolean('Detection', 'loop')
    is_looping = True

    if event_type == 'modify':
        while is_looping:
            for file in files:
                additional_file = additional_files[files.index(file)] if len(files) <= len(additional_files) \
                    else additional_files[0] if len(additional_files) > 0 else ''
                if not filecmp.cmp(file, additional_file):
                    perform_action(action, file, additional_file)
                    if not loop:
                        is_looping = False
            sleep(delay)

    elif event_type == 'create':
        while is_looping:
            for file in files:
                additional_file = additional_files[files.index(file)] if len(files) <= len(additional_files) \
                    else additional_files[0] if len(additional_files) > 0 else ''
                if os.path.isfile(file):
                    perform_action(action, file, additional_file)
                    if not loop:
                        is_looping = False
            sleep(delay)

    elif event_type == 'remove':
        while is_looping:
            for file in files:
                additional_file = additional_files[files.index(file)] if len(files) <= len(additional_files) \
                    else additional_files[0] if len(additional_files) > 0 else ''
                if not os.path.isfile(file):
                    perform_action(action, file, additional_file)
                    if not loop:
                        is_looping = False
            sleep(delay)

    elif event_type == 'modify/remove':
        while is_looping:
            for file in files:
                additional_file = additional_files[files.index(file)] if len(files) <= len(additional_files) \
                    else additional_files[0] if len(additional_files) > 0 else ''
                if not os.path.isfile(file) or not filecmp.cmp(file, additional_file):
                    perform_action(action, file, additional_file)
                    if not loop:
                        is_looping = False
            sleep(delay)

    else:
        print('Unknown event type: %s' % event_type)
        any_key()


def exception_handler(exception_type, exception, traceback):
    print('An error occurred during program execution!')
    print('\nError information:')
    print('  Error type: %s' % exception_type)
    print('  Error message: %s' % (exception.message if hasattr(exception, 'message') else str(exception)))
    any_key()


def perform_action(action, file, additional_file):
    if action == 'copy':
        shutil.copy(additional_file, file)
    elif action == 'remove':
        os.remove(file)
    else:
        print('Unknown action: "%s"' % action)
    print('Action performed!')


def any_key():
    print('\nPress any key to exit...')
    getch()
    sys.exit()


sys.excepthook = exception_handler

if __name__ == '__main__':
    main()
