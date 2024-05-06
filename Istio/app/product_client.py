import requests


frontend_url = "http://frontend-service:8080"

def get_product_list():
    try:
        response = requests.get(frontend_url + "/products")
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener la lista de productos:", response.status_code)
            return None
    except Exception as e:
        print("Error al conectarse al servicio de frontend:", e)
        return None

if __name__ == "__main__":
    
    product_list = get_product_list()
    if product_list:
        print("Lista de productos:")
        for product in product_list:
            print("- ", product)
