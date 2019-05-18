The idea is:

- find some urls and put them into a queue
- run one or more workers to put the queued urls into the Wayback Machine

## Basic

```
virtualenv env --python=python3
```

## Put some urls into the queue

Make the sqlite db (does nothing if `queue.db` already exists):

```
python env/bin/create-queue.py
```

Add some urls to the queue:

```
python env/bin/add-to-queue.py < some-list-of-urls
```

### Some urls...?

Why yes, like:

```
env/bin/pip install requests
env/bin/python extract_urls/democlub.py | env/bin/python add-to-queue.py
env/bin/python extract_urls/democlub-by-scraping.py | grep -vF -e democracyclub.org.uk -e whocanivotefor.co.uk | env/bin/python add-to-queue.py
sh extract_urls/electionleaflets.sh | env/bin/python add-to-queue.py
```

## Save to the Wayback Machine

In a virtualenv:

```
env/bin/pip install selenium
```

And you also need:

```
apt install chromedriver
```

A worker will run until there are no more urls in the queue:

```
Xvfb :99 -ac &
DISPLAY=:99 env/bin/python save-urls.py
```
