import pandas as pd

def modify_specific_street(address):
    new_addr = address

    if 'LAHDEN MOOTTORITIE'.lower() in address.lower():
        new_addr = "LAHDENVÄYLÄ"
    elif 'KEHÄ III'.lower() in address.lower(): # must be before 'KEHÄ I' check!
        new_addr = "KEHÄ 3"
    elif 'KEHÄ I'.lower() in address.lower():
        new_addr = 'KEHÄ 1'

    if address != new_addr:
        specific_changes_log.write("Address " + address + " changed into " + new_addr + "\n")
    return new_addr

def modify_katuosoite(address):
    stripped_address = address.strip()
    combined_address = "".join(stripped_address.lower().split(" ")) # changes KEHÄ 1 --> kehä1

    for road_name in road_usages_names:
        combined_road_name = "".join(road_name.lower().split(" ")) # changes KEHÄ 1 --> kehä1

        if combined_road_name in combined_address:

            if (road_name != stripped_address):
                change_log.write("Address " + stripped_address + " changed into " + road_name + "\n")
            else:
                non_changed_rows_count[0] += 1

            return road_name

    not_found_log.write(address + " not found\n")
    return "NOT_FOUND: " + address # TODO: maintain the address information if still needed further on


def main(accidents_save_path):
    df_accidents['Katuosoite'] = df_accidents['Katuosoite'].map(modify_specific_street).map(modify_katuosoite)
    df_accidents.to_csv(accidents_save_path, index = False)


if __name__ == '__main__':
    specific_changes_log = open('logs/4_katusoite_specific_changes.log', 'w')
    change_log = open('logs/4_katuosoite_changes.log', 'w')
    not_found_log = open('logs/4_katuosoite_not_founds.log', 'w')

    accidents_load_path = "data/1_accidents.csv"
    road_usages_load_path = "data/4_road_usages.csv"

    df_accidents = pd.read_csv(accidents_load_path)
    df_road_usages = pd.read_csv(road_usages_load_path)

    accidents_save_path = "data/5_accidents.csv"

    road_usages_names = df_road_usages.nimi.unique()

    non_changed_rows_count = [0] # reference global int
    main(accidents_save_path)

    specific_changes_log.close()
    change_log.close()
    not_found_log.close()

    print("Non changed rows count: " + str(non_changed_rows_count[0]))

    # 1193 non changed rows, 2541 changed rows, 6341 not found rows.
    # Total amount of rows that can be mapped together with road_usages: 1193 + 2541 = 3734
    # Total amount of rows: 10081
