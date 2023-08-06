========
DS_Get
========

ds_get - Thin client for interfacing with Synology DownloadStation.
Primarily used to add magnet and torrent files.

Associate magnet: and .torrent uris with this script in your browser and directly start them in your Synology DS

* Free software: MIT license


Features
--------

- Send magnet links and torrent files to Synology DS Get via command line
- Check download tasks


Installation
------------

pip install -e git+https://github.com/dekomote/ds_get.git#egg=ds_get

Soon on the PyPi

Usage
-----

usage: ds_get [-h] [--ip_address [IP_ADDRESS]] [--port [PORT]] [--username [USERNAME]] [--password [PASSWORD]] [--secure [SECURE]]
              [--cert_verify [CERT_VERIFY]] [--dsm_version [DSM_VERSION]] [--debug [DEBUG]]
              links [links ...]

Some of the arguments can also be set in env: DSGET_IP_ADDRESS DSGET_PORT DSGET_USERNAME DSGET_PASSWORD DSGET_SECURE DSGET_CERT_VERIFY DSGET_DSM_VERSION DSGET_DEBUG


Bugs / TODO
-----------

Use the issue tracker
