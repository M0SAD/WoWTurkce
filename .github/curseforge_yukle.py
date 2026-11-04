import json, os, re, subprocess, sys, urllib.request, zipfile

API = "https://wow.curseforge.com/api"
key, pid = os.environ["CF_API_KEY"], os.environ["CF_PROJECT_ID"]
src = "WoWTurkce.zip"

with zipfile.ZipFile(src) as z:
    names = z.namelist()
    toc = next(n for n in names if n.endswith("WoWTurkce.toc") and n.count("/") == 1)
    txt = z.read(toc).decode("utf-8", "ignore")
    root = toc.split("/")[0]
    # Yalnızca WoWTurkce klasörü, içinde dışarıdan .exe vb. yok
    bad = [n for n in names if not n.startswith(root + "/") or n.lower().endswith((".exe", ".dll"))]
    if bad:
        sys.exit("zip beklenmedik dosya içeriyor: %s" % bad[:5])

ver = re.search(r"^## Version:\s*(\S+)", txt, re.M).group(1)
ifaces = re.search(r"^## Interface:\s*(.+)$", txt, re.M).group(1)
wanted = set()
for n in re.findall(r"\d+", ifaces):
    n = int(n)
    wanted.add("%d.%d.%d" % (n // 10000, (n // 100) % 100, n % 100))

def get(path):
    req = urllib.request.Request(API + path, headers={"X-Api-Token": key})
    return json.load(urllib.request.urlopen(req, timeout=60))

gv = get("/game/versions")
ids, hit = [], set()
for v in gv:
    if v.get("name") in wanted:
        ids.append(v["id"]); hit.add(v["name"])
print("Aranan sürümler:", sorted(wanted))
print("CurseForge'da bulunan:", sorted(hit))
if not ids:
    sys.exit("hiçbir oyun sürümü eşleşmedi; yükleme yapılmadı")

notes = "SURUM_NOTU.txt"
change = open(notes, encoding="utf-8").read().strip() if os.path.exists(notes) else "Sürüm %s. Ayrıntılar için GitHub sayfasına bakın." % ver
out = "WoWTurkce-v%s.zip" % ver
import shutil; shutil.copyfile(src, out)
meta = {"changelog": change, "changelogType": "markdown", "displayName": "WoWTürkçe v%s" % ver,
        "gameVersions": ids, "releaseType": "release"}
r = subprocess.run(["curl", "-sS", "-w", "\n%{http_code}", "-H", "X-Api-Token: " + key,
                    "-F", "metadata=" + json.dumps(meta, ensure_ascii=False) + ";type=application/json",
                    "-F", "file=@" + out, API + "/projects/%s/upload-file" % pid],
                   capture_output=True, text=True)
body, code = r.stdout.rsplit("\n", 1)
print("CurseForge yanıtı:", code, body[:300])
if not code.startswith("2"):
    sys.exit("yükleme başarısız")
