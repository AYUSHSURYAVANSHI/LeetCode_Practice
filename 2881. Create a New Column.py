<<<<<<< HEAD
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
=======
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
    return employees.assign(bonus = 2 * employees['salary'])