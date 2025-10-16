# src/order_service.py
from dataclasses import dataclass
from typing import Dict, List, Union, TypedDict, Optional

class OrderDict(TypedDict):
    id: int
    amount: int
    priority: bool


@dataclass
class ProcessedOrder:
    id: int
    status: str
    priority: bool = False


def handle_orders(
    data: Union[List[OrderDict], None],
) -> List[ProcessedOrder]:
    results: List[ProcessedOrder] = []
    if data is not None:
        for datum in data: 
            if datum.get("amount") is None or datum.get("amount") <= 0:
                results.append(ProcessedOrder(id=datum.get("id"), status="error"))
                continue
            
            results.append(ProcessedOrder(id=datum.get("id"), status="ok",priority=datum.get("priority")))

        results.sort(key=lambda p: p.priority, reverse=True)
    return results


def process_data(items):
    return handle_orders(items)
