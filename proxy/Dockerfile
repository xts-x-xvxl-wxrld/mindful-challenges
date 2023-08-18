FROM nginx:1.15-alpine
LABEL mainteiner="ravilgaleev715@gmail.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8443
ENV APP_HOST=meditation-app
ENV APP_PORT=9000

RUN apk update && \
    apk add --no-cache certbot certbot-nginx && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

CMD ["/run.sh"]
