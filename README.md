# flask-api-boilerplate

git clone https://github.com/VishnuPrasad1998/flask-api-boilerplate.git flask-api-boilerplate

# Create the virtual environment
pipenv shell

# Install required Python packages
pip install -r requirements.txt

# Create DB tables
python manage.py init_db

#Initial migration
python manage.py runserver db init

#Initial migration for diff dbs
python manage.py runserver db init --multidb


python manage.py runserver db migrate
python manage.py runserver db upgrade

# Start the Flask development web server
python manage.py runserver

# Start the Flask development web server
py.test tests/