#!/usr/bin/env bash

echo "Processing combined data."


echo "(1/N) Removing more columns..."
pipenv run python 7_remove_combined_columns.py


echo "Processing done!"