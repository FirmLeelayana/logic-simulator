"""Test the parse module."""
import pytest

from names import Names
from network import Network
from devices import Devices
from monitors import Monitors
from scanner import Symbol, Scanner
from parse import Parser


@pytest.fixture
def check_valid_device_parser():
    """Return a Parser instance using check_valid_device.txt"""
    path = "parse_example_text_files/check_valid_device.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def check_valid_device_parser_errors():
    """Return a Parser instance using check_valid_device_errors.txt"""
    path = "parse_example_text_files/check_valid_device_errors.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def assign_device_parser():
    """Return a Parser instance using assign_device.txt"""
    path = "parse_example_text_files/assign_device.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def assign_device_edge_parser():
    """Return a Parser instance using assign_device.txt"""
    path = "parse_example_text_files/assign_device_edge.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def assign_device_parser_errors():
    """Return a Parser instance using assign_device_errors.txt"""
    path = "parse_example_text_files/assign_device_errors.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def check_device_semantics_parser():
    """Return a Parser instance using check_device_semantics.txt"""
    path = "parse_example_text_files/check_device_semantics.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def device_list_parser():
    """Return a Parser instance using device_list.txt"""
    path = "parse_example_text_files/device_list.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def device_list_errors_parser():
    """Return a Parser instance using device_list_errors.txt"""
    path = "parse_example_text_files/device_list_errors.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def device_list_errors_two_parser():
    """Return a Parser instance using device_list_errors_two.txt"""
    path = "parse_example_text_files/device_list_errors_two.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def device_list_errors_three_parser():
    """Return a Parser instance using device_list_errors_three.txt"""
    path = "parse_example_text_files/device_list_errors_three.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def signame_parser():
    """Return a Parser instance using signame.txt"""
    path = "parse_example_text_files/signame.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def signame_errors_parser():
    """Return a Parser instance using signame_errors.txt"""
    path = "parse_example_text_files/signame_errors.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_parser():
    """Return a Parser instance using connection.txt"""
    path = "parse_example_text_files/connection.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_error_parser():
    """Return a Parser instance using connection_error.txt"""
    path = "parse_example_text_files/connection_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_semantics_parser():
    """Return a Parser instance using check_connection_semantics.txt"""
    path = "parse_example_text_files/check_connection_semantics.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_list_parser():
    """Return a Parser instance using connection_list.txt"""
    path = "parse_example_text_files/connection_list.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_list_error_parser():
    """Return a Parser instance using connection_list_error.txt"""
    path = "parse_example_text_files/connection_list_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def connection_list_error_two_parser():
    """Return a Parser instance using connection_list_error_two.txt"""
    path = "parse_example_text_files/connection_list_error_two.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def monitor():
    """Return a Parser instance using monitor.txt"""
    path = "parse_example_text_files/monitor.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def monitor_error():
    """Return a Parser instance using monitor_error.txt"""
    path = "parse_example_text_files/monitor_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def check_monitor_semantics_parser():
    """Return a Parser instance using check_monitor_semantics.txt"""
    path = "parse_example_text_files/check_monitor_semantics.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def monitor_list_parser():
    """Return a Parser instance using monitor_list.txt"""
    path = "parse_example_text_files/monitor_list.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def monitor_list_error_parser():
    """Return a Parser instance using monitor_list_error.txt"""
    path = "parse_example_text_files/monitor_list_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def monitor_list_error_two_parser():
    """Return a Parser instance using monitor_list_error_two.txt"""
    path = "parse_example_text_files/monitor_list_error_two.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def empty_monitor_list_parser():
    """Return a Parser instance using empty_monitor_list.txt"""
    path = "parse_example_text_files/empty_monitor_list.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def adder_parser():
    """Return a Parser instance using single_bit_adder.txt"""
    path = "full_example_text_files/single_bit_adder.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def adder_parser_error():
    """Return a Parser instance using single_bit_adder_error.txt"""
    path = "full_example_text_files/single_bit_adder_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def adder_parser_error_two():
    """Return a Parser instance using single_bit_adder_error_two.txt"""
    path = "full_example_text_files/single_bit_adder_error_two.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def adder_parser_error_three():
    """Return a Parser instance using single_bit_adder_error_three.txt"""
    path = "full_example_text_files/single_bit_adder_error_three.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def adder_parser_error_four():
    """Return a Parser instance using single_bit_adder_error_four.txt"""
    path = "full_example_text_files/single_bit_adder_error_four.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def missing_stopping_symbols():
    """Return a Parser instance using missing_stopping_symbols.txt"""
    path = "full_example_text_files/missing_stopping_symbols.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def catastrophic_error_parser():
    """Return a Parser instance using catastrophic_error.txt"""
    path = "full_example_text_files/catastrophic_error.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def inputs_missing_parser():
    """Return a Parser instance using inputs_missing.txt"""
    path = "parse_example_text_files/inputs_missing.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def missing_lists_parser():
    """Return a Parser instance using missing_lists.txt"""
    path = "parse_example_text_files/missing_lists.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


@pytest.fixture
def empty_text_parser():
    """Return a Parser instance using empty.txt"""
    path = "parse_example_text_files/empty.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    return Parser(new_names, new_devices, new_network,
                  new_monitors, new_scanner)


def test_initialisation_raises_exceptions():
    """Test if initialisation raises expected exceptions."""
    path = "parse_example_text_files/assign_device.txt"
    new_names = Names()
    new_scanner = Scanner(path, new_names)
    new_devices = Devices(new_names)
    new_network = Network(new_names, new_devices)
    new_monitors = Monitors(new_names, new_devices, new_network)
    with pytest.raises(TypeError):
        Parser(new_devices, new_devices, new_network,
               new_monitors, new_scanner)
    with pytest.raises(TypeError):
        Parser(new_names, new_names, new_network,
               new_monitors, new_scanner)
    with pytest.raises(TypeError):
        Parser(new_names, new_devices, new_names,
               new_monitors, new_scanner)
    with pytest.raises(TypeError):
        Parser(new_names, new_devices, new_network,
               new_names, new_scanner)
    with pytest.raises(TypeError):
        Parser(new_names, new_devices, new_network,
               new_monitors, new_names)


