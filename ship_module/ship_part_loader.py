import os
import csv

# this is not dynamic! Only loads once. Doesn't matter that it is copied by cfg.all_ship_parts
part_dict = {}


def init_all_ship_parts(m):
    cfg = m.cfg
    asp = m.cfg.all_ship_parts

    csv_file_name = "ship_parts.csv"
    path = "assets/"
    csv_path = os.path.join(path, csv_file_name)
    # print("[spl] csv_path:", csv_path)

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # print(row['type'], row['name'], row["crew"])
            # Generate dict from read data
            add_to_part_dict(row["type"], row["name"], row["special_value"], m)

    cfg.all_ship_parts = part_dict


def determine_special_value_type(part):
    pd = {"cockpit": "crew",
          "wingbody": "cargo",
          "wings": "slots",
          "power_plant": "power_generation",
          "shield": "power",
          "engine": "thrust",
          "reverse_thruster": "reverse_thrust",
          "side_thruster": "turn_factor"}

    try:
        return pd[part]
    except KeyError:
        print("[determine_special_value_type] KEY ERROR using KEY:", part)


def add_to_part_dict(part, name, special_value, m, power_drain=0):
    """
    Generates dict from the data collected from CSV-file.

    Image file name is deduced from the name of the object! This does not need to be specified.
    TODO: Fix power_drain and so on for all items.
    TODO: Make a complete CSV file.
    :return:
    """

    part_obj_name = "".join((part, name))
    image_file_name = "".join((part_obj_name, ".png"))

    special_value_name = determine_special_value_type(part)

    if part not in part_dict:
        part_dict[part] = {part_obj_name: {"image": image_file_name, special_value_name: int(special_value)}}

    else:
        part_dict[part][part_obj_name] = {"image": image_file_name, special_value_name: int(special_value)}

    # print(part_dict)


def make_ship_part(part, part_dict_entry, m):
    sp = m.ship_parts
    pde = part_dict_entry

    td = {"cockpit": sp.Cockpit,
          "wingbody": sp.Wingbody,
          "wings": sp.Wings,
          "power_plant": sp.PowerPlant,
          "engine": sp.Engine,
          "reverse_thruster": sp.ReverseThruster,
          "side_thruster": sp.SideThruster,
          "shield": sp.ShieldGen}
    # print("[make_ship_part] called with:", part, part_dict_entry, m)
    return td[part](pde["image"], pde[determine_special_value_type(part)])


def get_ship_part(part, part_name, m):
    if part in part_dict:
        return_part = make_ship_part(part, part_dict[part][part_name], m)
    else:
        return_part = None

    # print(return_part)
    return return_part
