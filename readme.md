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