def test_display_error_raises_exceptions(check_valid_device_parser):
    """Test if display_error raises expected exceptions."""
    my_symbol = Symbol()
    with pytest.raises(TypeError):
        check_valid_device_parser.display_error('3', my_symbol)
    with pytest.raises(TypeError):
        check_valid_device_parser.display_error(3, 50)
    with pytest.raises(TypeError):
        check_valid_device_parser.display_error(3, my_symbol, 3)
    error_code_count = check_valid_device_parser.names.error_code_count + 1
    with pytest.raises(ValueError):
        check_valid_device_parser.display_error(error_code_count, my_symbol)
    with pytest.raises(ValueError):
        check_valid_device_parser.display_error(-5, my_symbol)


def test_check_valid_device(check_valid_device_parser):
    """Test if check_valid_device gives expected output for valid syntax."""
    parser = check_valid_device_parser
    parser.symbol = parser.scanner.get_symbol()
    # Check if XOR device is correct.
    assert parser.check_valid_device() == ("XOR", None)
    parser.symbol = parser.scanner.get_symbol()
    # Check if DTYPE device is correct.
    assert parser.check_valid_device() == ("DTYPE", None)
    parser.symbol = parser.scanner.get_symbol()
    # Check if AND device is correct.
    assert parser.check_valid_device() == ("AND", 2)
    parser.symbol = parser.scanner.get_symbol()
    # Check if NAND device is correct.
    assert parser.check_valid_device() == ("NAND", 10)
    parser.symbol = parser.scanner.get_symbol()
    # Check if OR device is correct.
    assert parser.check_valid_device() == ("OR", 3)
    parser.symbol = parser.scanner.get_symbol()
    # Check if NOR device is correct.
    assert parser.check_valid_device() == ("NOR", 3)
    parser.symbol = parser.scanner.get_symbol()
    # Check if SWITCH device is correct.
    assert parser.check_valid_device() == ("SWITCH", 1)
    parser.symbol = parser.scanner.get_symbol()
    # Check if CLOCK device is correct.
    assert parser.check_valid_device() == ("CLOCK", 4)
    parser.symbol = parser.scanner.get_symbol()
    # Check if SIGGEN device is checked correctly.
    assert parser.check_valid_device() == ("SIGGEN", "-___-")


def test_check_valid_device_errors(check_valid_device_parser_errors, capsys):
    """Test if check_valid_device gives expected output for invalid syntax."""
    parser = check_valid_device_parser_errors

    # First line of text file.
    parser.symbol = parser.scanner.get_symbol()
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Invalid device type\nsomething ;\n    ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Second line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_two = "Line 2: Syntax Error: Expected a '(' sign"
    line_2 = "\nSWITCH - ;\n       ^\n"
    assert captured.out == line_two + line_2
    capsys.readouterr()

    # Third line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_three = "Line 3: Syntax Error: Expected 'initial_state'"
    line_3 = "\nSWITCH (- ;\n        ^\n"
    assert captured.out == line_three + line_3
    capsys.readouterr()

    # Fourth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_four = "Line 4: Syntax Error: Expected a ':' sign"
    line_4 = "\nSWITCH (initial_state- ;\n                     ^\n"
    assert captured.out == line_four + line_4
    capsys.readouterr()

    # Fifth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_five = "Line 5: Syntax Error: Expected an integer value"
    line_5 = "\nSWITCH (initial_state:- ;\n                      ^\n"
    assert captured.out == line_five + line_5
    capsys.readouterr()

    # Sixth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_six = "Line 6: Syntax Error: Expected a ')' sign"
    line_6 = "\nSWITCH (initial_state:1- ;\n                       ^\n"
    assert captured.out == line_six + line_6
    capsys.readouterr()

    # Seventh line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_seven = "Line 7: Syntax Error: Expected a '(' sign"
    line_7 = "\nAND -;\n    ^\n"
    assert captured.out == line_seven + line_7
    capsys.readouterr()

    # Eighth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_eight = "Line 8: Syntax Error: Expected 'number_of_inputs'"
    line_8 = "\nAND (-;\n     ^\n"
    assert captured.out == line_eight + line_8
    capsys.readouterr()

    # Ninth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_nine = "Line 9: Syntax Error: Expected a ':' sign"
    line_9 = "\nAND(number_of_inputs-;\n                    ^\n"
    assert captured.out == line_nine + line_9
    capsys.readouterr()

    # Tenth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_ten = "Line 10: Syntax Error: Expected an integer value"
    line_10 = "\nAND (number_of_inputs:-;\n                      ^\n"
    assert captured.out == line_ten + line_10
    capsys.readouterr()

    # Eleventh line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_eleven = "Line 11: Syntax Error: Expected a ')' sign"
    line_11 = "\nAND  (number_of_inputs  :  2-;"
    line_11_extra = "\n                            ^\n"
    assert captured.out == line_eleven + line_11 + line_11_extra
    capsys.readouterr()

    # Twelfth line of text file.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line_twelve = "Line 12: Syntax Error: Expected 'cycle'"
    line_12 = "\nCLOCK (-;\n       ^\n"
    assert captured.out == line_twelve + line_12
    capsys.readouterr()

    # Check if SIGGEN raises correct errors.
    # Missing left bracket.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 13: Syntax Error: Expected a '(' sign"
    line_cont = "\nSIGGEN asd;\n        ^\n"
    assert captured.out == line + line_cont
    capsys.readouterr()
    # Missing 'waveform'.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 14: Syntax Error: Expected 'waveform'"
    line_cont = "\nSIGGEN (-;\n        ^\n"
    assert captured.out == line + line_cont
    capsys.readouterr()
    # Missing ':'.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 15: Syntax Error: Expected a ':' sign"
    line_cont = "\nSIGGEN (waveform-;\n                ^\n"
    assert captured.out == line + line_cont
    capsys.readouterr()
    # Missing LOGIC.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 16: Syntax Error: Expected logic levels (underscores "
    line_cont = "and dashes)\nSIGGEN (waveform:asd;\n                  ^\n"
    assert captured.out == line + line_cont
    capsys.readouterr()
    # Missing right bracket.
    assert parser.check_valid_device() == (None, None)
    captured = capsys.readouterr()
    line = "Line 17: Syntax Error: Expected a ')' sign"
    line_cont = "\nSIGGEN (waveform:-_-some;\n                     ^\n"
    assert captured.out == line + line_cont
    capsys.readouterr()


