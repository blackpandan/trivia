# Trivia App

this is a trivia game website that was created as part of my udacity course with some modifications from me,random questions are generated for you to answer based on the category you selected, it was developed using flask for backend and a react frontend.

the flask backend follows PEP8 guidelines for python.


## **Getting Started**

you need to have python installed on your system with node and npm (a package manager for node)


---
### Backend
---
- install python if it's not installed from the [official website](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

- create a virtual environment in other to have an isolated system more info [here](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20a,part%20of%20your%20operating%20system.)

- change directory to backend, install dependencies using pip
    ```
    pip install -r requirements.txt
    ```

- due to Flask-Cors depreciation some codes have to be corrected from the flask module, open ```core.py``` in ```{path to your env}/python/version/lib/python/site-packages/flask_cors/core.py```

    on **line 322 and 342** change ```collections.Iterable``` to ```collections.abc.Iterable```

- install a relational database management system (rdbms), recommended rdbms is postgresql you can download and get more info [here](https://www.postgresql.org/download/)

- create a database for the backend

    ```
    createdb trivia
    ```

- you can choose to populated the trivia database with sample data provided or by yourself.
to popluate the database change directory to ```./backend``` and run
    ```
    psql trivia < trivia.psql
    ```

- now to get the flask server running, if you intend to run it in a development environment, export the flask_env variable first

    for window cmd
    ```
    set FLASK_ENV=development
    ```
    for window powershell
    ```
    $Env:FLASK_ENV=development
    ```
    for linux
    ```
    export FLASK_ENV=development
    ```

    finally run the server with

    ```
    flask run
    ```

---
### Frontend
---


---
### Test

---

tests are located in the backend directory in test_flaskr.py file, to run tests: 
- change directory to backend

- create a database for the tests
    ```
    createdb trivia_test
    ```

- populate the database with sample data 
    ```
    psql trivia_test < trivia.psql
    ```

- then run the script with python
    ```
    python test_flaskr.py
    ```


## Api Reference

the documentation for the api is in the backedn folder, [link here](./backend/APIDOC.md)







