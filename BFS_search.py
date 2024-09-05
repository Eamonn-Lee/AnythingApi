import json
from anytree import Node, RenderTree
from collections import deque

def page_search(data, keyword):
    queue = deque([("", data)]) #root
    while queue:
        path, current_node = queue.popleft()
        if isinstance(current_node, dict):

            for key, value in current_node.items():
                new_path = f"{path}/{key}".strip("/")
                if search(key, keyword):
                    return new_path, value
                queue.append((new_path, value))
        else:
            # If it's not a dictionary, it's a leaf node
            continue
    return None

def search(target, keyword):
    if keyword.lower() in target.lower():
        return True
    return False

def find(json_data, keyword):
    data = json.loads(json_data)

    result = page_search(data, keyword)

    if result:
        print(result)
    else:
        print("Keyword '{}' not found.".format(keyword))
