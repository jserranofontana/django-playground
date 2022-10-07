django-htmx
Samples about htmx-alpine use in Django

Boilerplate based on info
https://geoff.tuxpup.com/posts/django_tailwind_htmx_how_i_start/

Write initial .env file
echo DEBUG=True >>.env
echo DJANGO_SECRET_KEY=$(poetry run python -c "import secrets; print(secrets.token_urlsafe())") >>.env
DATABASE_URL=<your Postgres URL>

Boilerplate.
- poetry virtualenv
- Python-3.10
- GitHub
- Project level templates

PreCommit 
- black = "^22.10.0"
- djhtml = "^1.5.2"
- pre-commit = "^2.20.0"

Dependencies
- python = "3.10.7"
- Django = "^4.1.2"
- django-htmx = "^1.12.2"
- django-extensions = "^3.2.1"
- django-environ = "^0.9.0"
- django-browser-reload = "^1.6.0"
- python-dotenv = "^0.21.0"
- crispy-bootstrap5 = "^0.7"
- django-bootstrap5 = "^22.1"
- django-allauth = "^0.51.0"
- django-forms-dynamic = "^1.0.0"
- django-widget-tweaks = "^1.4.12"
- fontawesomefree = "^6.2.0"
- psycopg2-binary = "^2.9.4"
- dj-database-url = "^1.0.0"


