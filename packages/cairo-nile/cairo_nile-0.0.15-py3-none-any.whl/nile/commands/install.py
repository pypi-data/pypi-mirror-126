"""Command to install a specific version of Cairo."""
import subprocess
import sys


def install_command():
    """Install Cairo package with the given tag."""
    print("🗄  Installing Cairo")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cairo-lang"])
    print("✨  Cairo successfully installed!")
