import pandas as pd
#create table from dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

#filter rows where age > 30
adults = df[df['Age'] > 30]
print(adults)

#calculate average age
average_age = df['Age'].mean()
print(average_age) #output: 30.0

#add new column 'Salary'
df['Salary'] = [70000, 80000, 90000]
print(df)

#save dataframe to csv file
df.to_csv('people.csv', index=False)
print