2. Edit the ``/etc/os_resource_classes/os_resource_classes.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://os_resource_classes:OS_RESOURCE_CLASSES_DBPASS@controller/os_resource_classes
