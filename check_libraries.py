import importlib
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError
else:
    from importlib_metadata import version, PackageNotFoundError

required_libraries = [
    "Flask",
    "chainlit",
    "langchain",
    "langchain_community",
    "huggingface_hub",
    "requests",
    "numpy",
    "pandas",
    "scikit-learn",
    "mlflow",
    "boto3",
    "tensorflow",
    "torch",
    "pydantic",
    "sqlalchemy"
]

def check_libraries(libraries):
    for lib in libraries:
        try:
            lib_version = version(lib)
            print(f"{lib} is installed with version {lib_version}")
        except PackageNotFoundError:
            print(f"{lib} is NOT installed")
        except ImportError:
            print(f"Failed to import {lib}")

if __name__ == "__main__":
    check_libraries(required_libraries)
