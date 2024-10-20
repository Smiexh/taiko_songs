#!/bin/sh

js_file_path="dist/taiko_songs.js"

echo "// $(date)" > $js_file_path
echo "const jsonData =" >> $js_file_path
python3 get_taiko_songs.py >> $js_file_path