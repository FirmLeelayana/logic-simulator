"""Test the names module."""
import pytest

from names import Names


@pytest.fixture
def default_name():
    """Return a new, default names instance."""
    return Names()


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


def test_initialisation(default_name, error_names, with_names):
    """Test if the attributes of the class returns the expected output."""
    # Name_list is empty.
    assert default_name.names_list == []
    # Name_list has 3 existing names.
    assert with_names.names_list == ["Dave", "David", "Daniel"]
    # Error codes = 0.
    assert default_name.error_code_count == 0
    # Error codes = 3.
    assert error_names.error_code_count == 3


def test_unique_error_codes_raises_exceptions(default_name):
    """Test if unique_error_codes method raises expected exceptions."""
    with pytest.raises(TypeError):
        default_name.unique_error_codes("Hello")
    with pytest.raises(TypeError):
        default_name.unique_error_codes(1.55)
    with pytest.raises(ValueError):
        default_name.unique_error_codes(-1)


def test_unique_error_codes(default_name, error_names):
    """Test if unique_error_codes method returns the expected output."""
    # Error codes = 0.
    assert default_name.unique_error_codes(0) == range(0)
    # Error codes = 3.
    assert default_name.unique_error_codes(3) == range(3)
    # Error codes = 3 when 3 error codes are already defined.
    assert error_names.unique_error_codes(3) == range(3, 6)


def test_query_raises_exceptions(default_name):
    """Test if query method raises expected exceptions."""
    with pytest.raises(TypeError):
        default_name.query(1)
    with pytest.raises(TypeError):
        default_name.query(1.55)
    with pytest.raises(TypeError):
        default_name.query(["David", "Daniel"])


@pytest.mark.parametrize("name_string, expected_id", [
    ("Dave", 0),
    ("David", 1),
    ("Daniel", 2),
])
def test_query(default_name, with_names, name_string, expected_id):
    """Test if query method returns the expected output."""
    assert with_names.query(name_string) == expected_id
    assert isinstance(with_names.query("Dave"), int)
    assert with_names.query("Alice") is None
    assert default_name.query("Alice") is None


def test_lookup_raises_exceptions(default_name):
    """Test if lookup method raises expected exceptions."""
    with pytest.raises(TypeError):
        default_name.query(1)
    with pytest.raises(TypeError):
        default_name.query(1.55)
    with pytest.raises(TypeError):
        default_name.query([1])
    with pytest.raises(TypeError):
        default_name.query(["David", "Dave", 2.123])
    with pytest.raises(TypeError):
        default_name.query(["David", ["Alice", "Bob"]])
    with pytest.raises(TypeError):
        default_name.query([])


@pytest.mark.parametrize("name_string, expected_id", [
    ("Dave", 0),
    ("David", 1),
    ("Daniel", 2),
])
def test_lookup(with_names, default_name, name_string, expected_id):
    """Test if lookup method returns the expected output."""
    assert with_names.lookup([name_string]) == [expected_id]
    assert default_name.lookup(["Alan"]) == [0]
    assert default_name.lookup(["Alan", "Alice", "Daniel"]) == [0, 1, 2]
    assert with_names.lookup(["Dave", "David", "Daniel"]) == [0, 1, 2]
    assert with_names.lookup(["Daniel"]) == [2]
    assert with_names.lookup(["David", "Dave", "Alice",
                              "Daniel", "Tanner"]) == [1, 0, 3, 2, 4]
    # The output is returned as a list.
    assert isinstance(default_name.lookup(["Alan", "Alice", "Daniel"]), list)
    # Each ID in output is an integer.
    for id in with_names.lookup(["Dave", "David", "Daniel"]):
        assert isinstance(id, int)


def test_get_name_string_raises_exceptions(with_names):
    """Test if get_name_string method raises expected exceptions."""
    with pytest.raises(TypeError):
        with_names.get_name_string(1.4)
    with pytest.raises(TypeError):
        with_names.get_name_string("hello")
    with pytest.raises(ValueError):
        with_names.get_name_string(-1)


@pytest.mark.parametrize("name_id, expected_string", [
    (0, "Dave"),
    (1, "David"),
    (2, "Daniel"),
    (3, None)
])
def test_get_name_string(with_names, default_name, name_id, expected_string):
    """Test if get_name_string method returns the expected string."""
    # Name is present.
    assert with_names.get_name_string(name_id) == expected_string
    # Name is absent.
    assert default_name.get_name_string(name_id) is None
    # Output is string.
    assert isinstance(with_names.get_name_string(0), str)
