#! /bin/bash

mkdir -p ~/.rssr
mkdir -p ~/.rssr/articles
touch ~/.rssr/feeds
cp rssr.html ~/.rssr/rssr.html

sudo cp rssr.py /usr/local/lib/python$(python3 -c 'from sys import version_info; print("{}.{}".format(version_info.major, version_info.minor))')/dist-packages/rssr.py

sudo chmod +x rssr
sudo chmod +x rssr-pull
sudo chmod +x rssr-read
sudo cp rssr /usr/bin/rssr
sudo cp rssr-pull /usr/bin/rssr-pull
sudo cp rssr-read /usr/bin/rssr-read
