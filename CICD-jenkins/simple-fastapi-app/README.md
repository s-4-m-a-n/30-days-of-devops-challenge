# A Simple Two tier Fastapi

## run using docker compose 
```
sudo docker compose up 
```

## run using docker build and docker network

- build app
```
docker build -t fastapi-app .
```
- create network
```
docker network create app-network
```
- run redis in the app-network
```
docker run -d --name redis --network app-network redis:latest
```
- run fastapi-app
```
docker run -p 8000:8000 --name fastapi-app --network app-network -e REDIS_HOST=redis fastapi-app
```

