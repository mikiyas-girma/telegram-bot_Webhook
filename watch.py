
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

bot_process = None


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event: FileSystemEvent) -> None:
        print("Bot code modified. Restarting bot...")
        restart_bot()


def restart_bot():
    global bot_process
    if bot_process is not None:
        bot_process.kill()
    bot_process = subprocess.Popen(["python3", "bot.py"])


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    # start the bot initially
    subprocess.Popen(["python3", "bot.py"])
    # restart_bot()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
