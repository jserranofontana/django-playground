# django-htmx  
Samples about htmx-alpine use in Django  

**Tutorials**
- Responsive HTMX Table (with sorting, filtering and pagination)
`https://enzircle.com/responsive-table-with-django-and-htmx#cl57uqo780ho4ownv740lc6wb`
- Also with infinite scroll (see first comment)
`https://htmx.org/examples/infinite-scroll/`

**Preparing remote repository**  
`echo "# django-playground" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/jserranofontana/django-playground.git  
git push -u origin main`  

**Store GitHub PAT on Manjaro Keyring**  
<https://noabody.wordpress.com/2020/12/22/git-manjaro-linux-personal-access-token-keyring/>  
`git config --global credential.helper /usr/lib/git-core/git-credential-libsecret  
cd myrepo  
git push`  

**Boilerplate based on info**  
<https://geoff.tuxpup.com/posts/django_tailwind_htmx_how_i_start/>  

*Write initial .env file*  
`echo DEBUG=True >>.env  
echo DJANGO_SECRET_KEY=$(poetry run python -c "import secrets; print(secrets.token_urlsafe())") >>.env  
DATABASE_URL=<your Postgres URL>`  

*Boilerplate.*  
- poetry virtualenv
- Python-3.10
- GitHub
- Project level templates

*PreCommit* 
- black = "^22.10.0"
- djhtml = "^1.5.2"
- pre-commit = "^2.20.0"

*Dependencies*
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

**Comandos**
- Para crear un fichero con los datos iniciales (los que haya en ese momento en la BB.DD) de un modelo
`python manage.py dumpdata demo.todo --indent 4 > fixtures/todo.json`
- Para crear un fichero con los datos iniciales de 'todos' los modelos
`python manage.py dumpdata DomcaProAccess --indent 4 > fixtures/DomcaProAccess.json`

- Para cargar los datos iniciales a partir de un fichero
`python manage.py loaddata fixtures/todo.json --app demo.todo`
- Para cargar los datos iniciales de 'toda' la aplicación a partir de un fichero
`python manage.py loaddata fixtures/DomcaProAccess --app DomcaProAccess`

