
<h3 align="center">Visie simple CRUD Test</h3>

---

<p align="center"> A small test for Python API development
</p>
<p>

</p>


##  Running the project

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.10+
Python 3.6+ (Not Tested)
```

### Installing

A step by step series of examples that tell you how to get a development env running.


1. Get this project

```
git clone https://github.com/Vrrl/
cd visie-crud
```
##### Without Docker

2. Installing the dependences (virtualenv recommended)

```
pip install -r requirements.txt
```
3. Configure env file

```
cp .env.example .env

# fill .env variables
```

4. Run the server API

```
python server.py
```

5. Check if it is running with curl request

```
curl http://127.0.0.1:8000/docs

```

## Running the tests

To run the Unit Tests with PyTest after installation run in the project folder

```
pytest -v
```


### And coding style tests

Test the code quality according to the pylint config file

```
pylint src
```

## Usage

Go to the API Documentation at http://127.0.0.1:8000/docs and make a request

## Built Using 

- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Sqlalchemy](https://www.sqlalchemy.org/) - Database ORM
- [PyTest](https://pytest.org/) - Test Tools

