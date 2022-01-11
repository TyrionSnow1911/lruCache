import sys
from collections import defaultdict


class LRUCache:
    def __init__(self, size=sys.maxsize) -> None:
        self.size = size
        self.table = defaultdict(None)
        self.stack = []

    def put(self, key, value):
        self.table[key] = value
        self.__updateLru(key)

    def get(self, key):
        result = self.table[key]
        self.__updateLru(key)
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
        if len(self.table.keys()) >= self.size:
            self.table.pop(self.stack[0], None)
            self.stack.pop(0)  # remove LRU
            self.stack.append(key)  # Add MRU
        else:
            try:
                self.stack.remove(key)
            except:
                pass
            self.stack.append(key)


if __name__ == "__main__":
    # Code block below runs LRU Cache in offline mode.
    import argparse

    parser = argparse.ArgumentParser(description="LRU Cache Application")

    parser.add_argument(
        "-s",
        "--size",
        help="lru max size; \
                Tells the app the maximum size to initialize LRU cache with.",
    )

    args = vars(parser.parse_args())
    maxSize = args["size"]

    lruCache = LRUCache(maxSize)

    while True:
        try:
            userInput = input(
                "Please enter desired command; \
                \n put <key> <value>\
                \n get <key>\
                \n delete <key>\
                \n reset. \n"
            )
            args = userInput.split(" ")
            command = args[0]
            if command == "put":
                key = args[1]
                value = args[2]
                lruCache.put(key, value)
            elif command == "get":
                key = args[1]
                payload = {"key": key}
                result = lruCache.get(key)
                print("The value of {} is {}".format(key, result))
            elif command == "delete":
                key = args[1]
                lruCache.delete(key)
            elif command == "reset":
                lruCache.reset()
            else:
                raise Exception("Invalid command entered!!")
        except Exception as e:
            print(e)
