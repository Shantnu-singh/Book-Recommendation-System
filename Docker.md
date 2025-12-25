# Write Docker file
- add layers
- Instruction / steps
- read top to bottom

# Docker Image
- Base layer is the first line ( can be imported using FROM )

# Then do docker built
use docker build -t app_name . --> this step will give us a docker image

# Run Images 
docker run image_name

# Port mapping
docker run -p5000:5000 image_name

# detach mode
docker run -d # so that we don't engage the terminal 

# docker stop
docker stop container_name

# docker run container with name
docker run --name sample_name -d image_name

docker ps -a #to see all docker contrainers

docker rm container_name
docker rmi image_name

docker tag old_image_name new_image_name


# session 2 :
 - Setting up env varibale in docker 

# Normally env varibels are use to store secrerets (API key, Auth Keys)
--env PORT=8000 in docker run

# Go inside a running continer
docker exec -it container_name bash

# Make default env
- in DockerFile ENV PORT = 5000 ## can be overwrite in docker run 

# take env from file
--env-file .env in docker run command


# Session 3 :
caching and mutli stage builds

- layer concept :
dockerfile is step of instu : each statement is a seperate layers
- docker file read from top to bottom 
- each layer have a unique SHA Value
- layer get stack one on top to other
- FROM is BaseLayer
- each layer cache from, and if SHA is aviliable is doesn't get built it get rebuild from cached.
- cached invalidate : if a layer is cached ivaliadate all the layer below that need to be rebuild, caching won't be there. (downstream layer will be rebuild)

### mutlistage build
- to reduce size of docker image
- in single dockerfile, define muitiple stage
- a single stage starts from 'FROM' statements
- stage 1 : Builder stage: install packages and compile
- stage 2 : copy these compile stage ino final file
- and then discard Builder stage. Hence final stage is of smaller size.
- can use mutiple stages, final stage is final dockerfile 