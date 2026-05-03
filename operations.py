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

def expense_exists(expense_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM expenses WHERE id = ?", (expense_id,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


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
        cursor.execute("SELECT SUM(amount) FROM expenses")
        rows = cursor.fetchone()

    conn.close()
    return rows

def get_details(category = None, month = None):
    conn = connect()
    cursor = conn.cursor()

    query = "SELECT * FROM expenses"
    conditions = []
    params = []

    if category:
        conditions.append("category = ?")
        params.append(category)

    if month:
        conditions.append("substr(date, 1, 7) = ?")
        params.append(month)
    
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()
    return rows

