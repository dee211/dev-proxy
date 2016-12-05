parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"
sudo apt-get install libpcre3 libpcre3-dev
pip install -r requirements.txt