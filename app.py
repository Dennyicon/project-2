from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# MySQL database configuration (update host for cloud DB if needed)
db_config = {
    'user': 'root',
    'password': '10104488',
    'host': 'host.docker.internal',  # will need cloud MySQL later
    'database': 'inventory_db'
}

@app.route('/products', methods=['GET'])
def get_products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, stock, price) VALUES (%s, %s, %s)",
        (data['name'], data['stock'], data['price'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Product added'}), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT automatically
    app.run(debug=True, host='0.0.0.0', port=port)
