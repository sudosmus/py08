from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


def check_dependencies() -> dict[str, str | None]:
    versions: dict[str,str | None] = {}

    try:
        import pandas as pd
        versions["pandas"] = pd.__version__
    except ImportError:
        versions["pandas"] = None

    try:
        import numpy as np
        versions["numpy"] = np.__version__
    except ImportError:
        versions["numpy"] = None

    try:
        import requests as rq
        versions["requests"] = rq.__version__
    except ImportError:
        versions["requests"] = None

    try:
        import matplotlib
        versions["matplotlib"] = matplotlib.__version__
    except ImportError:
        versions["matplotlib"] = None

    return versions

def print_dependencies(versions: dict[str,str | None]) -> None:
    labels = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualisation ready",
    }
    for package, version in versions.items():
        if version is not None:
            print(f"[OK] {package} ({version}) - {labels[package]}")
        else:
            print(f"[MISSING] {package} - install with pip or poetry")

def generate_matrix() -> np.ndarray:
    import numpy as np
    data = np.random.normal(50, 10, 1000)
    return data

def generate_graph(data: np.ndarray) -> str:
    import matplotlib
    import matplotlib.pyplot as plt
    plt.hist(data)
    plt.title("Matrix data distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    filename: str = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()
    return filename

def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    versions = check_dependencies()
    print_dependencies(versions)
    print()
    if not all(versions.values()):
        print("Install with pip: pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        return
    print()
    print("Analysing Matrix data...")
    data = generate_matrix()
    print(f"Processing {len(data)} data points")
    print("Generating visualisation...")
    print()
    filename: str = generate_graph(data)
    print("Analysis complete!")
    print(f"Result saved to: {filename}")


if __name__ == "__main__":
    main()