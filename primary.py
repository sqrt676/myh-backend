import sqlite3
import random
from datetime import datetime, timedelta

# Function to generate synthetic data for UltraTechCem
def generate_data(start_date, end_date):
    data = []
    current_date = start_date
    while current_date <= end_date:
        sales = random.randint(50, 200)
        inventory = random.randint(20, 100)
        price = random.uniform(300, 600)
        data.append((current_date.strftime('%Y-%m-%d'), sales, inventory, price))
        current_date += timedelta(days=1)
    return data

# Connect to SQLite database
conn = sqlite3.connect('product_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS ultratech_cem (
                    date TEXT PRIMARY KEY,
                    sales INTEGER,
                    inventory INTEGER,
                    price REAL
                )''')

# Generate synthetic data for 1 year
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
data = generate_data(start_date, end_date)

# Insert data into SQLite database
cursor.executemany('INSERT OR IGNORE INTO ultratech_cem VALUES (?, ?, ?, ?)', data)

# Commit changes and close connection
conn.commit()
conn.close()
