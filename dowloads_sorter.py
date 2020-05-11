import os
import json
import time
#
from watchdog.observers import Observer
#
from watchdog.events import FileSystemEventHandler


class Folders:
    folder_to_track = '/Users/antoncesnov/test_folder/'
    folder_destination = 'Users/antoncesnov/test_folder_mv/'


class DowloadsHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(Folders.folder_to_track):
            source_file = os.path.join(Folders.folder_to_track, filename)
            destination_file = os.path.join(Folders.folder_destination, filename)
            os.rename(source_file, destination_file)


def handle_event():
    handler = DowloadsHandler()
    observer = Observer()
    observer.schedule(handler, Folders.folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