def test_assign_device(assign_device_parser, capsys):
    """Test if assign_device gives expected output for valid syntax."""
    parser = assign_device_parser

    # Add test cases for valid devices.
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(6):
        parser.assign_device()
        captured = capsys.readouterr()
        assert captured.out == ''

    # Check if devices are made properly.
    assert len(parser.devices.devices_list) == 6
    [DTYPE_ID, AND_ID, NOR_ID, SWITCH_ID, CLOCK_ID,
     SIGGEN_ID] = parser.names.lookup(["DTYPE", "AND", "NOR",
                                       "SWITCH", "CLOCK", "SIGGEN"])
    assert parser.devices.devices_list[0].device_kind == DTYPE_ID
    assert parser.devices.devices_list[1].device_kind == AND_ID
    assert len(parser.devices.devices_list[1].inputs) == 2
    assert parser.devices.devices_list[2].device_kind == NOR_ID
    assert len(parser.devices.devices_list[2].inputs) == 3
    assert parser.devices.devices_list[3].device_kind == SWITCH_ID
    assert parser.devices.devices_list[3].switch_state == 1
    assert parser.devices.devices_list[4].device_kind == CLOCK_ID
    assert parser.devices.devices_list[4].clock_half_period == 4
    # Check if siggen device initialised correctly.
    assert parser.devices.devices_list[5].device_kind == SIGGEN_ID
    assert parser.devices.devices_list[5].siggen_period == 3
    assert parser.devices.devices_list[5].siggen_waveform == [1, 2, 3]
    assert parser.devices.devices_list[5].siggen_counter == 0
    assert parser.devices.devices_list[5].initial_state == 1


def test_assign_device_edge(assign_device_edge_parser, capsys):
    """Test if assign_device gives expected output for bad formatting."""
    parser = assign_device_edge_parser

    # Add test cases for valid devices.
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(5):
        parser.assign_device()
        captured = capsys.readouterr()
        assert captured.out == ''

    # Check if devices are made properly.
    assert len(parser.devices.devices_list) == 5
    [DTYPE_ID, AND_ID, NOR_ID, SWITCH_ID,
     CLOCK_ID] = parser.names.lookup(["DTYPE", "AND", "NOR",
                                      "SWITCH", "CLOCK"])
    assert parser.devices.devices_list[0].device_kind == DTYPE_ID
    assert parser.devices.devices_list[1].device_kind == AND_ID
    assert len(parser.devices.devices_list[1].inputs) == 2
    assert parser.devices.devices_list[2].device_kind == NOR_ID
    assert len(parser.devices.devices_list[2].inputs) == 3
    assert parser.devices.devices_list[3].device_kind == SWITCH_ID
    assert parser.devices.devices_list[3].switch_state == 1
    assert parser.devices.devices_list[4].device_kind == CLOCK_ID
    assert parser.devices.devices_list[4].clock_half_period == 4


def test_assign_device_errors(assign_device_parser_errors, capsys):
    """Test if assign_device gives expected output for invalid syntax."""
    parser = assign_device_parser_errors

    # Check that invalid devices give correct errors.
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(5):
        parser.assign_device()
    captured = capsys.readouterr()

    # Missing device name.
    line_1 = "Line 1: Syntax Error: Expected a device name"
    line_1_cont = "\n, = XOR;\n^\n"

    # Missing equals sign.
    line_2 = "Line 2: Syntax Error: Expected an '=' sign"
    line_2_cont = "\nxor1 , XOR;\n     ^\n"
    line_3 = "Line 3: Syntax Error: Expected an '=' sign"
    line_3_cont = "\nxor1 XOR;\n      ^\n"

    # Check_valid_device returns an error.
    line_4 = "Line 4: Syntax Error: Expected a ':' sign\nsw1 = SWITCH ("
    line_4_cont = "initial_state- ;\n                           ^\n"

    # Missing semi-colon. Should print pointer after the symbol.
    line_5 = "Line 5: Syntax Error: Expected a ';' sign"
    line_5_cont = "\nXOR1 = XOR\n          ^\n"
    assert captured.out == (line_1 + line_1_cont + line_2 + line_2_cont
                            + line_3 + line_3_cont + line_4 + line_4_cont
                            + line_5 + line_5_cont)

    # Check that no devices are made.
    assert parser.devices.devices_list == []


def test_assign_device_semantic_errors(check_device_semantics_parser, capsys):
    """Test if assign_device gives expected output for semantic errors."""
    parser = check_device_semantics_parser
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(7):
        parser.assign_device()
        parser.error_count = 0
    captured = capsys.readouterr()

    # Test for Semantic Errors.
    line_1 = "Line 1: Semantic Error: Invalid use of"
    line_1_cont = " reserved keyword as a name.\n"
    line_2 = "CLOCK = AND (number_of_inputs:2) # Use of "
    line_3 = "Reserved Keyword #;\nLine 3: Semantic Error: Device already"
    line_3_cont = " exists in the device list\n"
    line_4 = "sw1 = SWITCH (initial_state:0) # Device Present #;\n"
    line_5 = "Line 5: Semantic Error: Device already exists in "
    line_5_cont = "the device list\nsiggen1 = SIGGEN (waveform:-_-);\n"
    line_6 = "Line 6: Semantic Error: Invalid use of reserved keyword "
    line_6_cont = "as a name.\nSIGGEN = AND (number_of_inputs:2);\n"
    line_7 = "Line 7: Semantic Error: Invalid use of reserved "
    line_7_cont = "keyword as a name.\nwaveform = AND (number_of_inputs:2);\n"

    assert captured.out == (line_1 + line_1_cont + line_2 + line_3
                            + line_3_cont + line_4 + line_5 + line_5_cont
                            + line_6 + line_6_cont + line_7 + line_7_cont)


