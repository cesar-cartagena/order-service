# src/order_service.py
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

OrderDict = Dict[str, int]


@dataclass
class ProcessedOrder:
    id: int
    status: str
    priority: bool


PriorityFlag = Optional[str]


def handle_orders(
    data: Union[List[OrderDict], PriorityFlag, None],
) -> Union[List[ProcessedOrder], str]:
    results: List[ProcessedOrder] = []
    for d in data:  # type: ignore[assignment]
        if "amount" not in d or d["amount"] is None or d["amount"] <= 0:
            results.append({"id": d.get("id"), "status": "error"})
            continue

        if d.get("priority") == True:
            results.append({"id": d["id"], "status": "ok", "priority": True})
        else:
            results.append({"id": d["id"], "status": "ok", "priority": False})

    results = sorted(results, key=lambda x: x.get("priority", False))
    return results


def process_data(items):
    return handle_orders(items)
