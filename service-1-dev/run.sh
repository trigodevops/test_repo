docker build -t trigo/service-a-dev .
docker run -d --hostname service-a-dev --name service-a-dev -e Trigo_server_name=service-a-dev -e Trigo_server_mode=production -e Trigo_server_status=online --network=tri-net trigo/service-a-dev
