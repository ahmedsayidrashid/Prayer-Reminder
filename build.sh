# Pre commit functions to use until I create a CI 

# Note that the rules for these tools are in pyproject.toml

# Update requirements each build
pip list --format=freeze > requirements.txt

# Run code formatters and linters
ruff check . --fix  --unsafe-fixes
black .

# check types
mypy .

# sort imports
isort .