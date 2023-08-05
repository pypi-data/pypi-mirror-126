muninn-generic-products
=======================

This python module provides a simple generic product type extension for muninn.

You need to install this module inside the same python environment in which
you have installed muninn.

You then need to add ``muninn_generic_products`` to the list of
``product_type_extensions`` in your muninn archive configuration file to
enable the extension.

You will then need to set the ``MUNINN_GENERIC_PRODUCT_CONFIG`` environment
variable and have it point to an ascii file containing on each line the name of
a product type, a space, and the python regular expression for the filename.
This regular expression needs to be unique enough to only match products of
the specific product type and it can have group name matches to allow
extraction of the validity start/stop and generation date properties.

For instance (using GOME-2 L1b products as example)::

    GOME2_L1B GOME_xxx_1B_..._(?P<validity_start>[\d]{14})Z_(?P<validity_stop>[\d]{14})Z_._._(?P<creation_date>[\d]{14})Z

Instead of a ``validity_start``/``validity_stop`` you can also provide one of
the following regular expression group names:

- ``validity_day`` (format = "YYYYMMDD")
- ``validity_month`` (format = "YYYYMM")
- ``validity_year`` (format = "YYYY")
 
Each of these will automatically set ``validity_stop`` to the end of the time
period.


Note that with this module you will only be able to populate a specific set of
the muninn core properties (and only based on the content of the filename).
For more functionality, you will either have to download a dedicated product
type extension or construct one of your own.
