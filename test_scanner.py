"""Test the scanner module."""
import pytest
import io

from scanner import Symbol, Scanner
from names import Names


# Suite of unit tests for the Symbol class.
@pytest.fixture
def default_symbol():
    """Return a new, default symbols instance."""
    return Symbol()


@pytest.fixture
def new_symbol():
    """Returns a Symbol instance, after defining all of its attributes."""
    my_symbol = Symbol()
    my_symbol.type = 0
    my_symbol.id = 2
    my_symbol.line_number = 23
    my_symbol.line_position = 4
    return my_symbol


def test_initialisation(default_symbol, new_symbol):
    """Test if attributes of the Symbol class returns the expected output."""
    # Default instance of Symbol.
    assert default_symbol.type is None
    assert default_symbol.id is None
    assert default_symbol.line_number is None
    assert default_symbol.line_position is None
    # Defined instance of Symbol.
    assert new_symbol.type == 0
    assert new_symbol.id == 2
    assert new_symbol.line_number == 23
    assert new_symbol.line_position == 4
    # Assert that it has the correct output type.
    assert isinstance(new_symbol.type, int)
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.line_number, int)
    assert isinstance(new_symbol.line_position, int)


# Suite of unit tests for the Scanner class.
@pytest.fixture
def default_scanner():
    """Return a new, default scanner instance."""
    my_name = Names()
    my_path = "example_text_files/example.txt"
    return Scanner(my_path, my_name)


@pytest.fixture
def example_one_scanner():
    """Return a scanner instance using 1st example file."""
    my_name = Names()
    my_path = "example_text_files/example.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "A"
    return my_scanner


@pytest.fixture
def example_two_scanner():
    """Return a scanner instance using 2nd example file."""
    my_name = Names()
    my_path = "example_text_files/example_two.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "A"
    return my_scanner


@pytest.fixture
def example_three_scanner():
    """Return a scanner instance using 3rd example file."""
    my_name = Names()
    my_path = "example_text_files/example_three.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "A"
    return my_scanner


@pytest.fixture
def example_four_scanner():
    """Return a scanner instance using 4th example file."""
    my_name = Names()
    my_path = "example_text_files/example_four.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "2"
    return my_scanner


@pytest.fixture
def example_five_scanner():
    """Return a scanner instance using 5th example file."""
    my_name = Names()
    my_path = "example_text_files/example_five.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "2"
    return my_scanner


@pytest.fixture
def example_six_scanner():
    """Return a scanner instance using 6th example file."""
    my_name = Names()
    my_path = "example_text_files/example_six.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "2"
    return my_scanner


@pytest.fixture
def example_fifteen_scanner():
    """Return a scanner instance using 15th example file."""
    my_name = Names()
    my_path = "example_text_files/example_fifteen.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "-"
    return my_scanner


@pytest.fixture
def example_sixteen_scanner():
    """Return a scanner instance using 16th example file."""
    my_name = Names()
    my_path = "example_text_files/example_sixteen.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = "-"
    return my_scanner


@pytest.fixture
def default_names():
    """Return a new, default names instance."""
    my_name = Names()
    return my_name


@pytest.fixture
def error_names():
    """Returns a name instance, after adding 3 error codes."""
    my_name = Names()
    my_name.unique_error_codes(3)
    return my_name


@pytest.fixture
def name_string_list():
    """Return a list of example names."""
    return ["Dave", "David", "Daniel"]


@pytest.fixture
def with_names(name_string_list):
    """Return a names instance, after three names have been added."""
    my_name = Names()
    my_name.lookup(name_string_list)
    return my_name


@pytest.mark.parametrize("path", [
    (2),
    (1.22),
    ([1, 2]),
])
def test_scanner_init_raises_exceptions(default_names, path):
    """Test if Scanner initialisation raises expected exceptions."""
    # Checking if path is a string.
    with pytest.raises(TypeError):
        Scanner(path, default_names)


