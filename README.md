# TupiLabs.com

TupiLabs website. Generated as static site, through [PieCrust](https://bolt80.com/piecrust).

## Requirements

* Python 3 (preferably with Continuum Anaconda Python 3) and pip
* `pip install -r requirements.txt`
* [Apache Ant](https://ant.apache.org)

## Building

To run the site locally.

`ant blog-run`

## Deploying

Deployments are done with SSH authentication.

`ant deploy -Dssh.username=myuser -Dssh.host=myhost -Dssh.port=myport -Dssh.dir=/srv/var/www/tupilabs.com/public_html`

## Scripts

`scripts/trello_tupi.py` is used to generate TupiLabs reports posts. You must have a dotEnv
file, with the following settings.

```
# File: .env

TRELLO_URL_1=https://trello/boards...
TRELLO_URL_1=https://trello/lists...
```
