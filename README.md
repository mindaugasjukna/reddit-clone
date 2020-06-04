# reddit-clone

How to install (on windows):
1. Clone project. Open terminal and redirect to the project in the terminal

2. Make sure python is installed 
```bash
python -V
```

3. Create a virtual environment in the project folder
```bash
python -m venv .
```

4. Activate the virtual environment
```bash
Scripts/activate
```
ProjectName should now highlight green if Scripts is located in ProjectName/Scripts/activate


4. Upgrade to the latest version of pip
```bash
pip install --upgrade pip
```

6. Install the requirements for the project
```bash
pip install -r requirements.txt
```

7. Run the server 
```bash
python manage.py runserver
```