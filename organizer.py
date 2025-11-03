import argparse
from pathlib import Path
import os
import shutil

def organize_directory(path, dry_run):
    if not path.exists() or not path.is_dir():
        print(f"The specified path {path} doesn't exists or is not a directory.")
        return

    for root, _, files in os.walk(path):
        # avoid to go in subdirectories already created
        if Path(root) != path:
            print("qui")
            continue

        for file in files:
            file_path = Path(root) / file
            if not file_path.is_file():
                continue

            ext = file_path.suffix.lower().lstrip(".") or "without_extension"
            dest_dir = path / ext

            if not dest_dir.exists() and not dry_run:
                dest_dir.mkdir()

            dest_path = dest_dir / file_path.name

            # to handle name conflicts
            counter = 1
            while dest_path.exists():
                dest_path = dest_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
                counter += 1

            if dry_run:
                print(f"[DRY RUN] Would move: {file_path} → {dest_path}")
            else:
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved:{file_path.name} to {dest_dir.name}")


def main():
    parser = argparse.ArgumentParser(description="Organize files into subfolders by extension type")
    parser.add_argument("path", help="Directory path to be organised")
    parser.add_argument("--dry-run", action="store_true", help="Simula senza spostare i file")

    args = parser.parse_args()
    organize_directory(Path(args.path).resolve(), dry_run=args.dry_run)

if __name__ == "__main__":
    main()