def test_scanner_initialisation(default_scanner):
    """Test if attributes of the Scanner class returns the expected output."""
    # Check list_symbol_types was defined correctly.
    assert default_scanner.list_symbol_types == range(15)
    # Check that each symbol in list_symbol_types is an int.
    for symbol in default_scanner.list_symbol_types:
        assert isinstance(symbol, int)
    # Check that list_keywords is a list.
    assert isinstance(default_scanner.list_keywords, list)
    # Check that each symbol in list_keywords is a str.
    for keyword in default_scanner.list_keywords:
        assert isinstance(keyword, str)
    # Check that scanner.names is a Names instance.
    assert isinstance(default_scanner.names, Names)
    assert isinstance(default_scanner.file_object, io.IOBase)


@pytest.mark.parametrize("current_char", [
    (1.4),  # If current character is not a string.
    (1),
    (["Hello"]),
    ("("),  # If current character is not alphabetical.
    (" "),
    ("."),
    ("Hello")  # If current character is not a single letter.
])
def test_get_name_raises_exceptions(current_char):
    """Test if get_name method raises expected exceptions."""
    my_name = Names()
    my_path = "example_text_files/example.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = current_char
    with pytest.raises(TypeError):
        my_scanner.get_name()


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
])
def test_get_name(example_one_scanner, example_two_scanner,
                  example_three_scanner, path):
    """Test if get_name method returns the expected output."""
    # First example file.
    assert example_one_scanner.get_name() == "ADEVICES"
    # Second example file.
    assert example_two_scanner.get_name() == "Axor_123"
    # Third example file.
    assert example_three_scanner.get_name() == "Axor123"
    # Check that only a single digit will be returned.
    my_scanner = Scanner("example_text_files/example_six.txt", Names())
    my_scanner.current_character = "c"
    assert my_scanner.get_name() == "c"
    # Check that current character is updated.
    assert my_scanner.current_character == "("
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "A"
    my_scanner.get_name()
    assert my_scanner.current_character == " "
    my_scanner = Scanner("example_text_files/example_three.txt", Names())
    my_scanner.current_character = "A"
    my_scanner.get_name()
    assert my_scanner.current_character == "."


@pytest.mark.parametrize("current_char", [
    (1.4),  # If current character is not a string.
    (1),
    (["Hello"]),
    ("H"),  # If current character is not a digit.
    (" "),
    ("."),
    ("Hello"),
    ("32232")  # If current character is not a single digit.
])
def test_get_number_raises_exceptions(current_char):
    """Test if get_number method raises expected exceptions."""
    my_name = Names()
    my_path = "example_text_files/example.txt"
    my_scanner = Scanner(my_path, my_name)
    my_scanner.current_character = current_char
    with pytest.raises(TypeError):
        my_scanner.get_number()


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
    ("example_text_files/example_three.txt"),
])
def test_get_number(example_four_scanner, example_five_scanner,
                    example_six_scanner, path):
    """Test if get_number method returns the expected output."""
    # Fourth example file.
    assert example_four_scanner.get_number() == 2123232
    # Fifth example file.
    assert example_five_scanner.get_number() == 22
    # Sixth example file.
    assert example_six_scanner.get_number() == 2
    # Check that only a single digit will be returned.
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "1"
    assert my_scanner.get_number() == 1
    # Check that the current_character updates correctly.
    my_scanner = Scanner("example_text_files/example_four.txt", Names())
    my_scanner.current_character = "1"
    assert my_scanner.get_number() == 1123232
    assert my_scanner.current_character == " "
    another_scanner = Scanner("example_text_files/example_five.txt", Names())
    another_scanner.current_character = "1"
    assert another_scanner.get_number() == 12
    assert another_scanner.current_character == "t"


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
    ("example_text_files/example_three.txt"),
    ("example_text_files/example_four.txt"),
    ("example_text_files/example_five.txt"),
    ("example_text_files/example_six.txt")
])
def test_advance(path):
    """Test if advance method updates the current_character."""
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "1"
    my_scanner.advance()
    file_object = open(path, "r")
    for _ in range(2):
        assert my_scanner.current_character == file_object.read(1)
        my_scanner.advance()
    assert my_scanner.current_character == file_object.read(1)
    file_object.close()
    # Testing if it ignores EOL.
    new_scanner = Scanner("example_text_files/example.txt", Names())
    new_scanner.current_character = "D"
    for _ in range(10):
        new_scanner.advance()
    assert new_scanner.current_character == "x"


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
    ("example_text_files/example_three.txt"),
    ("example_text_files/example_four.txt"),
    ("example_text_files/example_five.txt"),
    ("example_text_files/example_six.txt")
])
def test_skip_spaces(path):
    """Test if skip_spaces method updates the current_character."""
    # When current character is not a space.
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "r"
    my_scanner.skip_spaces()
    assert my_scanner.current_character == "r"
    # When current character is a space.
    my_scanner.current_character = " "
    my_scanner.skip_spaces()
    file_object = open(path, "r")
    assert my_scanner.current_character == file_object.read(1)
    # Using example test file seven.
    new_scanner = Scanner("example_text_files/example_seven.txt", Names())
    new_scanner.current_character = " "
    new_scanner.skip_spaces()
    assert new_scanner.current_character == "s"
    file_object.close()


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
    ("example_text_files/example_three.txt"),
])
def test_skip_comments(path):
    """Test if skip_comments method updates the current_character."""
    # When current character is not a comment.
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "r"
    my_scanner.skip_comments()
    assert my_scanner.current_character == "r"
    # When current character is a comment, and has an end.
    new_scanner = Scanner("example_text_files/example_eight.txt", Names())
    new_scanner.current_character = "#"
    new_scanner.skip_comments()
    assert new_scanner.current_character == " "
    # When current character is a comment, and has no end.
    next_scanner = Scanner(path, Names())
    next_scanner.current_character = "#"
    next_scanner.skip_comments()
    assert next_scanner.current_character == ""


