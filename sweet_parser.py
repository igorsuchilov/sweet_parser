import sys
import json
import csv
import itertools

def main(input_file, output_file):
    """
    Parser for sweets JSON file

    :param input_file (str): Path to input JSON file
    :param output_file (str): Path to output file
    :return: None
    """

    with open(input_file, 'r') as input_json:
        sweets = json.load(input_json)

    with open(output_file, 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow(["Id", "Type", "Name", "Batter", "Topping"])

        for item in sweets['items']['item']:
            
            # Prepare lists of batters and toppings for each sweets item
            batters_list = [batter_dict for batter_dict in item["batters"]["batter"]]
            batter_types_list = [batter_type["type"] for batter_type in batters_list]
            topping_types_list = [topping_type["type"] for topping_type in item["topping"]]

            # Calculate all combinations of batters and toppings and write resulted lines into a file
            for batter_topping_combinations in itertools.product(batter_types_list, topping_types_list):
                line_to_write = [item["id"], item["type"], item["name"], *batter_topping_combinations]
                writer.writerow(line_to_write)
    

if __name__ == "__main__":
    # Check if the user has provided both: input and output file names as arguments
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except IndexError as e:
        print("ARGUMENT ERROR: Please provide a JSON file as a first argument and output file name as a second argument")
        sys.exit(1)
    # Check if input file has correct extension .json
    if input_file.endswith("json"):
        main(input_file, output_file)
    else:
        print("ARGUMENT ERROR: Please provide a valid JSON file as a first argument")
        sys.exit(1)

