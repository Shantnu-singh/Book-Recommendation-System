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