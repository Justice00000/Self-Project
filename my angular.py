class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = self.password
        self.profile = {}

    def create_profile(self, personal_info, financial_info):
        self.profile['personal_info'] = personal_info

    def confirm_password(self, password):
        self.confirm_password = self.password
        if
            self.confirm_password = self.password
            print("Account Created")
        else:
            print("Password Not Match")



class MTN:
    def __init__(self):
        self.users = []
        self.accounts = []

    def register_user(self, username, email, password):
        new_user = User(username, email, password)
        self.users.append(new_user)
        return new_user
