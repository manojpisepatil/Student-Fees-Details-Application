# NextGen-edunet

</hr>

**Project Structure**

student_fees/
│── student_fees/         # Django project folder
│   │── settings.py       # Project settings
│   │── urls.py           # Project-wide URL routing
│   │── wsgi.py           # WSGI entry point
│
│── fees/                 # Django app
│   │── models.py         # Database models
│   │── views.py          # Views (logic)
│   │── urls.py           # App-specific URL routing
│   │── forms.py          # Forms handling
│   │── templates/fees/   # HTML files
│   │── static/fees/      # CSS & JS files
│
│── db.sqlite3            # Database (for SQLite)
│── manage.py             # Django CLI