def test_device_list(device_list_parser, capsys):
    """Test if device_list method returns expected output."""
    parser = device_list_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.device_list()

    # Check if no errors occur.
    captured = capsys.readouterr()
    assert captured.out == ''
    assert parser.error_count == 0

    # Check if devices are made properly.
    assert len(parser.devices.devices_list) == 5
    [XOR_ID, CLOCK_ID, AND_ID, SWITCH_ID,
     SIGGEN_ID] = parser.names.lookup(["XOR", "CLOCK", "AND",
                                       "SWITCH", "SIGGEN"])
    assert parser.devices.devices_list[0].device_kind == XOR_ID
    assert parser.devices.devices_list[1].device_kind == CLOCK_ID
    assert parser.devices.devices_list[1].clock_half_period == 2
    assert parser.devices.devices_list[2].device_kind == AND_ID
    assert len(parser.devices.devices_list[2].inputs) == 2
    assert parser.devices.devices_list[3].device_kind == SWITCH_ID
    assert parser.devices.devices_list[3].switch_state == 1
    assert parser.devices.devices_list[4].device_kind == SIGGEN_ID
    assert parser.devices.devices_list[4].siggen_waveform == [1]


def test_device_list_errors(device_list_errors_parser,
                            check_valid_device_parser,
                            device_list_errors_two_parser,
                            device_list_errors_three_parser,
                            capsys):
    """Test if device_list method returns expected error outputs."""
    parser = device_list_errors_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.device_list()
    assert parser.error_count == 4
    assert len(parser.devices.devices_list) == 1

    # Check that correct errors are printed.
    captured = capsys.readouterr()
    l1 = "Line 3: Semantic Error: Device already exists in the device list\n"
    l2 = "SW1 = SWITCH (initial_state:1);\n"
    l3 = "Line 4: Syntax Error: Expected an '=' sign\n"
    l4 = "xor1  XOR;\n"
    l5 = "       ^\n"
    l6 = "Line 5: Syntax Error: Expected a '(' sign\n"
    l7 = "and1 = AND number_of_inputs:2);\n"
    l8 = "                  ^\n"
    l9 = "Line 6: Syntax Error: Expected 'number_of_inputs'\n"
    l10 = "and1 = AND (initial_state:2);\n"
    l11 = "                  ^\n"
    assert captured.out == (l1 + l2 + l3 + l4 + l5 + l6 +
                            l7 + l8 + l9 + l10 + l11)

    # Test for 'DEVICES'.
    parser = check_valid_device_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.device_list()
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Expected the keyword 'DEVICES'\nXOR\n ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Test for left curly.
    parser = device_list_errors_two_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.device_list()
    captured = capsys.readouterr()
    line1 = "Line 1: Syntax Error: Expected a '{' sign\nDEVICES\n       ^\n"
    line2 = "Line 2: Syntax Error: Invalid device type\n"
    line3 = "and1 = and;\n        ^\n"
    line4 = "Line 2: Syntax Error: Expected a '}' sign\n"
    line5 = "and1 = and;\n           ^\n"
    assert captured.out == (line1 + line2 + line3 + line4 + line5)
    capsys.readouterr()

    # Test for right curly.
    parser = device_list_errors_three_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.device_list()
    captured = capsys.readouterr()
    line = "Line 3: Syntax Error: Expected a '}' sign\nxor = XOR;"
    line_cont = "\n          ^\n"
    assert captured.out == line + line_cont


def test_signame(signame_parser, capsys):
    """Test if signame method returns expected output."""
    parser = signame_parser
    [I6_ID, I2_ID, CLK_ID,
     Q_ID, QBAR_ID] = parser.names.lookup(["I6", "I2",
                                           "CLK", "Q", "QBAR"])

    # Test for input signals.
    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame()
    [correct_device] = parser.names.lookup(["nand1"])
    assert (device_id, port_id) == (correct_device, I6_ID)
    captured = capsys.readouterr()
    assert captured.out == ''

    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame()
    [correct_device] = parser.names.lookup(["or2"])
    assert (device_id, port_id) == (correct_device, I2_ID)
    captured = capsys.readouterr()
    assert captured.out == ''

    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame()
    [correct_device] = parser.names.lookup(["d2"])
    assert (device_id, port_id) == (correct_device, CLK_ID)
    captured = capsys.readouterr()
    assert captured.out == ''

    # Test for output signals.
    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame(input_port=False)
    [correct_device] = parser.names.lookup(["d1"])
    assert (device_id, port_id) == (correct_device, Q_ID)
    captured = capsys.readouterr()
    assert captured.out == ''

    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame(input_port=False)
    [correct_device] = parser.names.lookup(["d1"])
    assert (device_id, port_id) == (correct_device, QBAR_ID)
    captured = capsys.readouterr()
    assert captured.out == ''

    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame(input_port=False)
    [correct_device] = parser.names.lookup(["sw2"])
    assert (device_id, port_id) == (correct_device, None)
    captured = capsys.readouterr()
    assert captured.out == ''

    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame(input_port=False)
    [correct_device] = parser.names.lookup(["nor4"])
    assert (device_id, port_id) == (correct_device, None)
    captured = capsys.readouterr()
    assert captured.out == ''

    # Siggen device.
    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame(input_port=False)
    [correct_device] = parser.names.lookup(["siggen1"])
    assert (device_id, port_id) == (correct_device, None)
    captured = capsys.readouterr()
    assert captured.out == ''


