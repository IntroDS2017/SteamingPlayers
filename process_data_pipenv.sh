echo "Attempting to process data..."


echo "\n(1/6) Removing unnecessary columns from accidents data..."
pipenv run python 1_remove_accidents_columns.py

echo "\n(2/6) Renaming streets, dropping uncertain road-addresses..."
pipenv run python 2_modify_road_usages_names.py

echo "\n(3/6) Dropping somewhat duplicate road usages data from streets with multiple measurement points..."
pipenv run python 3_drop_additional_road_usages_measurements.py

echo "\n(4/6) By car count, merging rows sharing (year, hour) which are in 15-minute range instead of hourly range..."
pipenv run python 4_merge_road_usages_hours.py

echo "\n(5/6) Formatting accident-data address-names to match road-usage-data..."
pipenv run python 5_change_accidents_katuosoite.py

echo "\n(6/6) Filtering accidents by addresses, which are included in usage-data..."
pipenv run python 6_select_accidents_in_road_usages.py


echo "Processing done!"
