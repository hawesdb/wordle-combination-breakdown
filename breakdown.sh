#!/bin/bash
if [[ ! -d 'wordle-env' ]]; then
  python -m venv wordle-env
fi

source wordle-env/Scripts/activate
pip install -r requirements.txt
python wordle-breakdown.py
deactivate