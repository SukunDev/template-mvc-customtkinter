import hashlib
from datetime import datetime
from tkinter import messagebox


def encode_md5(input_string) -> str:
    byte_string = input_string.encode('utf-8')
    md5_hash = hashlib.md5()
    md5_hash.update(byte_string)
    encoded_string = md5_hash.hexdigest()
    
    return encoded_string

def created_at() -> datetime:
    created_at = datetime.now()
    return created_at

def show_message(mtype, message) -> None:
    if mtype == "error":
        messagebox.showerror("Error", message=message)
    elif mtype == "warning":
        messagebox.showwarning("Warning", message=message)
    elif mtype == "info":
        messagebox.showinfo("Info", message=message)