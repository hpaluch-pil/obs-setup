#!/bin/bash
set -euo pipefail
#set -x


cd $(dirname $0)

rng_base=/srv/www/obs/docs/api/
proj_rng=$rng_base/project.rng
pkg_rng=$rng_base/package.rng

validate_file ()
{
	local f="$1"

	[ -n "$f" ] || {
		echo "validate_file error - argument empty" >&2
		exit 1
	}
	[ -f "$f" -a -r "$f" ] || {
		echo "'$f' is not file or unreadable" >&2
		exit 1
	}
	[ -s "$f" ] || {
		echo "File '$f' is empty" >&2
		exit 1
	}
}


validate_xml_file ()
{
	local xml="$1"
	local rng="$2"

	for i in "$xml" "$rng"
	do
		[ -n "$i" ] || {
			echo "Internal error - argument empty" >&2
			exit 1
		}
		validate_file "$i"
	done
	echo "Validating '$xml':"
	echo -n "- "
	xmllint --noout --relaxng $rng $xml

}

merge_changes ()
{
	local f="$1"
	[ -n "$f" ] || {
		echo "merge_changes: missing argument" >&2
		exit 1
	}
	validate_file "$f.new"
	if [ -f "$f" ];then
		if diff -u "$f" "$f.new" ;then
			rm -f "$f.new"
		else
			mv -f "$f.new" "$f"
		fi	
	else
		mv -f "$f.new" "$f"
	fi

}


f=home-hpaluch-pil-proj.xml
osc api /source/home\:hpaluch-pil/_meta > $f.new
validate_xml_file $f.new $proj_rng 
merge_changes $f

f=home-hpaluch-pil-proj.spec
osc api /source/home\:hpaluch-pil/_config > $f.new
validate_file $f.new
merge_changes $f


f=clockres-pkg.xml
osc api /source/home\:hpaluch-pil/clockres/_meta > $f.new
validate_xml_file $f.new $pkg_rng
merge_changes $f

exit 0