def test_get_line_position_raises_exceptions(default_scanner):
    """Test if get_line_position method raises expected exceptions."""
    with pytest.raises(TypeError):
        default_scanner.get_line_position("5")
    with pytest.raises(TypeError):
        default_scanner.get_line_position(5)
    with pytest.raises(TypeError):
        default_scanner.get_line_position(["5"])


def test_get_line_position():
    """Test if get_line_position method updates the Symbol attributes."""
    # "S"
    my_scanner = Scanner("example_text_files/example.txt", Names())
    for _ in range(7):
        my_scanner.advance()
    my_symbol = Symbol()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 1
    assert my_symbol.line_position == 7
    assert my_scanner.current_character == "S"
    # "{"
    for _ in range(2):
        my_scanner.advance()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 1
    assert my_symbol.line_position == 9
    assert my_scanner.current_character == "{"
    # "x"
    my_scanner.advance()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 2
    assert my_symbol.line_position == 1
    assert my_scanner.current_character == "x"
    # ";"
    for _ in range(10):
        my_scanner.advance()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 2
    assert my_symbol.line_position == 11
    assert my_scanner.current_character == ";"
    # "a"
    my_scanner.advance()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 3
    assert my_symbol.line_position == 1
    assert my_scanner.current_character == "a"
    # EOF, ""
    for _ in range(300):
        my_scanner.advance()
    my_scanner.get_line_position(my_symbol)
    assert my_symbol.line_number == 20
    assert my_symbol.line_position == 3
    assert my_scanner.current_character == ""


