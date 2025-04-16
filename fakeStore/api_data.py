import requests

# Fake Store API'den ürün verilerini çek
def fetch_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    
    # Eğer başarılı bir şekilde veri alındıysa
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Verileri al ve yazdır
products = fetch_products()

# Verileri kontrol et
if products:
    print("Ürünler başarıyla alındı!")
else:
    print("Veri alınırken bir hata oluştu.")
