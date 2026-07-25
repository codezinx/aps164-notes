import re
import os

def replace_obsidian_images_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace ![alt|width](path) → <img src="path" alt="alt" width="width">
    pattern = r'!\[([^\|\]]+)\|(\d+)\]\(([^)]+)\)'
    replaced = re.sub(pattern, r'<img src="\3" alt="\1" width="\2">', content)

    # Only write if something changed
    if content != replaced:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(replaced)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith('.md'):
                file_path = os.path.join(root, filename)
                replace_obsidian_images_in_file(file_path)

if __name__ == '__main__':
    import sys
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    process_directory(target_dir)
