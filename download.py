import argparse,json,requests,os,colorama
from colorama import Fore

colorama.init()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input")
ap.add_argument("-o", "--output")

args = ap.parse_args()

if not os.path.exists(args.output):
    os.mkdir(args.output)
if not os.path.isdir(args.output):
    os.remove(args.output)

fp = open(args.input, "r")
j = json.load(fp)
fp.close()

for a in j:
    print(Fore.CYAN + "Downloading " + a["name"] + " from Update Servers..." + colorama.Style.RESET_ALL)
    r = requests.get(a["link"])
    if r.status_code != 200:
        print(Fore.RED + "Failed to download " + a["name"] + f" with error {r.status_code}" + colorama.Style.RESET_ALL)
        continue
    print("Length is: " + f"{len(r.content)}" + " bytes ig")
    f = open(args.output + "/" + a["name"], "wb")
    f.write(r.content)
    f.close()
    print(Fore.GREEN + "Downloaded " + a["name"] + " from Update Servers..." + colorama.Style.RESET_ALL)
    