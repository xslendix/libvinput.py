# Python bindings for libvinput 

## Installation

You can install the bindings this way:
```
$ python3 -m pip install vinput
```

You do need to get the latest shared library and place it in your current
working directory in order for the binding to be installed, alternatively, you
can install the library system wide. See the
[releases](https://github.com/xslendix/libvinput/releases/) page for the latest
binaries or build them yourself.

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

