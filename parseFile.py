import argparse, requests, io, json
a = argparse.ArgumentParser()
a.add_argument("--input", "-i")
a.add_argument("--output", "-o")

p = a.parse_args()

r = requests.get(p.input)
content = r.text.strip().split("\n\n")
links = []
for entry in content:
    lines = entry.split("\n")
    link = lines[0]
    filename = lines[1].replace("  out=", "")
    checksum = lines[2].replace("  checksum=sha-1=", "")
    links.append({"name":filename, "link":link, "checksum":checksum})

f = open(p.output, "w")
f.write(json.dumps(links))
f.close()