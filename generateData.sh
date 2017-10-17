#!/usr/bin/env bash

# Runs data-generation python-scripts with pipenv.
echo "Attempting to generate data..."

echo "(1/4) Renaming streets, dropping uncertain road-addresses..."
python3 2_modify_road_usages_names.py

echo "(2/4) Merging car-count by hour..."
python3 3_merge_read_usages_hours.py

echo "(3/4) Formatting accident-data address-names to match road-usage-data..."
python3 4_change_accidents_katuosoite.py

echo "(4/4) Filtering accidents by addresses, which are included in usage-data..."
python3 5_select_accidents.py

echo "Generation done!"
