EXPENSE TRACKER CLI

A command-line expense tracking app built with Python and SQLite that logs, manages, and analyzes personal expenses.

FEATURES
- Add expenses with one word description, amount, category, and date
- View all expenses
- Delete expenses with ID
- Filter expenses by category and/or month
- View total spending or filter by category or month
- Data is persistent through SQLite

USAGE
Add:
    python main.py add "coffee" 5 food

Delete:
    python main.py delete 1

VIEW DETAILS
List all:
    python main.py details

List by category:
    python main.py details --category food

List by month:
    python main.py details --month 2026-05

List by category within a month:
    python main.py details --category food --month 2026-05

VIEW SPENDING SUMMARIES
Total spending:
    python main.py summary

Spending by categories:
    python main.py summary --category

Spending by months:
    python main.py summary --month



KEY FEATURES:
- delete with ID validation
- dynamic SQL filtering
- aggregated spending summaries
- modular code structure
- persistent storage