from models import Model
from models.user_model import UserModel
from views import View
from utils.helper import show_message

class SignUpController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup_view"]
        
        self._bind()
        self.model.user.add_event_listener("user_created", self.auth_state_listener)

    def _bind(self):
        self.frame.signin_btn.configure(command=self.signin_btn)
        self.frame.signup_btn.configure(command=self.signup_btn)

    def auth_state_listener(self, data: UserModel) -> None:
        show_message("info", "Success to create user")
        self.view.switch('signin_view')

    def signin_btn(self):
        self.view.switch("signin_view")

    def signup_btn(self):
        fullname =  self.frame.fullname_input.get()
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        if len(fullname) < 1:
            show_message("warning", "Full Name field can't empty")
            return
        if len(username) < 1:
            show_message("warning", "username field can't empty")
            return
        if len(password) < 1:
            show_message("warning", "password field can't empty")
            return
        self.model.user.create_user(username=username, password=password, full_name=fullname)
        self.clear_form()
    
    def clear_form(self) -> None:
        fullname = self.frame.fullname_input.get()
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        self.frame.fullname_input.delete(0, last_index=len(fullname))
        self.frame.fullname_input.focus()
        self.frame.username_input.delete(0, last_index=len(username))
        self.frame.password_input.delete(0, last_index=len(password))