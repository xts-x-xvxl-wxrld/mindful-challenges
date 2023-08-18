FROM nginxinc/nginx-unprivileged:1-alpine
LABEL mainteiner="ravilgaleev715@gmail.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh
COPY ./init-letsencrypt.sh /init-letsencrypt.sh

ENV LISTEN_PORT=8443
ENV APP_HOST=meditation-app
ENV APP_PORT=9000

USER root

RUN apk update && \
    apk add --no-cache bash && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh && \
    chmod +x /init-letsencrypt.sh

VOLUME /vol/static

USER nginx

CMD ["/init-letsencrypt.sh"]
