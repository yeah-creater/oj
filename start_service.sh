#nginx
sudo service nginx start
# redis
sudo redis-server /etc/redis/redis.conf
# websocket
daphne -b 0.0.0.0 -p 5015 oj.asgi:application
