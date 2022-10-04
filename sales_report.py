"""Generate sales report showing total melons each salesperson sold."""

import sys 
melon_sales = {}
file = open(sys.argv[1])

def make_sales_record(file):
        for line in file:
            line = line.rstrip()
            salesperson, total_amount, melons = line.split('|')
            if salesperson in melon_sales:
                melon_sales[salesperson] += int(melons)
            else: 
                melon_sales[salesperson] = int(melons)
        return melon_sales


def print_sales_record(melon_sales):
        for key, value in melon_sales.items():
            print(f"{key} sold {value} melons.")


print_sales_record(make_sales_record(file))
file.close()