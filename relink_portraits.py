"""
Rebuilds interface/TAD_commander_portraits.gfx.

Run it from the root of the mod folder:   python TOOLS/relink_portraits.py

For every character it looks for gfx/leaders/<TAG>/Portrait_<KEY>.dds (and _small.dds).
If the file exists it is used; if not, the sprite falls back to the shared placeholder.
So: drop your own art in with the right filename, run this, done.
"""
import os, re, glob

PH_L = "gfx/leaders/TAD/Portrait_TAD_placeholder.dds"
PH_S = "gfx/leaders/TAD/Portrait_TAD_placeholder_small.dds"

rows = []
for f in glob.glob("common/characters/TAD_*.txt"):
    tag = os.path.basename(f).split("_")[1]
    text = open(f, encoding="utf-8", errors="ignore").read()
    for ck in re.findall(r"\n\t(\w+) = \{", text):
        rows.append((tag, ck))

out = ["spriteTypes = {", ""]
custom = 0
for tag, ck in sorted(set(rows)):
    large = f"gfx/leaders/{tag}/Portrait_{ck}.dds"
    small = f"gfx/leaders/{tag}/Portrait_{ck}_small.dds"
    if not os.path.exists(large): large = PH_L
    else: custom += 1
    if not os.path.exists(small): small = PH_S
    else: custom += 1
    for name, path in ((f"GFX_Portrait_{ck}", large), (f"GFX_Portrait_{ck}_small", small)):
        out += ["\tspriteType = {", f'\t\tname = "{name}"', f'\t\ttexturefile = "{path}"', "\t}", ""]
out += ["}", ""]

open("interface/TAD_commander_portraits.gfx", "w", encoding="utf-8").write("\n".join(out))
print(f"{len(set(rows))} characters, {custom} custom portrait files found, rest on the placeholder.")
