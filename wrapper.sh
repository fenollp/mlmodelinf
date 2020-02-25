#!/bin/bash

# pip3 install --user coremltools pillow

pp=''
for p in /usr/local/lib/python3.7/site-packages \
             /usr/local/Cellar/protobuf/3.6.1.3_1/libexec/lib/python3.7/site-packages
do
    if [[ "$pp" = '' ]]; then
        pp="$p"
    else
        pp="$pp:$p"
    fi
done

PYTHONPATH="$pp" $@
