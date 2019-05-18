while sleep 600; do
	echo '------------------------------------'
	date
	echo '------------------------------------'

	# start this again in case it crashed
	Xvfb :99 -ac &
	pid=$!

	DISPLAY=:99 env/bin/python save-urls.py

	kill "$pid"
done >> /tmp/save-urls.log 2>&1
