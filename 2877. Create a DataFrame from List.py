<<<<<<< HEAD
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(
        data = student_data,
        columns = ['student_id','age'],
=======
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(
        data = student_data,
        columns = ['student_id','age'],
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
    )