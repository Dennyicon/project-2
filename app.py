from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# -----------------------------
# Root route for testing
# -----------------------------
@app.route("/")
def home():
    return "Flask app is running!"

# -----------------------------
# MySQL configuration (optional, will fail on Render if local)
# -----------------------------
db_config = {
    'user': 'root',
    'password': '10104488',
    'host': 'host.docker.internal',  # works locally only
    'database': 'inventory_db'
}

# -----------------------------
# Mock database for testing on Render
# -----------------------------
mock_products = [
    {"name": "Product A", "stock": 10, "price": 100},
    {"name": "Product B", "stock": 5, "price": 50}
]

@app.route('/products', methods=['GET'])
def get_products():
    # Uncomment below to use real MySQL (will fail on Render without cloud DB)
    # conn = mysql.connector.connect(**db_config)
    # cursor = conn.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM products")
    # products = cursor.fetchall()
    # cursor.close()
    # conn.close()
    # return jsonify(products)

    # Using mock database for Render
    return jsonify(mock_products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    # Uncomment below to use real MySQL
    # conn = mysql.connector.connect(**db_config)
    # cursor = conn.cursor()
    # cursor.execute(
    #     "INSERT INTO products (name, stock, price) VALUES (%s, %s, %s)",
    #     (data['name'], data['stock'], data['price'])
    # )
    # conn.commit()
    # cursor.close()
    # conn.close()
    # return jsonify({'message': 'Product added'}), 201

    # Using mock database for Render
    mock_products.append(data)
    return jsonify({"message": "Product added"}), 201

# -----------------------------
# Run the app with Render dynamic port
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(debug=True, host='0.0.0.0', port=port)

