
# Project Title

Here I want to create a Streamlit App where I'll be able to generate Bob Dylan style lyrics

The main reason I want to do this is **nerd enthusiasm**, but, beyond that, i want to try neural networks and this is the best way that I've could think of doing it.


## Installation

    1. install virtualenv:
         `python -m venv env`

    2. install requirements in virtual env:
        `env/bin/pip install -r requirements.txt`

    3. you can launch an interpreter in the env context like this:
        `env/bin/python`

## Usage/Examples



You can launch it like this:
```
env/bin/python -m get_data_build_streamlit.get_lyrics_from_genius
```

The script **will emit a text file** in our directory lyrics with Bob Dylan songs.

You can check if your data is correct to the App **running the dashboard on a local server**:
```
env/bin/streamlit run get_data_build_streamlit/text_generator.py
```
To share publicly this dashboard, you have to [ask for a invitation](https://streamlit.io/sharing)

## Running Tests

#### flake8 linting

Run flake8 on the packages:
```
env/bin/python -m flake8 --select F get_data_build_streamlit
```
#### mypy type checks

This runs [mypy](http://mypy-lang.org/) static typechecks on the code:
```
env/bin/python -m mypy --check-untyped-defs --ignore-missing-imports get_data_build_streamlit
```
## Authors

- [@74minutos](https://www.github.com/74minutos)
