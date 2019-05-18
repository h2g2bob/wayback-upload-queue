#!/bin/sh
wget --quiet -O- 'https://electionleaflets.org/leaflets/' | grep -E -o '/leaflets/[0-9]+/' | while read relurl; do
	echo "https://electionleaflets.org${relurl}"
done
