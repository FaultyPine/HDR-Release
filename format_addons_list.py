import sys
import os

def trim_newlines(string):
    return string.strip("\n")

def add_new_list_entry(master_lines, version, description, author, name, is_last_line): # " :: " + trim_newlines(author)
    if is_last_line:
        newline = trim_newlines(name) + " :: " + trim_newlines(version) + " :: " + trim_newlines(author) + " :: " + trim_newlines(description)
    else:
        newline = trim_newlines(name) + " :: " + trim_newlines(version) + " :: " + trim_newlines(author) + " :: " + trim_newlines(description) + "\n"
    master_lines.append(newline)


def address_hdr_base(master_lines):
    f = open("HDR-Base/ultimate/mods/HDR-Base/info.ini", "r")
    info_lines = f.readlines()
    f.close()

    for line in info_lines:
        if "version=" in line:
            hdr_base_version = line[line.find("=")+1 : ]
            print("HDR base version: " + hdr_base_version)
        elif "description=" in line:
            hdr_base_description = line[line.find("=")+1 : ]
            print("HDR base description: " + hdr_base_description)
        elif "author=" in line:
            hdr_base_author = line[line.find("=")+1 : ]
            print("HDR base author: " + hdr_base_author)

    add_new_list_entry(master_lines, hdr_base_version, hdr_base_description, hdr_base_author,  "HDR-Base", False)





def address_hdr_addons(master_lines):
    listdir = os.listdir("HDR-Addons")
    for entry_num in range(len(listdir)):
        entry = listdir[entry_num]
        f = open("HDR-Addons/" + entry + "/ultimate/mods/" + entry + "/info.ini")
        info_lines = f.readlines()
        f.close()
        for line in info_lines:
            if "version=" in line:
                entry_version = line[line.find("=")+1 : ]
                print(entry + " version: " + entry_version)
            elif "description=" in line:
                entry_description = line[line.find("=")+1 : ]
                print(entry + " description: " + entry_description)
            elif "author=" in line:
                entry_author = line[line.find("=")+1 : ]
                print(entry + " author: " + entry_author)
        if entry_num == len(listdir)-1:
            add_new_list_entry(master_lines, entry_version, entry_description, entry_author, entry, True)
        else:
            add_new_list_entry(master_lines, entry_version, entry_description, entry_author, entry, False)


def main():
    file = open("HDR-Addons-List.txt", "w+")
    lines = file.readlines()
    address_hdr_base(lines)
    address_hdr_addons(lines)
    file.writelines(lines)
    file.close()

main()