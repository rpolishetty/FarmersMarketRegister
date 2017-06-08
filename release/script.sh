#! /bin/sh

cd $PWD/docker	
docker build -t farmersmarket:fmarket .
docker run --name register -it farmersmarket:fmarket


