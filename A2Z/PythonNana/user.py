class User:
    def __init__(self, user_email, user_name, user_password, current_job_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.password = new_job_title

