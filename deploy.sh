#!/bin/bash
DIR=$(dirname "$0")

chef --root="$DIR" purge
chef --root="$DIR" bake --output=blog --force
#cp $DIR/CNAME blog/

cp "$DIR/CNAME" "$DIR/blog/"

ghp-import -n -m "Publishing tupilabs.com" -p -r origin -b master blog
