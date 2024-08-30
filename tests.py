import unittest
from unittest.mock import MagicMock
from ctypes import c_uint16, c_char, c_char_p, c_size_t
import sys
import time

import vinput

# Platform-specific keysyms
if sys.platform.startswith('linux'):
    KEYSYM_ENTER = 0xFF0D      # XK_Return
    KEYSYM_A = 0x0041          # XK_A
elif sys.platform.startswith('win'):
    KEYSYM_ENTER = 0x0D        # VK_RETURN
    KEYSYM_A = 0x41            # VK_A
else:
    print('Invalid platform. Only Linux and macOS are supported for this test suite.', file=sys.stderr)
    sys.exit(1)

class TestEventEmulator(unittest.TestCase):
    def setUp(self):
        self.mock_vinput = MagicMock()
        vinput.vinput = self.mock_vinput

    def test_init_and_del(self):
        self.mock_vinput.EventEmulator_create.return_value = 0
        emulator = vinput.EventEmulator()
        self.assertIsInstance(emulator, vinput.EventEmulator)

        self.mock_vinput.EventEmulator_free.return_value = 0
        del emulator

    def test_keyboard_press(self):
        emulator = vinput.EventEmulator()

        self.mock_vinput.EventEmulator_press.return_value = 1
        self.mock_vinput.VInput_error_get_message.return_value = b"error"
        try:
            emulator.keyboard_press(KEYSYM_A)
        except vinput.VInputException:
            self.fail('keyboard_press() failed unexpectedly!')

        self.mock_vinput.EventEmulator_press.return_value = 0
        emulator.keyboard_press(KEYSYM_A)

    def test_keyboard_release(self):
        emulator = vinput.EventEmulator()

        self.mock_vinput.EventEmulator_release.return_value = 1
        self.mock_vinput.VInput_error_get_message.return_value = b"error"
        try:
            emulator.keyboard_release(KEYSYM_A)
        except vinput.VInputException:
            self.fail('keyboard_release() failed unexpectedly!')

        self.mock_vinput.EventEmulator_release.return_value = 0
        emulator.keyboard_release(KEYSYM_A)

    def test_keyboard_typec(self):
        emulator = vinput.EventEmulator()

        self.mock_vinput.EventEmulator_typec.return_value = 1
        self.mock_vinput.VInput_error_get_message.return_value = b"error"
        try:
            emulator.keyboard_typec('a')
        except vinput.VInputException:
            self.fail('keyboard_typec() failed unexpectedly!')

        self.mock_vinput.EventEmulator_typec.return_value = 0
        emulator.keyboard_typec('a')

    def test_keyboard_types(self):
        emulator = vinput.EventEmulator()

        self.mock_vinput.EventEmulator_types.return_value = 1
        self.mock_vinput.VInput_error_get_message.return_value = b"error"
        try:
            emulator.keyboard_types('hello')
        except vinput.VInputException:
            self.fail('keyboard_types() failed unexpectedly!')

        self.mock_vinput.EventEmulator_types.return_value = 0
        emulator.keyboard_types('hello')

if __name__ == '__main__':
    print('Please focus on another window.')
    time.sleep(5)
    unittest.main()
