# cm.py
bill_items = []

def add_item(name, price, qty):
    item = {
        "name": name,
        "price": price,
        "qty": qty,
        "total": price * qty
    }
    bill_items.append(item)

def calculate_total():
    return sum(item["total"] for item in bill_items)

def get_items():
    return bill_items

def reset_bill():
    bill_items.clear()
