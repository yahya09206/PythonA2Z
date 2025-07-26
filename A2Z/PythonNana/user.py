class User:
    def __init__(self, user_email, user_name, user_password, current_job_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")


app_user_one = User("email@email.com", "johnny bravo", "hubba", "body builder")
app_user_one.get_user_info()

app_user_one.change_job_title("trainer")
app_user_one.get_user_info()
