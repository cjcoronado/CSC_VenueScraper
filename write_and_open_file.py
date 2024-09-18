import os


def write_and_open_file(filename, content):
    # Writing the content to the file
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Content has been written to {filename}")

    # Opening the file in the default text editor
    os.system(f"notepad.exe {filename}")