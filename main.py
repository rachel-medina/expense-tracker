#TODO spending by category, monthly totals
#       date filtering
#       CLI output

import argparse
from datetime import date
from db import create_table
from operations import add_expense, get_expenses, delete_expense, get_total, get_category

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")
add_parser.add_argument("amount", type=float)
add_parser.add_argument("category")

subparsers.add_parser("list")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

category_parser = subparsers.add_parser("category")
category_parser.add_argument("category")

summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--category", action="store_true")
summary_parser.add_argument("--month", action="store_true")


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

    elif args.command == "category":
        cat_list = get_category(args.category)
        for row in cat_list:
            print (row)
    elif args.command == "summary":
        if args.category:
            results = get_total("--category")
            for category, total in results:
                print(f"{category}: ${total:.2f}")

        elif args.month:
            results = get_total("--month")
            for month, total in results:
                print(f"{month}: ${total:.2f}")

        else:
            total = get_total()
            print(f"Total: ${total[0]:.2f}")
        


    else:
        parser.print_help()

if __name__ == "__main__":
    main()