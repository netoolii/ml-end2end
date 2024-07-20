FROM mariadb:10.4



ENV MARIADB_ROOT_PASSWORD=password
ENV MARIADB_DATABASE=workshop
ENV MARIADB_USER=admin
ENV MARIADB_PASSWORD=password

EXPOSE 3306

COPY ./mariadb/ /docker-entrypoint-initdb.d

VOLUME [ "/var/lib/mysql" ]