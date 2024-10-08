# st-repeating-field-group

A Streamlit plugin for creating dynamic, repeating field groups with add/remove functionality and conditional field display.

## Installation

Install the package using pip:

```bash
pip install st-repeating-field-group
```

## Features

- Create repeating groups of form fields
- Dynamically add and remove field groups
- Support for various field types: text, number, date, checkbox, toggle, slider, range slider, and dropdown
- Conditional field display based on other field values
- Customizable default values

## Usage

### Basic Usage

Here's a simple example of how to use the `generate_repeating_field_group` function:

```python
import streamlit as st
from st_repeating_field_group import generate_repeating_field_group

keys = {
    "name": {"type": str, "default": ""},
    "age": {"type": int, "default": 0},
    "is_student": {"type": "checkbox", "default": False}
}

group_id = "example_group"
default_values = [
    {"name": "John Doe", "age": 30, "is_student": False},
    {"name": "Jane Smith", "age": 25, "is_student": True}
]

rows = generate_repeating_field_group(keys, group_id, default_values)

st.write(rows)
```

### Advanced Usage with Conditional Fields and Range Slider

You can use the `only_show_if` parameter to conditionally display fields based on the values of other fields in the same group. Here's an example that also includes a range slider:

```python
import streamlit as st
from st_repeating_field_group import generate_repeating_field_group

keys = {
    "name": {"type": str, "default": ""},
    "age": {"type": int, "default": 0},
    "is_student": {"type": "checkbox", "default": False},
    "school_name": {
        "type": str,
        "default": "",
        "only_show_if": {
            "kwargs": {"is_student": "is_student"},
            "func": lambda is_student: is_student
        }
    },
    "job_title": {
        "type": str,
        "default": "",
        "only_show_if": {
            "kwargs": {"is_student": "is_student"},
            "func": lambda is_student: not is_student
        }
    },
    "salary_range": {
        "type": "range_slider",
        "default": (30000, 80000),
        "min": 0,
        "max": 200000,
        "step": 1000,
        "only_show_if": {
            "kwargs": {"is_student": "is_student"},
            "func": lambda is_student: not is_student
        }
    }
}

group_id = "advanced_example_group"
default_values = [
    {"name": "John Doe", "age": 30, "is_student": False, "job_title": "Engineer", "salary_range": (50000, 100000)},
    {"name": "Jane Smith", "age": 25, "is_student": True, "school_name": "University XYZ"}
]

rows = generate_repeating_field_group(keys, group_id, default_values)

st.write(rows)
```

In this example, the "school_name" field will only be displayed if "is_student" is checked, while the "job_title" and "salary_range" fields will only be displayed if "is_student" is not checked.

### Supported Field Types

The `generate_repeating_field_group` function supports the following field types:

- `str` or `"str"`: Text input
- `int` or `"int"`: Integer input
- `float` or `"float"`: Float input
- `"choice"`: Dropdown selection
- `"date"`: Date input
- `"toggle_switch"`: Toggle switch
- `"checkbox"`: Checkbox
- `"slider"`: Slider input
- `"range_slider"`: Range slider input

### Parameters

- `keys` (dict): A dictionary defining the fields and their properties.
- `group_id` (str): A unique identifier for the field group.
- `default_values` (list, optional): Default values for the fields.

#### Field Properties

Each field in the `keys` dictionary can have the following properties:

- `type`: The data type or input type of the field (required).
- `default`: The default value for the field (required).
- `choices`: A list of options for dropdown fields (required for "choice" type).
- `min`: Minimum value for numeric or slider fields (optional).
- `max`: Maximum value for numeric or slider fields (optional).
- `step`: Step size for numeric or slider fields (optional).
- `only_show_if`: A dictionary containing conditional display logic (optional).

#### Using `only_show_if`

The `only_show_if` property allows you to conditionally display fields based on the values of other fields in the same group. It has two sub-properties:

- `kwargs`: A dictionary mapping parameter names to field names in the current group.
- `func`: A function that takes the mapped field values as arguments and returns a boolean indicating whether the field should be displayed.

Example:

```python
"school_name": {
    "type": str,
    "default": "",
    "only_show_if": {
        "kwargs": {"is_student": "is_student"},
        "func": lambda is_student: is_student
    }
}
```

In this example, the "school_name" field will only be displayed if the "is_student" checkbox is checked.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.