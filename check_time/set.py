import pandas as pd
import time

#처음 제한시간 설정
df=pd.DataFrame([[0,120],
                 [0,60],
                 [0,30]],
               index=['user1','user2','user3'],
                columns=['사용시간(분)','제한시간(분)'])

#파일로 저장
df.to_csv('C:/Users/Agwoo/Desktop/새 폴더/test2.csv',header='False',encoding='utf-8-sig')
