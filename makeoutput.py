import json, argparse
a = argparse.ArgumentParser()
a.add_argument("--input", "-i")
a.add_argument("--output", "-o")
p = a.parse_args()

f = open(p.input, "r")
j = json.load(f)

total = ""

for a in j:
    total += f"{a['link']}\n  filename={a['name']}\n  checksum=sha-1={a['checksum']}\n"
    
f = open(p.output, "w")
f.write(total)
f.close()