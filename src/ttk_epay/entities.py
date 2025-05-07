from dataclasses import dataclass
from typing import Optional

@dataclass
class Invoice:
    id: int
    invoice_number: Optional[int] = None
    order_id: Optional[str] = None
    invoice_date: Optional[str] = None  # Can be converted to datetime if needed
    invoice_type_code: Optional[str] = None
    net_amount: Optional[float] = None
    invoice_tva: Optional[float] = None
    amount_tva: Optional[float] = None
    amount_ttc: Optional[float] = None
    invoice_state_code: Optional[str] = None
    order_name: Optional[str] = None
    client_code: Optional[int] = None
    client_name: Optional[str] = None
    client_nrc: Optional[str] = None
    client_address: Optional[str] = None
    client_mail: Optional[str] = None
    client_idf: Optional[str] = None
    product_name: Optional[str] = None
    is_paid: bool = False


@dataclass
class InvoiceDto:
    invoice_number: int
    order_id: Optional[str] = None
    invoice_date: Optional[str] = None  # Can also be datetime
    invoice_type_code: Optional[str] = None
    net_amount: Optional[float] = None
    client_code: Optional[int] = None
    client_name: Optional[str] = None
    client_address: Optional[str] = None
    client_mail: Optional[str] = None
    product_name: Optional[str] = None
