
import requests
import pytz
from datetime import datetime

class CNotiSender:
    
    def __init__(self):
        self.m_Token = "7979531835:AAGiJuuOOvzeO_-qbaZt39S45KPmq8Tr6hA"
        self.m_Chat_Id = "5354904842"
        self.m_Zone = pytz.timezone("Asia/Ho_Chi_Minh")
    #end init

    def sendMessage(self, msg):
        if msg != '':
            content = f'[{datetime.now(self.m_Zone).strftime("%Y-%m-%d %H:%M:%S")}]\n{msg}'
            reponse = requests.post(
                f"https://api.telegram.org/bot{self.m_Token}/sendMessage", 
                data={"chat_id": self.m_Chat_Id, "text": content}
                )
            status = 'SUCCESS'
            if (reponse.status_code != 200): 
                status = 'FAILED'
            print(f'[SENT][{status}]')
            print(f'{content}')
#end_def