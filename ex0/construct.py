import os
import sys
import site

def main() -> None:

    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        venv_name: str = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system\n")
        print("Package installation path:\n")
        try:
            path_list: list[str] = site.getsitepackages()
            print(f"{path_list[0]}")
        except (AttributeError, IndexError):
            version_str: str = f"python{sys.version_info.major}.{sys.version_info.minor}"
            n_path: str = os.path.join(sys.prefix, "lib", version_str, "site-packages")
            print(n_path)

    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print(
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install."
        )
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env\n")
        print(r"source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")

if __name__ == "__main__":
    main()