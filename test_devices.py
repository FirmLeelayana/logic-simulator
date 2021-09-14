"""Test the devices module."""
import pytest

from names import Names
from devices import Devices


@pytest.fixture
def new_devices():
    """Return a new instance of the Devices class."""
    new_names = Names()
    return Devices(new_names)


@pytest.fixture
def devices_with_items():
    """Return a Devices class instance with three devices in the network."""
    new_names = Names()
    new_devices = Devices(new_names)

    [AND1_ID, NOR1_ID, SW1_ID] = new_names.lookup(["And1", "Nor1", "Sw1"])

    new_devices.make_device(AND1_ID, new_devices.AND, 2)
    new_devices.make_device(NOR1_ID, new_devices.NOR, 16)
    new_devices.make_device(SW1_ID, new_devices.SWITCH, 0)

    return new_devices


def test_get_device(devices_with_items):
    """Test if get_device returns the correct device."""
    names = devices_with_items.names
    for device in devices_with_items.devices_list:
        assert devices_with_items.get_device(device.device_id) == device

        # get_device should return None for non-device IDs
        [X_ID] = names.lookup(["Random_non_device"])
        assert devices_with_items.get_device(X_ID) is None


def test_find_devices(devices_with_items):
    """Test if find_devices returns the correct devices of the given kind."""
    devices = devices_with_items
    names = devices.names
    device_names = [AND1_ID, NOR1_ID, SW1_ID] = names.lookup(["And1", "Nor1",
                                                              "Sw1"])

    assert devices.find_devices() == device_names
    assert devices.find_devices(devices.AND) == [AND1_ID]
    assert devices.find_devices(devices.NOR) == [NOR1_ID]
    assert devices.find_devices(devices.SWITCH) == [SW1_ID]
    assert devices.find_devices(devices.XOR) == []


def test_make_device(new_devices):
    """Test if make_device correctly makes devices with their properties."""
    names = new_devices.names

    [NAND1_ID, CLOCK1_ID, D1_ID, I1_ID,
     I2_ID] = names.lookup(["Nand1", "Clock1", "D1", "I1", "I2"])
    new_devices.make_device(NAND1_ID, new_devices.NAND, 2)  # 2-input NAND
    # Clock half period is 5
    new_devices.make_device(CLOCK1_ID, new_devices.CLOCK, 5)
    new_devices.make_device(D1_ID, new_devices.D_TYPE)

    nand_device = new_devices.get_device(NAND1_ID)
    clock_device = new_devices.get_device(CLOCK1_ID)
    dtype_device = new_devices.get_device(D1_ID)

    assert nand_device.inputs == {I1_ID: None, I2_ID: None}
    assert clock_device.inputs == {}
    assert dtype_device.inputs == {new_devices.DATA_ID: None,
                                   new_devices.SET_ID: None,
                                   new_devices.CLEAR_ID: None,
                                   new_devices.CLK_ID: None}

    assert nand_device.outputs == {None: new_devices.LOW}

    # Clock could be anywhere in its cycle
    assert clock_device.outputs in [{None: new_devices.LOW},
                                    {None: new_devices.HIGH}]

    assert dtype_device.outputs == {new_devices.Q_ID: new_devices.LOW,
                                    new_devices.QBAR_ID: new_devices.LOW}

    assert clock_device.clock_half_period == 5
    # Clock counter and D-type memory are initially at random states
    assert clock_device.clock_counter in range(5)
    assert dtype_device.dtype_memory in [new_devices.LOW, new_devices.HIGH]


@pytest.mark.parametrize("function_args, error", [
    ("(AND1_ID, new_devices.AND, 17)", "new_devices.INVALID_QUALIFIER"),
    ("(SW1_ID, new_devices.SWITCH, None)", "new_devices.NO_QUALIFIER"),
    ("(X1_ID, new_devices.XOR, 2)", "new_devices.QUALIFIER_PRESENT"),
    ("(D_ID, D_ID, None)", "new_devices.BAD_DEVICE"),
    ("(CL_ID, new_devices.CLOCK, 0)", "new_devices.INVALID_QUALIFIER"),
    ("(CL_ID, new_devices.CLOCK, 10)", "new_devices.NO_ERROR"),

    # Note: XOR device X2_ID will have been made earlier in the function
    ("(X2_ID, new_devices.XOR)", "new_devices.DEVICE_PRESENT"),
])
def test_make_device_gives_errors(new_devices, function_args, error):
    """Test if make_device returns the appropriate errors."""
    names = new_devices.names
    [AND1_ID, SW1_ID, CL_ID, D_ID, X1_ID,
     X2_ID] = names.lookup(["And1", "Sw1", "Clock1", "D1", "Xor1", "Xor2"])

    # Add a XOR device: X2_ID
    new_devices.make_device(X2_ID, new_devices.XOR)

    # left_expression is of the form: new_devices.make_device(...)
    left_expression = eval("".join(["new_devices.make_device", function_args]))
    right_expression = eval(error)
    assert left_expression == right_expression


