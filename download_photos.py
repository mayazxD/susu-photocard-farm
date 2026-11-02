from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import hashlib, mimetypes, time, sys

ROOT = Path(__file__).resolve().parent
DEFAULT_NEW_PER_MEMBER = 25  # asked at each run; 12 members x 25 = up to 300 new downloads
MIN_BYTES = 8_000
MAX_BYTES = 15 * 1024 * 1024
ALLOWED = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
MEMBERS = [
    ("TXT", "soobin", "Tomorrow X Together TXT Soobin"),
    ("TXT", "yeonjun", "Tomorrow X Together TXT Yeonjun"),
    ("TXT", "beomgyu", "Tomorrow X Together TXT Beomgyu"),
    ("TXT", "taehyun", "Tomorrow X Together TXT Taehyun"),
    ("TXT", "hueningkai", "Tomorrow X Together TXT Huening Kai"),
    ("ENHYPEN", "jungwon", "ENHYPEN Jungwon"),
    ("ENHYPEN", "heeseung", "ENHYPEN Heeseung"),
    ("ENHYPEN", "jay", "ENHYPEN Jay"),
    ("ENHYPEN", "jake", "ENHYPEN Jake"),
    ("ENHYPEN", "sunghoon", "ENHYPEN Sunghoon"),
    ("ENHYPEN", "sunoo", "ENHYPEN Sunoo"),
    ("ENHYPEN", "niki", "ENHYPEN Ni-ki"),
]

def existing_hashes():
    seen = set()
    for group, member, _ in MEMBERS:
        folder = ROOT / group / member
        folder.mkdir(parents=True, exist_ok=True)
        for p in folder.iterdir():
            if p.is_file() and p.suffix.lower() in ALLOWED:
                try: seen.add(hashlib.sha256(p.read_bytes()).hexdigest())
                except OSError: pass
    return seen

def get_ext(url, content_type):
    ext = Path(urlparse(url).path).suffix.lower()
    if ext in ALLOWED: return ".jpg" if ext == ".jpeg" else ext
    ext = mimetypes.guess_extension(content_type.split(";")[0].strip().lower()) if content_type else None
    if ext == ".jpe": ext = ".jpg"
    return ext if ext in ALLOWED else None

def main():
    try:
        from ddgs import DDGS
    except ImportError:
        print("Missing dependency. Run: py -m pip install ddgs")
        sys.exit(1)

    new_per_member = DEFAULT_NEW_PER_MEMBER
    if len(sys.argv) > 1:
        try: new_per_member = max(1, min(100, int(sys.argv[1])))
        except ValueError: print("Usage: py download_photos.py [new-images-per-member]"); sys.exit(2)

    seen = existing_hashes()
    total = 0
    for group, member, query in MEMBERS:
        folder = ROOT / group / member
        already = sum(1 for p in folder.iterdir() if p.is_file() and p.suffix.lower() in ALLOWED)
        need = new_per_member
        print(f"\nSearching {query} (goal: up to {need} NEW images; already have {already})...")
        saved = 0
        try:
            with DDGS() as ddgs:
                results = list(ddgs.images(query, max_results=min(max(need * 4, 40), 100), safesearch="moderate"))
        except Exception as e:
            print(f"  Search failed: {e}")
            continue
        for item in results:
            if saved >= need: break
            url = item.get("image") or item.get("url")
            if not url or not url.startswith(("http://", "https://")): continue
            try:
                req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PersonalPhotoGallery/1.0)"})
                with urlopen(req, timeout=12) as response:
                    ctype = response.headers.get("Content-Type", "")
                    if not ctype.lower().startswith("image/"): continue
                    ext = get_ext(url, ctype)
                    if not ext: continue
                    data = response.read(MAX_BYTES + 1)
                if len(data) < MIN_BYTES or len(data) > MAX_BYTES: continue
                digest = hashlib.sha256(data).hexdigest()
                if digest in seen: continue
                seen.add(digest)
                filename = f"auto_{digest[:12]}{ext}"
                (folder / filename).write_bytes(data)
                saved += 1; total += 1
                print(f"  + {filename}")
                time.sleep(0.25)
            except (HTTPError, URLError, TimeoutError, OSError, ValueError):
                continue
        print(f"  Saved {saved} new images; this folder now has about {already + saved} images.")
        time.sleep(1.2)  # reduce search rate-limit risk

    print("\nRebuilding photos.json...")
    import subprocess
    result = subprocess.run([sys.executable, str(ROOT / "build_gallery.py")], cwd=ROOT)
    print(f"\nDone. Downloaded {total} new images.")
    print("Review each member folder before using the gallery; search results can be mislabeled.")
    print("Respect each image's copyright and source terms, especially before publishing the site.")
    sys.exit(result.returncode)

if __name__ == "__main__": main()
