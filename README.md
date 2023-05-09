# README

Tutorial which I follow at the topics Python, Django and Test-driven 
development.

A to-do list app is developed.

The created code is based on the tutorial from the book *Test-Driven 
Development with Python: Obey the Testing Goat* by *Harry Percival*

[Link to the book](http://www.obeythetestinggoat.com/ "Obey the Testing Goat!")

# Initial Setup (only necessary after checkout)
## Create virtual environment

Open a cmd in your Windows user directory.

Create the directory .virtualenvs and enter it.

Now create the virtual environment:

    # Create a virtualenv
    python -m venv webapp-env

## Activate the virtual environment
To activate the environment call:
    
    # WINDOWS when using CMD:
    c:\Users\{user-account}\.virtualenvs\webapp-env\Scripts\activate.bat

    # WINDOWS when using PowerShell:
    c:\Users\{user-account}\.virtualenvs\webapp-env\Scripts\activate.ps1

    # LINUX:
    $ source ~/.virtualenvs/webapp-env/bin/activate

Where {user-account} has to be replaced by your Windows login.

## Activate the virtual environment from Git Bash

From page 160 of the book, Git Bash is required on Windows to use the
staging server. Activating the  virtual environment then goes like this:

    $ source /C/Users/{user-account}/.virtualenvs/webapp-env/Scripts/activate

Then you can enter the development directory and run the functional
tests:

    $ cd /E/Dev/Superlists
    $ STAGING_SERVER=superlists.your-domain.com python manage.py test functional_tests
    ...
    ...
    AssertionError: 'TODO' not found in 'Welcome to nginx!'

**If that fails because of execution policy:**
With PowerShell in admin mode, check if script execution is not allowed:

    > Get-ExecutionPolicy
    Restricted

So change it to allow signed scripts:

    Set-ExecutionPolicy RemoteSigned

Answer the question with 'yes' and then the activation script should run successfully.

The new Python environment has to be set up in VSCode.

So, in VSCode open the Command Palette (Ctrl+Shift+P).

Type: *Select Python Interpreter*

In the combobox you see all Python interpreters, also the ones in the
virtual environments. Select the newly created one.

#### Install Django and Selenium

Django should be installed while the virtual env is activated:

    pip install "django==3.2" selenium gunicorn fabric invocations patchwork

#### Install Gecko driver

Geckodriver is available from
[here](https://github.com/mozilla/geckodriver/releases). You need to
download and extract it and put it somewhere on your system path. 

- For macOS or Linux, one convenient place to put it is ~/.local/bin
- For Windows, put it in your Python Scripts folder 

To test that you’ve got this working, open up a Bash console and you should be able to run:

    geckodriver --version 
    geckodriver 0.17.0 
    The source code of this program is available at 
    https://github.com/mozilla/geckodriver. 
    
    This program is subject to the terms of the Mozilla Public License 2.0. 
    You can obtain a copy of the license at https://mozilla.org/MPL/2.0/.
