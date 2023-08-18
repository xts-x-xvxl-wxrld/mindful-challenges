server {
    listen 8080;

    location / {
        return 301 https://$host$request_uri;
    }
    location /.well-known/acme-challenge/ {
    root /var/www/certbot;
    }
}

server {
    listen ${LISTEN_PORT};

    location / {
        uwsgi_pass  ${APP_HOST}:${APP_PORT};
        include     /etc/nginx/uwsgi_params;
    }
    location /static {
        alias /vol/static;
    }
}
