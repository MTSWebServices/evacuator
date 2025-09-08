.. title

Evacuator
=========

|Repo Status| |PyPI Latest Release| |PyPI License| |PyPI Python Version| |PyPI Downloads|
|Documentation| |CI Status| |Test Coverage| |pre-commit.ci Status|

.. |Repo Status| image:: https://www.repostatus.org/badges/latest/active.svg
    :alt: Repo status - Active
    :target: https://github.com/MobileTeleSystems/evacuator
.. |PyPI Latest Release| image:: https://img.shields.io/pypi/v/evacuator
    :alt: PyPI - Latest Release
    :target: https://pypi.org/project/evacuator/
.. |PyPI License| image:: https://img.shields.io/pypi/l/evacuator.svg
    :alt: PyPI - License
    :target: https://github.com/MobileTeleSystems/evacuator/blob/develop/LICENSE.txt
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/evacuator.svg
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/evacuator/
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/evacuator
    :alt: PyPI - Downloads
    :target: https://pypi.org/project/evacuator/
.. |Documentation| image:: https://readthedocs.org/projects/evacuator/badge/?version=stable
    :alt: Documentation - ReadTheDocs
    :target: https://evacuator.readthedocs.io/
.. |CI Status| image:: https://github.com/MobileTeleSystems/evacuator/workflows/Tests/badge.svg
    :alt: Github Actions - latest CI build status
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |Test Coverage| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/
    MTSOnGithub/03e73a82ecc4709934540ce8201cc3b4/raw/evacuator_badge.json
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/MobileTeleSystems/evacuator/develop.svg
    :alt: pre-commit.ci - status
    :target: https://results.pre-commit.ci/latest/github/MobileTeleSystems/evacuator/develop

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code.

Designed to be used in `Apache Airflow <https://airflow.apache.org/>`__ with:
    * `BashOperator <https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#skipping>`_ (`airflow>2.1`)
    * `PythonVirtualenvOperator <https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.PythonVirtualenvOperator>`_ (`airflow>=2.6`)
    * `ExternalPythonOperator <https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.ExternalPythonOperator>`_ (`airflow>=2.6`)
    * `DockerOperator <https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#airflow.providers.docker.operators.docker.DockerOperator>`_ (`apache-airflow-providers-docker>=3.5`)
    * `KubernetesPodOperator <https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/_api/airflow/providers/cncf/kubernetes/operators/pod/index.html#airflow.providers.cncf.kubernetes.operators.pod.KubernetesPodOperator>`_ (`apache-airflow-providers-cncf-kubernetes>=6.1`)
    * `SSHOperator <https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/operators/ssh/index.html#airflow.providers.ssh.operators.ssh.SSHOperator>`_ (`apache-airflow-providers-ssh>=3.10`)
    * any other operator support skipping task when process is exited with some specific exit code (``skip_on_exit_code`` option)

.. installation

How to install
---------------

.. code:: bash

    pip install evacuator

.. documentation

Documentation
-------------

See https://evacuator.readthedocs.io/