def test_signame_errors(signame_errors_parser, capsys):
    """Test if signame method returns expected error outputs."""
    # Test signame identifies invalid device error.
    parser = signame_errors_parser
    parser.symbol = parser.scanner.get_symbol()
    [device_id, port_id] = parser.signame()
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 1: Syntax Error: Expected a device name\n"
    l2 = "CONNECT # Not Device Name #;\n"
    l3 = "   ^\n"
    assert captured.out == l1 + l2 + l3

    # Test signame identifies missing input port.
    [device_id, port_id] = parser.signame()
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 2: Syntax Error: Expected device port\n"
    l2 = "and1 # Port absent for input device #;\n"
    l3 = "    ^\n"
    assert captured.out == l1 + l2 + l3

    # Test signame for invalid input port.
    [device_id, port_id] = parser.signame()
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 3: Syntax Error: Invalid device port\n"
    l2 = "nor1.QBAR # Invalid port for input #;\n"
    l3 = "      ^\n"
    assert captured.out == l1 + l2 + l3

    # Test signame for invalid output port.
    [device_id, port_id] = parser.signame(input_port=False)
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 4: Syntax Error: Invalid device port\n"
    l2 = "d1.I4 # Invalid port for output #;\n"
    l3 = "   ^\n"
    assert captured.out == l1 + l2 + l3

    # Test signame for invalid Siggen output port.
    [device_id, port_id] = parser.signame(input_port=False)
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 5: Syntax Error: Invalid device port\n"
    l2 = "siggen1.I4 # Invalid port for output #;\n"
    l3 = "        ^\n"
    assert captured.out == l1 + l2 + l3

    # Test signame for EOF error.
    [device_id, port_id] = parser.signame()
    assert (device_id, port_id) == (None, None)
    captured = capsys.readouterr()
    l1 = "Line 6: Syntax Error: Invalid device port\n"
    l2 = "d1.\n"
    l3 = "   ^\n"
    assert captured.out == l1 + l2 + l3


def test_connnection(connection_parser, capsys):
    """Test if connection method gives the expected output for valid syntax."""
    parser = connection_parser

    # Add devices in test cases.
    [SW1_ID, SW2_ID, xor1_ID, and1_ID,
     siggen1_ID] = parser.names.lookup(["SW1", "SW2", "xor1",
                                        "and1", "siggen1"])
    [SWITCH_ID, XOR_ID,
     AND_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "XOR",
                                               "AND", "SIGGEN"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(SW2_ID, SWITCH_ID, 0)
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.devices.make_device(and1_ID, AND_ID, 3)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-_-")

    # Add test cases for valid connections.
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(5):
        parser.connection()
        captured = capsys.readouterr()
        assert captured.out == ''

    # Check if connections are made properly.
    [I1_ID, I2_ID, I3_ID] = parser.names.lookup(["I1", "I2", "I3"])
    xor1_device = parser.devices.get_device(xor1_ID)
    and1_device = parser.devices.get_device(and1_ID)
    assert xor1_device.inputs[I1_ID] == (SW1_ID, None)
    assert xor1_device.inputs[I2_ID] == (SW2_ID, None)
    assert and1_device.inputs[I1_ID] == (SW1_ID, None)
    assert and1_device.inputs[I2_ID] == (SW2_ID, None)
    assert and1_device.inputs[I3_ID] == (siggen1_ID, None)


def test_connnection_error(connection_error_parser, capsys):
    """Test if connection gives expected output for invalid syntax."""
    # Test no equals sign.
    parser = connection_error_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.connection()
    captured = capsys.readouterr()
    l1 = "Line 1: Syntax Error: Expected an '=' sign\n"
    l2 = "SW1 xor1.I1;\n"
    l3 = "   ^\n"
    assert captured.out == l1 + l2 + l3

    # Test no semi-colon sign. (and test EOF case)
    parser.connection()
    captured = capsys.readouterr()
    l1 = "Line 2: Syntax Error: Expected a ';' sign\n"
    l2 = "SW2 = xor1.I2\n"
    l3 = "             ^\n"
    assert captured.out == l1 + l2 + l3


def test_connection_semantic_errors(connection_semantics_parser, capsys):
    """Test if connection gives expected output for semantic errors."""
    parser = connection_semantics_parser

    # Add devices in test cases.
    [D10_ID, and1_ID,
     sw1_ID, siggen1_ID] = parser.names.lookup(["D10", "and1",
                                                "sw1", "siggen1"])
    [SWITCH_ID, DTYPE_ID,
     AND_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "DTYPE",
                                               "AND", "SIGGEN"])
    parser.devices.make_device(D10_ID, DTYPE_ID)
    parser.devices.make_device(sw1_ID, SWITCH_ID, 0)
    parser.devices.make_device(and1_ID, AND_ID, 2)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-_-")

    parser.symbol = parser.scanner.get_symbol()
    for _ in range(8):
        parser.connection()
        parser.error_count = 0

    captured = capsys.readouterr()
    l1 = "Line 1: Semantic Error: Specified port does not exist.\n"
    l2 = "D10 = and1.I1 # Unspecified output #;\n"
    l3 = "Line 2: Semantic Error: Specified port does not exist.\n"
    l4 = "D10.Q = sw1.I1 # Switch input #;\n"
    l5 = "Line 3: Semantic Error: Specified port does not exist.\n"
    l6 = "D10.Q = and1.I10 # Input doesn't exist #;\n"
    l7 = "Line 4: Semantic Error: Specified port does not exist.\n"
    l8 = "D10.Q = and1.DATA # Input doesn't exist #;\n"
    l9 = "Line 5: Semantic Error: Specified port does not exist.\n"
    l10 = "sw1.QBAR = and1.I1 # Output doesn't exist #;\n"
    l11 = "Line 6: Semantic Error: A stated device is"
    l11_1 = " not in the device list.\n"
    l12 = "sw10 = and1.I1 # Use of undefined device #;\n"
    l13 = "Line 7: Semantic Error: Specified port does not exist.\n"
    l14 = "sw1 = siggen1.I2;\n"
    l15 = "Line 8: Semantic Error: Specified port does not exist.\n"
    l16 = "siggen1.QBAR = and1.I1;\n"
    assert captured.out == (l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
                            + l9 + l10 + l11 + l11_1 + l12 + l13
                            + l14 + l15 + l16)


