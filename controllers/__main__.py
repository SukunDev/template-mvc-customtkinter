from views import View
from models import Model
from .signin_controller import SignInController
from .signup_controller import SignUpController
from .home_controller import HomeController


class Controller:
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model

        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)

    def start_app(self):
        self.view.switch("signin_view")
        self.view.start_mainloop()