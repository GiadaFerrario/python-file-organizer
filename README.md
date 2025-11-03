# 📁 File Organizer

A simple Python script that **organizes files into subfolders** based on their **file extensions**.  
Built only with standard libraries — `os`, `shutil`, `argparse`, and `pathlib`.

---

## ⚙️ Features

- Automatically sorts files into subfolders by extension  
  (e.g., `photo.jpg` → `jpg/photo.jpg`)  
- Creates missing subfolders automatically  
- Handles filename conflicts gracefully (`file_1.txt`, `file_2.txt`, etc.)  
- Includes a **dry-run mode** to preview changes without moving files  

---

## 🧩 Requirements

- Python **3.13**
- No external dependencies

---

## 🚀 Usage

```bash
# Run normally (actually moves files)
python organizer.py /path/to/directory

# Dry run mode (simulation only, no changes)
python organizer.py /path/to/directory --dry-run
```

---

## Example

If your directory initially contains:
```bash
photo.jpg
report.pdf
notes.txt
script.py
file (without extention)
```

After running the script the structure will become:
```bash
jpg/photo.jpg
pdf/report.pdf
txt/notes.txt
py/script.py
without_extention/file
```


