import json

def evaluate_layout(prompt, components):
    score = 0
    prompt = prompt.lower()
    if "login" in prompt and "entry:password" in [c.lower() for c in components]:
        score += 1
    if "total" in prompt and any("label:total" in c.lower() for c in components):
        score += 1
    if "contact card" in prompt and "entry:email" in [c.lower() for c in components]:
        score += 1
    return score

def save_to_log(prompt, components, score, rating=None, filename="data_store.json"):
    data = {
        "prompt": prompt,
        "components": components,
        "score": score,
        "user_rating": rating
    }
    try:
        with open(filename, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(data)

    with open(filename, "w") as f:
        json.dump(history, f, indent=2)

