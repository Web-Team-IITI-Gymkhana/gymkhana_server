import os


def activate_venv():
    current_path = os.getcwd()
    activation_file = os.path.join(current_path, "venv", "bin", "activate_this.py")
    exec(open(activation_file).read(), {"__file__": activation_file})