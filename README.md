# Setup Instruction for Custom Geonode

* Make sure that docker has been installed on the host machine. If not install docker and
docker-compose following instructions at [docker-compose-install](https://docs.docker.com/compose/install/)
and [docker-install](https://docs.docker.com/engine/installation/)

* Clone the univengis repository by running:

  `git clone git@github.com:kartoza/univengis.git`

* Run `cd unievengis/deployment`

* Clone the geonode repository by running:

  `git clone git@github.com:GeoNode/geonode.git docker-geonode`
* Navigate to the cloned folder `cd docker-geonode`

* Edit the file `docker-compose.yml` by replacing:

  ```
  postgres:
    image: postgres
  ```
  with
  ```
  postgres:
    image: kartoza/postgis:9.5-2.2
    volumes:
      - ./pg/postgres_data:/var/lib/postgresql
    environment:
      - USERNAME=docker
      - PASS=docker
      - ALLOW_IP_RANGE=0.0.0.0/0
  ```

* Edit the file `docker-geonode/scripts/docker/env/production/django.env` by replacing:

  ```
  data_dir_conf:
    image: geonode/geoserver_data:2.9.x-oauth2
    container_name: geoserver_data_dir
    command: /bin/true
    volumes:
      - /geoserver_data/data
  ```
  
  with 
  
  ```
   data_dir_conf:
    image: geonode/geoserver_data:2.9.x-oauth2
    container_name: geoserver_data_dir
    command: /bin/true
    volumes:
      - /geoserver_data/data
      - /gis:/gis_data

  ```

  ```
  DATABASE_URL=postgres://postgres:postgres@postgres:5432/postgres
  BROKER_URL=amqp://guest:guest@rabbitmq:5672/
  DJANGO_SETTINGS_MODULE=geonode.settings
  ALLOWED_HOSTS=['django',]
  C_FORCE_ROOT=1
  GEOSERVER_PUBLIC_LOCATION=http://geonode/geoserver/
  GEOSERVER_LOCATION=http://geonode/geoserver/
  SITEURL=http://geonode/
  ```
  
  With
  
  ```
  DATABASE_URL=postgres://docker:docker@postgres:5432/gis
  BROKER_URL=amqp://guest:guest@rabbitmq:5672/
  DJANGO_SETTINGS_MODULE=geonode.settings
  ALLOWED_HOSTS=['django','SERVER_IP',]
  C_FORCE_ROOT=1
  GEOSERVER_PUBLIC_LOCATION=http://SERVER_IP/geoserver/
  GEOSERVER_LOCATION=http://geonode/geoserver/
  SITEURL=http://SERVER_IP/

  ```
  
* Edit the file `docker-geonode/scripts/docker/env/production/geoserver.env` by replacing:

  ```
  DOCKER_HOST
  PUBLIC_PORT=80
  DOCKER_HOST_IP
  DJANGO_URL=http://django:8000/
  GEOSERVER_PUBLIC_LOCATION=http://geonode/geoserver/
  GEOSERVER_LOCATION=http://geoserver:8080/geoserver/
  SITEURL=http://geonode/
  ```
  With
  
  ```
  DOCKER_HOST
  PUBLIC_PORT=80
  DOCKER_HOST_IP
  DJANGO_URL=http://django:8000/
  GEOSERVER_PUBLIC_LOCATION=http://SERVER_IP/geoserver/
  GEOSERVER_LOCATION=http://geoserver:8080/geoserver/
  SITEURL=http://SERVER_IP/

  ```
 where SERVER_IP is the ip address of your server or can be the domain registration
 

* Clone the repository for doing pg_backups
 
  `git clone git@github.com:NyakudyaA/docker-pg-backup.git`

* We will use the docker-compose.yml to build geonode.

* Create folders for storing the backups and storing the postgres data. 
  Run `mkdir backups && mkdir -p pg/postgres_data`

* Run `docker-compose up -d --build` and see other instructions for running [geonode](https://github.com/GeoNode/geonode)

* The postgres database takes a couple of minutes before it starts up.

* Run `make sync` for creating the django tables.

* If `make sync` gives errors it is because the Postgres container hasn't connected properly
  to the django container through the subnet ip address and you need to run 
  `docker restart geonode-db`

* This will start the docker containers and your services should be available 
  `http://localhost`

## Set up backup for postgres database 

* Pull the bysync image from docker hub by running `docker pull kartoza/btsync`

* We will use the docker image to create a backup of the files located in pg/postgres_data and the geoserver_data
  directory.

* Follow the instructions at [docker-bt-sync kartoza](https://github.com/kartoza/docker-btsync)

## Backup geoserver data directory

* The geoserver data directory is a docker data container. It contains all the 
configurations for setting up geoserver. It needs to be backed up once when all users 
have been created.

* `/gis/` is mounted into the geoserver data container and exposes all the available layers
to geoserver.

## Installing QGIS and QGIS SERVER

* Run `docker pull kartoza/qgis-desktop:2.14.6` to get the image for QGIS Desktop LTR

* Run the qgis container by following the instructions at [QGIS Desktop] (https://github.com/kartoza/docker-qgis-desktop)

NB: Since geonode also uses docker-postgis we can link this container to  running geonode postgis container.

* To link to an already running container we use the external links.

* Edit the file [run qgis](https://github.com/kartoza/docker-qgis-desktop/blob/develop/2.14/run-qgis-2.14ltr-in-docker.sh)
  and include:
  
    ```
    --links name_of_db:name_of_db
           
    ```
  This ensures that we use the same postgis container in QGIS and geonode

### QGIS SERVER

* We are going to be using LTR version for the server

* Run `docker pull kartoza/qgis-server:LTR`

* Follow the instructions at [docker qgis server](https://github.com/kartoza/docker-qgis-server) on how to run the
  image you have just downloaded.


