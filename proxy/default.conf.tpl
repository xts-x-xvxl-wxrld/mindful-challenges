server {
    listen 8000;
    server_name mindful-challenges.xyz www.mindful-challenges.xyz;

    location / {
        return 301 https://$host$request_uri;
    }
    location /.well-known/acme-challenge/ {
    root /var/www/certbot;
    }
}

server {
    listen ${LISTEN_PORT} ssl;
    server_name mindful-challenges.xyz www.mindful-challenges.xyz;

    ssl_certificate /etc/letsencrypt/live/mindful-challenges.xyz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mindful-challenges.xyz/privkey.pem;

    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        uwsgi_pass  ${APP_HOST}:${APP_PORT};
        include     /etc/nginx/uwsgi_params;
    }
    location /static {
        alias /vol/static;
    }
}
