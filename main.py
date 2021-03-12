#!/usr/bin/python3

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from utils.move_file import move_file
from settings import DIRECTORY_TO_WATCH, DESTINATION_FOLDER, IMAGE_DESTINATION_FOLDER, CODE_DESTINATION_FOLDER, MEDIA_DESTINATION_FOLDER, DOCUMENTS_DESTINATION_FOLDER, MEDIA, IMAGES, DOCUMENTS, CODE
import sys

ALL_CUSTOM_FILE_TYPES = MEDIA + CODE + IMAGES + DOCUMENTS


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_moved(event):
        if event.is_directory:
            return None
        # wait for download to finish
        if event.dest_path.startswith("Unconfirmed") or ".crdownload" in event.dest_path:
            print("Unconfirmed download detected.... Waiting for download to complete...")
            time.sleep(5)
        else:
            if any(ext in event.dest_path for ext in ALL_CUSTOM_FILE_TYPES):
                for img in IMAGES:
                    if img in event.dest_path:
                        time.sleep(5)
                        move_file(event.dest_path,
                                  IMAGE_DESTINATION_FOLDER)
                        print(
                            f"Moved {event.dest_path} to {IMAGE_DESTINATION_FOLDER}")
                for code in CODE:
                    if code in event.dest_path:
                        time.sleep(5)
                        move_file(event.dest_path,
                                  CODE_DESTINATION_FOLDER)
                        print(
                            f"Moved {event.dest_path} to {CODE_DESTINATION_FOLDER}")
                for media in MEDIA:
                    if media in event.dest_path:
                        time.sleep(5)
                        move_file(event.dest_path,
                                  MEDIA_DESTINATION_FOLDER)
                        print(
                            f"Moved {event.dest_path} to {MEDIA_DESTINATION_FOLDER}")
                for doc in DOCUMENTS:
                    if doc in event.dest_path:
                        time.sleep(5)
                        move_file(event.dest_path,
                                  DOCUMENTS_DESTINATION_FOLDER)
                        print(
                            f"Moved {event.dest_path} to {DOCUMENTS_DESTINATION_FOLDER}")
            else:
                time.sleep(5)
                move_file(event.dest_path, DESTINATION_FOLDER)
                print(f"Moved {event.dest_path} to {IMAGE_DESTINATION_FOLDER}")


class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            print("Error : ", sys.exc_info()[0])
            self.observer.stop()

        self.observer.join()


if __name__ == '__main__':
    w = Watcher()
    w.run()
