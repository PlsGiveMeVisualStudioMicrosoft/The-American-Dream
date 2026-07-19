from pathlib import Path
import re

# Folder containing your state files
FOLDER = r"C:\Users\User\Documents\Paradox Interactive\Hearts of Iron IV\mod\TheAmericanDream\history\states"

for file in Path(FOLDER).glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    # Replace owner with USA
    text = re.sub(
        r'(^\s*owner\s*=\s*)[A-Z0-9_]+',
        r'\1USA',
        text,
        flags=re.MULTILINE
    )

    # Add USA as an additional core after every existing add_core_of
    text = re.sub(
        r'(^\s*add_core_of\s*=\s*[A-Z0-9_]+\s*$)',
        r'\1\n\t\tadd_core_of = USA',
        text,
        flags=re.MULTILINE
    )

    file.write_text(text, encoding="utf-8")

print("Done!")