----------------------------------------------------------------------------
SUPER SECCY INVENTORY MANAGEMENT SYSTEM
----------------------------------------------------------------------------

summary: this code connects to a mongodb server and can be used to manage
  the items in a certain inventory.

----------------------------------------------------------------------------
INSTALLATION
----------------------------------------------------------------------------

* install mongodb on a remote server. This program is intended to be run
  against a raspberry pi. there's a guide here:
    https://pimylifeup.com/mongodb-raspberry-pi/
* run "pip install requirements.txt" on the client computer
* configure the config.json to reflect the configuration of your system. you
  shouldn't have to change anything much other than:
    dburl: the url of your mongodb server. set to the hostname of your pi.
    You can find the hostname of your pi using the "hostname" command in the
    terminal.

----------------------------------------------------------------------------
USAGE
----------------------------------------------------------------------------

TBD
