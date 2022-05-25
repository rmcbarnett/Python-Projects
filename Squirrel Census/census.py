# The great squirrel census of Central Park.. I used the data to create a pandas df and figure out how many of each type pf critter there are.. 


import pandas


data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_counts = data['Primary Fur Color'].value_counts()
print(type(fur_counts))
print(fur_counts)

FurColor = []
Color_Count = []

for index, value in fur_counts.items():
    print(f"Index : {index}, Value : {value}")
    FurColor.append(index)
    Color_Count.append(value)

new_data = {'Fur Color':FurColor,'Count':Color_Count}

# Create DataFrame
df = pandas.DataFrame(new_data)
print(df)

df.to_csv('./new_data.csv')
