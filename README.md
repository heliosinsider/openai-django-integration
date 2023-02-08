# Project setup and run

1. Clone the repository 
  ```bash
  $ git clone git@github.com:mominur-helios/openai-django-integration.git
  $ # or
  $ git clone https://github.com/mominur-helios/openai-django-integration.git
  ```
2. `cd` into the folder
3. Rename the `.env.example` file to `.env` and add the credentials. For the `API_KEY` go to this [link](https://platform.openai.com/account/api-keys) and generate a new secret key
4. Install the dependencies
  ```bash
  $ pip install -r requirements.txt
  ```
5. Start the app

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```