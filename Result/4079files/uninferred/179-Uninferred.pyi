import pandas as pd
from typing import Any, Optional

def one_hot_encoder(dictionary_of_Dictionaries: dict) -> pd.DataFrame: ...
def get_ICD9_descriptions(filename: Optional[Any] = ...) -> None: ...
def Rollup_ICD9_Code(IDC9_Code: str) -> str: ...
def ICD9_One_HotEncoded(Location_of_the_CSV_Files: str = ..., print_details: bool = ...): ...