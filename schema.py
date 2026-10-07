
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

class BlockType(str, Enum):
    HEADING="heading"; PARAGRAPH="paragraph"; LIST="list"; TABLE="table"
    FIGURE="figure"; EQUATION="equation"; FOOTNOTE="footnote"
    HEADER="header"; FOOTER="footer"; SIDEBAR="sidebar"

class Cell(BaseModel):
    row:int; col:int; rowspan:int=1; colspan:int=1
    text:str=""; is_header:bool=False

class Block(BaseModel):
    id:str
    type:BlockType
    page:int
    bbox:Optional[List[float]]=None   # [x0,y0,x1,y1]
    reading_order:int=0
    text:str=""
    confidence:float=1.0
    needs_review:bool=False
    level:Optional[int]=None          # heading level
    cells:Optional[List[Cell]]=None   # tables
    markdown:Optional[str]=None
    latex:Optional[str]=None          # equations
    chart_data:Optional[dict]=None    # figures
    metadata:dict={}

class ErrorInfo(BaseModel):
    error_code:str
    message:str
    page:Optional[int]=None

class Document(BaseModel):
    doc_id:str
    source_format:str
    page_count:int=0
    blocks:List[Block]=[]
    errors:List[ErrorInfo]=[]
    stats:dict={}
