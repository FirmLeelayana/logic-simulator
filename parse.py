"""Parse the definition file and build the logic network.

Used in the Logic Simulator project to analyse the syntactic and semantic
correctness of the symbols received from the scanner and then builds the
logic network.

Classes
-------
Parser - parses the definition file and builds the logic network.
"""

from names import Names
from network import Network
from devices import Devices
from monitors import Monitors
from scanner import Symbol, Scanner


class Parser:
    """Parse the definition file and build the logic network.

    The parser deals with error handling. It analyses the syntactic and
    semantic correctness of the symbols it receives from the scanner, and
    then builds the logic network. If there are errors in the definition file,
    the parser detects this and tries to recover from it, giving helpful
    error messages.

    Parameters
    ----------
    names: instance of the names.Names() class.
    devices: instance of the devices.Devices() class.
    network: instance of the network.Network() class.
    monitors: instance of the monitors.Monitors() class.
    scanner: instance of the scanner.Scanner() class.

    Public methods
    --------------
    print_message(self, message): Print and append the error message
                                  to self.error_messages.

    display_error(self, error_type, symbol, syntax_error=True,
                        afterward=False): Display the error message
                        and calls the error recovery function.

    parse_network(self): Parses the circuit definition file
                         and returns true if there are no errors.
    """

    def __init__(self, names, devices, network, monitors, scanner):
        """Initialise constants."""
        # Exception handling.
        if not isinstance(names, Names):
            raise TypeError("Expected an instance of Names.")
        elif not isinstance(devices, Devices):
            raise TypeError("Expected an instance of Devies.")
        elif not isinstance(network, Network):
            raise TypeError("Expected an instance of Network.")
        elif not isinstance(monitors, Monitors):
            raise TypeError("Expected an instance of Monitors.")
        elif not isinstance(scanner, Scanner):
            raise TypeError("Expected an instance of Scanner.")

        self.names = names
        self.devices = devices
        self.network = network
        self.monitors = monitors
        self.scanner = scanner

        self.symbol = None
        self.prev_symbol = None
        self.error_count = 0

        # List of syntax errors
        [self.NOT_DEVICE_NAME, self.NO_EQUALS, self.NO_LEFT_BRACKET,
            self.NO_RIGHT_BRACKET, self.NOT_NUM_INPUTS,
            self.NO_COLON, self.NOT_INITIAL_STATE, self.NOT_CYCLE,
            self.INVALID_DEVICE, self.NOT_NUMBER, self.NO_DEVICES_KEYWORD,
            self.NO_SEMICOLON, self.NO_LEFT_CURLY,
            self.NO_RIGHT_CURLY, self.NO_DOT, self.INVALID_PORT,
            self.PORT_ABSENT, self.NO_CONNECT_KEYWORD,
            self.NO_MONITOR_KEYWORD, self.AFTER_END,
            self.NO_END, self.INVALID_PROPERTY, self.USED_KEYWORD,
            self.NO_LIST, self.NOT_LOGIC,
            self.NOT_WAVEFORM] = self.names.unique_error_codes(26)

        # Error messages stored in a list
        self.error_messages = []

    def print_message(self, message):
        """Print and appends the error message to self.error_messages."""
        print(message)
        self.error_messages.append(message + "\n")

    def error_recovery(self, error_type):
        """Recovers from an error.

        Resumes parsing at an appropriate point.
        """
        # List of error which do not require skipping symbols
        pass_errors = [self.NO_LEFT_CURLY, self.NO_SEMICOLON,
                       self.NO_LEFT_CURLY, self.NO_DEVICES_KEYWORD,
                       self.NO_CONNECT_KEYWORD, self.NO_MONITOR_KEYWORD]
        # List of stopping symbols when error_type == self.NO_LIST
        no_list_symbols = [self.scanner.LEFT_CURLY, self.scanner.EOF]
        list_keywords = self.names.lookup(["CONNECT", "MONITOR", "END"])
        # Statement Recovery
        if error_type in pass_errors:
            pass
        # Panic Mode Recovery (error_type == self.NO_LIST)
        elif error_type == self.NO_LIST:
            while (self.symbol.type not in no_list_symbols):
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
                if (self.symbol.type == self.scanner.KEYWORD and
                   self.symbol.id in list_keywords):
                    break
        # Panic Mode Recovery
        else:
            stopping_symbols = [self.scanner.SEMICOLON,
                                self.scanner.RIGHT_CURLY,
                                self.scanner.LEFT_CURLY, self.scanner.EOF]
            while self.symbol.type not in stopping_symbols:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()

    def display_error(self, error_type, symbol, syntax_error=True,
                      afterward=False):
        """Display the error message and where the error occurred.

        Calls the error handling function to resume parsing at an
        appropriate point.
        """
        # Exception handling.
        if not isinstance(error_type, int):
            raise TypeError("Expected an integer ID.")
        elif error_type >= self.names.error_code_count or error_type < 0:
            raise ValueError("Expected a valid integer ID.")
        elif not isinstance(symbol, Symbol):
            raise TypeError("Expected an instance of Symbol.")
        elif not isinstance(syntax_error, bool):
            raise TypeError("Expected a boolean syntax_error.")
        elif not isinstance(afterward, bool):
            raise TypeError("Expected a boolean afterward.")

        # Add to error count
        self.error_count += 1

        # Display Line Number
        print(f"Line {symbol.line_number}: ", end='')
        start_message = "Line " + str(symbol.line_number) + ": "
        self.error_messages.append(start_message)

        # Display error message
        if error_type == self.NOT_DEVICE_NAME:
            self.print_message("Syntax Error: Expected a device name")
        elif error_type == self.INVALID_DEVICE:
            self.print_message("Syntax Error: Invalid device type")
        elif error_type == self.NO_EQUALS:
            self.print_message("Syntax Error: Expected an '=' sign")
        elif error_type == self.NO_LEFT_BRACKET:
            self.print_message("Syntax Error: Expected a '(' sign")
        elif error_type == self.NO_RIGHT_BRACKET:
            self.print_message("Syntax Error: Expected a ')' sign")
        elif error_type == self.NOT_NUM_INPUTS:
            self.print_message("Syntax Error: Expected 'number_of_inputs'")
        elif error_type == self.NO_COLON:
            self.print_message("Syntax Error: Expected a ':' sign")
        elif error_type == self.NOT_INITIAL_STATE:
            self.print_message("Syntax Error: Expected 'initial_state'")
        elif error_type == self.NOT_CYCLE:
            self.print_message("Syntax Error: Expected 'cycle'")
        elif error_type == self.NOT_WAVEFORM:
            self.print_message("Syntax Error: Expected 'waveform'")
        elif error_type == self.NOT_NUMBER:
            self.print_message("Syntax Error: Expected an integer value")
        elif error_type == self.NOT_LOGIC:
            self.print_message("Syntax Error: Expected "
                               + "logic levels (underscores and dashes)")
        elif error_type == self.NO_DEVICES_KEYWORD:
            self.print_message("Syntax Error: Expected the keyword 'DEVICES'")
        elif error_type == self.NO_CONNECT_KEYWORD:
            self.print_message("Syntax Error: Expected the keyword 'CONNECT'")
        elif error_type == self.NO_MONITOR_KEYWORD:
            self.print_message("Syntax Error: Expected the keyword 'MONITOR'")
        elif error_type == self.NO_SEMICOLON:
            self.print_message("Syntax Error: Expected a ';' sign")
        elif error_type == self.NO_LEFT_CURLY:
            self.print_message("Syntax Error: Expected a '{' sign")
        elif error_type == self.NO_RIGHT_CURLY:
            self.print_message("Syntax Error: Expected a '}' sign")
        elif error_type == self.devices.INVALID_QUALIFIER:
            self.print_message("Semantic Error: Invalid device property")
        elif error_type == self.devices.NO_QUALIFIER:
            self.print_message("Semantic Error: " +
                               "Expected a device property for initialisation")
        elif error_type == self.devices.QUALIFIER_PRESENT:
            self.print_message("Semantic Error: " +
                               "Expected no device property for this device")
        elif error_type == self.devices.DEVICE_PRESENT:
            self.print_message("Semantic Error: " +
                               "Device already exists in the device list")
        elif error_type == self.devices.BAD_DEVICE:
            self.print_message("Semantic Error: Invalid type of device")
        elif error_type == self.NO_DOT:
            self.print_message("Syntax Error: Expected a '.' sign")
        elif error_type == self.INVALID_PORT:
            self.print_message("Syntax Error: Invalid device port")
        elif error_type == self.network.INPUT_TO_INPUT:
            self.print_message("Semantic Error: Cannot connect an input" +
                               " port to another input port.")
        elif error_type == self.network.OUTPUT_TO_OUTPUT:
            self.print_message("Semantic Error: Cannot connect an output" +
                               " port to another output port.")
        elif error_type == self.network.INPUT_CONNECTED:
            self.print_message("Semantic Error: " +
                               "Input port of device already connected.")
        elif error_type == self.network.PORT_ABSENT:
            self.print_message("Semantic Error: " +
                               "Specified port does not exist.")
        elif error_type == self.network.DEVICE_ABSENT:
            self.print_message("Semantic Error: " +
                               "A stated device is not in the device list.")
        elif error_type == self.PORT_ABSENT:
            self.print_message("Syntax Error: Expected device port")
        elif error_type == self.AFTER_END:
            self.print_message("Syntax Error: Unexpected symbols after 'END'")
        elif error_type == self.NO_END:
            self.print_message("Syntax Error: Expected the keyword 'END'")
        elif error_type == self.INVALID_PROPERTY:
            self.print_message("Syntax Error: Invalid device property")
        elif error_type == self.USED_KEYWORD:
            self.print_message("Semantic Error: " +
                               "Invalid use of reserved keyword as a name.")
        elif error_type == self.monitors.NOT_OUTPUT:
            self.print_message("Semantic Error: Expected an output signal")
        elif error_type == self.monitors.MONITOR_PRESENT:
            self.print_message("Semantic Error: " +
                               "Monitor already exists in the monitor list")
        else:
            raise ValueError("Expected a valid error code.")

        if syntax_error:
            # Print error position and pointer if syntax error
            scanner_message = self.scanner.print_pointer(symbol,
                                                         after=afterward)
            print(scanner_message, end='')
            self.error_messages.append(scanner_message)
        else:
            # Print current line only if semantic error
            scanner_message = self.scanner.print_pointer(symbol, pointer=False)
            print(scanner_message, end='')
            self.error_messages.append(scanner_message)
        # Call error recovery function to resume parsing at appropriate point
        self.error_recovery(error_type)

    def check_valid_device(self):
        """Check if the device kind and properties are valid.

        Return device_kind and device_property if device is valid.
        Return None, None if syntax errors occur.
        """
        variable_input_gates = self.names.lookup(["AND", "OR", "NAND", "NOR"])
        [SWITCH_ID, CLOCK_ID, DTYPE_ID, INITIAL_STATE_ID,
         NUM_INPUTS_ID, XOR_ID, CYCLE_ID, SIGGEN_ID,
         WAVEFORM_ID] = self.names.lookup(["SWITCH", "CLOCK", "DTYPE",
                                           "initial_state", "number_of_inputs",
                                           "XOR", "cycle", "SIGGEN",
                                           "waveform"])

        # If symbol is an AND, OR, NAND, or NOR gate
        if (self.symbol.id in variable_input_gates):
            device_kind = self.names.get_name_string(self.symbol.id)
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_BRACKET:
                self.symbol = self.scanner.get_symbol()
                if self.symbol.id == NUM_INPUTS_ID:
                    self.symbol = self.scanner.get_symbol()
                    if self.symbol.type == self.scanner.COLON:
                        self.symbol = self.scanner.get_symbol()
                        if self.symbol.type == self.scanner.NUMBER:
                            if self.symbol.id not in range(1, 17):
                                self.display_error(self.INVALID_PROPERTY,
                                                   self.symbol)
                                return None, None
                            device_property = self.symbol.id
                            self.symbol = self.scanner.get_symbol()
                            if self.symbol.type == self.scanner.RIGHT_BRACKET:
                                return device_kind, device_property
                            else:
                                self.display_error(self.NO_RIGHT_BRACKET,
                                                   self.symbol)
                                return None, None
                        else:
                            self.display_error(self.NOT_NUMBER, self.symbol)
                            return None, None
                    else:
                        self.display_error(self.NO_COLON, self.symbol)
                        return None, None
                else:
                    self.display_error(self.NOT_NUM_INPUTS, self.symbol)
                    return None, None
            else:
                self.display_error(self.NO_LEFT_BRACKET, self.symbol)
                return None, None
        # If symbol is a SWITCH
        elif (self.symbol.id == SWITCH_ID):
            device_kind = self.names.get_name_string(self.symbol.id)
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_BRACKET:
                self.symbol = self.scanner.get_symbol()
                if self.symbol.id == INITIAL_STATE_ID:
                    self.symbol = self.scanner.get_symbol()
                    if self.symbol.type == self.scanner.COLON:
                        self.symbol = self.scanner.get_symbol()
                        if self.symbol.type == self.scanner.NUMBER:
                            if self.symbol.id not in [0, 1]:
                                self.display_error(self.INVALID_PROPERTY,
                                                   self.symbol)
                                return None, None
                            device_property = self.symbol.id
                            self.symbol = self.scanner.get_symbol()
                            if self.symbol.type == self.scanner.RIGHT_BRACKET:
                                return device_kind, device_property
                            else:
                                self.display_error(self.NO_RIGHT_BRACKET,
                                                   self.symbol)
                                return None, None
                        else:
                            self.display_error(self.NOT_NUMBER, self.symbol)
                            return None, None
                    else:
                        self.display_error(self.NO_COLON, self.symbol)
                        return None, None
                else:
                    self.display_error(self.NOT_INITIAL_STATE, self.symbol)
                    return None, None
            else:
                self.display_error(self.NO_LEFT_BRACKET, self.symbol)
                return None, None
        # If symbol is a CLOCK
        elif (self.symbol.id == CLOCK_ID):
            device_kind = self.names.get_name_string(self.symbol.id)
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_BRACKET:
                self.symbol = self.scanner.get_symbol()
                if self.symbol.id == CYCLE_ID:
                    self.symbol = self.scanner.get_symbol()
                    if self.symbol.type == self.scanner.COLON:
                        self.symbol = self.scanner.get_symbol()
                        if self.symbol.type == self.scanner.NUMBER:
                            device_property = self.symbol.id
                            self.symbol = self.scanner.get_symbol()
                            if self.symbol.type == self.scanner.RIGHT_BRACKET:
                                return device_kind, device_property
                            else:
                                self.display_error(self.NO_RIGHT_BRACKET,
                                                   self.symbol)
                                return None, None
                        else:
                            self.display_error(self.NOT_NUMBER, self.symbol)
                            return None, None
                    else:
                        self.display_error(self.NO_COLON, self.symbol)
                        return None, None
                else:
                    self.display_error(self.NOT_CYCLE, self.symbol)
                    return None, None
            else:
                self.display_error(self.NO_LEFT_BRACKET, self.symbol)
                return None, None
        # If device is a SIGGEN.
        elif (self.symbol.id == SIGGEN_ID):
            device_kind = self.names.get_name_string(self.symbol.id)
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_BRACKET:
                self.symbol = self.scanner.get_symbol()
                if self.symbol.id == WAVEFORM_ID:
                    self.symbol = self.scanner.get_symbol()
                    if self.symbol.type == self.scanner.COLON:
                        self.symbol = self.scanner.get_symbol()
                        if self.symbol.type == self.scanner.LOGIC:
                            device_property = self.symbol.id
                            self.symbol = self.scanner.get_symbol()
                            if self.symbol.type == self.scanner.RIGHT_BRACKET:
                                return device_kind, device_property
                            else:
                                self.display_error(self.NO_RIGHT_BRACKET,
                                                   self.symbol)
                                return None, None
                        else:
                            self.display_error(self.NOT_LOGIC, self.symbol)
                            return None, None
                    else:
                        self.display_error(self.NO_COLON, self.symbol)
                        return None, None
                else:
                    self.display_error(self.NOT_WAVEFORM, self.symbol)
                    return None, None
            else:
                self.display_error(self.NO_LEFT_BRACKET, self.symbol)
                return None, None
        # If symbol is DTYPE device or XOR gate
        elif (self.symbol.id == DTYPE_ID or self.symbol.id == XOR_ID):
            device_kind = self.names.get_name_string(self.symbol.id)
            device_property = None
            return device_kind, device_property
        else:
            self.display_error(self.INVALID_DEVICE, self.symbol)
            return None, None

    def assign_device(self):
        """Parse a single line in the device list.

        Make the device if there are no errors.
        """
        if self.symbol.type == self.scanner.NAME:
            device_id = self.symbol.id
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.EQUALS:
                self.symbol = self.scanner.get_symbol()
                self.prev_symbol = self.symbol
                device_kind, device_property = self.check_valid_device()
                # Get ID of device_kind string
                if device_kind is not None:
                    [device_kind] = self.names.lookup([device_kind])
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
                    if self.symbol.type != self.scanner.SEMICOLON:
                        self.display_error(self.NO_SEMICOLON, self.prev_symbol,
                                           afterward=True)
            else:
                self.display_error(self.NO_EQUALS, self.symbol)
        else:
            if self.symbol.type == self.scanner.KEYWORD:
                self.display_error(self.USED_KEYWORD, self.symbol, False)
            else:
                self.display_error(self.NOT_DEVICE_NAME, self.symbol)
        # If no errors, make the device
        if self.error_count == 0:
            error_type = self.devices.make_device(device_id, device_kind,
                                                  device_property)
            if error_type != self.devices.NO_ERROR:
                self.display_error(error_type, self.symbol, False)
        # If semicolon not missing, grab the next symbol
        if self.symbol.type == self.scanner.SEMICOLON:
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()

    def device_list(self):
        """Parse the device list."""
        [DEVICES_ID, CONNECT_ID] = self.names.lookup(["DEVICES", "CONNECT"])
        if (self.symbol.type == self.scanner.KEYWORD and
           self.symbol.id == DEVICES_ID):
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
            else:
                self.display_error(self.NO_LEFT_CURLY, self.prev_symbol,
                                   afterward=True)
            while self.symbol.type != self.scanner.RIGHT_CURLY:
                if (self.symbol.id == CONNECT_ID or
                   self.symbol.type == self.scanner.EOF):
                    self.display_error(self.NO_RIGHT_CURLY, self.prev_symbol,
                                       afterward=True)
                    break
                else:
                    self.assign_device()
            # If right curly not missing, grab the next symbol
            if self.symbol.type == self.scanner.RIGHT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
        else:
            self.display_error(self.NO_DEVICES_KEYWORD, self.symbol)
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
                while self.symbol.type != self.scanner.RIGHT_CURLY:
                    if (self.symbol.id == CONNECT_ID or
                       self.symbol.type == self.scanner.EOF):
                        self.display_error(self.NO_RIGHT_CURLY,
                                           self.prev_symbol, afterward=True)
                        break
                    else:
                        self.assign_device()
                # If right curly not missing, grab the next symbol
                if self.symbol.type == self.scanner.RIGHT_CURLY:
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
            else:
                # If missing both the keyword and left curly
                self.error_recovery(self.NO_LIST)  # Assume missing list

    def signame(self, input_port=True):
        """Return the device_id and the corresponding output or input port.

        Return None, None if error occurs.
        """
        valid_input_ports = self.names.lookup(["DATA", "CLK", "SET", "CLEAR",
                                               "I1", "I2", "I3", "I4", "I5",
                                               "I6", "I7", "I8", "I9", "I10",
                                               "I11", "I12", "I13", "I14",
                                               "I15", "I16"])
        valid_output_ports = self.names.lookup(["Q", "QBAR"])
        if self.symbol.type == self.scanner.NAME:
            self.prev_symbol = self.symbol
            device_id = self.symbol.id
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.DOT:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
                if (input_port is True and
                   self.symbol.id in valid_input_ports):
                    device_port = self.symbol.id
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
                    return device_id, device_port
                elif (input_port is False and
                      self.symbol.id in valid_output_ports):
                    device_port = self.symbol.id
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
                    return device_id, device_port
                else:
                    if self.symbol.type == self.scanner.EOF:
                        # Accounting for EOF.
                        self.display_error(self.INVALID_PORT,
                                           self.prev_symbol, afterward=True)
                    else:
                        # Check for other symbols i.e. a semicolon.
                        self.display_error(self.INVALID_PORT, self.symbol)
                    return None, None
            else:
                # If input then syntax error
                if input_port:
                    self.display_error(self.PORT_ABSENT, self.prev_symbol,
                                       afterward=True)
                    return None, None
                else:
                    return device_id, None
        else:
            self.display_error(self.NOT_DEVICE_NAME, self.symbol)
            return None, None

    def connection(self):
        """Parse a single line in the connection list.

        Make the connection if there are no errors.
        """
        [out_device_id, out_port_id] = self.signame(input_port=False)
        if (out_device_id, out_port_id) != (None, None):
            if self.symbol.type == self.scanner.EQUALS:
                self.symbol = self.scanner.get_symbol()
                [in_device_id, in_port_id] = self.signame()
                if (in_device_id, in_port_id) != (None, None):
                    if self.symbol.type != self.scanner.SEMICOLON:
                        self.display_error(self.NO_SEMICOLON, self.prev_symbol,
                                           afterward=True)
            else:
                self.display_error(self.NO_EQUALS, self.prev_symbol,
                                   afterward=True)
        # If no errors, make the connection
        if self.error_count == 0:
            error_type = self.network.make_connection(in_device_id, in_port_id,
                                                      out_device_id,
                                                      out_port_id)
            if error_type != self.network.NO_ERROR:
                self.display_error(error_type, self.symbol, False)
        # If semicolon not missing, grab the next symbol
        if self.symbol.type == self.scanner.SEMICOLON:
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()

    def connection_list(self):
        """Parse the connection list."""
        [CONNECT_ID, MONITOR_ID] = self.names.lookup(["CONNECT", "MONITOR"])
        if (self.symbol.type == self.scanner.KEYWORD and
           self.symbol.id == CONNECT_ID):
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
            else:
                self.display_error(self.NO_LEFT_CURLY, self.prev_symbol,
                                   afterward=True)
            while self.symbol.type != self.scanner.RIGHT_CURLY:
                if (self.symbol.id == MONITOR_ID or
                   self.symbol.type == self.scanner.EOF):
                    self.display_error(self.NO_RIGHT_CURLY, self.prev_symbol,
                                       afterward=True)
                    break
                else:
                    self.connection()
            # If right curly not missing, grab the next symbol
            if self.symbol.type == self.scanner.RIGHT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
        else:
            self.display_error(self.NO_CONNECT_KEYWORD, self.symbol)
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
                while self.symbol.type != self.scanner.RIGHT_CURLY:
                    if (self.symbol.id == MONITOR_ID or
                       self.symbol.type == self.scanner.EOF):
                        self.display_error(self.NO_RIGHT_CURLY,
                                           self.prev_symbol, afterward=True)
                        break
                    else:
                        self.connection()
                # If right curly not missing, grab the next symbol
                if self.symbol.type == self.scanner.RIGHT_CURLY:
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
            else:
                # If missing both the keyword and left curly
                self.error_recovery(self.NO_LIST)  # Assume missing list

    def assign_monitor(self):
        """Parse a single line in the monitor list.

        Add the monitor if no errors.
        """
        monitor_device, monitor_port = self.signame(input_port=False)
        if (monitor_device, monitor_port) != (None, None):
            if self.symbol.type != self.scanner.SEMICOLON:
                self.display_error(self.NO_SEMICOLON, self.prev_symbol,
                                   afterward=True)
        # If no errors, make the monitor
        if self.error_count == 0:
            error_type = self.monitors.make_monitor(monitor_device,
                                                    monitor_port)
            if error_type != self.monitors.NO_ERROR:
                self.display_error(error_type, self.symbol, False)
        # If semicolon not missing, grab the next symbol
        if self.symbol.type == self.scanner.SEMICOLON:
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()

    def monitor_list(self):
        """Parse the monitor list."""
        [MONITOR_ID, END_ID] = self.names.lookup(["MONITOR", "END"])
        if (self.symbol.type == self.scanner.KEYWORD and
           self.symbol.id == MONITOR_ID):
            self.prev_symbol = self.symbol
            self.symbol = self.scanner.get_symbol()
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
            else:
                self.display_error(self.NO_LEFT_CURLY, self.prev_symbol,
                                   afterward=True)
            while self.symbol.type != self.scanner.RIGHT_CURLY:
                if (self.symbol.id == END_ID or
                   self.symbol.type == self.scanner.EOF):
                    self.display_error(self.NO_RIGHT_CURLY, self.prev_symbol,
                                       afterward=True)
                    break
                else:
                    self.assign_monitor()
            # If right curly not missing, grab the next symbol
            if self.symbol.type == self.scanner.RIGHT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
        else:
            self.display_error(self.NO_MONITOR_KEYWORD, self.symbol)
            if self.symbol.type == self.scanner.LEFT_CURLY:
                self.prev_symbol = self.symbol
                self.symbol = self.scanner.get_symbol()
                while self.symbol.type != self.scanner.RIGHT_CURLY:
                    if (self.symbol.id == END_ID or
                       self.symbol.type == self.scanner.EOF):
                        self.display_error(self.NO_RIGHT_CURLY,
                                           self.prev_symbol, afterward=True)
                        break
                    else:
                        self.assign_monitor()
                # If right curly not missing, grab the next symbol
                if self.symbol.type == self.scanner.RIGHT_CURLY:
                    self.prev_symbol = self.symbol
                    self.symbol = self.scanner.get_symbol()
            else:
                # If missing both the keyword and left curly
                self.error_recovery(self.NO_LIST)  # Assume missing list

    def parse_network(self):
        """Parse the circuit definition file.

        Return True if there are no errors in the circuit definition file.
        """
        self.symbol = self.scanner.get_symbol()
        # Check if the circuit definition file is empty
        if self.symbol.type == self.scanner.EOF:
            self.error_count += 1
            self.print_message("Error: Cannot parse an empty text file")
        else:
            # Parse Device List
            self.device_list()

            # Parse Connection List
            self.connection_list()
            # Check if all inputs are connected
            if self.error_count == 0:
                inputs_connected = self.network.check_network()
                if not inputs_connected:
                    self.error_count += 1
                    self.print_message("Semantic Error: Not all inputs "
                                       + "in the network are connnected")

            # Parse Monitor List
            self.monitor_list()

            # Check for END
            [END_ID] = self.names.lookup(["END"])
            if self.symbol.id == END_ID:
                self.symbol = self.scanner.get_symbol()
                if self.symbol.type != self.scanner.EOF:
                    self.display_error(self.AFTER_END, self.symbol)
            else:
                self.display_error(self.NO_END, self.prev_symbol,
                                   afterward=True)

        # Return True if self.error_count is 0
        if self.error_count == 0:
            return True
        else:
            # Display total number of errors
            if self.error_count == 1:
                (final_message) = ("Total of " + str(self.error_count) +
                                   " error detected")
            else:
                (final_message) = ("Total of " + str(self.error_count) +
                                   " errors detected")
            self.print_message(final_message)
            return False
