# List tools

Various helpers for lists.

## Requirements
* **Python**: >=3.5

## Installation
```sh
python -m pip install list_tools
```

## Current functions
### `chunk`
Split list into chunks by size you provide.

Example:
```python
from list_tools import chunk

items = ['foo', 'bar', 'baz']

for part in chunk(items, 2):
	print(part)
	# ['foo', 'bar'] <- first iteration
	# ['baz']        <- second iteration
```
