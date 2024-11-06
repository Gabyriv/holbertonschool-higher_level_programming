#!/usr/bin/python3

from flask import Flask, render_template, json, csv, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data['items']
            return render_template('items.html', items=items)
    except Exception as e:
        return render_template('items.html', items=[])

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                            error="Wrong source")

    try:
        products = []
        if source == 'json':
            with open('products.json', 'r') as file:
                data = json.load(file)
                products = data['products']
        else:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        if product_id:
            products = [product for product in products if str(product.get('id')) == str(product_id)]
            if not products:
                return render_template('product_display.html',
                                    error="Product not found")

        return render_template('product_display.html',
                            products=products)

    except Exception as e:
        return render_template('product_display.html',
                            error=f"Error reading file: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
