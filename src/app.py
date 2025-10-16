# src/app.py
import json
from pathlib import Path
from .order_service import process_data

def main():
    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_orders.json"
    if sample_path.exists():
        try:
            items = json.loads(sample_path.read_text())
        except json.decoder.JSONDecodeError:
            print("The json is invalid")
            items = [{"id": 1, "amount": 100, "priority": False},
                 {"id": 2, "amount": 50, "priority": True},
                 {"id": 3, "amount": 0}]

    else:
        items = [{"id": 1, "amount": 100, "priority": False},
                 {"id": 2, "amount": 50, "priority": True},
                 {"id": 3, "amount": 0}]

    result = process_data(items)
    convert_result = [datum.__dict__ for datum in result]
    
    print(json.dumps(convert_result, indent=2))

if __name__ == "__main__":
    main()
