import win32api
import pandas as pd

df=pd.read_csv('파일 경로',index_col=0,engine='python')
time_used=df.loc['user1','사용시간']
time_limit=in_df.loc['user1','제한시간']
remain=time_limit-time_used  #남은 시간

#바로 알림창 띄우기
if remain==10:
    win32api.MessageBox(0, "10분 남았습니다.", "알림", 48)
