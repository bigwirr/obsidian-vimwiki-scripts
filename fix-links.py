import os
import re
from pathlib import Path


def fix_all_links(root_dir):
    for dir_, _, files in os.walk(root_dir):
        rel_paths = get_relative_paths(root_dir, dir_)

        for file in files:
            if not file.endswith('.md'):
                continue

            fix_links_in_file(os.path.join(dir_, file), rel_paths)


def fix_links_in_file(file, rel_paths):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        new_lines.append(swap_link(line, rel_paths))

    f = open(file, 'w')
    f.writelines(new_lines)
    f.close()


def swap_link(line, rel_paths):
    return re.sub(r"(\[\[)(.*?[^\|\]]*)(.*?\]\])", lambda input: replace_with_rel(input, rel_paths), line)


def replace_with_rel(input: re.Match, rel_paths):
    key = input.group(2)
    if key not in rel_paths:
        return input.group(0)

    new_path = rel_paths[key]

    # Leave [[foo]] and [[foo|bar]] alone if previous path same as new path
    if new_path == input.group(2):
        return input.group(0)

    # Leave [[foo]] and [[foo|bar]] alone instead of switching to [[./foo|foo]] or [[./foo|bar]]
    if len(new_path) >= 2 and new_path[0:2] == "./" and new_path[2:] == input.group(2):
        return input.group(0)

    # Change [[foo|bar]] to [[new/path/to/foo|bar]]
    if len(input.group(3)) >= 1 and input.group(3)[0] == "|":
        return input.group(1) + new_path + input.group(3)

    # Change [[foo]] to [[new/path/to/foo|foo]]
    return input.group(1) + new_path + "|" + input.group(2) + input.group(3)


def get_relative_paths(root_dir, cur_dir):
    md_files = {}
    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            if file_name.endswith('.md'):
                path = Path(file_name)
                rel_dir = os.path.relpath(dir_, cur_dir)
                rel_file = os.path.join(rel_dir, str(path.with_suffix('')))
                md_files[str(path.with_suffix(''))] = rel_file
    return md_files


def main():
    rootdir = os.getcwd()
    fix_all_links(rootdir)


if __name__ == "__main__":
    main()
