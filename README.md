# WORKSHOP FLASK 2

**1. Install the python lib requirements :**

<code>pip install -r requirements.txt</code>

Flask default environment is **ENV=Production**

## Run app with bash command

**2. First set flask environment :**

<code>$ export FLASK_ENV=development</code>

or

<code>$ export FLASK_ENV=testing</code>


**3. Then run app :**

<code>$ flask run</code>


## Run app with windows Powershell (in virtual python env):

**2. First set flask app and environment :**

<code>$env:FLASK_APP = "main.py"</code>

<code>$env:FLASK_ENV = "development"</code>

or

<code>$env:FLASK_ENV = "testing"</code>


**3. Then run app :**

<code>flask run</code>


