import os
from pathlib import Path
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s........')

project_name = "cnnClassifier"

list_of_files = [ 
    "./github/workflows/·gitkeep",
    f"src/{project_name}/_init__.py",
    f"src/{project_name}/components/__init_.py",
    f"src/{project_name}/utils/__init__.PY",
    f"src/{project_name}/config/__init__PY",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    # Platform independence:
    # pathlib handles path separators and other platform-specific details automatically, 
    # making your code more portable across different operating systems (Windows, macOS, Linux).
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Check if the directory exists, if not create it   
    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Check if the file exists, if not create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:   
        logging.info(f"{filename} is already exists")
