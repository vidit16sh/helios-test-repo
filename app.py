# helios-test-repo/app.py

from flask import Flask
# Let's imagine a simple in-memory "database" for this example
DB = {}
NEXT_ID = 1

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# New, complex function with a race condition
def process_order(items):
    """
    Creates an order, saves it, and immediately fetches it.
    BUG: The 'save_to_db' is mocked to be slow, creating a race condition.
    """
    global NEXT_ID
    order_id = NEXT_ID
    order = {"id": order_id, "items": items, "status": "pending"}
    
    # This simulates a slow database write
    save_to_db(order)
    
    # This tries to fetch the order immediately
    fetched_order = get_from_db(order_id)
    
    if not fetched_order:
        # This is the error that will be triggered
        raise ValueError(f"Order {order_id} could not be confirmed as it was not found.")

    NEXT_ID += 1
    return fetched_order

# --- Mock Database Functions ---
def save_to_db(order):
    # In a real test, we would mock this to introduce a delay
    DB[order["id"]] = order

def get_from_db(order_id):
    return DB.get(order_id)