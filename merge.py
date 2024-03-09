import pandas as pd

final_planet_df = pd.read_csv('/Applications/Coding Classes/Python/Homework Projects/H129/final_data.csv')

final_planet_df.head()

final_planet_df.drop(columns=['Unnamed: 0'], inplace=True)
final_planet_df.head()

final_planet_df.shape

final_planet_df.head()

final_planet_df.tail()