Prerequisites
-------------

Before you install and configure the Resource Classes for OpenStack service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``os_resource_classes`` database:

     .. code-block:: none

        CREATE DATABASE os_resource_classes;

   * Grant proper access to the ``os_resource_classes`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON os_resource_classes.* TO 'os_resource_classes'@'localhost' \
          IDENTIFIED BY 'OS_RESOURCE_CLASSES_DBPASS';
        GRANT ALL PRIVILEGES ON os_resource_classes.* TO 'os_resource_classes'@'%' \
          IDENTIFIED BY 'OS_RESOURCE_CLASSES_DBPASS';

     Replace ``OS_RESOURCE_CLASSES_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``os_resource_classes`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt os_resource_classes

   * Add the ``admin`` role to the ``os_resource_classes`` user:

     .. code-block:: console

        $ openstack role add --project service --user os_resource_classes admin

   * Create the os_resource_classes service entities:

     .. code-block:: console

        $ openstack service create --name os_resource_classes --description "Resource Classes for OpenStack" resource classes for openstack

#. Create the Resource Classes for OpenStack service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        resource classes for openstack public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        resource classes for openstack internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        resource classes for openstack admin http://controller:XXXX/vY/%\(tenant_id\)s
