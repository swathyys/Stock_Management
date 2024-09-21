from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conversion rate from dollars to rupees
USD_TO_INR = 82.0  # You can adjust this rate as needed

# Dummy data for stock items
stock_items = [
    {"id": 1, "name": "Laptop", "quantity": 50, "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Office Chair", "quantity": 150, "price": 199.99, "category": "Furniture"},
    {"id": 3, "name": "Wireless Mouse", "quantity": 200, "price": 29.99, "category": "Electronics"},
    {"id": 4, "name": "Desk Lamp", "quantity": 75, "price": 49.99, "category": "Furniture"},
    {"id": 5, "name": "Keyboard", "quantity": 120, "price": 89.99, "category": "Electronics"},
]

@app.route('/')
def index():
    return render_template('index.html', stock_items=stock_items, usd_to_inr=USD_TO_INR)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form.get('price', 0.0))
    category = request.form.get('category', '')
    new_id = len(stock_items) + 1
    stock_items.append({"id": new_id, "name": name, "quantity": quantity, "price": price, "category": category})
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    global stock_items
    stock_items = [item for item in stock_items if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
