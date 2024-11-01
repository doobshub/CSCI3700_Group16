# Homework 3


## Quick Start
### Local Test Setup

Install a Python 3 virtual environment:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

Activate the virtual environment:
```
source python_venv/bin/activate
```

Install the requiremnts:
```
pip3 install -r requirements.txt
```

Add the database tables to your database if you do not already have them:
```
CREATE TABLE basket_a (

    a INT PRIMARY KEY,

    fruit_a VARCHAR (100) NOT NULL

);

CREATE TABLE basket_b (

    b INT PRIMARY KEY,

    fruit_b VARCHAR (100) NOT NULL

);

```
```
INSERT INTO basket_a (a, fruit_a)

VALUES

    (1, 'Apple'),

    (2, 'Orange'),

    (3, 'Banana'),

    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)

VALUES

    (1, 'Orange'),

    (2, 'Apple'),

    (3, 'Watermelon'),

    (4, 'Pear');
```

Start the server:
```
python3 main.py
```
