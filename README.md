# OpenSourceSession

[![Build Status](https://travis-ci.org/vaibhavsingh97/OpenSourceSession.svg?branch=master)](https://travis-ci.org/vaibhavsingh97/OpenSourceSession)
[![Requirements Status](https://requires.io/github/vaibhavsingh97/OpenSourceSession/requirements.svg?branch=master)](https://requires.io/github/vaibhavsingh97/OpenSourceSession/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/vaibhavsingh97/OpenSourceSession/badge.svg?branch=master)](https://coveralls.io/github/vaibhavsingh97/OpenSourceSession?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://vaibhavsingh97.mit-license.org/)


The website is created to provide information about the event for open source and students can register their interest in the event.

[Website](https://open-source-session.herokuapp.com/)


### Technologies Used

This project uses a number of open source projects:

* [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/docs/3.3/) - Responsive frontend framework
* [Heroku](https://www.heroku.com/) - Webapp deployed here
* [Travis](travis-ci.org) - Continuous Integration of the project

## Installations
Run
```
pip install -r requirements.txt
```
to install everything required to run this project on heroku as well as on your local.


## To run this in your local

1. Clone this repository using
	```
	$ git clone https://github.com/vaibhavsingh97/OpenSourceSession.git
	```

2. Go inside main Django app [Instructional video on installing Django](https://youtu.be/qgGIqRFvFFk)
	```
	$ cd OpenSourceSession
	```

3. Collectstatic files using
	```
	$ python manage.py collectstatic
	```

3. Migrating files using
	```
	$ python manage.py makemigrations
    $ python manage.py migrate
	```

4. Run the app
	```
	$ python manage.py runserver
	```

To run the web app in Debug mode set the DEBUG environment variable.
In Linux, run the `export DEBUG=True` command in the terminal.

## Issues

You can report the bugs at the [issue tracker](https://github.com/vaibhavsingh97/StalkPy/issues)

## License

Built with ♥ by Vaibhav Singh([@vaibhavsingh97](https://github.com/vaibhavsingh97)) under [MIT License](https://vaibhavsingh97.mit-license.org/)

