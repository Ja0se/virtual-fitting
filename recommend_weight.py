import pandas as pd

def Add(Up,Bottom):
    up_bottom=[[0]*17 for i in range(17)]
    
    if Up != -1 and Bottom !=-1:
        up_bottom[Up][Bottom]=1
        df1=pd.read_csv('./csv/up_bottom.csv')
        up_bottom=pd.DataFrame(up_bottom)
        up_bottom.to_csv('./csv/test.csv',index=False)
        up_bottom=pd.read_csv('./csv/test.csv')
        df1= df1+ up_bottom
        df1.to_csv('./csv/up_bottom.csv',index=False)
    
    

if __name__=='__main__':
    x=[[0]*17 for i in range(17)]
    Add(x)
    # x=pd.DataFrame(x)
    # x.to_csv('./csv/up_bottom.csv',index=False)
    # x.to_csv('./csv/up_outer.csv',index=False)
    # x.to_csv('./csv/bottom_outer.csv',index=False)
