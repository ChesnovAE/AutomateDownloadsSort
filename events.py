import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DowloadsHandler(FileSystemEventHandler):
    def __init__(self,
                 track_dir,
                 dest_dir):
        super(DowloadsHandler, self).__init__()
        self._folder_to_track = track_dir
        self._folder_destination = dest_dir

    def on_modified(self, event):
        for filename in os.listdir(self._folder_to_track):
            source_file = os.path.join(self._folder_to_track, filename)
            # Чекаем формат файла или директорию
            if os.path.isdir(source_file):
                file_format = 'folders'
            elif os.path.isfile(source_file):
                try:
                    file_format = filename.split('.')[-1]
                except IndexError:
                    file_format = 'unknowns'
            else:
                print('WTF is this?!')
            # Назначаем папку, в которой хранятся файлы данного формата
            destination_dir = os.path.join(self._folder_destination, file_format)
            # Если такой папки нет, то создаем ее
            if not os.path.exists(destination_dir):
                print('Такой штука нет')
                os.mkdir(destination_dir)
            
            # Определяем куда переместить файл
            destination_file = os.path.join(destination_dir, filename)
            # Перемещаем файлик
            os.rename(source_file, destination_file)


def handle_event(track_dir='/Users/antoncesnov/Downloads/',
                 dest_dir='/Users/antoncesnov/DownloadsMirror/'):
    handler = DowloadsHandler(track_dir=track_dir, dest_dir=dest_dir)
    observer = Observer()
    observer.schedule(handler, track_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()