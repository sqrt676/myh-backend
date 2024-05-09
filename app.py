from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to fetch data from SQLite database based on input parameters
def fetch_data(product_id, product_category, data_frequency, start_date, end_date):
    conn = sqlite3.connect('product_data.db')
    cursor = conn.cursor()

    # Construct SQL query based on input parameters
    sql_query = f"SELECT * FROM ultratech_cem WHERE date BETWEEN ? AND ?"
    cursor.execute(sql_query, (start_date, end_date))
    data = cursor.fetchall()

    # Close connection
    conn.close()

    return data

@app.route('/fetch_product_data', methods=['POST'])
def fetch_product_data():
    request_data = request.json

    # Extract input parameters from request
    product_id = request_data.get('product_id')
    product_category = request_data.get('product_category')
    data_frequency = request_data.get('data_frequency')
    start_date = request_data['time_period']['start_date']
    end_date = request_data['time_period']['end_date']

    # Fetch data from SQLite database
    data = fetch_data(product_id, product_category, data_frequency, start_date, end_date)

    return jsonify({
        'product_id': product_id,
        'product_category': product_category,
        'data': data
    })

if __name__ == '__main__':
    app.run(debug=True)
