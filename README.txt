SUSU PC FARM — LOCAL GALLERY STARTER

WHAT'S INSIDE
- index.html: your existing farm adapted to use a local image manifest.
- build_gallery.py: scans each member folder and creates photos.json.
- photos.json: generated list of images (created when you run the script).
- TXT and ENHYPEN: put each member's image files in their matching folder.
- review: keep uncertain member photos here until you identify them.

MEMBER FOLDERS
TXT/soobin, TXT/yeonjun, TXT/beomgyu, TXT/taehyun, TXT/hueningkai
ENHYPEN/jungwon, ENHYPEN/heeseung, ENHYPEN/jay, ENHYPEN/jake,
ENHYPEN/sunghoon, ENHYPEN/sunoo, ENHYPEN/niki

IMPORTANT
1. Put image files (.jpg, .jpeg, .png, .webp, .gif) into the matching member folders.
2. Double-clicking index.html directly may not load photos.json due to browser file security. Use the local server steps below.
3. Install Python from https://www.python.org/downloads/windows/ if the 'py' command isn't available.

EACH TIME YOU ADD IMAGES
1. Open the susu-gallery folder in File Explorer.
2. Click the address bar, type cmd, and press Enter.
3. Run: py build_gallery.py
4. Run: py -m http.server 8000
5. In Chrome, visit: http://localhost:8000
6. To stop the server, go back to Command Prompt and press Ctrl+C.

START SMALL
Aim for about 25 approved images per member (12 members = 300 total). Image filenames can be anything, but keep each image in the correct member folder. Do not put images in review if you want them to appear in the game.

ONLINE LATER
When ready to publish, upload index.html, photos.json, and the member image folders (or a web-sized images folder) to the same static website location. Only publish images you have permission to redistribute. Never upload private downloads or account cookies.


ONE-CLICK WINDOWS SHORTCUTS
- Double-click ONE_CLICK_DOWNLOAD.bat to install/check the free dependency, download additional images, sort them into member folders, and rebuild photos.json. Keep the window open until it finishes.
- Double-click OPEN_WEBSITE.bat to start the local server and open the website in your browser. Keep its window open while playing.
- Existing images are preserved. The downloader defaults to a target of 25 images per member, so it may skip folders already at that target.


NEW PHOTO COUNT: Double-click ONE_CLICK_DOWNLOAD.bat and enter the number of NEW images you want it to try downloading for EACH member. Example: 50 means up to 600 new images across 12 members. Actual totals may be lower because of duplicates, blocked hosts, or search limits. Existing images are kept.
