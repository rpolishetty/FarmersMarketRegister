#! /bin/sh

cd $PWD/docker	
docker build -t farmersmarket:fmarket .
docker run -it farmersmarket:fmarket bootstrap.sh -automate

