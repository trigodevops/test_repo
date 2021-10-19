docker build -t trigo/service-b .
docker run -d --hostname service-b --name service-b -e Trigo_server_name=service-b -e Trigo_server_mode=production -e Trigo_server_status=online --network=tri-net trigo/service-b
apt-get  install mosquitto-clients -y
mosquitto_pub -m "prod" -t trigo/server_mode -h $(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mosquitto-a)
mosquitto_pub -m "service-b" -t trigo/server_name -h $(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mosquitto-a)
mosquitto_pub -m "online" -t trigo/server_status -h $(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mosquitto-a)
