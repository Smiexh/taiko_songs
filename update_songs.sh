#!/bin/sh

echo "// $(date)" > taiko_songs.js
echo "const jsonData =" >> taiko_songs.js
python3 get_taiko_songs.py >> taiko_songs.js