def test_connection_list(connection_list_parser, capsys):
    """Test if connection_list method returns expected output."""
    parser = connection_list_parser

    # Add devices in test cases.
    [SW1_ID, SW2_ID, xor1_ID, and1_ID,
     siggen1_ID] = parser.names.lookup(["SW1", "SW2", "xor1",
                                        "and1", "siggen1"])
    [SWITCH_ID, XOR_ID,
     AND_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "XOR",
                                               "AND", "SIGGEN"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(SW2_ID, SWITCH_ID, 0)
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.devices.make_device(and1_ID, AND_ID, 3)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-_-")
    parser.symbol = parser.scanner.get_symbol()
    parser.connection_list()

    # Check if no errors occur.
    captured = capsys.readouterr()
    assert captured.out == ''
    assert parser.error_count == 0

    # Check if connections are made properly.
    [I1_ID, I2_ID, I3_ID] = parser.names.lookup(["I1", "I2", "I3"])
    xor1_device = parser.devices.get_device(xor1_ID)
    and1_device = parser.devices.get_device(and1_ID)
    assert xor1_device.inputs[I1_ID] == (SW1_ID, None)
    assert xor1_device.inputs[I2_ID] == (SW2_ID, None)
    assert and1_device.inputs[I1_ID] == (SW1_ID, None)
    assert and1_device.inputs[I2_ID] == (SW2_ID, None)
    assert and1_device.inputs[I3_ID] == (siggen1_ID, None)


def test_connection_list_errors(check_valid_device_parser,
                                connection_list_error_parser,
                                connection_list_error_two_parser,
                                capsys):
    """Test if connection_list method returns expected error outputs."""
    # Test for CONNECT.
    parser = check_valid_device_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.connection_list()
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Expected the keyword 'CONNECT'\nXOR\n ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Test for left curly.
    parser = connection_list_error_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.connection_list()
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Expected a '{' sign\nCONNECT\n       ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Test for right curly.
    parser = connection_list_error_two_parser
    [SW1_ID, xor1_ID] = parser.names.lookup(["SW1", "xor1"])
    [SWITCH_ID, XOR_ID] = parser.names.lookup(["SWITCH", "XOR"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.symbol = parser.scanner.get_symbol()
    parser.connection_list()
    captured = capsys.readouterr()
    line = "Line 2: Syntax Error: Expected a '}' sign\nSW1 = xor1.I1;"
    line_cont = "\n              ^\n"
    assert captured.out == line + line_cont


def test_assign_monitor(monitor, capsys):
    """Test if assign_monitor method returns expected output."""
    parser = monitor

    # Add devices in test cases.
    [SW1_ID, SW2_ID, xor1_ID, and1_ID,
     siggen1_ID] = parser.names.lookup(["SW1", "SW2", "xor1",
                                        "and1", "siggen1"])
    [SWITCH_ID, XOR_ID,
     AND_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "XOR",
                                               "AND", "SIGGEN"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(SW2_ID, SWITCH_ID, 0)
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.devices.make_device(and1_ID, AND_ID, 3)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-_-")

    # Add connections in test cases.
    [I1_ID, I2_ID, I3_ID] = parser.names.lookup(["I1", "I2", "I3"])
    parser.network.make_connection(SW1_ID, None, xor1_ID, I1_ID)
    parser.network.make_connection(SW2_ID, None, xor1_ID, I2_ID)
    parser.network.make_connection(SW1_ID, None, and1_ID, I1_ID)
    parser.network.make_connection(SW2_ID, None, and1_ID, I2_ID)
    parser.network.make_connection(siggen1_ID, None, and1_ID, I3_ID)
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(3):
        parser.assign_monitor()

    # Check that no errors occur.
    captured = capsys.readouterr()
    assert captured.out == ''
    assert parser.error_count == 0

    # Check if monitors are made.
    monitors_made = parser.monitors.monitors_dictionary
    assert len(list(monitors_made)) == 3
    assert ((xor1_ID, None) in monitors_made)
    assert ((and1_ID, None) in monitors_made)
    assert ((siggen1_ID, None) in monitors_made)


def test_assign_monitor_error(monitor_error, capsys):
    """Test if assign_monitor gives expected output for invalid syntax."""
    # Test no semi-colon sign. (and test EOF case)
    parser = monitor_error
    parser.symbol = parser.scanner.get_symbol()
    for _ in range(2):
        parser.assign_monitor()
    captured = capsys.readouterr()
    l1 = "Line 1: Syntax Error: Invalid device port\n"
    l2 = "SW1.I2;\n"
    l3 = "    ^\n"
    l4 = "Line 2: Syntax Error: Expected a ';' sign\n"
    l5 = "SW1\n"
    l6 = "   ^\n"
    assert captured.out == l1 + l2 + l3 + l4 + l5 + l6


def test_monitor_semantics(check_monitor_semantics_parser, capsys):
    """Test if assign_monitor gives expected output for semantic errors."""
    parser = check_monitor_semantics_parser

    # Add devices in test cases.
    [D10_ID, SW1_ID, siggen1_ID] = parser.names.lookup(["D10", "SW1",
                                                        "siggen1"])
    [SWITCH_ID, DTYPE_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "DTYPE",
                                                            "SIGGEN"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(D10_ID, DTYPE_ID)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-__")

    parser.symbol = parser.scanner.get_symbol()
    for _ in range(8):
        parser.assign_monitor()
        parser.error_count = 0

    captured = capsys.readouterr()
    l1 = "Line 1: Semantic Error: A stated device is not in the device list.\n"
    l2 = "sw10 # Use of undefined device #;\n"
    l3 = "Line 2: Semantic Error: Expected an output signal\n"
    l4 = "D10 # Unspecified output #;\n"
    l5 = "Line 3: Semantic Error: Expected an output signal\n"
    l6 = "SW1.Q # Invalid output #;\n"
    l7 = "Line 5: Semantic Error: Monitor already exists in the monitor list\n"
    l8 = "D10.Q # Monitor present #;\n"
    l9 = "Line 7: Semantic Error: Monitor already exists in the monitor list\n"
    l10 = "siggen1;\n"
    l11 = "Line 8: Semantic Error: Expected an output signal\n"
    l12 = "siggen1.Q;\n"
    assert captured.out == (l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
                            + l10 + l11 + l12)


def test_monitor_list(monitor_list_parser, capsys):
    """Test if monitor_list method returns expected output."""
    parser = monitor_list_parser

    # Add devices in test cases.
    [SW1_ID, SW2_ID, xor1_ID, and1_ID,
     siggen1_ID] = parser.names.lookup(["SW1", "SW2", "xor1",
                                        "and1", "siggen1"])
    [SWITCH_ID, XOR_ID,
     AND_ID, SIGGEN_ID] = parser.names.lookup(["SWITCH", "XOR",
                                               "AND", "SIGGEN"])
    parser.devices.make_device(SW1_ID, SWITCH_ID, 0)
    parser.devices.make_device(SW2_ID, SWITCH_ID, 0)
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.devices.make_device(and1_ID, AND_ID, 3)
    parser.devices.make_device(siggen1_ID, SIGGEN_ID, "-_-")

    # Add connections in test cases.
    [I1_ID, I2_ID, I3_ID] = parser.names.lookup(["I1", "I2", "I3"])
    parser.network.make_connection(SW1_ID, None, xor1_ID, I1_ID)
    parser.network.make_connection(SW2_ID, None, xor1_ID, I2_ID)
    parser.network.make_connection(SW1_ID, None, and1_ID, I1_ID)
    parser.network.make_connection(SW2_ID, None, and1_ID, I2_ID)
    parser.network.make_connection(siggen1_ID, None, and1_ID, I3_ID)
    parser.symbol = parser.scanner.get_symbol()
    parser.monitor_list()

    # Check that no errors occur.
    captured = capsys.readouterr()
    assert captured.out == ''
    assert parser.error_count == 0

    # Check if monitors are made.
    monitors_made = parser.monitors.monitors_dictionary
    assert len(list(monitors_made)) == 3
    assert ((xor1_ID, None) in monitors_made)
    assert ((and1_ID, None) in monitors_made)
    assert ((siggen1_ID, None) in monitors_made)


def test_monitor_list_error(check_valid_device_parser,
                            monitor_list_error_parser,
                            monitor_list_error_two_parser,
                            capsys):
    """Test if monitor_list method returns expected errors."""
    # Test for MONITOR.
    parser = check_valid_device_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.monitor_list()
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Expected the keyword 'MONITOR'\nXOR\n ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Test for left curly.
    parser = monitor_list_error_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.monitor_list()
    captured = capsys.readouterr()
    line = "Line 1: Syntax Error: Expected a '{' sign\nMONITOR\n       ^\n"
    assert captured.out == line
    capsys.readouterr()

    # Test for right curly.
    parser = monitor_list_error_two_parser
    [xor1_ID, and1_ID] = parser.names.lookup(["xor1", "and1"])
    [XOR_ID, AND_ID] = parser.names.lookup(["XOR", "AND"])
    parser.devices.make_device(xor1_ID, XOR_ID)
    parser.devices.make_device(and1_ID, AND_ID, 2)
    parser.symbol = parser.scanner.get_symbol()
    parser.monitor_list()
    captured = capsys.readouterr()
    line = "Line 3: Syntax Error: Expected a '}' sign\nand1;\n     ^\n"
    assert captured.out == line


def test_empty_monitor_list(empty_monitor_list_parser, capsys):
    """Test if monitor_list method returns expected output for empty list."""
    parser = empty_monitor_list_parser
    parser.symbol = parser.scanner.get_symbol()
    parser.monitor_list()

    # Check for no errors.
    captured = capsys.readouterr()
    assert captured.out == ''
    # Check that no monitors are made.
    monitors_made = parser.monitors.monitors_dictionary
    assert len(list(monitors_made)) == 0


def test_parse_adder(adder_parser, capsys):
    """Test if parse_network method returns expected output."""
    parser = adder_parser
    parser_output = parser.parse_network()

    # Check if no errors occur.
    captured = capsys.readouterr()
    assert captured.out == ''
    assert parser.error_count == 0
    assert parser_output

    # Check devices made properly.
    assert len(parser.devices.devices_list) == 4
    [XOR_ID, AND_ID, SWITCH_ID] = parser.names.lookup(["XOR", "AND", "SWITCH"])
    [SW1_ID, SW2_ID,
     xor1_ID, and1_ID] = parser.names.lookup(["SW1", "SW2",
                                              "xor1", "and1"])
    assert parser.devices.devices_list[0].device_kind == XOR_ID
    assert parser.devices.devices_list[0].device_id == xor1_ID
    assert parser.devices.devices_list[1].device_kind == AND_ID
    assert parser.devices.devices_list[1].device_id == and1_ID
    assert len(parser.devices.devices_list[1].inputs) == 2
    assert parser.devices.devices_list[2].device_kind == SWITCH_ID
    assert parser.devices.devices_list[2].switch_state == 1
    assert parser.devices.devices_list[2].device_id == SW1_ID
    assert parser.devices.devices_list[3].device_kind == SWITCH_ID
    assert parser.devices.devices_list[3].switch_state == 1
    assert parser.devices.devices_list[3].device_id == SW2_ID

    # Check connections made properly.
    [I1_ID, I2_ID] = parser.names.lookup(["I1", "I2"])
    xor1_device = parser.devices.get_device(xor1_ID)
    and1_device = parser.devices.get_device(and1_ID)
    assert xor1_device.inputs[I1_ID] == (SW1_ID, None)
    assert xor1_device.inputs[I2_ID] == (SW2_ID, None)
    assert and1_device.inputs[I1_ID] == (SW1_ID, None)
    assert and1_device.inputs[I2_ID] == (SW2_ID, None)

    # Check if monitors made properly.
    monitors_made = parser.monitors.monitors_dictionary
    assert len(list(monitors_made)) == 2
    assert ((xor1_ID, None) in monitors_made)
    assert ((and1_ID, None) in monitors_made)


def test_parse_adder_error(adder_parser_error, adder_parser_error_two, capsys):
    """Test if parse_network returns expected output for invalid syntax."""
    # Test for no 'END'.
    parser = adder_parser_error
    parser.parse_network()
    captured = capsys.readouterr()
    line1 = "Line 20: Syntax Error: Expected the keyword 'END'\n}\n ^\n"
    line2 = "Total of 1 error detected\n"
    assert captured.out == line1 + line2
    capsys.readouterr()

    # Test for symbol after 'END'.
    parser = adder_parser_error_two
    parser.parse_network()
    captured = capsys.readouterr()
    line1 = "Line 22: Syntax Error: Unexpected symbols after 'END'"
    line1_cont = "\nSomething\n    ^\n"
    line2 = "Total of 1 error detected\n"
    assert captured.out == line1 + line1_cont + line2
    capsys.readouterr()


def test_parse_adder_error_random(adder_parser_error_three, capsys):
    """Test overall functionality of parser."""
    parser = adder_parser_error_three
    parser.parse_network()
    captured = capsys.readouterr()
    line_1 = "Line 11: Syntax Error: Expected an '=' sign\n"
    line_1_cont = "SW1 xor1.I120; #Some comment#\n   ^\n"
    line_2 = "Line 13: Syntax Error: Expected a device name\nSW1 = .I1;"
    line_2_cont = "\n      ^\n"
    line_3 = "Line 14: Syntax Error: Invalid device port\nSW2 = and1.;"
    line_3_cont = "\n           ^\n"
    line_4 = "Line 20: Syntax Error: Expected the keyword 'END'\n}\n ^\n"
    line_5 = "Total of 4 errors detected\n"
    assert captured.out == (line_1 + line_1_cont + line_2 + line_2_cont
                            + line_3 + line_3_cont + line_4 + line_5)


def test_missing_stopping_symbols(missing_stopping_symbols, capsys):
    """Test if parser can recover from missing stopping symbols."""
    parser = missing_stopping_symbols
    parser.parse_network()
    captured = capsys.readouterr()
    line1 = "Line 3: Syntax Error: Expected the keyword 'DEVICES'\n"
    line2 = " {\n ^\n"
    line3 = "Line 5: Syntax Error: Expected a ';' sign\n"
    line4 = "and1 = AND (number_of_inputs:2)\n"
    line5 = "                               ^\n"
    line6 = "Line 11: Syntax Error: Expected the keyword 'CONNECT'\n"
    line7 = "SW1 = xor1.I1;\n ^\n"
    line8 = "Line 17: Syntax Error: Expected a '{' sign\n"
    line9 = "MONITOR\n       ^\n"
    line10 = "Line 18: Syntax Error: Expected a ';' sign\n"
    line11 = "xor1\n    ^\nTotal of 5 errors detected\n"
    assert captured.out == (line1 + line2 + line3 + line4 + line5 + line6
                            + line7 + line8 + line9 + line10 + line11)


def test_catastrophic_error(catastrophic_error_parser, capsys):
    """Test if a syntax error followed by a missing semicolon gives
    the expected output.
    """
    parser = catastrophic_error_parser
    parser.parse_network()
    captured = capsys.readouterr()
    # Error message should miss SWITCHy entirely.
    line1 = "Line 3: Syntax Error: Expected a '(' sign\n"
    line2 = "and1 = AND number_of_inputs:2)\n"
    line3 = "                  ^\nTotal of 1 error detected\n"
    assert captured.out == (line1 + line2 + line3)


def test_error_messages(adder_parser_error_three, capsys):
    """Test that printing from self.parse.error_messages gives the same
    result as error message in std output.
    """
    parser = adder_parser_error_three
    parser.parse_network()
    captured = capsys.readouterr()
    # Error Message stored in parser.error_messages.
    full_error_message = "".join(parser.error_messages)
    assert captured.out == full_error_message


def test_parse_adder_error_random(adder_parser_error_four, capsys):
    """Combining multiple syntatic and semantic errors, plus error recovery."""
    parser = adder_parser_error_four
    parser.parse_network()
    captured = capsys.readouterr()
    line_1 = "Line 5: Semantic Error: Device already exists in the device list"
    line_2 = "\nxor1 = XOR; # Semantic #\n"
    line_3 = "Line 6: Syntax Error: Expected a '(' sign\nand1 = AND "
    line_4 = "number_of_inputs:1); # Syntatic #\n                  ^\n"
    line_5 = "Line 7: Syntax Error: Expected a ';' sign\n"
    line_6 = "SW1 = SWITCH (initial_state:1) # Error Recovery + Syntatic Error"
    line_7 = " #\n                              ^\n"
    line_8 = "Line 8: Syntax Error: Invalid device property\nSW2 = SWITCH "
    line_9 = "(initial_state:10); # Syntatic error #\n                        "
    line_10 = "    ^\nLine 12: Syntax Error: Invalid device port\nSW1 = xor1."
    line_11 = "I120; # Syntatic #\n            ^\n"
    line_12 = "Line 14: Syntax Error: Expected a device name\nSW1 = .I1"
    line_13 = "; #Syntatic#\n      ^\n"
    line_14 = "Line 15: Syntax Error: Invalid device port\nSW2 = and1.; "
    line_15 = "#Syntatic#\n           ^\n"
    line_16 = "Line 21: Syntax Error: Expected the keyword 'END'\n}"
    line_17 = "\n ^\nTotal of 8 errors detected\n"
    assert captured.out == (line_1 + line_2 + line_3 + line_4 + line_5 + line_6
                            + line_7 + line_8 + line_9 + line_10 + line_11
                            + line_12 + line_13 + line_14 + line_15 + line_16
                            + line_17)


def test_inputs_missing(inputs_missing_parser, capsys):
    """Test that semantic error raised if not all inputs in network
    are connected.
    """
    parser = inputs_missing_parser
    parser.parse_network()
    captured = capsys.readouterr()
    line = "Semantic Error: Not all inputs in the network are connnected\n"
    line_cont = "Total of 1 error detected\n"
    assert captured.out == line + line_cont


def test_missing_lists(missing_lists_parser, capsys):
    """Test that parser gives expected output for missing connection
    and monitorlist.
    """
    parser = missing_lists_parser
    parser.parse_network()
    captured = capsys.readouterr()
    line1 = "Line 10: Syntax Error: Expected the keyword 'CONNECT'\n"
    line2 = "END\n ^\n"
    line3 = "Line 10: Syntax Error: Expected the keyword 'MONITOR'\n"
    line4 = "END\n  ^\n"
    line5 = "Line 10: Syntax Error: Expected the keyword 'END'\n"
    line6 = "END\n   ^\nTotal of 3 errors detected\n"
    assert captured.out == line1 + line2 + line3 + line4 + line5 + line6


def test_empty_file(empty_text_parser, capsys):
    """Test that parser gives expected output for empty text file."""
    parser = empty_text_parser
    parser.parse_network()
    captured = capsys.readouterr()
    line1 = "Error: Cannot parse an empty text file\n"
    line2 = "Total of 1 error detected\n"
    assert captured.out == line1 + line2
