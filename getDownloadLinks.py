import json, argparse
a = argparse.ArgumentParser()
a.add_argument("--input", "-i")
a.add_argument("--output", "-o")
p = a.parse_args()

def filter(entry):
    if "appx" in entry.split("."[-1]) or "msix" in entry.split("."[-1]):
        if "language" not in entry:
            return True

    return False
f = open(p.input, "r")
j = json.load(f)
valid = []
for entry in j:
    if filter(entry["name"]):
        valid.append(entry)

f = open(p.output, "w")
json.dump(valid, f)
f.close()