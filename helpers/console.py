import os
import shutil


def get_terminal_width():
    return shutil.get_terminal_size().columns
