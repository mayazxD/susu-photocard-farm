from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
MEMBERS = {
    "TXT": ["soobin", "yeonjun", "beomgyu", "taehyun", "hueningkai"],
    "ENHYPEN": ["jungwon", "heeseung", "jay", "jake", "sunghoon", "sunoo", "niki"],
}

library = {}
for group, members in MEMBERS.items():
    for member in members:
        folder = ROOT / group / member
        folder.mkdir(parents=True, exist_ok=True)
        images = []
        for path in sorted(folder.iterdir()):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
                rel = path.relative_to(ROOT).as_posix()
                images.append({"u": rel, "p": "", "a": "", "l": "", "source": "Local gallery"})
        library[member] = images

(ROOT / "photos.json").write_text(json.dumps(library, ensure_ascii=False, indent=2), encoding="utf-8")
count = sum(len(items) for items in library.values())
print(f"Gallery list created: {count} image(s) across {len(MEMBERS['TXT']) + len(MEMBERS['ENHYPEN'])} member folders.")
print("TXT:", sum(len(library[m]) for m in MEMBERS["TXT"]), "images")
print("ENHYPEN:", sum(len(library[m]) for m in MEMBERS["ENHYPEN"]), "images")
print("Next: run 'py -m http.server 8000' in this folder and open http://localhost:8000")
