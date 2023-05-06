# Water Melon Markets

Make sure you have Python installed.

In the project root directory, open a terminal and run `python -m venv env` to start a new virtual environment called _env_. 
>This can actually be what ever you want to call it but just run `python -m venv <name you like>`.

Activate your virtual environment `env\scripts\activate` 
>Or `<name you like>\scripts\activate` If you are using a custom name for your env.

Next make sure you have pip installed then run `pip install -r requirements.txt` to install all project dependencies.

Now it's ready to run. The project uses SQLite file system database and will automatically create one when you run it. 
You probably want to allow that on your os. 

>Please before you run, run tests using `python manage.py test` to ensure all tests pass. 

The project was built with Python 3.10 and has not been tested yet with other python versions. Therefore running tests should be necessary.

>Debug was left on to let you detect any errors and know what's going on.

Now run it and test in your browser by navigating to the url **http://localhost:8000** or **http://127.0.0.1:8000** if your network doesn't support *localhost*

>To run, use `python manage.py runserver`
