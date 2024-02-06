from random import randint
from turtle import title
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self) -> None:
        self.title = title
        self.length = randint(5,6)

class MediaPlayerQueue(Queue):
    def __init__(self) -> None:
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"Count: {self.count}")

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}")

            sleep(current_track_node.length)

