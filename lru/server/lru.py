import sys
import argparse
from collections import defaultdict


class LRUCache:
    def __init__(self, size: int = sys.maxsize):
        self.size = size
        self.table = defaultdict(None)
        self.stack = []

    def put(self, key, value):
        self.table[key] = value
        self.__updateLru(key)

    def get(self, key):
        result = None
        try:
            result = self.table[key]
            self.__updateLru(key)
        except:
            pass
        return result

    def delete(self, key):
        try:
            self.table.pop(key, None)
            self.stack.remove(key)
        except:
            pass  # no-op

    def reset(self):
        self.table = defaultdict()

    def __updateLru(self, key):
        if len(self.table.keys()) > self.size:
            # self.table.pop(self.stack[0], None)
            try:
                del self.table[self.stack[0]]
                self.table.pop(self.stack[0], None)
                self.stack.pop(0)  # remove LRU value
                self.stack.append(key)  # Add MRU value
            except:
                pass
        else:
            try:
                self.stack.remove(key)
            except:
                pass
            self.stack.append(key)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="LRU Cache Application")

    parser.add_argument(
        "-s",
        "--size",
        help="lru max size; \
                Tells the app the size of LRU.",
    )

    args = vars(parser.parse_args())
    maxSize = int(args["size"])

    lruCache = LRUCache(maxSize)

    while True:
        try:
            userInput = input(
                'Please enter desired command; \
               \nAvailable Commands: \
               \nput "<key>" "<value>"\
               \nget "<key>"\
               \ndelete "<key>"\
               \nreset. \n'
            )
            args = userInput.split(" ")
            command = args[0]
            if command == "put":
                key = int(args[1])
                value = int(args[2])
                lruCache.put(key, value)
            elif command == "get":
                key = int(args[1])
                value = lruCache.get(key)
                if value == None:
                    print('No value exists for key : "{}".'.format(key))
                else:
                    print("The value of {} is {}".format(key, value))
            elif command == "delete":
                key = int(args[1])
                lruCache.delete(key)
            elif command == "reset":
                lruCache.reset()
            else:
                raise Exception("Invalid command entered!!")
        except Exception as e:
            print(e)
