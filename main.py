import argparse
from datetime import date
from db import create_table
from operations import add_expense, get_expenses, delete_expense

create_table()


if __name__ == "__main__":
    delete_expense(1)

    expenses = get_expenses()

    for x in expenses:
        print(x)