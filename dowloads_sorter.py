import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


folder_to_track = '/Users/antoncesnov/Downloads/'
folder_destination = '/Users/antoncesnov/DownloadsMirror/'


class DowloadsHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            source_file = os.path.join(folder_to_track, filename)
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
            destination_dir = os.path.join(folder_destination, file_format)
            # Если такой папки нет, то создаем ее
            if not os.path.exists(destination_dir):
                print('Такой штука нет')
                os.mkdir(destination_dir)
            
            # Определяем куда переместить файл
            destination_file = os.path.join(destination_dir, filename)
            # Перемещаем файлик
            os.rename(source_file, destination_file)


def handle_event():
    handler = DowloadsHandler()
    observer = Observer()
    observer.schedule(handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

handle_event()