![CustomCrypto logo](https://mauricelambert.github.io/info/python/security/CustomCrypto_small_background.png "CustomCrypto logo")

# CustomCrypto

## Description

This package implements tools to build your custom cipher.

## Requirements

This package require :
 - python3
 - python3 Standard Library

## Installation
```bash
pip install CustomCrypto
```

## Usages

### Python script

```python
from CustomCrypto import CustomCrypto, xor, viginere, decipher_viginere
import string

crypto = CustomCrypto(xor)

cipher = crypto.dynamic_key_1(b'00', [ord('0')])
decipher = bytes(crypto.reverse_dynamic_key_1(cipher, [ord('0')]))

cipher = CustomCrypto(viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_2('ACCA', ('C', 'A'))
decipher = CustomCrypto(decipher_viginere, string.ascii_uppercase, alphabet_length=26).dynamic_key_2('CCCC', ('C', 'A'))

crypto = CustomCrypto(None)

shuffle_data = crypto.shuffle('ABCDEFGH', 4)
data = crypto.unshuffle(shuffle_data, 4)

shuffle_data = crypto.reverse('ABCD')
data = crypto.reverse(shuffle_data)

modified_data = crypto.shift(b'\xff\x00\xf0\xa5\xaa')
data = crypto.shift(modified_data)

lines = crypto.group('0' * 40, '0')
lines = "\n".join(" ".join("".join(chars) for chars in words) for words in lines)
print(lines)
```

## Links

 - [Github Page](https://github.com/mauricelambert/CustomCrypto/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/CustomCrypto.html)
 - [Pypi package](https://pypi.org/project/CustomCrypto/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
