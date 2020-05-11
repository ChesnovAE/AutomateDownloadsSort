import argparse
from events import handle_event

parser = argparse.ArgumentParser()
parser.add_argument('--track_dir', help='Folder that you want to track')
parser.add_argument('--dest_dir', help='Folder in which you want to move files')

args = parser.parse_args()
handle_event(args.track_dir, args.dest_dir)