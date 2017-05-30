from watchdog.observers import Observer

from .ptyeventhandler import AIOEventHandler

class _PtyWatchdog(object):

    def __init__(self, path='.', recursive=True, event_handler=None):
        self._observer = Observer()

        evh = event_handler or AIOEventHandler()

        self._observer.schedule(evh, path, recursive)

    def start(self):
        self._observer.start()

    def stop(self):
        self._observer.stop()
        self._observer.join()
