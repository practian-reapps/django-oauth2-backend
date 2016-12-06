########################################
oauth2_backend
########################################

.. class:: no-web

    oauth2_backend es una manera fácil de extender la clase ``AbstractUser`` de `Django`_ y define un modelo de *autenticación/autorización* para **aplicaciones de microservicios** para los proyectos con `Django`_.



    .. image:: https://github.com/practian-reapps/django-oauth2-backend/blob/master/docs/media/a2-arquitectura_de_micoservicios.png
        :alt: oauth2_backend
        :width: 100%
        :align: center

    .. image:: https://github.com/practian-reapps/django-oauth2-backend/blob/master/docs/media/a1-ejemplo_de_arquitectura_de_micoservicios.png
        :alt: oauth2_backend compared to cURL
        :width: 100%
        :align: center



.. contents::

.. section-numbering::

.. raw:: pdf

   PageBreak oneColumn


============
Installation
============

--------------
Requirements
--------------

* Python 3.4, 3.5
* Django 1.9, 1.10



-------------------
Development version
-------------------


The **latest development version** can be installed directly from github_:

.. code-block:: bash
    
    # De preferencia, trabaje dentro de un virtualenv
    # Universal
    $ pip install --upgrade https://github.com/practian-reapps/django-oauth2-backend/raw/master/dist/django-oauth2-backend-0.1.zip

or clone from github_:

.. code-block:: bash

    $ git clone https://github.com/practian-reapps/django-oauth2-backend.git

(If ``pip`` installation fails for some reason, you can try ``easy_install`` as a fallback.)



Add "oauth2_backend" to your INSTALLED_APPS setting like this:

.. code-block:: bash

    INSTALLED_APPS = [
        ...

        'oauth2_backend',
    ]


Settings AUTH_USER_MODEL the default user model by the following value model::

    AUTH_USER_MODEL = 'oauth2_backend.User'


Finally, run ``python manage.py migrate`` to create the oauth2_backend models.




====
Meta
====

----------
Change log
----------

See `CHANGELOG <https://github.com/practian-reapps/django-oauth2-backend/blob/master/CHANGELOG.rst>`_.


-------
Licence
-------

BSD-3-Clause: `LICENSE <https://github.com/practian-reapps/django-oauth2-backend/blob/master/LICENSE>`_.



-------
Authors
-------

- Angel Sullon Macalupu (asullom@gmail.com)



-------
Contributors
-------

See https://github.com/practian-reapps/django-oauth2-backend/graphs/contributors

.. _github: https://github.com/practian-reapps/django-oauth2-backend
.. _Django: https://www.djangoproject.com
.. _Django REST Framework: http://www.django-rest-framework.org
.. _Django OAuth Toolkit: https://django-oauth-toolkit.readthedocs.io
.. _oauth2_backend: https://github.com/practian-reapps/django-oauth2-backend
.. _Authorization server: https://github.com/practian-ioteca-project/oauth2_backend_service







