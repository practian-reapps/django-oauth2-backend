########################################
Django oauth2_backend
########################################

.. class:: no-web

    Django oauth2 backend es una manera fácil de extender la clase ``AbstractUser`` de `Django`_ y define un modelo de *autenticación/autorización* para **aplicaciones SaaS** para los proyectos de `Django`_.


    .. image:: https://github.com/submitconsulting/backengo/blob/master/media/test_images/img1.png
        :alt: HTTPie compared to cURL
        :width: 100%
        :align: center





.. contents::

.. section-numbering::

.. raw:: pdf

   PageBreak oneColumn


============
Installation
============


-------------------
Development version
-------------------

The **latest development version** can be installed directly from github_:

.. code-block:: bash
    
    # Universal
    $ pip install --upgrade https://github.com/practian-reusable-applications/django-oauth2-backend/raw/master/dist/django-oauth2-backend-0.1.zip

or clone from github_ githubdos_ github xamgithub_:

.. code-block:: bash

    $ git clone https://github.com/practian-reusable-applications/django-oauth2-backend.git

(If ``pip`` installation fails for some reason, you can try
``easy_install `` as a fallback.)


--------------
Python version
--------------

Python 3.4.4 is recommended to install Django oauth2 backend


=====
Usage
=====


Hello World:


.. code-block:: bash

    $ http httpie.org


Synopsis:

.. code-block:: bash

    $ http [flags] [METHOD] URL [ITEM [ITEM]]


See also ``http --help``.


--------
Examples
--------

Custom `HTTP method`_, `HTTP headers`_ and `JSON`_ data:

.. code-block:: bash

    $ http PUT example.org X-API-Token:123 name=John


Submitting `forms`_:

.. code-block:: bash

    $ http -f POST example.org hello=World


See the request that is being sent using one of the `output options`_:

.. code-block:: bash

    $ http -v example.org


Use `Github API`_ to post a comment on an
`issue <https://github.com/jkbrzt/httpie/issues/83>`_
with `authentication`_:

.. code-block:: bash

    $ http -a USERNAME POST https://api.github.com/repos/jkbrzt/httpie/issues/83/comments body='HTTPie is awesome! :heart:'


Upload a file using `redirected input`_:

.. code-block:: bash

    $ http example.org < file.json


Download a file and save it via `redirected output`_:

.. code-block:: bash

    $ http example.org/file > file


Download a file ``wget`` style:

.. code-block:: bash

    $ http --download example.org/file

Use named `sessions`_ to make certain aspects or the communication persistent
between requests to the same host:

.. code-block:: bash

    $ http --session=logged-in -a username:password httpbin.org/get API-Key:123

    $ http --session=logged-in httpbin.org/headers


Set a custom ``Host`` header to work around missing DNS records:

.. code-block:: bash

    $ http localhost:8000 Host:example.com

..

--------

*What follows is a detailed documentation. It covers the command syntax,
advanced usage, and also features additional examples.*


===========
Quick start
===========

1. Add "oauth2_backend" to your INSTALLED_APPS setting like this:

.. code-block:: bash

    INSTALLED_APPS = [
        ...

        'oauth2_backend',
    ]


2. Settings AUTH_USER_MODEL the default user model by the following value model::

    AUTH_USER_MODEL = 'oauth2_backend.User'


3. Finally, run ``python manage.py migrate`` to create the oauth2_backend models.

====
Meta
====

----------
Change log
----------

See `CHANGELOG <https://github.com/practian-reusable-applications/django-oauth2-backend/blob/master/CHANGELOG.rst>`_.


-------
Licence
-------

BSD-3-Clause: `LICENSE <https://github.com/practian-reusable-applications/django-oauth2-backend/blob/master/LICENSE>`_.



-------
Authors
-------

- Angel Sullon Macalupu (asullom@gmail.com)

.. _Django OAuth Toolkit: https://django-oauth-toolkit.readthedocs.io
.. _Django: https://www.djangoproject.com
.. _github: https://github.com/practian-reusable-applications/django-oauth2-backend


-------
Contributors
-------

See https://github.com/practian-reusable-applications/django-oauth2-backend/graphs/contributors





