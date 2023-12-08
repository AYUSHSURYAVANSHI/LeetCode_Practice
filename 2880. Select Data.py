import pandas as pd

def selectData(df: pd.DataFrame) -> pd.DataFrame:
  return df[df['student_id'] == 101] [['name','age']]