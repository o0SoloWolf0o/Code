from pptx import Presentation
from getpass import getpass

characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "

length = 8

def open_pptx_file(file_path, password):
    try:
        presentation = Presentation(file_path, password=password)
        print(f"Successfully opened the PowerPoint file. Password: {password}")
        raise SystemExit
    except Exception as e:
        print(f"Failed to open the PowerPoint file with password '{password}'. Error: {e}")

if __name__ == "__main__":
    file_path = "C:/Users/porpu/Desktop/1.pptx"
    for i in range(len(characters)):
        for j in range(len(characters)):
            for k in range(len(characters)):
                for l in range(len(characters)):
                    for m in range(len(characters)):
                        for n in range(len(characters)):
                            for o in range(len(characters)):
                                for p in range(len(characters)):
                                    combination = characters[i] + characters[j] + characters[k] + characters[l] + characters[m] + characters[n] + characters[o] + characters[p]
                                    print(combination)
                                    password = getpass(combination)
                                    open_pptx_file(file_path, combination)
