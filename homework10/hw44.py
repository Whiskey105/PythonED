import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print('------------------------------------------------')
print(data)

different_values = data['whoAmI'].unique()

one_hot = pd.DataFrame()

for value in different_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

one_hot.head()
print('------------------------------------------------')
print(one_hot)