def test_get_symbol():
    """Test if get_symbol method returns the expected output."""
    # Example text file nine, check correct sequence of symbols returned.
    my_scanner = Scanner("example_text_files/example_nine.txt", Names())
    # Handles end of line correctly for keyword.
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.KEYWORD
    assert [my_symbol.id] == my_scanner.names.lookup(["DEVICES"])
    assert my_symbol.line_number == 1
    assert my_symbol.line_position == 7
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)
    # Handles end of line correctly for name.
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.NAME
    assert [my_symbol.id] == my_scanner.names.lookup(["device2"])
    assert my_symbol.line_number == 2
    assert my_symbol.line_position == 7
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)
    # Handles end of line correctly for number.
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.NUMBER
    assert my_symbol.id == 123
    assert my_symbol.line_number == 3
    assert my_symbol.line_position == 3
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)
    # Handles EOF correctly.
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.NAME
    assert [my_symbol.id] == my_scanner.names.lookup(["Something"])
    assert my_symbol.line_number == 4
    assert my_symbol.line_position == 9
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)

    # Example text file ten, check correct sequence of symbols returned.
    # Extensive testing of all possible combinations.
    new_scanner = Scanner("example_text_files/example_ten.txt", Names())
    # DEVICES
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == my_scanner.KEYWORD
    assert [new_symbol.id] == my_scanner.names.lookup(["DEVICES"])
    assert new_symbol.line_number == 1
    assert new_symbol.line_position == 7
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.type, int)
    # {
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.LEFT_CURLY
    assert new_symbol.id is None
    assert new_symbol.line_number == 1
    assert new_symbol.line_position == 9
    assert isinstance(new_symbol.type, int)
    # xor1
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.NAME
    assert [new_symbol.id] == new_scanner.names.lookup(["xor1"])
    assert new_symbol.line_number == 2
    assert new_symbol.line_position == 4
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.type, int)
    # =
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.EQUALS
    assert new_symbol.id is None
    assert new_symbol.line_number == 2
    assert new_symbol.line_position == 6
    assert isinstance(new_symbol.type, int)
    # XOR
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.KEYWORD
    assert [new_symbol.id] == new_scanner.names.lookup(["XOR"])
    assert new_symbol.line_number == 2
    assert new_symbol.line_position == 10
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.type, int)
    # ;
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.SEMICOLON
    assert new_symbol.id is None
    assert new_symbol.line_number == 2
    assert new_symbol.line_position == 11
    assert isinstance(new_symbol.type, int)
    # (
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.LEFT_BRACKET
    assert new_symbol.id is None
    assert new_symbol.line_number == 3
    assert new_symbol.line_position == 1
    assert isinstance(new_symbol.type, int)
    # number_of_inputs
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.KEYWORD
    assert [new_symbol.id] == new_scanner.names.lookup(["number_of_inputs"])
    assert new_symbol.line_number == 3
    assert new_symbol.line_position == 17
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.type, int)
    # :
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.COLON
    assert new_symbol.id is None
    assert new_symbol.line_number == 3
    assert new_symbol.line_position == 18
    assert isinstance(new_symbol.type, int)
    # 2
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.NUMBER
    assert new_symbol.id == 2
    assert new_symbol.line_number == 3
    assert new_symbol.line_position == 19
    assert isinstance(new_symbol.type, int)
    # )
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.RIGHT_BRACKET
    assert new_symbol.id is None
    assert new_symbol.line_number == 3
    assert new_symbol.line_position == 20
    assert isinstance(new_symbol.type, int)
    # ".", also checks if it can handle trailing whitespaces.
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.DOT
    assert new_symbol.id is None
    assert new_symbol.line_number == 4
    assert new_symbol.line_position == 1
    assert isinstance(new_symbol.type, int)
    # I2
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.KEYWORD
    assert [new_symbol.id] == new_scanner.names.lookup(["I2"])
    assert new_symbol.line_number == 4
    assert new_symbol.line_position == 3
    assert isinstance(new_symbol.id, int)
    assert isinstance(new_symbol.type, int)
    # ,
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.COMMA
    assert new_symbol.id is None
    assert new_symbol.line_number == 4
    assert new_symbol.line_position == 6
    assert isinstance(new_symbol.type, int)
    # @, not a valid character.
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.ERROR
    assert new_symbol.id is None
    assert new_symbol.line_number == 4
    assert new_symbol.line_position == 8
    assert isinstance(new_symbol.type, int)
    # }, and skips the comment.
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.RIGHT_CURLY
    assert new_symbol.id is None
    assert new_symbol.line_number == 5
    assert new_symbol.line_position == 1
    assert isinstance(new_symbol.type, int)
    # Checks if it can handle EOF, "".
    new_symbol = new_scanner.get_symbol()
    assert new_symbol.type == new_scanner.EOF
    assert new_symbol.id is None
    assert new_symbol.line_number == 5
    assert new_symbol.line_position == 2
    assert isinstance(new_symbol.type, int)

    # Example text file eleven, check it can handle new lines.
    my_scanner = Scanner("example_text_files/example_eleven.txt", Names())
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.KEYWORD
    assert [my_symbol.id] == my_scanner.names.lookup(["DEVICES"])
    assert my_symbol.line_number == 2
    assert my_symbol.line_position == 7
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)

    # Example text file twelve, check it can handle multiple comments.
    my_scanner = Scanner("example_text_files/example_twelve.txt", Names())
    for _ in range(3):
        my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.NAME
    assert [my_symbol.id] == my_scanner.names.lookup(["xor1"])
    assert my_symbol.line_number == 2
    assert my_symbol.line_position == 4
    assert isinstance(my_symbol.id, int)
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.line_number, int)
    assert isinstance(my_symbol.line_position, int)

    # Example text file fourteen, check that comment handling is as expected.
    # Check that comments in between a keyword is rejected.
    my_scanner = Scanner("example_text_files/example_fourteen.txt", Names())
    my_symbol = my_scanner.get_symbol()
    assert my_symbol.type != my_scanner.KEYWORD
    assert my_symbol.type == my_scanner.NAME
    assert isinstance(my_symbol.type, int)
    # Check that spaces in between a keyword is rejected.
    for _ in range(2):
        my_symbol = my_scanner.get_symbol()
    assert my_symbol.type != my_scanner.KEYWORD
    assert my_symbol.type == my_scanner.NAME
    assert isinstance(my_symbol.type, int)
    # Check that comments within an input specification are accepted.
    for _ in range(2):
        my_symbol = my_scanner.get_symbol()
    # '('
    assert my_symbol.type == my_scanner.LEFT_BRACKET
    my_symbol = my_scanner.get_symbol()
    # 'number_of_inputs'
    assert my_symbol.type == my_scanner.KEYWORD
    my_symbol = my_scanner.get_symbol()
    # ':'
    assert my_symbol.type == my_scanner.COLON
    my_symbol = my_scanner.get_symbol()
    # '2'
    assert my_symbol.type == my_scanner.NUMBER
    my_symbol = my_scanner.get_symbol()
    # ')'
    assert my_symbol.type == my_scanner.RIGHT_BRACKET

    # Example text seventeen, check that LOGIC type gives expected output.
    my_scanner = Scanner("example_text_files/example_seventeen.txt", Names())
    my_symbol = my_scanner.get_symbol()
    # Check that first sequence is received.
    assert my_symbol.type == my_scanner.LOGIC
    assert my_symbol.id == "___"
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.id, str)
    # Check that second sequence is received.
    for _ in range(2):
        my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.LOGIC
    assert my_symbol.id == "--___--"
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.id, str)
    # Check that third sequence is received.
    for _ in range(7):
        my_symbol = my_scanner.get_symbol()
    assert my_symbol.type == my_scanner.LOGIC
    assert my_symbol.id == "-___---__---"
    assert isinstance(my_symbol.type, int)
    assert isinstance(my_symbol.id, str)


