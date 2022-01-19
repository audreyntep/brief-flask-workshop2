# WORKSHOP FLASK 2

**1. Install the python lib requirements**

<code>pip install -r requirements.txt</code>

**2. Set flask app and environment, then run**

Flask default environment config is **ENV=Production**


- BASH :

<code>$ export FLASK_ENV=development</code>

<code>$ flask run</code>    


- Windows POWERSHELL :

<code>$env:FLASK_APP = "main.py"</code>

<code>$env:FLASK_ENV = "development"</code>

<code>flask run</code>


- Windows CMD :

<code>set FLASK_APP=main</code>

<code>set FLASK_ENV=development</code>

<code>flask run</code>


