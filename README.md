# jsonapi

This Python package provides a customized encoder and decoder for specific data structures like `complex` and `range` that are not directly supported by the standard JSON module.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Encode the data](#Encode the data)
  - [Decode the JSON data](#Decode the JSON data)
- [Contributing](#contributing)
- [License](#license)


## Installation

You can install the package using `pip`:

```bash
pip install jsonapi
```


## Usage

from jsonapi import YEncoder, YDecoder, dumps, loads

# Create an object to encode
data = {
    'complex_number': complex(1, 2),
    'range_object': range(1, 10, 2)
}

# Encode the data
encoded_data = YEncoder().encode(data)
print("Encoded Data:", encoded_data)

encoded_data = dumps(data, cls=YEncoder)
print("Encoded Data:", encoded_data)

# Sample JSON data (encoded using YEncoder)
json_data = '{"complex_number": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "range_object": {"start": 1, "stop": 10, "step": 2, "__extended_json_type__": "range"}}'

# Decode the JSON data
decoded_data = YDecoder().decode(json_data)
print("Decoded Data:", decoded_data)

decoded_data = loads(json_data, cls=YDecoder)
print("Decoded Data:", decoded_data)

## Contributing
Contributions are welcome!

## License
None