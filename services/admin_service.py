class AdminService:
    def __init__(self):
        self.admin_user = "pradip"
        self.admin_pass = "pradip1234"

    def verify_admin(self, username, password):
        return username == self.admin_user and password == self.admin_pass