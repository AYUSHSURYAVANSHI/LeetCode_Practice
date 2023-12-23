<<<<<<< HEAD
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
=======
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
    return customers.drop_duplicates(subset = ['email'])