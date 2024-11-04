# metmuseum-python

Python client library for accessing the Metropolitan Museum of Art's public API

## Installation

### With uv

```sh
uv add git+https://github.com/ulbwa/metmuseum-python
```

### With Poetry

```sh
poetry add git+https://github.com/ulbwa/metmuseum-python
```

## Running Tests

### 1. Create a Virtual Environment

```sh
uv venv
```

### 2. Install Dependencies (including dev dependencies)

```sh
uv sync --frozen --extra dev
```

### 3. Run Tests

```
uv run pytest
```

Or activate the virtual environment and run tests with pytest

```sh
source .venv/bin/activate
pytest
```
