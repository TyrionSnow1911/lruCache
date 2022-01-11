import requests

BASE_URL = "http:/localhost:8080/"

if __name__ == "__main__":
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
                payload = {"key": key, "value": value}
                response = requests.get("{}/put".format(BASE_URL), params=payload)

            elif command == "get":
                key = args[1]
                payload = {"key": key}
                response = requests.get("{}/get".format(BASE_URL), params=payload)
                print("The value of {} is {}".format(key, response.json()["data"]))

            elif command == "delete":
                key = args[1]
                payload = {"key": key}
                response = requests.get("{}/delete".format(BASE_URL), params=payload)

            elif command == "reset":
                response = requests.get("{}/reset".format(BASE_URL))
            else:
                raise Exception("Invalid command entered!!")
        except Exception as e:
            print(e)
