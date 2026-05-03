from pathlib import Path
from datetime import datetime
import shutil
import json
import csv
import time
import os
from collections import Counter
import string

# =========================
# STUDENT INFO
# =========================
student_id = "TUPM-25-0384"
student_name = "Brylle Edsil F. Untalasco"

print("Setup complete for:", student_name)
print("Student ID:", student_id)

# =========================
# BASE DIRECTORY
# =========================
base_dir = Path.home() / "Documents" / "Activity_5_Files"
base_dir.mkdir(parents=True, exist_ok=True)

# =========================
# LOGGING SYSTEM
# =========================
log_file = base_dir / "file_log.txt"

def log_action(action, filename):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {action} - {filename}\n")

# =========================
# PROCEDURE 1: CREATE FILE
# =========================
intro_file = base_dir / f"intro_{student_id}.txt"

intro_file.write_text(
    f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!\n"
    "Python makes file handling easy!\n"
    "File saved successfully using pathlib."
)

print("\nProcedure 1 completed:", intro_file)
log_action("Create file", intro_file.name)

# =========================
# PROCEDURE 2: READ FILE
# =========================
print("\n--- FILE CONTENT ---")
print(intro_file.read_text())
log_action("Read file", intro_file.name)

# =========================
# PROCEDURE 3: APPEND FILE
# =========================
with intro_file.open("a") as f:
    f.write("\nThis line was added!")

print("\nProcedure 3 completed: Appended.")
log_action("Append file", intro_file.name)

# =========================
# PROCEDURE 4: BACKUP FILE
# =========================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = base_dir / f"intro_{student_id}_backup_{timestamp}.txt"
shutil.copy(intro_file, backup_file)

print("\nBackup created:", backup_file.name)
log_action("Backup file", backup_file.name)

# =========================
# PROCEDURE 5: MULTI-LINE FILE
# =========================
lines_file = base_dir / f"lines_{student_id}.txt"
lines = ["Line 1", "Line 2", "Line 3"]

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print("\nLines file created.")
log_action("Create lines file", lines_file.name)

# =========================
# PROCEDURE 6: READ LINE BY LINE
# =========================
print("\n--- LINE BY LINE ---")
with lines_file.open("r") as f:
    for line in f:
        print(line.strip())

# =========================
# PROCEDURE 7: WORD COUNT
# =========================
text = lines_file.read_text()
word_count = len(text.split())
print("\nWord Count:", word_count)

# =========================
# PROCEDURE 8: COPY FILE
# =========================
copy_file = base_dir / f"intro_copy_{student_id}.txt"
shutil.copy(intro_file, copy_file)
print("\nFile copied.")

# =========================
# PROCEDURE 9: RENAME FILE
# =========================
renamed_file = base_dir / f"intro_renamed_{student_id}.txt"
copy_file.rename(renamed_file)
print("File renamed.")

# =========================
# PROCEDURE 10: DELETE FILE
# =========================
if renamed_file.exists():
    renamed_file.unlink()
    print("File deleted.")

# =========================
# PROCEDURE 11: SUBDIRECTORY
# =========================
data_dir = base_dir / f"data_{student_id}"
data_dir.mkdir(exist_ok=True)
print("\nSubdirectory created.")

# =========================
# PROCEDURE 12: JSON WRITE
# =========================
json_file = data_dir / f"student_{student_id}.json"
data = {
    "name": student_name,
    "id": student_id,
    "course": "BSME-1B"
}

json_file.write_text(json.dumps(data, indent=4))
print("JSON written.")

# =========================
# PROCEDURE 13: JSON READ
# =========================
print("\nJSON:", json.loads(json_file.read_text()))

# =========================
# PROCEDURE 14: CSV WRITE
# =========================
csv_file = base_dir / f"students_{student_id}.csv"

rows = [
    ["Name", "ID", "Score"],
    ["Anna", "2025-1001", 90],
    ["Ben", "2025-1002", 85],
    [student_name, student_id, 95]
]

with csv_file.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("\nCSV created.")

# =========================
# PROCEDURE 15: CSV READ
# =========================
print("\n--- CSV CONTENT ---")
with csv_file.open("r") as f:
    for row in csv.reader(f):
        print(row)

# =========================
# PROCEDURE 16: FILE STATS
# =========================
stat = intro_file.stat()
print("\nSize:", stat.st_size, "bytes")
print("Modified:", time.ctime(stat.st_mtime))

# =========================
# PROCEDURE 17: MERGE FILES
# =========================
merged_file = base_dir / f"merged_{student_id}.txt"

merged_file.write_text(
    intro_file.read_text() + "\n" + lines_file.read_text()
)

print("\nFiles merged.")

# =========================
# PROCEDURE 18: LIST FILES
# =========================
print("\n--- FILE LIST ---")
for f in base_dir.glob("*"):
    print("-", f.name)

# =========================
# PROCEDURE 19: TEXT ANALYSIS (EXTRA - MATCHES CLASSMATE)
# =========================
print("\n--- TEXT ANALYSIS ---")

all_words = []

for file in base_dir.glob("*.txt"):
    content = file.read_text().lower()
    content = content.translate(str.maketrans('', '', string.punctuation))
    words = content.split()
    all_words.extend(words)

stopwords = ["the", "is", "and", "to", "in", "it", "of", "a"]
filtered = [w for w in all_words if w not in stopwords]

counts = Counter(filtered)

print("Top Words:")
for word, count in counts.most_common(5):
    print(word, ":", count)

# =========================
# ERROR HANDLING
# =========================
print("\n--- ERROR HANDLING ---")

try:
    open(base_dir / "missing.txt", "r")
except FileNotFoundError:
    print("Handled missing file safely.")

# =========================
# DONE
# =========================
print("\nActivity 5 COMPLETE.")