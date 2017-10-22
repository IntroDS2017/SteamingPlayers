echo "Attempting to process data..."


echo "(1/6) Removing unnecessary columns from accidents data..."
python3 1_remove_accidents_columns.py

echo "(2/6) Renaming streets, dropping uncertain road-addresses..."
python3 2_modify_road_usages_names.py

echo "(3/6) Dropping somewhat duplicate road usages data from streets with multiple measurement points..."
python3 3_drop_additional_road_usages_measurements.py

echo "(4/6) By car count, merging rows sharing (year, hour) which are in 15-minute range instead of hourly range..."
python3 4_merge_road_usages_hours.py

echo "(5/6) Formatting accident-data address-names to match road-usage-data..."
python3 5_change_accidents_katuosoite.py

echo "(6/6) Filtering accidents by addresses, which are included in usage-data..."
python3 6_select_accidents_in_road_usages.py


echo "Processing done!"
