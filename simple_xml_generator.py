import os
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--track_dir', help='Folder that you want to track')
parser.add_argument('--dest_dir', help='Folder in which you want to move files')
args = parser.parse_args()

home_path = str(Path.home())
python_version = sys.version_info[0]
if python_version == '2':
    python_path = '/usr/bin/python'
elif python_version == '3':
    python_path = '/usr/local/bin/python3'

xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.downloads.sorter</string>
    <key>ServiceDescription</key>
    <string>Daemon which sort downloads</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>/opt/projects/download_sorter/downloads_sorter.py</string>
        <string>--track-dir</string>
        <string>{args.track_dir}</string>
        <string>--dest-dir</string>
        <string>{args.dest_dir}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
'''
with open(f'{home_path}/Library/LaunchAgents/com.downloads.sort.plist', 'w') as xml_file:
    xml_file.write(xml)