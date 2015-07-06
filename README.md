rssr
====

A simple python3 rssr reader

Installation
------------

```sh
sudo chmod +x install-all.sh
./install-all.sh
```

Dependecies
-----------

 * python3
 * python3-feedparser
 * python3-lxml
 * surf (only by default, you can use any web browser you want, just run `rss-read` with `-c YOUR_WEB_BROWSER`, also write this to the `rss` shell script)

Cron
----

If you want to pull new articles from your feeds automaticly, you can use cron:

```sh
crontab -e
```

An editor should open. Jump to the end and write:

```sh
0 0,4,8,12,16,20 * * * /usr/bin/rssr-pull
```

Save and close and your done. From this moment cron will execute `rssr-pull` every four hours.

Feeds
-----

Feeds are in `~/.rssr/feeds`.

Adding a new feed is pretty simple:

```sh
echo FEED_URL >> ~/.rssr/feeds
```
