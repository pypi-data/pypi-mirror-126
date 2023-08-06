.. sknrf documentation introduction file

..  figure:: ../_images/PNG/sknrf_logo.png
    :width: 500 pt
    :align: center

Linux
=====

Build from Scratch
------------------

Install Ubuntu 18.04 and manually install the following:

.. literalinclude:: ../../../machine_configs/py3_7-glibc2_27-x86_64/ubuntu18_04/install_root.sh
    :language: bash
    :lines: 1-57
    :emphasize-lines: 57
    :linenos:

Automatically install the remaining libraries:

.. code-block:: bash

    sudo bash install_root.sh

Verify the installation:

.. code-block:: bash

    less -R install.log

Source the default python virtual environment:

.. code-block:: bash

    cd ${HOME}/repos/sknrf-core
    eval $ENV

This will configure the environment variables as follows:

.. literalinclude:: ../../../machine_configs/py3_7-glibc2_27-x86_64/ubuntu18_04/env.sh
    :language: bash
    :linenos:

.. tip::
    Run  mv ~/anaconda3/bin/qtpaths ~/anaconda3/bin/qtpaths-qt5 to avoid qt conflict with KDE user login process

Run the unit tests:

.. code-block:: bash

    nosetests --config=nose.cfg --with-coverage


Build from Source
-----------------

Download the source code:

.. code-block:: bash

    eval $ENV
    git clone https://gitlab.com/scikit-nonlinear/sknrf-core.git
    cd ${HOME}/repos/sknrf-core
    git submodule sync
    git submodule update --init --recursive --remote


Build an install both the Python front-end and C++ back-end:

.. code-block:: bash

    python setup.py clean                         # make clean
    python setup.py config                        # configure
    python setup.py build                         # make
    python setup.py install                       # make install DESTDIR="${CONDA_PREFIX}"
    python setup.py develop                       # make install DESTDIR="${CONDA_PREFIX}" as symlink


Optionally, build (or rebuild) just the C++ back-end:

.. code-block:: bash

    rm -rf build ; mkdir build ; cd build         # make clean
    cmake -G"Ninja" ..                            # configure
    cmake --build .                               # make
    cmake --install . --prefix "${CONDA_PREFIX}"  # make install DESTDIR="${CONDA_PREFIX}"


Run the unit tests:

.. code-block:: bash

    nosetests --config=nose.cfg --with-coverage