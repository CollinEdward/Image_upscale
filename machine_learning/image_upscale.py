import platform
import os

print("Image URL not Path")


# Remember to insert your own api key here for the tool to work - https://deepai.org/
api_key = "Insert your api key here"



def main_script(command: str) -> None:
    match command.split():
        case ["image" | "img", url]:
            os.system(f"curl -F 'image={url}' -H 'api-key:{api_key}' https://api.deepai.org/api/torch-srgan \n")
            print("\n")

        case ["exit" | "quit"]:
            exit()

        case _:
            os.system(command)


def main():
    while 1: 
        command = input(f"{platform.node()} $ ")
        main_script(command)

if __name__ == "__main__":
    main()