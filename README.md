# Python bindings for libvinput 

## Installation

You can install the bindings this way:
```
$ python3 -m pip install vinput
```

Please note on Linux, you need libxdo installed.

## Example

The simplest program is the following:
```python
import vinput
l = vinput.EventListener(True)
l.start(print)
```

You can log mouse buttons and movements too:
```python
import vinput
l = vinput.EventListener(True, True, True)
l.start(print, print, print)
```

## License

This software is licensed under the AGPLv3 license, more info in the LICENSE
file.

