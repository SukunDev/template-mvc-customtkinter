from models import Model
from models.user_model import UserModel
from views import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home_view"]
    
        self._bind()
        self.model.user.add_event_listener("user_logged", self.auth_state_listener)
    
    def _bind(self):
        self.frame.signout_btn.configure(command=self.signout_btn)

    def auth_state_listener(self, data: UserModel) -> None:
        current_user = self.model.user.current_user
        if data.is_logged:
            self.frame.greeting.configure(text=f"Welcome, {current_user.full_name}!")
        else:
            self.view.switch('signin_view')
    
    def signout_btn(self):
        self.model.user.logout()