@pytest.mark.parametrize("test", [
    ("5"),
    (5.5),
    ([5])
])
def test_print_pointer_raises_exceptions(default_scanner, test):
    """Test if print_pointer method raises expected exceptions."""
    my_symbol = Symbol()
    my_symbol.line_position = test
    my_symbol.line_number = test
    with pytest.raises(TypeError):
        default_scanner.print_pointer("5")
    with pytest.raises(TypeError):
        default_scanner.print_pointer(5)
    with pytest.raises(TypeError):
        default_scanner.print_pointer(["5"])
    with pytest.raises(TypeError):
        default_scanner.print_pointer(my_symbol)


def test_print_pointer(default_scanner, capsys):
    """Test if print_pointer prints the correct statement."""
    # Handles keywords (odd length).
    my_symbol = default_scanner.get_symbol()
    message = default_scanner.print_pointer(my_symbol)
    print(message, end="")
    captured = capsys.readouterr()
    assert captured.out == "DEVICES {\n   ^\n"
    assert message == "DEVICES {\n   ^\n"

    # Optional argument for pointer works correctly.
    message = default_scanner.print_pointer(my_symbol,
                                            pointer=True)
    print(message, end="")
    captured_1 = capsys.readouterr()
    assert captured_1.out == "DEVICES {\n   ^\n"
    assert message == "DEVICES {\n   ^\n"
    message = default_scanner.print_pointer(my_symbol,
                                            pointer=False)
    print(message, end="")
    captured_2 = capsys.readouterr()
    assert captured_2.out == "DEVICES {\n"
    assert message == "DEVICES {\n"

    # Optional argument for pointer after works.
    message = default_scanner.print_pointer(my_symbol, pointer=True,
                                            after=False)
    print(message, end="")
    captured_3 = capsys.readouterr()
    assert captured_3.out == "DEVICES {\n   ^\n"
    assert message == "DEVICES {\n   ^\n"
    message = default_scanner.print_pointer(my_symbol, pointer=True,
                                            after=True)
    print(message, end="")
    captured_4 = capsys.readouterr()
    assert captured_4.out == "DEVICES {\n       ^\n"
    assert message == "DEVICES {\n       ^\n"

    # Handles punctuation.
    my_symbol = default_scanner.get_symbol()
    message = default_scanner.print_pointer(my_symbol)
    print(message, end="")
    captured_5 = capsys.readouterr()
    assert captured_5.out == "DEVICES {\n        ^\n"
    assert message == "DEVICES {\n        ^\n"

    # Handles names (even length).
    my_symbol = default_scanner.get_symbol()
    message = default_scanner.print_pointer(my_symbol)
    print(message, end="")
    captured_6 = capsys.readouterr()
    assert captured_6.out == "xor1 = XOR;\n ^\n"
    assert message == "xor1 = XOR;\n ^\n"

    # Handles numbers.
    for _ in range(10):
        my_symbol = default_scanner.get_symbol()
    message = default_scanner.print_pointer(my_symbol)
    print(message, end="")
    captured_7 = capsys.readouterr()
    line_one = "and1 = AND (number_of_inputs:2);\n"
    line_two = "                             ^\n"
    assert captured_7.out == line_one + line_two
    assert message == line_one + line_two

    # Handles LOGIC type without 'after' argument.
    my_scanner = Scanner("example_text_files/example_seventeen.txt", Names())
    my_symbol = my_scanner.get_symbol()
    message = my_scanner.print_pointer(my_symbol)
    print(message, end="")
    captured_8 = capsys.readouterr()
    assert captured_8.out == "___asdasd--___--\n ^\n"
    assert message == "___asdasd--___--\n ^\n"

    # Handles LOGIC type with 'after' argument.
    message = my_scanner.print_pointer(my_symbol, after=True)
    print(message, end="")
    captured_9 = capsys.readouterr()
    assert captured_9.out == "___asdasd--___--\n   ^\n"
    assert message == "___asdasd--___--\n   ^\n"


