import os.path

filepath = os.path.normpath(r"C:\Users\barto\OneDrive\Pulpit\piholelist.txt")

with open(os.path.join(os.path.dirname(filepath), 'newlist.txt'), "a+") as newf:
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = str(line).split("â€“")[-1].strip()
            print(line)
            newf.write(line + "\n")
