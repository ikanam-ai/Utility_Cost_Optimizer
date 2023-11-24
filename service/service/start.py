import os
import subprocess


def start() -> None:
    cmd = ["poetry", "run", "streamlit", "run", "service/auth.py",
           "--server.port", os.environ.get("STREAMLIT_PORT", 7484)]
    subprocess.run(cmd)
