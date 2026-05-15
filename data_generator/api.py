from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import json

app = FastAPI(title="Fake Commerce API", version="1.0.0")

# ============= MODÈLES PYDANTIC =============
class Order(BaseModel):
    order_id: int
    customer_id: int
    product_id: int
    quantity: int
    price: float
    order_date: str
    region: str

class Customer(BaseModel):
    customer_id: int
    name: str
    email: str
    country: str

class Product(BaseModel):
    product_id: int
    product_name: str
    category: str
    price: float

# ============= DONNÉES FAKE =============
REGIONS = ["North America", "Europe", "Asia", "South America", "Africa"]
CATEGORIES = ["Electronics", "Clothing", "Home", "Sports", "Books"]
COUNTRIES = ["USA", "UK", "France", "Germany", "Japan", "Canada", "Brazil"]

def generate_fake_orders(num_orders: int = 100) -> list:
    """Générer des commandes FAKE avec du bruit intentionnel"""
    orders = []
    for i in range(num_orders):
        orders.append({
            "order_id": i + 1,
            "customer_id": random.randint(1, 50),
            "product_id": random.randint(1, 30),
            "quantity": random.randint(-5, 20),  # ❌ BUG: quantités négatives
            "price": round(random.uniform(10, 500), 2),
            "order_date": (datetime.now() - timedelta(days=random.randint(0, 90))).isoformat(),
            "region": random.choice(REGIONS) if random.random() > 0.1 else None,  # ❌ BUG: nulls
        })
    return orders

def generate_fake_customers(num_customers: int = 50) -> list:
    """Générer des clients FAKE"""
    customers = []
    for i in range(num_customers):
        customers.append({
            "customer_id": i + 1,
            "name": f"Customer_{i+1}",
            "email": f"customer{i+1}@example.com" if random.random() > 0.05 else None,  # ❌ BUG: emails nulls
            "country": random.choice(COUNTRIES),
        })
    return customers

def generate_fake_products(num_products: int = 30) -> list:
    """Générer des produits FAKE"""
    products = []
    for i in range(num_products):
        products.append({
            "product_id": i + 1,
            "product_name": f"Product_{i+1}",
            "category": random.choice(CATEGORIES),
            "price": round(random.uniform(5, 1000), 2),
        })
    return products

# ============= ENDPOINTS =============
@app.get("/")
def root():
    return {"message": "🎉 Fake Commerce API is running!", "version": "1.0.0"}

@app.get("/api/orders")
def get_orders(limit: int = 100):
    """Retourner des commandes FAKE"""
    orders = generate_fake_orders(limit)
    return {"count": len(orders), "data": orders}

@app.get("/api/customers")
def get_customers(limit: int = 50):
    """Retourner des clients FAKE"""
    customers = generate_fake_customers(limit)
    return {"count": len(customers), "data": customers}

@app.get("/api/products")
def get_products(limit: int = 30):
    """Retourner des produits FAKE"""
    products = generate_fake_products(limit)
    return {"count": len(products), "data": products}

@app.post("/api/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
