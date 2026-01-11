import os
import re

base_dir = r"c:\Users\WELCOME\Documents\New folder (5)"

folders = [
    "AnaluseCampaign",
    "Connectors",
    "DashboardAttribution",
    "DashboardPaid",
    "DashboardPaidCampaigns",
    "Overview"
]

# Mapping of labels to target folder index.html
links = {
    "Home": "../index.html",
    "Overview": "../Overview/index.html",
    "Connectors": "../Connectors/index.html",
    "Paid": "../DashboardPaid/index.html",
    "Campaign": "../DashboardPaidCampaigns/index.html",
    "Attribution": "../DashboardAttribution/index.html"
}

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update sidebar items
    for label, target in links.items():
        # Match <div class="sidebar-items"> or <div class="group-1000005703"> (Home is often in a different class)
        # Home in Overview/index.html is <div class="group-1000005703">...<div class="home">Home</div>...</div>
        
        if label == "Home":
            # Home is unique: <div class="link">...<div class="group-1000005703">...<div class="home">Home</div>...</div>...</div>
            # We want to wrap the inner group or the outer link.
            pattern = re.compile(r'(<div class="group-1000005703">.*?<div class="home">Home</div>.*?</div>)', re.DOTALL)
            matches = pattern.findall(content)
            for match in matches:
                new_block = match.replace('<div class="group-1000005703">', f'<a href="{target}" class="group-1000005703" style="display: flex; text-decoration: none;">')
                if new_block.rstrip().endswith('</div>'):
                    idx = new_block.rfind('</div>')
                    new_block = new_block[:idx] + '</a>' + new_block[idx+6:]
                content = content.replace(match, new_block)
        else:
            pattern = re.compile(f'(<div class="sidebar-items">.*?<div class="default\d*">{label}</div>.*?</div>)', re.DOTALL)
            matches = pattern.findall(content)
            for match in matches:
                if f'href="{target}"' in match: continue # Already linked
                new_block = match.replace('<div class="sidebar-items">', f'<a href="{target}" class="sidebar-items" style="display: block;">')
                if new_block.rstrip().endswith('</div>'):
                    idx = new_block.rfind('</div>')
                    new_block = new_block[:idx] + '</a>' + new_block[idx+6:]
                content = content.replace(match, new_block)

    # Specific fix for "Analyse Campaign" button in DashboardAttribution
    pattern_btn = re.compile(r'(<div class="master-secondary-button3">.*?<div class="button-text">Analyse Campaign</div>.*?</div>)', re.DOTALL)
    matches_btn = pattern_btn.findall(content)
    for match in matches_btn:
        if 'href=' in match: continue
        new_block = match.replace('<div class="master-secondary-button3">', '<a href="../AnaluseCampaign/index.html" class="master-secondary-button3" style="display: block; text-decoration: none;">')
        if new_block.rstrip().endswith('</div>'):
            idx = new_block.rfind('</div>')
            new_block = new_block[:idx] + '</a>' + new_block[idx+6:]
        content = content.replace(match, new_block)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".html"):
                print(f"Updating {folder}/{file}...")
                update_file(os.path.join(folder_path, file))

print("Done!")
