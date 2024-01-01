#! /usr/bin/env bash

function pause(){
  read -r -s -n 1 -p "Press any key to continue . . ."
  echo ""
}

pyenv local
poetry config warnings.export false
poetry install --no-root
poetry env info
poetry export --only main --without-hashes -o requirements.txt
# Windows compatibility (`poetry env info --executable` returns the path with \ instead of / even if running gitbash)
EXECUTABLE=$(poetry run python -c "import sys, pathlib; print(pathlib.Path(sys.executable).as_posix())")
sed -i.bak "/<interpreter_path>/ s#<interpreter_path>#$EXECUTABLE#" \
  .vscode/settings.json
rm .vscode/settings.json.bak
git init
git add .
git commit -m "Generate project with cookiecutter"
touch .env

# For debugging
# pause