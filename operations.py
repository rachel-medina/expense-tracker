from db import connect

def add_expense(description, amount, category, date):
    conn = connect() #connect to db
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO expenses (description, amount, category, date) VALUES (?,?,?,?)",
        (description, amount, category, date)
    )

    conn.commit()
    conn.close()

def get_expenses():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    conn.close()

    return rows

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()