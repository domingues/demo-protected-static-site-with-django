# [Demo] Protected Static Site with Django

Protect a static site with user/password authentication.

## Install and run

### Development

#### Install
```bash
git clone https://github.com/domingues/demo-protected-static-site-with-django.git demo-protected-static-site-with-django
```
```bash
cd demo-protected-static-site-with-django
```
```bash
pip install -e .
```

#### Config
```bash
cat > .env << DOTENV
SECRET_KEY=
DEBUG=true
INTERNAL_IPS=127.0.0.1
DOTENV
```

#### Prepare
```bash
./manage.py compilemessages
```
```bash
./manage.py migrate
```

#### Run
```bash
./manage.py runserver
```

### Production

#### Install
Replace `$VERSION` with the desired version number, e.g. `1.0.0`.
```bash
pip install demo-protected-static-site-with-django@git+https://github.com/domingues/demo-protected-static-site-with-django.git@$VERSION
```

#### Config
Read the official [deployment checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/).
```bash
export DJANGO_SETTINGS_MODULE=domingues.protected_static_site.settings
```
```bash
cat > .env << DOTENV
SECRET_KEY=
ALLOWED_HOSTS=
DOTENV
```

#### Prepare
```bash
django-admin collectstatic
```
```bash
django-admin compilemessages
```
```bash
django-admin migrate
```

#### Run
```bash
gunicorn domingues.protected_static_site.wsgi
```
And serve static files of `$PWD/static/` and `$PWD/media/` on HTTP `/static/` and `/media/`.

# Environment variables

| Name      | Default value                    | Description                                                                                                                                 |
| --------- |----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| PROJECT_BASE_DIR | `""` (current working directory) | Folder containing the project runtime files: `.env`, databases, media and collected statics.                                                |
| LOAD_DOTENV | `True`                           | Try to load environment variables from `$PROJECT_BASE_DIR/.env` file.                                                                       |
| SECRET_KEY |                                  | Django [`SECRET_KEY`](https://docs.djangoproject.com/en/4.2/ref/settings/#std:setting-SECRET_KEY) setting.                                  |
| DEBUG     | `False`                          | Django [`DEBUG`](https://docs.djangoproject.com/en/4.2/ref/settings/#debug) setting.                                                        |
| ALLOWED_HOSTS | `[]`                             | Django [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts) setting.                                        |
| INTERNAL_IPS | `[]`                             | Django [`INTERNAL_IPS`](https://docs.djangoproject.com/en/4.2/ref/settings/#internal-ips) setting. Also used to activate the debug toolbar. |
| SITE_DIR  | `$PROJECT_BASE_DIR/site_files`   | Folder containing the static site files. |
| SHOW_INDEXES | `False`                        | Show site directory indexes. |
