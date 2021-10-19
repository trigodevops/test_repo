docker build -t trigo/nginx-proxy .
docker network create -d bridge tri-net
docker run -d -p 8080:8080 --hostname nginx-proxy --name nginx-proxy --network tri-net trigo/nginx-proxy
