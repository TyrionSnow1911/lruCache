import requests

BASE_URL = "http://localhost:8080"

if __name__ == "__main__":
    while True:
        try:
            userInput = input(
                'Please enter desired command; Available Commands: \
               \n- put "<key>" "<value>"\
               \n- get "<key>"\
               \n- delete "<key>"\
               \n- reset\
               \n>'
            )
            args = userInput.split(" ")
            command = args[0]
            if command == "put":
                key = args[1]
                value = args[2]
                payload = {"key": key, "value": value}
                response = requests.put("{}//put".format(BASE_URL), params=payload)

            elif command == "get":
                key = args[1]
                payload = {"key": key}
                response = requests.get("{}//get".format(BASE_URL), params=payload)
                value = response.json()["data"]
                if value == None:
                    print('No value exists for key : "{}".'.format(key))
                else:
                    print("The value of {} is {}".format(key, response.json()["data"]))

            elif command == "delete":
                key = args[1]
                payload = {"key": key}
                response = requests.delete(
                    "{}//delete".format(BASE_URL), params=payload
                )

            elif command == "reset":
                response = requests.post("{}//reset".format(BASE_URL))
            else:
                raise Exception("Invalid command entered!!")
        except Exception as e:
            print(e)
