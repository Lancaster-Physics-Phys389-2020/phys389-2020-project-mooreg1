import pandas as pd

initial=pd.DataFrame({'Pressure Oxygen':[],'Pressure Nitrogen':[],'Pressure Total':[],'Volume':[],'Number Oxygen':[],'Number Nitrogen':[],'Number Total':[],'Temperature':[]})
initial.to_pickle("Macro_data.csv")