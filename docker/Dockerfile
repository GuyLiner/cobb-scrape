FROM python:3.12-bookworm AS cobb-tracker-site
VOLUME /minutes
VOLUME /var/db

ADD scripts/ /scripts
RUN /scripts/init.sh

VOLUME /minutes
VOLUME /var/db

FROM cobb-tracker-site AS prod
EXPOSE 8001
CMD ["/usr/local/bin/datasette","serve","-h","0.0.0.0", "/var/db/minutes.db"]

FROM cobb-tracker-site AS staging
EXPOSE 8002
CMD ["/usr/local/bin/datasette","/var/www/cobb-tracker","-p","8002","-h","0.0.0.0"]
