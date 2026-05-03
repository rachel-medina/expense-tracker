from db import connect

def add_expense(description, amount, category, date):
    conn = connect() #connect to db
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?,?,?,?)",
        (description, amount, category, date)
    )

    conn.commit()
    conn.close()


def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def get_total(group_by=None):
    conn = connect()
    cursor = conn.cursor()

    if group_by == "category":
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            GROUP BY category
        """)
        rows = cursor.fetchall()

    elif group_by == "month":
        cursor.execute("""
            SELECT substr(date, 1, 7) AS month, SUM(amount)
            FROM expenses
            GROUP BY month
        """)
        rows = cursor.fetchall()

    else:
        cursor.execute("""
            SELECT SUM(amount)
            FROM expenses
        """)
        rows = cursor.fetchone()

    conn.close()
    return rows

def get_details(group_by = None, value = None):
    conn = connect()
    cursor = conn.cursor()

    if group_by == "category":
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (value,))
        rows = cursor.fetchall()
    elif group_by == "--month":
        cursor.execute("SELECT * FROM esxpenses WHERE substr(date, 1, 7) = ?", (value,))
        rows = cursor.fetchall
    else:
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

    conn.close()
    return rows

