# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Project structure

{% if cookiecutter.project_package %}- `/{{ cookiecutter.project_slug }}` - Core package containing reusable extraction code
{% endif -%}
- `/data` -  Directory for project data (not versioned)
{%- if cookiecutter.notebooks %}
- `/notebooks` - Jupyter notebooks with examples and demos
{%- endif %}

## Installation

1. Get [poetry](https://python-poetry.org/docs/).
2. `poetry install{% if not cookiecutter.project_package %} --no-root{% endif %}`

## Usage

1. Open one of the notebooks in `notebooks/` folder.
2. Set the kernel of the notebook to the `.venv/bin/python` executable.
3. Follow on the notebook for test and demo usage.

If you need to activate the python environment of the project in the terminal, use `poetry shell`.
