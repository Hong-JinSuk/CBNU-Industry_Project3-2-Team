import pandas as pd
import time
from datetime import timedelta

def check_time(PID):
    if "게임 중":
        #파일 읽어오기
        in_df=pd.read_csv('파일 경로',index_col=0,engine='python')

        time_used=in_df.loc['user1','사용시간']
        time_limit=in_df.loc['user1','제한시간']

        #사용시간 > 제한시간 이면 게임 강제 종료
        #그 외에 정상적으로 진행
        while True:
            if time_used>time_limit:
                killprocess(PID)
                break

            else:
                start=time.process_time()
                #게임 중

                while True:
                    if "게임 종료":
                        end=time.process_time()
                        break

                t=end-start

                #사용시간 최신화
                time_used+=t
                in_df.loc['user1','사용시간']=timedelta(time_used)

                in_df.to_csv('파일 경로',header='False',encoding='utf-8-sig')
