import os, re
from datetime import datetime

README_PATH = os.path.join(".", "README.md")
AUTHOR = "HaallooBim" 

def getCurrentWriteUp():
    ListWriteUp = [
        d for d in os.listdir(".") if os.path.isdir(d) and (d).lower().endswith("-cyberdefender-wu")
    ]
    return sorted(ListWriteUp, key=lambda d: os.path.getmtime(d), reverse=True)

def extractWriteUpDetail(WriteUpDir):
    with open(os.path.join(WriteUpDir, "README.md"), "r") as f:
        content = f.read()
        title = re.search(r"# \[ WriteUp \] \[(.*?)\]", content).group(1)
        difficulty = re.search(r"2. Difficulty\: (.*)", content).group(1)
        return title, difficulty
    
def updateReadme():
    header = """# Cyber Defender Blue Team Labs WriteUp

## Author: {AUTHOR}

## Description
This repository contains Write-Ups for various Cyber Defender Blue Team Labs. Most of the collection primarily discuss on free labs. Please feel free to explore my write up ^^

## Write Up List

| Lab Name | Difficulty | Writeup Link | Last Modified |
| -------- | ------------ | ------------ | ------------- |
"""
    rows = []
    for writeup in getCurrentWriteUp():
        WRITEUP_PATH = os.path.join(".", writeup)
        last_modified = datetime.fromtimestamp(os.path.getmtime(WRITEUP_PATH)).strftime("%Y-%m-%d %H:%M:%S")
        title, difficulty = extractWriteUpDetail(writeup)
        rows.append(f"| {title} | {difficulty} | [here]({WRITEUP_PATH}) | {last_modified} |")
        # print(f"| {title} | {difficulty} | [here]({WRITEUP_PATH}) | {last_modified} |")
    
    # print(header + "\n".join(rows) + "\n")
    with open(README_PATH, "w") as f:   
        f.write(header + "\n".join(rows) + "\n")   

updateReadme()