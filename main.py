import argparse
from datetime import date
from db import create_table
from operations import add_expense, get_expenses, delete_expense

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")
add_parser.add_argument("amount", type=float)
add_parser.add_argument("category")

subparsers.add_parser("list")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)


def main():
    create_table()
    args = parser.parse_args()


    if args.command == "add":
        today = str(date.today())
        add_expense(args.description, args.amount, args.category, today)

    elif args.command == "list":
        expenses = get_expenses()
        for row in expenses:
            print (row)

    elif args.command == "delete":
        delete_expense(args.id)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()