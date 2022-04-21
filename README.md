# Manage Encryption Key
### _Generating and Managing Encryption Key_

Manage Encryption Key is Windows and Linux compatible,
Powered by Python!

###### Code Formatting: autopep8 and black with 120 char length

_Built by Caleb Rott_

## Features

- Generate Encryption Key
- Decrypt Binary File
- Encrypt Data to Binary File

---

## Installation Prerequisite

Manage Encryption Key requires [Python](https://www.python.org/downloads/) v3.10.3+ to run.

Create a python virtual environment:
```sh
cd C:\app_location\
python -m venv env
```

Activate your virtual environment:
```sh
.\env\Scripts\activate
```

Install the dependencies using the provided requirements.txt file:
```sh
pip install -r requirements.txt
```

Confirm your dependencies are installed using:
```sh
pip list
```

## How to Run
##### The apps are ran via CLI in the terminal
- Launch the main app: **manage_encryption_key.py**
    - Create an encryption key
        - This will create a .env file in the root of the directory
        - Do not rename/move this file, it's how the **python-dotenv** finds the key for encrypting/decrypting
        - ![alt text](https://imgur.com/AF9bMvM)
    - Encrypt files
        - By default the script saves binary files to the **Data** folder
        - This can be updated using the **Settings** option
    - Decrypt files
        - Decrypt your binary files using the .env file
