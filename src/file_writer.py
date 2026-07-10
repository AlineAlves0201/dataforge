import json
from pathlib import Path


def save_json(data: dict, output_path: str) -> None:
    # Convert string path to Path object
    path = Path(output_path)

    # Create parent folders if they do not exist
    path.parent.mkdir(parents=True, exist_ok=True)

    # Save data as a JSON file
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"JSON file saved successfully: {path}")