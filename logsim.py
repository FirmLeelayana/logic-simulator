#!/usr/bin/env python3
"""Parse command line options and arguments for the Logic Simulator.

This script parses options and arguments specified on the command line, and
runs either the command line user interface or the graphical user interface.

Usage
-----
Show help: logsim.py -h
Command line user interface: logsim.py -c <file path>
Graphical user interface (English): logsim.py <file path>
Graphical user interface (Thai): logsim.py -t <file path>
Graphical user interface (French): logsim.py -f <file path>
"""
import getopt
import sys
import builtins
import os

import wx

from names import Names
from devices import Devices
from network import Network
from monitors import Monitors
from scanner import Scanner
from parse import Parser
from userint import UserInterface
from gui import Gui


def main(arg_list):
    """Parse the command line options and arguments specified in arg_list.

    Run either the command line user interface, the graphical user interface,
    or display the usage message.
    """
    umessage = ("Usage:\n"
                "Show help: logsim.py -h\n"
                "Command line user interface: logsim.py -c <file path>\n"
                "Graphical user interface (English): logsim.py <file path>\n"
                "Graphical user interface (Thai): logsim.py -t <file path>\n"
                "Graphical user interface (French): logsim.py -f <file path>\n"
                "For Linux or MacOS, you can set LANG=th_TH.UTF-8 (Thai)\n"
                "or LANG=fr_FR.UTF-8 (French) in the terminal and run "
                "logsim.py <file path>\n"
                "Specifying file path is optional")
    try:
        options, arguments = getopt.getopt(arg_list, "hc:t:f:")
    except getopt.GetoptError:
        print("Error: invalid command line arguments\n")
        print(umessage)
        sys.exit()

    # Initialise instances of the four inner simulator classes
    names = Names()
    devices = Devices(names)
    network = Network(names, devices)
    monitors = Monitors(names, devices, network)

    # Supported Languages
    supLang = {u"en_GB.UTF-8": wx.LANGUAGE_ENGLISH,
               u"th_TH.UTF-8": wx.LANGUAGE_THAI,
               u"fr_FR.UTF-8": wx.LANGUAGE_FRENCH, }

    for option, path in options:
        if option == "-h":  # print the usage message
            print(umessage)
            sys.exit()
        elif option == "-c":  # use the command line user interface
            scanner = Scanner(path, names)
            parser = Parser(names, devices, network, monitors, scanner)
            if parser.parse_network():
                # Initialise an instance of the userint.UserInterface() class
                userint = UserInterface(names, devices, network, monitors)
                userint.command_interface()
        elif option == "-t":  # Launch GUI in Thai
            scanner = Scanner(path, names)
            parser = Parser(names, devices, network, monitors, scanner)
            if parser.parse_network():
                app = wx.App()

                # Internationalisation
                builtins._ = wx.GetTranslation
                locale = wx.Locale()
                locale.Init(wx.LANGUAGE_THAI)  # Set language to Thai

                locale.AddCatalogLookupPathPrefix('locale')
                locale.AddCatalog('gui')

                gui = Gui("Logic Simulator", path, names, devices, network,
                          monitors)
                gui.Show(True)
                app.MainLoop()
        elif option == "-f":  # Launch GUI in French
            scanner = Scanner(path, names)
            parser = Parser(names, devices, network, monitors, scanner)
            if parser.parse_network():
                app = wx.App()

                # Internationalisation
                builtins._ = wx.GetTranslation
                locale = wx.Locale()
                locale.Init(wx.LANGUAGE_FRENCH)  # Set language to French

                locale.AddCatalogLookupPathPrefix('locale')
                locale.AddCatalog('gui')

                gui = Gui("Logic Simulator", path, names, devices, network,
                          monitors)
                gui.Show(True)
                app.MainLoop()

    if not options:  # no option given, use the graphical user interface

        if len(arguments) > 1:  # wrong number of arguments
            print("Error: Only one file path required\n")
            print(umessage)
            sys.exit()
        if arguments:   # Try to launch GUI with path
            [path] = arguments
            scanner = Scanner(path, names)
            parser = Parser(names, devices, network, monitors, scanner)
            if parser.parse_network():
                app = wx.App()

                # Internationalisation
                builtins._ = wx.GetTranslation
                locale = wx.Locale()
                # If an unsupported language is requested default to English
                try:
                    lang = os.environ["LANG"]  # Get LANG variable
                except KeyError:
                    lang = None  # Set to None if LANG unset
                if lang in supLang:
                    selLang = supLang[lang]
                else:
                    selLang = wx.LANGUAGE_ENGLISH
                locale.Init(selLang)

                locale.AddCatalogLookupPathPrefix('locale')
                locale.AddCatalog('gui')

                gui = Gui("Logic Simulator", path, names, devices, network,
                          monitors)
                gui.Show(True)
                app.MainLoop()
        else:   # Launch GUI without path
            app = wx.App()

            # Internationalisation
            builtins._ = wx.GetTranslation
            locale = wx.Locale()
            # If an unsupported language is requested default to English
            try:
                lang = os.environ["LANG"]  # Get LANG variable
            except KeyError:
                lang = None  # Set to None if LANG unset
            if lang in supLang:
                selLang = supLang[lang]
            else:
                selLang = wx.LANGUAGE_ENGLISH
            locale.Init(selLang)

            locale.AddCatalogLookupPathPrefix('locale')
            locale.AddCatalog('gui')

            gui = Gui("Logic Simulator", None, names, devices, network,
                      monitors)
            gui.Show(True)
            app.MainLoop()


if __name__ == "__main__":
    main(sys.argv[1:])
