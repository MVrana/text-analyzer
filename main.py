with (open("text-analyzer/Input.txt", "r", encoding="utf-8") as f):
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i][0] == "#":
            print(lines[i].replace("#", "").strip() + ": " + str(len(lines[i+1].strip().split(" "))) + " slov")