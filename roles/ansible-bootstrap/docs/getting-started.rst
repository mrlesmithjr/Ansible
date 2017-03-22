Getting Started
===============

.. contents::
   :local:

Variable examples
-----------------
There are only a few variables which are defined to get started with this role.

.. literalinclude:: ../defaults/main.yml
   :language: yaml

Variables explained:
~~~~~~~~~~~~~~~~~~~~

* The ``bootstrap_debian_set_root_pw`` defines if the ``root`` password should be set on Debian based systems.
* The ``bootstrap_install_fail2ban`` defines if ``fail2ban`` should be installed.
* The ``bootstrap_root_password`` defines the ``root`` password to be set.
* The ``bootstrap_set_root_pw`` defines if non Debian/Ubuntu root passwords should be set.

Playbook example
----------------
.. literalinclude:: playbooks/bootstrap.yml
   :language: yaml

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
