from models import Model
from models.user_model import UserModel
from views import View
from utils.helper import show_message


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin_view"]

        self._bind()
        self.model.user.add_event_listener("user_logged", self.auth_state_listener)

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signup_btn.configure(command=self.signup_btn)
        self.frame.signin_btn.configure(command=self.signin_btn)
    
    def auth_state_listener(self, data: UserModel) -> None:
        if data.is_logged:
            self.view.switch('home_view')

    def signup_btn(self) -> None:
        self.view.switch("signup_view")

    def signin_btn(self) -> None:
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        if len(username) < 1:
            show_message("warning", "Username field is empty")
            return
        if len(password) < 1:
            show_message("warning", "Password field is empty")
            return
        self.model.user.login(username=username, password=password)
        self.frame.password_input.delete(0, last_index=len(password))