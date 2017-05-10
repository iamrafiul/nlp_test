# Trivago Coding Challenge
This is the coding challenge given by trivago as a part of 'Software Engineer' position screening.

I am assuming that you already have Python 2.7 and virtual environment( "pip install virtualenv" ) installed in your machine.

To run the project, do the following after downloading/cloning the project in your machine:
1. Create a virtual environment using:
```shell
>> virtualenv venv
```
2. Enable virtual environment using:
```shell
>> source venv/bin/activate
```
3. Install all the dependencies from requirements.txt using:
```python
>> pip install -r requirements.txt
```
4. Once you're done with installing all the requirements, do the following to run the project:
```python
>> export FLASK_APP=app.py

>> flask run
```
This will run the app in your localhost at 5000 port. If everything goes well, you can access the app from browser using the url:

localhost:5000/?topic=<topic_name>
