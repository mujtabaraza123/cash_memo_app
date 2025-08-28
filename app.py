# app.py
import streamlit as st
from cm import add_item, calculate_total, get_items, reset_bill

st.title("Cash Memo System")

# Input fields
name = st.text_input("Enter Item Name")
price = st.number_input("Enter Price", min_value=0.0, step=0.5)
qty = st.number_input("Enter Quantity", min_value=1, step=1)

# Add item button
if st.button("Add Item"):
    if name and price > 0 and qty > 0:
        add_item(name, price, qty)
        st.success(f"Added {name} x {qty}")
    else:
        st.error("Please enter valid item details")

# Display items table
items = get_items()
if items:
    st.subheader("Bill Items")
    st.table(items)

    total = calculate_total()
    st.subheader(f"Total: {total}")

# Reset bill
if st.button("Reset Bill"):
    reset_bill()
    st.warning("Bill has been cleared")