def test_additional_keywords(default_scanner):
    """Test if additional keywords added properly."""
    assert default_scanner.names.query("SIGGEN") is not None
    assert default_scanner.names.query("waveform") is not None


@pytest.mark.parametrize("current_char, other_char", [
    (5.3, "H"),
    (10, "1"),
    (["Hello"], "@"),
    ("Hello", "."),
    ("32232", "s"),
    ("__---__", "|")
])
def test_get_logic_level_raises_exceptions(example_one_scanner,
                                           current_char, other_char):
    """Test if get_logic_level method raises expected exceptions."""
    example_one_scanner.current_character = current_char
    # Current_character not a string or single character.
    with pytest.raises(TypeError):
        example_one_scanner.get_logic_level()
    # Not an underscore or dash.
    example_one_scanner.current_character = other_char
    with pytest.raises(ValueError):
        example_one_scanner.get_logic_level()


@pytest.mark.parametrize("path", [
    ("example_text_files/example.txt"),
    ("example_text_files/example_two.txt"),
    ("example_text_files/example_three.txt"),
])
def test_get_logic_level(example_fifteen_scanner,
                         example_sixteen_scanner, path):
    """Test if get_logic_level method returns the expected output."""
    # Check that only a single dash will be returned.
    my_scanner = Scanner(path, Names())
    my_scanner.current_character = "-"
    assert my_scanner.get_logic_level() == "-"
    # 15th example file. Checks current character updates correctly.
    assert example_fifteen_scanner.get_logic_level() == "----___---"
    assert example_fifteen_scanner.current_character == " "
    # 16th example file. Checks current character updates correctly.
    assert example_sixteen_scanner.get_logic_level() == "-___"
    assert example_sixteen_scanner.current_character == "a"
