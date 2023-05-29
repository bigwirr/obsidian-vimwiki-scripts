== ABOUT ==

This script (fix-links.py) changes obsidian links for their short format:
    [[foo]] or [[foo|bar]]

to the format that vimwiki expects:
    [[../dir/foo|foo]] or [[../dir/foo|bar]]

It maintains the same link display text, so your markdown files should "look" the same.

This script only operates on ".md" files.


== DISCLAIMER  ==

BACKUP your obsidian vault first!!!!
This script is provided with no warranty or expectation that it will work, besides "idk bro it worked on my machine".
If you don't back up your stuff and you run this script, don't complain to me about it.


== USAGE ==
Use python 3 to run fix-links.py with the current working directory being the root directory of your Obsidian vault.

THIS SCRIPT WILL OPERATE ON ALL .md FILES WITHIN THAT DIRECTORY AND ALL NESTED DIRECTORIES.


