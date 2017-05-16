# Setup Instruction for Custom Geonode

* Make sure that docker and other tools have been installed on the host machine.

* Clone the univenda repository by running `git clone git@github.com:kartoza/univengis.git`

* Run `cd unievengis/deployment`

* Clone the geonode repository by running `git clone git@github.com:GeoNode/geonode.git docker-geonode`

* Copy the files located in deployment to their respective location

* Run `cp docker-compose.yml docker-geonode`

* Run `cp geoserver.env django.env docker-geonode/scripts/docker/env/production`

* Run `cp settings.py docker-geonode/geonode/`

* Navigate to the folder docker-geonode by running `cd docker-geonode`.

* Clone the repository for doing pg_backups `git clone git@github.com:NyakudyaA/docker-pg-backup.git`

* We will use the docker-compose.yml to build geonode.

* Create folders for storing the backups and storing the postgres data. Run `mkdir backups && mkdir -p pg/postgres_data`

* Run `docker-compose up -d`

* Wait for a couple of minutes and then run `make sync` which creates the necessary tables for geonode to start

* If `make sync` gives errors it is because the Postgres container hasn't connected properly to the django container
  through the subnet ip address and you need to run `docker restart geonode-db`

* This will start the docker containers and your services should be available `http://localhost:8500`

