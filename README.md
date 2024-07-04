# Code Quality with Ruff

This repository is a Python template that sets up code quality checks and formatting using [Ruff](https://beta.ruff.rs/docs/). Ruff is an extremely fast linter, formatter, and Python code checker that helps maintain a consistent and clean codebase.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

First, ensure you have [Poetry](https://python-poetry.org/) installed, as this project uses Poetry for dependency management and packaging.

1. **Clone the repository:**

```sh
git clone https://github.com/tumraja/python_code_quality
cd code_quality
```

2. **Install dependencies:**

```sh
poetry install
```

This will create a virtual environment and install all dependencies specified in the `pyproject.toml` file.

## Usage

To check code quality and formatting using Ruff, you can run:

```sh
poetry run ruff check .
```

## Configuration

The ruff configuration for this project is managed using `ruff.toml` file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
