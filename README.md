# Steps
1. Download an UUP creator from https://uupdump.net
2. Open the uup_download_windows.cmd with a text editor
3. Search for "https://uupdump.net/get.php" in the file
4. Copy the string (between quotes)
5. Run python parseFile.py -i [string you copied] -o links.json
6. Run python getDownloadLinks.py -i links.json -o valid.json
7. Run python download.py -i valid.json -o [a dirname (example: UUPs)]

## For developers
You can customize the filter in getDownloadLinks.py. Just change the filter function. It must return a boolean

## Troubleshooting

If you get errors (like 403 error codes), you can use the uup downloader with a tweak:
1. Execute all steps aboce up to step 6
2. Run python makeoutput.py -i valid.json -o aria2.txt
3. Upload that file somewhere in the internet
4. Copy that link and replace the ttps://uupdump.net/get.php[...] one in the file uup_download_windows.cmd with it
5. Delete the UUPs folder and restart the process. Enjoy!

If you are getting module not found errors, do pip install colorama and pip install requests