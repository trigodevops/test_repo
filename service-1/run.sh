docker build -t trigo/service-a .
docker run -d --hostname service-a --name service-a -e Trigo_server_name=service-a -e Trigo_server_mode=production -e Trigo_server_status=online --network=tri-net trigo/service-a
