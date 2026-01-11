import os
import re

root_dir = r"c:\Users\WELCOME\Documents\New folder (5)"
source_file = os.path.join(root_dir, "Overview", "index.html")
target_file = os.path.join(root_dir, "index.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Adjust CSS paths
content = content.replace('href="./vars.css"', 'href="./Overview/vars.css"')
content = content.replace('href="./style.css"', 'href="./Overview/style.css"')

# Adjust Image paths (src="...")
# Most images are in the Overview folder for this page
content = re.sub(r'src="([^"/]+)"', r'src="./Overview/\1"', content)

# Adjust Sidebar links
# Our previous script added links like ../Overview/index.html
# In the root index.html, these should be ./Overview/index.html
content = content.replace('href="../', 'href="./')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created root index.html based on Overview/index.html with adjusted paths.")
