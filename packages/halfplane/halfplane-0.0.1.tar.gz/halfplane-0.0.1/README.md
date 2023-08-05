# halfplane

# Dev set up

```
pyenv virtualenv $(basename $PWD)
pyenv local $(basename $PWD)
pip install --upgrade pip
pip install -e .[dev]
```

# Release

```
pip install build twine
```
