"""This module provides a tool to calculate the total
sales cost from a product catalogue and sales records."""

import json
import time
import sys


def load_json_file(file_path):
    """
    Load and return the JSON data from a file.

    :param file_path: Path to the JSON file to be loaded.
    :return: Loaded JSON data or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return None


def calculate_total_sales(catalogue, sales):
    """
    Calculate the total cost of all sales.

    :param catalogue: A list of dictionaries with the product catalogue.
    :param sales: A list of dictionaries representing the sales records.
    :return: Total cost of all sales.
    """
    total_cost = 0
    for sale in sales:
        product_name = sale['Product']
        quantity = sale['Quantity']

        # Simplified way to find the price for a given product name
        price = None
        for item in catalogue:
            if item['title'] == product_name:
                price = item['price']
                break

        if price is not None:
            total_cost += price * quantity
        else:
            print(f"Warning: '{product_name}' not found.")
    return total_cost


def write_results_to_file(file_path, result, execution_time):
    """
    Write the results and execution time to a file.

    :param file_path: Path to the output file.
    :param result: The total sales cost.
    :param execution_time: The execution time of the program.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Total Sales Cost: {result}\n")
        file.write(f"Execution Time: {execution_time} seconds\n")


def main(price_catalogue_path, sales_record_path):
    """
    Main function to calculate and write the total sales cost.

    :param price_catalogue_path: Path to the product catalogue JSON file.
    :param sales_record_path: Path to the sales record JSON file.
    """
    start_time = time.time()

    catalogue = load_json_file(price_catalogue_path)
    if catalogue is None:
        return
    sales = load_json_file(sales_record_path)
    if sales is None:
        return

    total_sales_cost = round(calculate_total_sales(catalogue, sales), 2)

    execution_time = time.time() - start_time
    print(f"Total Sales Cost: {total_sales_cost}")
    print(f"Execution Time: {execution_time} seconds")

    write_results_to_file('SalesResults.txt', total_sales_cost, execution_time)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: computeSales.py [catalogue] [sales]")
    else:
        main(sys.argv[1], sys.argv[2])
