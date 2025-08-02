import re

def parse_prompt(prompt):
    prompt = prompt.lower()
    components = []

    if "login" in prompt:
        components.extend([
            "label:Name", "entry:Name",
            "label:Password", "entry:Password",
            "button:Login"
        ])

    elif "menu" in prompt:
        item_count = re.search(r'(\d+)-item menu', prompt)
        count = int(item_count.group(1)) if item_count else 3
        for i in range(1, count + 1):
            components.append(f"label:Item {i}")
            components.append(f"entry:Item {i}")
        components.append("button:Calculate Total")
        components.append("label:Total")

    elif "contact card" in prompt:
        components.extend([
            "label:Name", "entry:Name",
            "label:Phone", "entry:Phone",
            "label:Email", "entry:Email",
            "button:Save Contact"
        ])

    return components
