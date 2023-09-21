class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.profile = {}
        self.linked_accounts = []
        self.transactions = []
        self.alert_preferences = {}

    def create_profile(self, personal_info, financial_info):
        self.profile['personal_info'] = personal_info
        self.profile['financial_info'] = financial_info

    def link_account(self, account):
        self.linked_accounts.append(account)

    def monitor_transactions(self):
        for account in self.linked_accounts:
            new_transactions = account.fetch_new_transactions()
            self.transactions.extend(new_transactions)
            self.notify_user_about_transactions(new_transactions)

    def notify_user_about_transactions(self, transactions):
        # Logic to send notifications to the user
        pass

    def set_alert_preference(self, alert_type, enabled):
        self.alert_preferences[alert_type] = enabled

    def fetch_transaction_history(self):
        return self.transactions

    def provide_feedback(self, transaction_id, feedback):
        # Logic to store user feedback for a specific transaction
        pass

    def get_customer_support(self, inquiry):
        # Logic to handle customer support inquiries
        pass


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def fetch_new_transactions(self):
        # Logic to retrieve new transactions from the bank
        pass

    def perform_transaction(self, receiver, amount, purpose):
        # Logic to perform a transaction and update transaction history
        pass


class CurrencyConverter:
    @staticmethod
    def get_conversion_rate(from_currency, to_currency):
        # Logic to fetch real-time currency conversion rates
        pass


class RemittanceApp:
    def __init__(self):
        self.users = []
        self.accounts = []

    def register_user(self, username, email, password):
        new_user = User(username, email, password)
        self.users.append(new_user)
        return new_user

    def create_bank_account(self, account_number, balance):
        new_account = BankAccount(account_number, balance)
        self.accounts.append(new_account)
        return new_account


# Example usage
if __name__ == "__main__":
    app = RemittanceApp()
    user1 = app.register_user("john_doe", "john@example.com", "secure_password")
    user1.create_profile(personal_info={"name": "John Doe", "dob": "1990-01-01"},
                         financial_info={"income": 50000, "credit_score": 750})
    bank_account = app.create_bank_account("123456789", 10000)
    user1.link_account(bank_account)

    # Simulate monitoring transactions and sending notifications
    user1.monitor_transactions()

    # Fetch transaction history
    transaction_history = user1.fetch_transaction_history()

    # Set alert preferences
    user1.set_alert_preference("transaction", True)

    # Perform currency conversion
    conversion_rate = CurrencyConverter.get_conversion_rate("USD", "EUR")

    # Provide feedback on a transaction
    user1.provide_feedback(transaction_id="xyz123", feedback="Great experience!")

    # Contact customer support
    user1.get_customer_support("I have a transaction-related inquiry.")
