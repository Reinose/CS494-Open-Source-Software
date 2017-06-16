FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD password
ENV MYSQL_USER reinose
ENV MYSQL_PASSWORD password
ENV MYSQL_DATABASE cs494

ADD init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

#RUN service mysql start
#RUN mysql -u reinose --password=password -e "source /docker-entrypoint-iinitdb.d/init.sql"
