import pytest
import os
import sys

# Ensure that project directories are accessible
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def run_tests():
    """Execute Pytest with custom arguments."""
    test_args = [
        "tests",  # Directory to run tests
        "--html=reports/test_report.html",  # Generate an HTML report
        "--self-contained-html"  # Ensure all assets are embedded
    ]

    # Run Pytest with specified arguments
    exit_code = pytest.main(test_args)

    # Exit with the same code as Pytest to indicate success/failure
    sys.exit(exit_code)


if __name__ == "__main__":
    run_tests()
