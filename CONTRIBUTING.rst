Contributing
============

1. Fork it.

2. Clone it

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/ab-anand/Filezen.git
    (develop)$ cd Filezen
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Filezen' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/ab-anand/Filezen.git
    (develop)$ cd Filezen
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

5. Run tests

.. code:: bash

    (develop) $ python -m unittest discover tests

Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature

6. Push to the branch (``$ git push origin my-new-awesome-feature``)

7. Create new Pull Request

Hack away!

To do
~~~~~

.. [*] A Desktop app using libraries like `Tkinter <https://docs.python.org/3/library/tkinter.html/>`__ which utilizes ``Filezen`` to organize files.
.. [*] Some more unittests
.. [*] Confirmation to move rename file if a file with a same name is already present

Tests
~~~~~

``Filezen`` uses ``unittesting`` for testing purposes.

Running the test cases

.. code:: bash

    $ python -m unittest discover tests

    .........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.008s

    OK


