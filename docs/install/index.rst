.. _avanti.install:

======================
Installing Lino Avanti
======================

- Install Lino (the framework) as documented in
  :ref:`lino.dev.install`

- Go to your :xfile:`repositories` directory and download also a copy
  of the *Lino Avanti* repository::

    cd ~/repositories
    git clone https://github.com/lino-framework/avanti
    
- Use pip to install this as editable package::

    pip install -e avanti

- Create a local Lino project as explained in
  :ref:`lino.tutorial.hello`.

- Change your project's :xfile:`settings.py` file so that it looks as
  follows:

  .. literalinclude:: settings.py

