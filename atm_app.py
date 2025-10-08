import streamlit as st

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"${amount:.2f} withdrawn successfully."


if 'atm' not in st.session_state:
    st.session_state.atm = ATM(balance=1000)

st.title("🏧 ATM System")


option = st.radio("Choose an option:", ["Check Balance", "Deposit", "Withdraw"])


if option == "Check Balance":
    st.success(st.session_state.atm.check_balance())

elif option == "Deposit":
    amount = st.number_input("Enter amount to deposit:", min_value=0.0, step=10.0, format="%.2f")
    if st.button("Deposit"):
        result = st.session_state.atm.deposit(amount)
        st.info(result)

elif option == "Withdraw":
    amount = st.number_input("Enter amount to withdraw:", min_value=0.0, step=10.0, format="%.2f")
    if st.button("Withdraw"):
        result = st.session_state.atm.withdraw(amount)
        st.info(result)

