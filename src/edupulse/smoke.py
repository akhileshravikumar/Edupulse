"""Dependency-free project health check for Day 1."""
from pathlib import Path
import sys


def main() -> None:
    assert sys.version_info >= (3, 11), "Python 3.11 or newer required"
    root = Path(__file__).resolve().parents[2]
    required = ("docs", "tests", "evidence", "data")
    missing = [name for name in required if not (root / name).is_dir()]
    if missing:
        raise RuntimeError(f"Missing directories: {missing}")
    print(f"EduPulse smoke: PASS | Python {sys.version.split()[0]}")
    print(f"Project root: {root}")


if __name__ == "__main__":
    main()