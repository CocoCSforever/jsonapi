# jsonapi

This Python package provides a customized encoder and decoder for specific data structures like `complex` and `range` that are not directly supported by the standard JSON module.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Two ways to import package](#two-ways-to-import-package)
  - [Create an object to encode](#create-an-object-to-encode)
  - [Encode the data](#encode-the-data)
  - [Sample JSON data](#sample-json-data-encoded-using-yencoder)
  - [Decode the JSON data](#decode-the-json-data)
- [Contributing](#contributing)
- [License](#license)


## Installation

You can install the package using `pip`:

```bash
pip install -e .
```

## Usage
#### Two ways to import package
1. import classes and functions from the package so you can call them directly
```bash
from jsonapi import YEncoder, YDecoder, dumps, loads
```
2. import jsonapi package as js
```bash
from jsonapi import jsonapi as js
```

#### Create an object to encode
```bash
data = {
    'complex_number': complex(1, 2),
    'range_object': range(1, 10, 2)
}
```

#### Encode the data
- 1
```bash
encoded_data = YEncoder().encode(data)
print("Encoded Data:", encoded_data)
```
```bash
encoded_data = dumps(data, cls=YEncoder)
print("Encoded Data:", encoded_data)
```
- 2
```bash
encoded_data = js.YEncoder().encode(data)
print("Encoded Data:", encoded_data)
```
```bash
encoded_data = js.dumps(data, cls=YEncoder)
print("Encoded Data:", encoded_data)
```

#### Sample JSON data (encoded using YEncoder)
```bash
json_data = '{"complex_number": {"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}, "range_object": {"start": 1, "stop": 10, "step": 2, "__extended_json_type__": "range"}}'
```

#### Decode the JSON data
- 1
```bash
decoded_data = YDecoder().decode(json_data)
print("Decoded Data:", decoded_data)
```
```bash
decoded_data = loads(json_data, cls=YDecoder)
print("Decoded Data:", decoded_data)
```
- 2
```bash
decoded_data = js.YDecoder().decode(json_data)
print("Decoded Data:", decoded_data)
```
```bash
decoded_data = js.loads(json_data, cls=YDecoder)
print("Decoded Data:", decoded_data)
```
## Contributing
Contributions are welcome!

## License
None