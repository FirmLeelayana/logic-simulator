import pytest
import wx
import builtins
import os


from names import Names
from devices import Devices
from network import Network
from monitors import Monitors
from scanner import Scanner
from parse import Parser
from gui import Gui

# Unit tests for the Gui Class.


def test_build_gui_monitor_dictionary():
    """Test if build_gui_monitor_dictionary() returns
    dictionary with elements 'monitor_name: [list_of_signals]'"""
    names = Names()
    devices = Devices(names)
    network = Network(names, devices)
    monitors = Monitors(names, devices, network)
    path = "example_text_files/example_thirteen.txt"
    scanner = Scanner(path, names)
    parser = Parser(names, devices, network, monitors, scanner)
    assert parser.parse_network()
    app = wx.App()
    # Internationalisation
    builtins._ = wx.GetTranslation
    locale = wx.Locale()
    selLang = wx.LANGUAGE_ENGLISH
    locale.Init(selLang)
    locale.AddCatalogLookupPathPrefix('locale')
    locale.AddCatalog('gui')
    ui = Gui("Logic Simulator", path, names, devices, network,
             monitors)
    monitor_dict = ui.build_gui_monitor_dictionary()
    assert monitor_dict == {'xor1': [], 'and1': []}
