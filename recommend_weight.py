import pandas as pd


array = [[0]*17 for i in range(17)]

a=pd.DataFrame(array)


df=pd.read_csv('color.csv')

print(df)
print('------------------------------------------------------')
a[0][2]=3
a.to_csv('./test.csv',index=False)
a=pd.read_csv('test.csv')

print('------------------------------------------------------')
print(a)
df= df+ a
print('------------------------------------------------------')

print(df)