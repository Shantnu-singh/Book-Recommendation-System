# 🐳 Docker Fundamentals – Structured Notes

## 1️⃣ What is a Dockerfile?

A **Dockerfile** is a text file that contains a series of **instructions** used to build a Docker image.

* Dockerfiles are read **from top to bottom**
* Each instruction creates a **new layer**
* Layers are stacked on top of each other

---

## 2️⃣ Docker Image & Layers

### 🔹 Docker Image

* A Docker image is a **blueprint** used to create containers
* Images are **immutable**
* Built using a Dockerfile

### 🔹 Layers Concept

* Each Dockerfile instruction = **one layer**
* Every layer has a **unique SHA hash**
* Layers are cached to speed up builds
* Layers are stacked sequentially

### 🔹 Base Layer

* The **first instruction** must always be:

```dockerfile
FROM
```

* This defines the **base image**
* All other layers are built on top of it

---

## 3️⃣ Building a Docker Image

Use the following command to build an image:

```bash
docker build -t app_name .
```

### Explanation:

* `-t app_name` → name/tag for the image
* `.` → build context (current directory)

✅ This command creates a **Docker image**

---

## 4️⃣ Running Docker Containers

### 🔹 Run a Container

```bash
docker run image_name
```

### 🔹 Port Mapping

```bash
docker run -p 5000:5000 image_name
```

* Left side → Host port
* Right side → Container port

---

## 5️⃣ Detached Mode

Run container in background (non-interactive):

```bash
docker run -d image_name
```

---

## 6️⃣ Container Management

### 🔹 Stop a Container

```bash
docker stop container_name
```

### 🔹 Run Container with a Name

```bash
docker run --name sample_name -d image_name
```

### 🔹 List Containers

```bash
docker ps -a
```

### 🔹 Remove Container

```bash
docker rm container_name
```

### 🔹 Remove Image

```bash
docker rmi image_name
```

### 🔹 Rename / Retag Image

```bash
docker tag old_image_name new_image_name
```

---

## 7️⃣ Session 2: Environment Variables

### 🔹 Why Environment Variables?

* Used to store **secrets** and **configurations**
* Examples:

  * API keys
  * Auth tokens
  * Port numbers

---

### 🔹 Pass Environment Variable at Runtime

```bash
docker run --env PORT=8000 image_name
```

---

### 🔹 Set Default Environment Variable in Dockerfile

```dockerfile
ENV PORT=5000
```

⚠️ This value **can be overridden** during `docker run`

---

### 🔹 Load Environment Variables from a File

```bash
docker run --env-file .env image_name
```

---

### 🔹 Access a Running Container

```bash
docker exec -it container_name bash
```

* `-it` → interactive terminal
* `bash` → shell inside container

---

## 8️⃣ Session 3: Docker Caching

### 🔹 Layer Caching Rules

* Docker caches each layer using its SHA
* If the instruction does not change → layer is reused
* If a layer changes:

  * That layer and **all layers below it** are rebuilt
  * Cache is invalidated downstream

---

## 9️⃣ Multi-Stage Builds

### 🔹 Why Multi-Stage Builds?

* Reduce final image size
* Remove unnecessary build dependencies
* Improve security & performance

---

### 🔹 How Multi-Stage Builds Work

* One Dockerfile
* Multiple `FROM` statements
* Each `FROM` starts a **new stage**

---

### 🔹 Typical Stages

#### 🏗 Stage 1: Builder Stage

* Install dependencies
* Compile/build application

#### 🚀 Stage 2: Final Stage

* Copy compiled artifacts from builder
* Exclude build tools
* Smaller and cleaner image

```dockerfile
FROM node:18 AS builder
# build steps

FROM node:18-slim
# copy only required files
```

✅ Only the **final stage** is used as the resulting image
❌ Builder stage is discarded

---

## 🔟 Key Takeaways

* Dockerfiles are **layer-based**
* Order of instructions matters
* Use caching wisely
* Use multi-stage builds for production
* Smaller images = faster, safer, better 🚀

## how normally we write data in docker
- a layer is created on top of all the docker layer 
- called writable layer. in which all the writing operation work in
- each time the container stop, this writable layer get removed and new layer is formed. all the layer is immutable except this one.

### Docker Volumne
- persistant memory
- docker conatiner is a isolated env, app_code + depe + os
- if container generate some data, outside the con, how to store it permanetly
- In docker demon, we create a volumne that is indep .. and we mount this volumne to container
- we can mount a single vol to many container 
- if we remove container. it doesn't remove volume
- vol are manager by docker demon
- vol are like hard drive for container

#### Type of volumnes
1) Volumn - manage and created by docker client
- In this we don't write data in writeable layer, we write this in volume
- volume are not accesabile without container 
- only container can read and write in volumns

2) Bind Mounts - filesystem mananger by host machine
- for container volume and bind mounts are same
- we can acess them by out host file system, folder and file
- are acessable without container
- also can be created on cloud like AWS

3) Temp file system - Store data in RAM
- resever space in ram as volumns
- Is temp

### syntax
- use --mount flag for mouting
- in mount we don't maintain key values pair order

> docker run --name book_recoomend --mount "type=bind,src=C:\Users\singh\College assignemnt\Resume Projects\Book Recommender System\audit,dst=/app/audit/"  -p5000:5000 -d book-recommendations-system:v2

in src and dst add absoulte path, it doesn;t work with relative path

### Docker Compose
- while passing flags, chances of mistakes are there
- Docker Compose is a file that has all those commands, this is a template that can be used to run all containers
- We can run multiple containers
- No need to run docker run command, good for reporodcubility

1) What is docker compose
- docker compose is a service, that is sep from docker 
- for build multi container application
- all the container are in the same network

2) Advantges
- single container -> Decoraative syntax, start container -> build + run container
- muliti container application -> Decoraative syntax, easy to manager muilti containers
- All contaiiner are on the same network
- same command use for stop and build
- nornally a config file, like compose.yaml, compose.yml