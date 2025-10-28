import re
import os

print("Program starting.")
print("This program can copy a file.")
filenamein = input("Insert source filename: ")

if not os.path.exists(filenamein):
    print(f"Error: source file '{filenamein}' not found.")
    print("Program ending.")
else:
    file = open(filenamein, 'r')
    L1 = len(re.findall(r"[\n']+", open(filenamein).read()))
    filenameout = input("Insert destination filename: ")

    open(filenameout, 'w').write('')

    def paaohjelma():
        while True:
            f = file.readline().replace('\n', '')
            if f == "":
                L2 = len(re.findall(r"[\n']+", open(filenameout).read()))
                print(f"Reading file '{filenamein}' content.")
                print("File content ready in memory.")
                print(f"Writing content into file '{filenameout}'.")
                print("Copying operation complete.")
                print("Program ending.")
                break

            if any(ch.isdigit() for ch in f):
                pass
            else:
                open(filenameout, 'a').write(f + '\n')

        file.close()

    paaohjelma()
