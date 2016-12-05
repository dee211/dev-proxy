parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"
cd '../'
uwsgi --http 127.0.0.1:3333 --master --http-timeout 1 -w wsgi:proxy_app -t 60 --processes 4 --threads 2