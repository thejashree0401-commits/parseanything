from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any


class BlockType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST = "list"
    TABLE = "table"
    FIGURE = "figure"
    EQUATION = "equation"
    FOOTNOTE = "footnote"
    HEADER = "header"
    FOOTER = "footer"
    SIDEBAR = "sidebar"


@dataclass
class Cell:
    text: str
    row_idx: int
    col_idx: int
    rowspan: int = 1
    colspan: int = 1
    is_header: bool = False


@dataclass
class Block:
    type: BlockType
    cells: Optional[List[Cell]] = None
    markdown: str = ""
    bbox: Optional[List[float]] = None  # [x0, y0, x1, y1]
    confidence: float = 1.0
    needs_review: bool = False
    page: int = 1
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ErrorInfo:
    error_code: str
    message: str


@dataclass
class Document:
    blocks: List[Block]
    error: Optional[ErrorInfo] = None
