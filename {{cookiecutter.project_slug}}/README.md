# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Project structure

{% if cookiecutter.project_package %}- `/{{ cookiecutter.project_slug }}` - Core package containing reusable extraction code
{% endif -%}
- `/data` -  Directory for project data (not versioned)
{%- if cookiecutter.notebooks %}
- `/notebooks` - Jupyter notebooks with examples and demos
{%- endif %}

## Installation and usage

Create a copy of `.env.template` as `.env` and fill out your credentials.

### uv (recommended)

1. [Get uv](https://github.com/astral-sh/uv).
2. `uv venv && uv sync`
{%- if cookiecutter.notebooks %}
3. Open the notebooks and set the kernel to the newly created `.venv/bin/python` interpreter.
4. Follow on the notebook for test and demo usage.
{%- endif %}

### Manual venv (deprecated)

```sh
$ python -venv .venv
$ source .venv/bin/activate
(.venv) $ pip install . -e
```
{%- if cookiecutter.notebooks %}
Open the notebooks and set the kernel to the newly created `.venv` virtual environment.
{%- endif %}
