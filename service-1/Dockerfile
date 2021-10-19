FROM nginx:latest
COPY ./default.conf /etc/nginx/conf.d/default.conf
copy 05-conf.sh /docker-entrypoint.d/05-conf.sh
RUN chmod +x /docker-entrypoint.d/05-conf.sh
