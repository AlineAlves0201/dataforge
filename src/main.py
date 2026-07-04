from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_FILE = RAW_DATA_DIR / "user_profile.json"


def ask_user_profile() -> dict[str, int | str]:
    name = input("Digite seu nome: ").strip()
    age = int(input("Digite sua idade: ").strip())

    return {
        "name": name,
        "age": age,
        "estimated_days_lived": age * 365,
    }


def save_json(data: dict[str, int | str], output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    profile = ask_user_profile()
    save_json(profile, OUTPUT_FILE)
    print(f"Arquivo salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

