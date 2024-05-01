import reflex as rx

class State(rx.State): ...

class LoginState(State):
    email: str
    password: str

    def update_email(self, email):
        self.email = email
    
    def update_password(self, password):
        self.password = password