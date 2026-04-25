import os, sys
import uuid
dir_path = os.path.dirname(os.path.abspath(__file__))

file = open(os.path.join(dir_path, f"pattern14_Output.txt"), "w", encoding="utf-8")


def PrintPattern(endCharacter):
    start = 65 if endCharacter.isupper() else 97
    end = ord(endCharacter)

    for i in range(end-start+1):
        for j in range(start, start+i+1):
            print(f"{chr(j)}", end="", file=file)
        print(file=file)


endCharacter = input("Enter any Alphbet(max_len=1): ")

while not endCharacter.isalpha() or len(endCharacter)>1:
    endCharcter = input("Enter any Alphbet(max_len=1):  ")

PrintPattern(endCharacter)
file.close()