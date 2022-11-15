# %%
from read_csv import read_csv
data = read_csv('./data.csv')
# print(data[1])
# %%
selection = ['Country/Territory','2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']

def select_data(selected_keys,data):
    new_dict ={}
    new_list = []
    for d in data:
        for sk in selected_keys:
            new_dict[sk[:4]] = d[sk]
        new_list.append(new_dict.copy())
    return new_list

new_data = []
new_data.append(select_data(selection,data))
print(new_data)

# %%
