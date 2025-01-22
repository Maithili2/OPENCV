import os
import subprocess
import sys

def create_and_activate_virtualenv():
    # Set up the environment name
    env_name = "opencv_env"

    # Create the virtual environment
    print(f"Creating virtual environment: {env_name}")
    subprocess.check_call([sys.executable, "-m", "venv", env_name])

    # Install opencv-python into the virtual environment
    print(f"Installing OpenCV in {env_name}")
    subprocess.check_call([os.path.join(env_name, 'Scripts', 'pip.exe'), 'install', 'opencv-python'])

    # Activate the virtual environment (Windows-specific)
    activate_script = os.path.join(env_name, 'Scripts', 'activate')
    print(f"To activate your virtual environment, run: {activate_script}")
    print("Note: Activation script is not executable directly through Python. Please activate it manually via the command line.")

if __name__ == "__main__":
    create_and_activate_virtualenv()
