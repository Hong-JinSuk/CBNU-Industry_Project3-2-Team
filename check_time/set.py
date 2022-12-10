import pandas as pd

#처음 제한시간 설정
df=pd.DataFrame([[0,120],
                 [0,60],
                 [0,30]],
               index=['user1','user2','user3'],
                columns=['사용시간','제한시간'])

#파일로 저장
df.to_csv('파일 경로',header='False',encoding='utf-8-sig')
