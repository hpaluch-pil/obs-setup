#!/bin/bash

# Validate XML files where possible

set -euo pipefail
#set -x
cd $(dirname $0)
for i in *-project.xml
do
	echo "Validating project '$i':"
	echo -n "- "
	xmllint --noout --relaxng /srv/www/obs/docs/api/project.rng $i
done
for i in distributions.xml
do
	echo "Validating distributions '$i':"
	echo -n "- "
	xmllint --noout --relaxng /srv/www/obs/docs/api/distributions.rng $i
done
for i in configuration.xml
do
	echo "Validating configuration '$i':"
	echo -n "- "
	xmllint --noout --relaxng /srv/www/obs/docs/api/configuration.rng $i
done
exit 0