def test_get_signal_name(devices_with_items):
    """Test if get_signal_name returns the correct signal name."""
    devices = devices_with_items
    names = devices.names
    [AND1, I1] = names.lookup(["And1", "I1"])

    assert devices.get_signal_name(AND1, I1) == "And1.I1"
    assert devices.get_signal_name(AND1, None) == "And1"


def test_get_signal_ids(devices_with_items):
    """Test if get_signal_ids returns the correct signal IDs."""
    devices = devices_with_items
    names = devices.names
    [AND1, I1] = names.lookup(["And1", "I1"])

    assert devices.get_signal_ids("And1.I1") == [AND1, I1]
    assert devices.get_signal_ids("And1") == [AND1, None]


def test_set_switch(new_devices):
    """Test if set_switch changes the switch state correctly."""
    names = new_devices.names
    # Make a switch
    [SW1_ID] = names.lookup(["Sw1"])
    new_devices.make_device(SW1_ID, new_devices.SWITCH, 1)
    switch_object = new_devices.get_device(SW1_ID)

    assert switch_object.switch_state == new_devices.HIGH

    # Set switch Sw1 to LOW
    new_devices.set_switch(SW1_ID, new_devices.LOW)
    assert switch_object.switch_state == new_devices.LOW


@pytest.mark.parametrize("sequence, sequence_two", [
    ("__----__", "123123"),
    ("____", "Something"),
    ("----", "__--asddasd-__"),
    ("-_-_-", ".."),
    ("---------------", " ")
])
def test_check_waveform(new_devices, sequence, sequence_two):
    """Test if check_waveform method returns the correct output."""
    # Correct input.
    assert new_devices.check_waveform(sequence)
    # Incorrect input.
    assert not new_devices.check_waveform(sequence_two)


@pytest.mark.parametrize("sequence, waveform", [
    ("__----__", [2, 6, 8]),
    ("____", [4]),
    ("----", [4]),
    ("-_-_", [1, 2, 3, 4]),
    ("---------------", [15]),
    ("_", [1])
])
def test_get_siggen_waveform(new_devices, sequence, waveform):
    """Test if get_siggen_waveform method returns expected output."""
    assert new_devices.get_siggen_waveform(sequence) == waveform


@pytest.mark.parametrize("sequence, starting_state", [
    ("__----__", 0),
    ("____", 0),
    ("----", 1),
    ("-_-_-", 1),
    ("---------------", 1),
    ("-", 1)
])
def test_get_starting_state(new_devices, sequence, starting_state):
    """Test if get_starting_state method returns expected output."""
    assert new_devices.get_starting_state(sequence) == starting_state


@pytest.mark.parametrize("id, wave, period, s_list, start, init", [
    ("siggen1", "__----__", 8, [2, 6, 8], 0, 0),
    ("something", "____", 4, [4], 0, 0),
    ("SIGGGENN1", "----", 4, [4], 1, 1),
    ("si1", "-_-_", 4, [1, 1, 1, 1], 1, 1),
    ("asd", "---------------", 15, [15], 1, 1),
    ("a11", "-", 1, [1], 1, 1)
])
def test_make_siggen(new_devices, id, wave, period, s_list,
                     start, init):
    """Test if make_siggen method correctly creates a siggen device."""
    new_devices.make_siggen(id, wave)
    my_device = new_devices.devices_list[0]
    my_device.device_kind == new_devices.SIGGEN
    my_device.device_id == id
    my_device.siggen_period == period
    my_device.siggen_waveform == s_list
    my_device.outputs[None] == start
    my_device.siggen_counter == 0
    my_device.initial_state == init


@pytest.mark.parametrize("sig_id, waveform, period", [
    ("siggen1", "--_---", 6),
    ("siggen2", "____", 4),
    ("siggen3", "-", 1)
])
def test_make_device_siggen(new_devices, sig_id, waveform, period):
    """Test if make_device method returns expected output for siggen."""
    names = new_devices.names
    [siggen_ID] = names.lookup([sig_id])

    # Make the siggen device.
    new_devices.make_device(siggen_ID, new_devices.SIGGEN, waveform)
    siggen = new_devices.get_device(siggen_ID)

    # No inputs to siggen.
    assert siggen.inputs == {}

    # Siggen output must be either low or high.
    assert siggen.outputs in [{None: new_devices.LOW},
                              {None: new_devices.HIGH}]

    # Check siggen period.
    assert siggen.siggen_period == period

    # Siggen counter initialised at 0.
    assert siggen.siggen_counter == 0


@pytest.mark.parametrize("sig_id, waveform, init", [
    ("siggen1", "--_---", 1),
    ("siggen2", "____", 0),
    ("siggen3", "-", 1)
])
def test_reset_siggen(new_devices, sig_id, waveform, init):
    """Test if cold_startup method resets siggen devices."""
    names = new_devices.names
    [siggen_ID] = names.lookup([sig_id])

    # Make the siggen device.
    new_devices.make_device(siggen_ID, new_devices.SIGGEN, waveform)
    siggen = new_devices.get_device(siggen_ID)

    # Reset the siggen device.
    new_devices.cold_startup()

    # Siggen output reset.
    assert siggen.outputs[None] == init

    # Siggen counter reset to 0.
    assert siggen.siggen_counter == 0
