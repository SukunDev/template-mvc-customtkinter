from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .observable_model import ObservableModel
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from utils.helper import created_at, encode_md5, show_message

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    full_name = Column(String)
    created_at = Column(Date)

    def __repr__(self):
        return f"<User(id='{self.id}', type='{self.username}')>"
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.full_name,
            'created_at': self.created_at,
        }

class UserModel(ObservableModel):
    def __init__(self):
        super().__init__()
        engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_TRACK_MODIFICATIONS)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
        self.current_user = None
        self.is_logged = False
        
    def create_user(self, full_name: str, username: str, password: str) -> None:
        if not full_name:
            raise Exception("parameter 'full_name' is empty")
        if not username:
            raise Exception("parameter 'username' is empty")
        if not password:
            raise Exception("parameter 'password' is empty")
        check_user = self.__get_user_by_username(username=username)
        if check_user is not None:
            show_message('error', 'Username has been registered')
            return
        new_user = User(username=username, password=encode_md5(password), full_name=full_name, created_at=created_at())
        self.session.add(new_user)
        self.session.commit()
        self.trigger_event("user_created")
    
    def login(self, username: str, password:str) -> None:
        if not username:
            raise Exception("parameter 'username' is empty")
        if not password:
            raise Exception("parameter 'password' is empty")
        user = self.__get_user_by_username(username=username)
        if user is None:
            show_message("warning", "Username not found, please Sign Up before Sign In")
            return
        if user.password != encode_md5(password):
            show_message("warning", "Credential not match")
            return
        self.is_logged = True
        self.current_user = user
        self.trigger_event("user_logged")
    
    def logout(self) -> None:
        self.is_logged = False
        self.current_user = None
        self.trigger_event("user_logged")
    
    def __get_user_by_username(self, username) -> User:
        return self.session.query(User).filter_by(username=username).first()
