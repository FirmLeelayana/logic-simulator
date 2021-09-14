"""Read the circuit definition file and translate the characters into symbols.

Used in the Logic Simulator project to read the characters in the definition
file and translate them into symbols that are usable by the parser.

Classes
-------
Scanner - reads definition file and translates characters into symbols.
Symbol - encapsulates a symbol and stores its properties.
"""

import sys


class Symbol:
    """Encapsulate a symbol and store its properties.

    Parameters
    ----------
    No parameters.

    Public methods
    --------------
    No public methods.
    """

    def __init__(self):
        """Initialise symbol properties."""
        self.type = None  # Int, representation of type of symbol.
        self.id = None  # Int, for KEYWORD, NAME, NUMBER. Str, for LOGIC.
        self.line_number = None  # Int, starts from 1.
        self.line_position = None  # Int, starts from 1.


class Scanner:
    """Read circuit definition file and translate the characters into symbols.

    Once supplied with the path to a valid definition file, the scanner
    translates the sequence of characters in the definition file into symbols
    that the parser can use. It also skips over comments and irrelevant
    formatting characters, such as spaces and line breaks.

    Parameters
    ----------
    path: path to the circuit definition file.
    names: instance of the names.Names() class.

    Public methods
    -------------
    get_name(self): Assumes current character is a letter, returns the names
                    string, and places the next non-alphanumeric character
                    in current_character.
    get_number(self): Assumes current character is a digit, returns the integer
                      number, and places next non-digit character in
                      current_character.
    get_logic_level(self): Assumes current character is a dash (-) or
                           underscore (_), returns the sequence of underscores
                           and dashes, and places the next non-dash and
                           non-underscore character in current_character.
    advance(self): Reads the next character from the definition file and places
                   it into current_character. Ignores line breaks.
    skip_spaces(self): Calls advance() as necessary until current_character is
                       a non white-space character.
    skip_comments(self): Calls advance() as necessary to ignore comments,
                         which start and end with #.
    get_line_position(self, symbol): Updates line position and line number
                                     attributes of a given symbol with the
                                     position of the current_character.
    get_symbol(self): Translates the next sequence of characters into a symbol
                      and returns the symbol.
    print_pointer(self, symbol,
                  pointer=True, after=False): Returns current
                                              input line, along with an
                                              optional marker on following
                                              line to show where an error
                                              has occurred.
    """

    def __init__(self, path, names):
        """Open specified file and initialise reserved words and IDs."""
        # Open specified file.
        windows_ending = b"\r\n"
        unix_mac_ending = b"\n"
        if not isinstance(path, str):
            raise TypeError("Expected path to be a string.")
        try:
            # Convert CRLF to LF form.
            with open(path, "rb") as opened_file:
                file_contents = opened_file.read()
            file_contents = file_contents.replace(windows_ending,
                                                  unix_mac_ending)
            with open(path, "wb") as open_file:
                open_file.write(file_contents)
            self.file_object = open(path, "r")
            self.path = path
        except IOError as arg:  # Path file does not exist.
            print("File does not exist. Please enter a valid path.\n", arg)
            sys.exit()

        # Creating an instance of the Names class.
        self.names = names

        # Defining all the symbol types, and their corresponding int IDs.
        self.list_symbol_types = [self.LEFT_CURLY, self.RIGHT_CURLY,
                                  self.EQUALS, self.COMMA, self.COLON,
                                  self.LEFT_BRACKET, self.RIGHT_BRACKET,
                                  self.SEMICOLON, self.DOT, self.KEYWORD,
                                  self.NUMBER, self.NAME, self.EOF,
                                  self.ERROR, self.LOGIC] = range(15)

        # Defining all the keywords for our logic description language.
        self.list_keywords = ["DEVICES", "CONNECT", "MONITOR", "END",
                              "CLOCK", "SWITCH", "AND", "NAND", "OR",
                              "NOR", "DTYPE", "XOR", "Q", "QBAR",
                              "DATA", "CLK", "SET", "CLEAR", "I1",
                              "I2", "I3", "I4", "I5", "I6", "I7",
                              "I8", "I9", "I10", "I11", "I12", "I13",
                              "I14", "I15", "I16", "cycle",
                              "initial_state", "number_of_inputs",
                              "SIGGEN", "waveform"]

        # Holds last character read from definition file.
        self.current_character = " "

        # Store all keywords in our Names instance.
        self.names.lookup(self.list_keywords)

    def get_name(self):
        """Return the alphanumeric name string, updates current_character."""
        if not isinstance(self.current_character, str):
            raise TypeError("Expected current_character to be a string.")
        elif not self.current_character.isalpha():
            raise TypeError("Expected current_character to be alphabetical.")
        elif len(self.current_character) != 1:
            raise TypeError("Expected current_character to be one letter.")
        # Initialise a name_string to concatenate to.
        name_string = str(self.current_character)
        self.current_character = self.file_object.read(1)
        # Considering underscore as alphanumerical.
        while (self.current_character.isalnum()
               or self.current_character == "_"):
            name_string += str(self.current_character)
            self.current_character = self.file_object.read(1)
        return name_string

    def get_number(self):
        """Return the integer number, and updates current_character."""
        if not isinstance(self.current_character, str):
            raise TypeError("Expected current_character to be a string.")
        elif not self.current_character.isdigit():
            raise TypeError("Expected current_character to be a digit.")
        elif len(self.current_character) != 1:
            raise TypeError("Expected current_character to be a single digit.")
        # Initialise a number_string to concatenate to.
        number_string = self.current_character
        self.current_character = self.file_object.read(1)
        while self.current_character.isdigit():
            number_string += str(self.current_character)
            self.current_character = self.file_object.read(1)
        return int(number_string)

    def get_logic_level(self):
        """Return the sequence of '-' and '_', and update current_character."""
        if not isinstance(self.current_character, str):
            raise TypeError("Expected current_character to be a string.")
        elif len(self.current_character) != 1:
            raise TypeError("Expected current_character to be a single digit.")
        elif not (self.current_character == "_"
                  or self.current_character == "-"):
            raise ValueError("Expected current_character to be '_' or '-'.")
        # Initialise a sequence_string to concatenate to.
        sequence_string = str(self.current_character)
        self.current_character = self.file_object.read(1)
        # Obtaining sequence of dashes and underscores.
        while (self.current_character == "_" or self.current_character == "-"):
            sequence_string += str(self.current_character)
            self.current_character = self.file_object.read(1)
        return sequence_string

    def advance(self):
        """Places next character into current_character."""
        self.current_character = self.file_object.read(1)
        # Accounting for EOL.
        if self.current_character == "\n":
            self.advance()

    def skip_spaces(self):
        """Places the next non white-space character into current_character."""
        while self.current_character.isspace():
            self.advance()

    def skip_comments(self):
        """Ignores the comment."""
        if self.current_character == "#":
            while True:
                self.advance()
                if self.current_character == "#":
                    self.advance()
                    break
                elif self.current_character == "":  # Reaches end of file.
                    break

    def get_line_position(self, symbol):
        """Update line position and number attributes of the given symbol."""
        if not isinstance(symbol, Symbol):
            raise TypeError("Expected symbol to be of the Symbol class.")
        # Get current position (tell adds one when \n found).
        position = self.file_object.tell()
        # Get length of each line in the file.
        file_object = open(self.path, "r")
        cumul_len_dict = {}
        cumulative_length_list = []
        total = 0  # Represents total characters up to that line.
        for number, line in enumerate(file_object):
            if "\n" in line:  # Finding lines with \n.
                length = len(line.rstrip("\n"))
                # Adding one to account for \n in LF, to work with tell().
                total += length + 1
            else:
                total += len(line)
            # Append to list and dict.
            cumul_len_dict[number] = total
            cumulative_length_list.append((number, total))
        file_object.close()
        # Obtain line number and position (starts from 1).
        for line_number, total_length in cumulative_length_list:
            # If position is less than cumulative characters total
            # up to and including that line, must be on that line.
            if position <= total_length:
                symbol.line_number = line_number + 1
                if symbol.line_number == 1:
                    symbol.line_position = position
                else:  # Accounting for previous lines.
                    symbol.line_position = (position
                                            - cumul_len_dict[line_number - 1])
                break

    def get_symbol(self):
        """Translate the next sequence of characters into a symbol."""
        my_symbol = Symbol()
        # Skip over comments and whitespaces.
        while (self.current_character.isspace()
               or self.current_character == "#"):
            self.skip_spaces()
            self.skip_comments()
            self.skip_spaces()
        # Skip over newlines.
        if self.current_character == "\n":
            self.advance()

        if self.current_character.isalpha():  # Start of a name/keyword.
            name_string = self.get_name()  # Get the alphanumeric name_string.
            if name_string in self.list_keywords:
                my_symbol.type = self.KEYWORD
            else:
                my_symbol.type = self.NAME
            # Grab ID of symbol.
            [my_symbol.id] = self.names.lookup([name_string])
            if self.current_character == "":
                # Accounting for EOF.
                pass
            else:
                # Go back a single character (in LF format).
                self.file_object.seek(self.file_object.tell() - 1)

        elif self.current_character.isdigit():  # Start of a number.
            my_symbol.type = self.NUMBER
            my_symbol.id = self.get_number()  # ID is the integer itself.
            if self.current_character == "":
                # Accounting for EOF.
                pass
            else:
                # Go back a single character (in LF format).
                self.file_object.seek(self.file_object.tell() - 1)

        elif (self.current_character == "-" or self.current_character == "_"):
            # Start of sequence of '-' and '_'.
            my_symbol.type = self.LOGIC
            my_symbol.id = self.get_logic_level()  # String sequence.
            if self.current_character == "":
                # Accounting for EOF.
                pass
            else:
                # Go back a single character (in LF format).
                self.file_object.seek(self.file_object.tell() - 1)

        elif self.current_character == "=":
            my_symbol.type = self.EQUALS

        elif self.current_character == "{":
            my_symbol.type = self.LEFT_CURLY

        elif self.current_character == "}":
            my_symbol.type = self.RIGHT_CURLY

        elif self.current_character == ",":
            my_symbol.type = self.COMMA

        elif self.current_character == ":":
            my_symbol.type = self.COLON

        elif self.current_character == "(":
            my_symbol.type = self.LEFT_BRACKET

        elif self.current_character == ")":
            my_symbol.type = self.RIGHT_BRACKET

        elif self.current_character == ";":
            my_symbol.type = self.SEMICOLON

        elif self.current_character == ".":
            my_symbol.type = self.DOT

        elif self.current_character == "":  # End of file.
            my_symbol.type = self.EOF

        else:  # Not a valid character.
            my_symbol.type = self.ERROR

        # Get line position, and advance one character.
        self.get_line_position(my_symbol)
        if self.current_character != "":  # Accounting for EOF.
            self.advance()

        return my_symbol

    def print_pointer(self, symbol, pointer=True, after=False):
        """Return current input line, and an optional error pointer."""
        if not isinstance(symbol, Symbol):
            raise TypeError("Expected symbol to be a Symbol object.")
        elif not isinstance(symbol.line_number, int):
            raise TypeError("Expected symbol to have an integer line_number.")
        elif not isinstance(symbol.line_position, int):
            raise TypeError("Expected an integer line_position attribute.")

        # Store current input line.
        message = ""
        file_object = open(self.path, "r")
        for number, line in enumerate(file_object):
            if number == (symbol.line_number - 1):
                message += str(line.rstrip()) + "\n"

        # Optional marker to show where error occurred.
        if pointer:
            sequence = ""
            if after:
                # Print pointer after the current character.
                line_position = symbol.line_position + 1
            else:
                # Marker points to the middle of NAME, KEYWORD, NUMBER, LOGIC.
                if symbol.type == self.KEYWORD or symbol.type == self.NAME:
                    name_length = len(self.names.get_name_string(symbol.id))//2
                    line_position = symbol.line_position - name_length
                elif symbol.type == self.NUMBER or symbol.type == self.LOGIC:
                    line_position = (symbol.line_position
                                     - (len(str(symbol.id))//2))
                # Otherwise, point to last character of sequence.
                else:
                    line_position = symbol.line_position
            for _ in range(line_position - 1):
                sequence += " "
            message += sequence + "^" + "\n"

        return message
