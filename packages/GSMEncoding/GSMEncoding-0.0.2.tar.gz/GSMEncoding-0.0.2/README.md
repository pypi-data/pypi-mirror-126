![GSMEncoding logo](https://mauricelambert.github.io/info/python/code/gsm_small_background.png "GSMEncoding logo")

# GSMEncoding

## Description

This package implements encode/decode functions for GSM (Global System for Mobile Communications - SMS - 2G).

## Requirements

This package require :
 - python3
 - python3 Standard Library

## Installation
```bash
pip install GSMEncoding
```

## Usages

```python
from GSMEncoding import gsm7bitencode, gsm7bitdecode

assert gsm7bitencode("Unit Test") == "55779A0EA296E774"
assert gsm7bitdecode("55779A0EA296E774").rstrip("\x00") == "Unit Test"
assert gsm7bitdecode(gsm7bitencode(b'Unit Test')).rstrip(b"\x00") == b"Unit Test"
```

## Links

 - [Github Page](https://github.com/mauricelambert/GSMEncoding/)
 - [Documentation](https://mauricelambert.github.io/info/python/code/GSMEncoding.html)
 - [Pypi package](https://pypi.org/project/GSMEncoding/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
