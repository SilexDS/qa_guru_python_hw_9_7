import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
FILES_DIR = os.path.join(CURRENT_DIR, "files")

if not os.path.exists("files"):
    os.mkdir("files")
