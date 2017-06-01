# Setup Instructions for Custom Geonode

* Make sure that docker and other tools have been installed on the host machine.

* Clone the univengis repository by running `git clone git@github.com:kartoza/univengis.git`

* Run `cd univengis/deployment`

* Clone the geonode repository by running `git clone git@github.com:GeoNode/geonode.git docker-geonode`

* Edit all the files in deployment and replace the variable `SERVER_IP` with the ip address of your server

* Copy the files located in deployment to their respective locations

* Run `cp docker-compose.yml docker-geonode`

* Run `cp geoserver.env django.env docker-geonode/scripts/docker/env/production`

* Run `cp settings.py docker-geonode/geonode/`

* Navigate to the folder docker-geonode by running `cd docker-geonode`.

* Clone the repository for doing pg_backups `git clone git@github.com:NyakudyaA/docker-pg-backup.git`

* We will use the docker-compose.yml to build geonode.

* Create folders for storing the backups and storing the postgres data. Run `mkdir backups && mkdir -p pg/postgres_data`

* Open `sudo nano /etc/hosts`  to update your host file and add the entry: `127.0.0.1       localhost geonode 255.255.255.255 broadcasthost ::1 localhost`

* Run `docker-compose up -d` and see other instructions for running [geonode](https://github.com/GeoNode/geonode)

* Wait for a couple of minutes and then run `make sync` which creates the necessary tables for geonode to start

* If `make sync` gives errors it is because the Postgres container hasn't connected properly to the django container
  through the subnet ip address and you need to run `docker restart geonode-db`

* This will start the docker containers and your services should be available `http://localhost:8500`

## Set up backup for postgres database and geoserver data

* Pull the bysync image from docker hub by running `docker pull kartoza/btsync`

* We will use the docker image to create a backup of the files located in pg/postgres_data and the geoserver_data
  directory.

* Follow the instructions at [docker-bt-sync kartoza](https://github.com/kartoza/docker-btsync)


## Installing QGIS and QGIS SERVER

* Run `docker pull kartoza/qgis-desktop:2.14.6` to get the image for QGIS Desktop LTR

* Run the qgis container by following the instructions at [QGIS Desktop] (https://github.com/kartoza/docker-qgis-desktop)

NB: Since geonode also uses docker-postgis we can link this container to  running geonode postgis container.

* To link to an already running container we use the external links.

* Edit the file [run qgis](https://github.com/kartoza/docker-qgis-desktop/blob/develop/2.14/run-qgis-2.14ltr-in-docker.sh)
  and include:
    ```
    - links name_of_db:name_of_db
    ```
  This ensures that we use the same postgis container in QGIS and geonode

### QGIS SERVER

* We are going to be using LTR version for the server

* Run `docker pull kartoza/qgis-server:LTR`

* Follow the instructions at [docker qgis server](https://github.com/kartoza/docker-qgis-server) on how to run the
  image you have just downloaded.


