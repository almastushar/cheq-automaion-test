**Setup**
-----------
1. Install Python 3.9.X or above
2. Clone the project
3. Create a virtual environment inside the project root directory
4. Activate virtual environment
5. Run following command in project root directory
`pip install -r requirements.txt`
6. Once the required packages are installed you are ready to write your tests

**Running Tests**
----------

#### **1. RUN ALL TESTS**

To run the tests run the command `pytest tests --html=report/report.html --capture=no`
this will run the test modules in tests folder and generate designated reports and logs.

#### **2. RUN REGRESSION TESTS**

To run the tests run the command `pytest -m regression --html=report/report.html --capture=no`
this will run the test modules in tests folder which has Regression tag on it and generate designated reports and logs.

#### **3. RUN SANITY TESTS**

To run the tests run the command `pytest -m sanity --html=report/report.html --capture=no`
this will run the test modules in tests folder which has Sanity tag on it and generate designated reports and logs.

#### **4. RUN ALL TESTS IN PARALLEL**

To run the tests run the command `pytest -n auto --html=report/report.html --capture=no`
this will run the test modules in tests folder in Parallel and generate designated reports and logs.

**Note**
-----
If you are using PyCharm IDE then, after cloning the project open the project directory in PyCharm and create a
virtual environment from PyCharm's project settings. After that if you open terminal in PyCharm it will automatically 
activate the virtual environment.