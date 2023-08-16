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