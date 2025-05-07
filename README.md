# Python Classroom Template

This repository serves as a template for Python projects in GitHub Classroom. It includes a basic structure and configuration to get started quickly.

## Project Structure
```
python-classroom-template/
├── LICENSE
├── README.md
├── requirements.txt      # Project dependencies
├── setup.py              # Package setup file
├── src/                  # Source code directory
│   ├── __init__.py       # Makes src a Python package
│   ├── __main__.py       # Entry point for running the package
│   ├── example.py        # Example code module
│   └── topics/           # Topic-specific exercises
│       ├── __init__.py
│       └── intro_to_variables/    # First topic
│           ├── __init__.py
│           └── variables.py       # Variables exercise
└── tests/                # Test directory
    ├── __init__.py       # Makes tests a Python package
    ├── test_example.py   # Tests for example module
    └── topics/           # Tests for topic exercises
        ├── __init__.py
        └── intro_to_variables/    # Tests for first topic
            ├── __init__.py
            └── test_variables.py  # Tests for variables exercise
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/python-classroom-template.git
   cd python-classroom-template
   ```

2. Create and activate a virtual environment
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Development

### Working with Topics
This template includes a structured approach to learning Python through topic-based exercises:

1. Each topic is organized in its own folder under `src/topics/`
2. Implementation tasks are in the topic's source files (e.g., `src/topics/intro_to_variables/variables.py`)
3. Tests for each topic are in the corresponding folder under `tests/topics/`

To complete a topic:
1. Read the function docstrings in the source file
2. Implement each function according to its requirements
3. Run the tests to check if your implementation is correct

### Running Tests for a Specific Topic
```bash
# Run tests for a specific topic
pytest tests/topics/intro_to_variables/

# Run a specific test file
pytest tests/topics/intro_to_variables/test_variables.py
```

### Running Tests
```bash
pytest
```

### Run with Coverage Report
```bash
pytest --cov=src tests/
```

### Code Formatting and Linting
This template includes several tools to help maintain code quality:

- **Black**: Code formatter
  ```bash
  black src tests
  ```

- **isort**: Import sorter
  ```bash
  isort src tests
  ```

- **flake8**: Linter
  ```bash
  flake8 src tests
  ```

- **mypy**: Type checker
  ```bash
  mypy src
  ```

## Assignment Submission Guidelines

1. Complete the assigned tasks by implementing the required functions
2. Make sure all tests pass
3. Follow the code style guidelines
4. Submit your work by pushing to your assignment repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.