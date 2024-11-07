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

def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data

def load_csv(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        try:
            products = load_json('products.json')
        except FileNotFoundError:
            error_message = "JSON file not found."
    elif source == 'csv':
        try:
            products = load_csv('products.csv')
        except FileNotFoundError:
            error_message = "CSV file not found."
    else:
        error_message = "Wrong source."

    if product_id and not error_message:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            error_message = "Product not found."

    return render_template('product_display.html', products=products, error_message=error_message)
