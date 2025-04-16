# app.py
from flask import Flask, render_template
from fakeStore.api_data import fetch_products  # api_data.py'dan fonksiyonu import et

app = Flask(__name__)

# Ana sayfa route'u
@app.route('/')
def index():
    products = fetch_products()  # API'den ürün verilerini al
    return render_template('index.html', products=products)  # Ürünleri HTML'ye gönder

if __name__ == '__main__':
    app.run(debug=True)
