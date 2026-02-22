import os
from typing import List

def load_txt_folder(folder_path: str) -> List[str]:
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents