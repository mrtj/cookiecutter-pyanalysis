import os, shutil

REMOVE_PATHS = [
    '{% if not cookiecutter.project_package %}{{ cookiecutter.project_slug }}{% endif %}',
    '{% if not cookiecutter.notebooks %}notebooks{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else shutil.rmtree(path)
