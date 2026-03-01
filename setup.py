from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="print-statements-hook",
    version="0.2.0",
    author="Kuldeep Modh",
    author_email="kuldeepmodh1823@gmail.com",
    description="A pre-commit hook to detect and prevent print statements in Python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kuldeep-Modh/print-statements-hook",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "check-print-statements=print_statement_hook.hook:check_print_statements",
        ],
    },
)