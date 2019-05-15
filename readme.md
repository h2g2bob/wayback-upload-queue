The idea is:

- find some urls and put them into a queue
- run one or more workers to put the queued urls into the Wayback Machine

## Put some urls into the queue

Make the sqlite db (does nothing if `queue.db` already exists):

```
python create-queue.py
```

Add some urls to the queue:

```
python add-to-queue.py < some-list-of-urls
```

## Save to the Wayback Machine

In a virtualenv:

```
pip install selenium==3.141.0
```

And you also need:

```
apt install chromedriver
```

And run with:

```
Xvfb :99 -ac &
DISPLAY=:99 env/bin/python save_urls.py <<< https://dbatley.com/
```
