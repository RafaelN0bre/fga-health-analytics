import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()
df_global = pd.read_excel(DATA_PATH.joinpath("covid_global_trans.xlsx"))

new_end_date_df1 = df_global[df_global.date == '22/08/2020']


df_global_top3 = new_end_date_df1.values.tolist()


count = 0
aux = []
for i in range(len(df_global_top3)):
    df_global_top3[i] = [df_global_top3[i][2], df_global_top3[i][6]]
    #(df_global_top3[i][2], df_global_top3[i][6])
