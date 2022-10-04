import pandas as pd

def Add(x):
    df=pd.read_csv('color.csv')
    x=pd.DataFrame(x)
    x.to_csv('./test.csv',index=False)
    x=pd.read_csv('test.csv')
    df= df+ x
    df.to_csv('./color.csv',index=False)
    return df

if __name__=='__main__':
    x=[[0]*17 for i in range(17)]
    x[0][3]=3
    Add(x)
