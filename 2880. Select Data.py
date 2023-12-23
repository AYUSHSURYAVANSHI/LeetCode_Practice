<<<<<<< HEAD
import pandas as pd

def selectData(df: pd.DataFrame) -> pd.DataFrame:
=======
import pandas as pd

def selectData(df: pd.DataFrame) -> pd.DataFrame:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
  return df[df['student_id'] == 101] [['name','age']]