#!/bin/sh

# dit werkt niet (password or username empty error)
curl -X POST \
	-F 'username=admin' \
	-F "password=\"georijgoierj'--\"" \
	https://secure.mc.ax/login
