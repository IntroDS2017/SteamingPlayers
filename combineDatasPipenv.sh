#!/usr/bin/env bash

# Runs data-generation python-scripts with pipenv.

echo "Attempting to generate data..."

echo "(1/5) Renaming streets, dropping uncertain road-addresses..."
pipenv run python 2_modify_road_usages_names.py

echo "(2/5) By car count, merging rows sharing (year, hour) which are in 15-minute range instead of hourly range..."
pipenv run python 3_merge_read_usages_hours.py

echo "(3/5) Formatting accident-data address-names to match road-usage-data..."
pipenv run python 4_change_accidents_katuosoite.py

echo "(4/5) Filtering accidents by addresses, which are included in usage-data..."
pipenv run python 5_select_accidents.py

echo "(5/5) Combining accident-data with road-usage-data..."
pipenv run python 6_combine_data.py

echo "Combining datas done!"
