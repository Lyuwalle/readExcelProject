# 怎么定义一个类
class User:
    def __init__(self, email, name, password, current_job_state):
        self.email = email
        self.password = password
        self.name = name
        self.current_job_state = current_job_state

    def change_password(self, new_password):
        self.password = new_password

    def change_job_state(self, new_job_state):
        self.current_job_state = new_job_state

    def get_user_info(self):
        print(f"User(name: {self.name}, email: {self.email}, password: {self.password}, work_state: {self.current_job_state})")


app_user_one = User("nn@nn.com", "nn", "pwd", "working")
app_user_one.get_user_info()
app_user_one.change_password("pwd2")
app_user_one.change_job_state("get_off_word")
app_user_one.get_user_info()

print(type(app_user_one))