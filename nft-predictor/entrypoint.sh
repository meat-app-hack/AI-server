#!/bin/bash

WEIGHTS_PATH="$PWD/data/6_class_4_layer_100epoch.h5"
if [ -f "$WEIGHTS_PATH" ]; then
  echo "$WEIGHTS_PATH exists"
else 
  ID="17tq47-ogip3DSfZxsqhrr80Vh4HeBQNP"
  URL="https://docs.google.com/uc?export=download&id=$ID"
  wget --load-cookies /tmp/cookies.txt \
    "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate $URL -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$ID" \
     -O $WEIGHTS_PATH && rm -rf /tmp/cookies.txt
fi

python $PWD/server.py
