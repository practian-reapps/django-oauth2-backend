
=====
oauth2_backend
=====



oauth2_backend is a oAuth2 with a Django backend. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "oauth2_backend" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...

        'oauth2_backend',
    ]


2. Settings AUTH_USER_MODEL the default user model by the following value model::

	AUTH_USER_MODEL = 'oauth2_backend.User'


3. Finally, run `python manage.py migrate` to create the oauth2_backend models.







NO CONTINUAR CON LA 
PARTE 2. Continúe configurando si desea extender la funcionalidad de oauth2_backend
-----------

    INSTALLED_APPS = [
        ...
        'django.contrib.admindocs',
        'rest_framework',
        'corsheaders',
        'oauth2_provider',
        ...

        'oauth2_backend',
    ]

4. Complete en MIDDLEWARE_CLASSES los Middleware class::

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',  # adding
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'django.contrib.admindocs.middleware.XViewMiddleware', # adding
        'oauth2_provider.middleware.OAuth2TokenMiddleware', # adding
    ]


5. Settings the DIRS key of TEMPLATES::

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]


6. Change CORS_ORIGIN_ALLOW_ALL for True::

    CORS_ORIGIN_ALLOW_ALL = True


7. Settings DEFAULT_AUTHENTICATION_CLASSES key of REST_FRAMEWORK ::

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        )
    }


8. Include the oauth2_backend URLconf in your project urls.py like this::

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ...

    url(r'^api/oauth2_backend/', include('oauth2_backend.urls')),


9. Start the development server and visit http://127.0.0.1:9000/admin/
   to create a auths (you'll need the Admin app enabled)::

   `python manage.py runserver 9000`


10. Visit http://127.0.0.1:9000/api/oauth2_backend/ to participate in the oauth2_backend.


Generate command
-----------
    
    python setup.py sdist
    pip install dist\django-oauth2-backend-0.1.tar.gz
    pip uninstall django-oauth2-backend
