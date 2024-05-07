import reflex as rx

from DevToolKit.api.api import user_login_endpoint, user_registration_endpoint

class State(rx.State):
    def void_event(self): ...

class LoginState(State):
    email: str
    password: str

    def update_email(self, email):
        self.email = email
    
    def update_password(self, password):
        self.password = password

class RegisterState(State):
    username:str
    email: str
    password: str

    def update_username(self, username):
        self.username = username

    def update_email(self, email):
        self.email = email

    def update_password(self, password):
        self.password = password

class Registration(RegisterState):
    async def user_registration(self):
        registration_result = await user_registration_endpoint(self.username, self.email, self.password)
        
        if registration_result is True:
            print("Registrado")
            return rx.redirect("/login")
        else:
            print("Error al registrar:", registration_result)

class Authentication(LoginState):
    access_token: str
    user_id: str
    user_email: str
    session_exp: str

    async def user_login(self):
        (    
            self.access_token,
            self.user_id,
            self.user_email,
            self.session_exp
        )= await user_login_endpoint(self.email, self.password)

        print(
            self.access_token,
            self.user_id,
            self.user_email,
            self.session_exp
        )
