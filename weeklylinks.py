import os
from datetime import datetime
import random

def get_user_input():
    url = input("Enter the URL: ")
    comment = input("Enter an optional comment (press Enter to skip): ")
    link_text = input("Enter the link text: ")
    return url, comment, link_text

def generate_random_intro():
    intros = [
        "Here are this week's interesting links:",
        "Check out these fascinating links from the past week:",
        "Dive into this week's curated collection of links:",
        "Explore the following intriguing links I've gathered:",
        "This week's roundup of captivating links awaits you:"
    ]
    return random.choice(intros)

def generate_random_goodbye():
    goodbyes = [
        "See you next time!",
        "Until next week, happy reading!",
        "Enjoy exploring these links!",
        "That's all for now. Stay curious!",
        "Looking forward to sharing more next week!"
    ]
    return random.choice(goodbyes)

def format_content(links):
    now = datetime.now()
    date_text = now.strftime("%B %d, %Y")
    date_format = now.strftime("%Y-%m-%d")
    
    content = f"""---
title: "Weekly Links for {date_text}"
date: {date_format}
draft: false
ShowToc: false
cover:
    image: "/link-cover.jpg"
    relative: true
tags: ["weekly links"]
params:
    description: "Paris Buttfield-Addison's weekly interesting links for {date_text}."
images:
 - "/link-cover.jpg"
title: "Paris Buttfield-Addison's weekly interesting links for {date_text}."
images:
 - "/link-cover.jpg"
---
{generate_random_intro()}

"""
    
    for link in links:
        url, comment, link_text = link
        if comment:
            content += f"* {comment}: [{link_text}]({url})\n"
        else:
            content += f"* [{link_text}]({url})\n"
    
    content += f"\n{generate_random_goodbye()}"
    return content

def save_to_file(content):
    now = datetime.now()
    filename = now.strftime("%m%d%Y.md")
    folder_path = os.path.join("content", "posts", "weekly-links")
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, "w") as f:
        f.write(content)
    
    print(f"File saved: {file_path}")

def main():
    links = []
    while True:
        url, comment, link_text = get_user_input()
        links.append((url, comment, link_text))
        
        another = input("Do you want to add another link? (y/n): ").lower()
        if another != 'y':
            break
    
    content = format_content(links)
    save_to_file(content)

if __name__ == "__main__":
    main()