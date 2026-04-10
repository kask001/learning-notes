# API Reference

## Core Functions

### `main_function(arg1, arg2)`

Main entry point for the package.

**Parameters:**
- `arg1` (str): First argument
- `arg2` (int): Second argument

**Returns:**
- `dict`: Result dictionary

**Raises:**
- `ValueError`: If arguments are invalid

**Example:**
```python
from project import main_function

result = main_function("hello", 42)
print(result)
```

## Classes

### `Client`

Main client class for interacting with the service.

#### Methods

- `connect()`: Establish connection
- `execute(query)`: Execute a query
- `close()`: Close connection
