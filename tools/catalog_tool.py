import json 

def load_catalog():
    with open("catalog.json", "r") as f:
        return json.load(f)


def search_catalog(query: str):
    catalog = load_catalog()
    query = query.lower()
    results = []
    for plan in catalog["plans"]:
        if query in plan["name"].lower():
            results.append(plan)
            continue
        for feature in plan["features"]:
            if query in feature.lower():
                results.append(plan)
                break
    return results      