import json
from pathlib import Path



def main():
    for p in Path("./").glob("*.json"):
        with p.open("r") as f:
            data = json.load(f)

            assert "key" in data, "json metadata must have \"key\" key"
            assert data["key"] == "value", "wrong value"

    print("All tests passed")

if __name__ == "__main__":
    main()
