#! /bin/sh

cd $PWD/docker	
docker build -t farmersmarket:fmarket .
docker run -it farmersmarket:fmarket
docker exec -it farmersmarket:fmarket python ./main.py

