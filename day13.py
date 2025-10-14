import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = "bank_data.json"

# ---------- Utility Functions ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Account Operations ----------
def create_account(data):
    st.subheader("Create Account")
    account_number = st.text_input("Enter account number")
    name = st.text_input("Enter name")
    initial_balance = st.number_input("Initial deposit", min_value=0, value=0)
    
    if st.button("Create Account"):
        if account_number in data:
            st.error("Account already exists!")
        else:
            data[account_number] = {
                "name": name,
                "balance": initial_balance,
                "transactions": [{"type": "Deposit", "amount": initial_balance, "time": str(datetime.now())}] if initial_balance > 0 else []
            }
            save_data(data)
            st.success(f"Account {account_number} created successfully!")

def view_account(data):
    st.subheader("View Account")
    account_number = st.text_input("Enter account number to view", key="view_acc")
    if account_number and account_number in data:
        account = data[account_number]
        st.write(f"**Name:** {account['name']}")
        st.write(f"**Balance:** {account['balance']}")
        st.write("**Transactions:**")
        for txn in reversed(account.get("transactions", [])):
            st.write(f"{txn['time']}: {txn['type']} - {txn['amount']}")
    elif account_number:
        st.error("Account not found!")

def deposit(data):
    st.subheader("Deposit Money")
    account_number = st.text_input("Account number", key="deposit_acc")
    amount = st.number_input("Deposit amount", min_value=0)
    if st.button("Deposit"):
        if account_number in data:
            data[account_number]["balance"] += amount
            data[account_number].setdefault("transactions", []).append({
                "type": "Deposit",
                "amount": amount,
                "time": str(datetime.now())
            })
            save_data(data)
            st.success(f"Deposited {amount} to {account_number}")
        else:
            st.error("Account not found!")

def withdraw(data):
    st.subheader("Withdraw Money")
    account_number = st.text_input("Account number", key="withdraw_acc")
    amount = st.number_input("Withdraw amount", min_value=0)
    if st.button("Withdraw"):
        if account_number in data:
            if data[account_number]["balance"] >= amount:
                data[account_number]["balance"] -= amount
                data[account_number].setdefault("transactions", []).append({
                    "type": "Withdraw",
                    "amount": amount,
                    "time": str(datetime.now())
                })
                save_data(data)
                st.success(f"Withdrew {amount} from {account_number}")
            else:
                st.error("Insufficient balance!")
        else:
            st.error("Account not found!")

def delete_account(data):
    st.subheader("Delete Account")
    account_number = st.text_input("Enter account number to delete", key="delete_acc")
    if st.button("Delete Account"):
        if account_number in data:
            del data[account_number]
            save_data(data)
            st.success(f"Account {account_number} deleted successfully!")
        else:
            st.error("Account not found!")

# ---------- Main App ----------
def main():
    st.title("🏦 Trust Bank Of India")
    data = load_data()
    
    menu = ["Create Account", "View Account", "Deposit", "Withdraw", "Delete Account"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Create Account":
        create_account(data)
    elif choice == "View Account":
        view_account(data)
    elif choice == "Deposit":
        deposit(data)
    elif choice == "Withdraw":
        withdraw(data)
    elif choice == "Delete Account":
        delete_account(data)

if __name__ == "__main__":
    main()
