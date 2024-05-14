import customtkinter
from typing import TypedDict
from config import APP_NAME, APP_WIDTH, APP_HEIGHT, APP_MIN_WIDTH, APP_MIN_HEIGHT
from .home_view import HomeView
from .signin_view import SignInView
from .signup_view import SignUpView

class Frames(TypedDict):
    signin_view: SignInView
    signup_view: SignUpView
    home_view: HomeView

class View(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.minsize(width=APP_MIN_WIDTH, height=APP_MIN_HEIGHT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignInView, "signin_view")
        self._add_frame(SignUpView, "signup_view")
        self._add_frame(HomeView, "home_view")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()
    
    def start_mainloop(self) -> None:
        self.mainloop()