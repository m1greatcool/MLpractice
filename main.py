import pandas
data = pandas.read_csv('datasets/titanic-machine-learning-from-disaster/train.csv',index_col = 'PassengerId')

print(data['Sex'].value_counts())

print(data['Survived'].value_counts()[1]/(data['Survived'].value_counts()[0]+ data['Survived'].value_counts()[1]))

classes = sum(data['Pclass'].value_counts())

print(data['Pclass'].value_counts()[1]/classes)

print(data['Parch'].corr(data['SibSp']))

print(data['Age'].mean())

print(data['Age'].median())

NS = data[['Name','Sex']]

femInd = [i for i in range(1,891) if (NS.Sex[i] == 'female')]

FemaleNames = []

for i in range(len(femInd)):
    if '(' in NS.Name[femInd[i]]:
        BraInd = NS.Name[femInd[i]].find('(')
        SpaInd = NS.Name[femInd[i]][BraInd:].find(' ')
        if SpaInd == -1:
            SpaInd = NS.Name[femInd[i]][BraInd:].find(')')
        FemaleNames.append(NS.Name[femInd[i]][BraInd+1:BraInd + SpaInd])
    else:
        MissInd = NS.Name[femInd[i]].find('.')
        SpaInd = NS.Name[femInd[i]][MissInd:].rsplit(' ')
        FemaleNames.append(SpaInd[1])

#print(FemaleNames.__contains__('"Mary"'))
print(set(FemaleNames))
print(max(set(FemaleNames),key=FemaleNames.count))