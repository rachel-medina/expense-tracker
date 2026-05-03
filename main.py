import argparse
from datetime import date
from db import create_table
from operations import add_expense, delete_expense, get_total, get_details, expense_exists

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")
add_parser.add_argument("amount", type=float)
add_parser.add_argument("category")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

category_parser = subparsers.add_parser("category")
category_parser.add_argument("category")

summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--category", action = "store_true")
summary_parser.add_argument("--month", action = "store_true")

details_parser = subparsers.add_parser("details")
details_parser.add_argument("--category")
details_parser.add_argument("--month")
details_parser.add_argument("value", nargs = "?")



def main():
    create_table()
    args = parser.parse_args()

    if args.command == "add":
        today = str(date.today())
        add_expense(args.description, args.amount, args.category, today)
        print("Expense added")

    elif args.command == "delete":
        if not expense_exists(args.id):
            print(f"Expense with ID {args.id} not found")
            return
        
        delete_expense(args.id)
        print("Expense deleted")

    elif args.command == "summary":
        if args.category:
            results = get_total("category")
            for category, total in results:
                print(f"{category}: ${total:.2f}")
        elif args.month:
            results = get_total("month")
            for month, total in results:
                print(f"{month}: ${total:.2f}")
        else:
            total = get_total()
            print(f"Total: ${total[0]:.2f}")

    elif args.command == "details":
        expenses = get_details(category=args.category, month=args.month)

        if not expenses:
            print("No matching expenses found.")
        else:
            print("ID | Description | Amount | Category | Date")
            print("-" * 50)
            for row in expenses:
                print(f"{row[0]} | {row[1]} | ${row[2]:.2f} | {row[3]} | {row[4]}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()