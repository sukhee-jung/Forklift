import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()

SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        
        # 메시지 제목 설정
        header = f"📢 *『김포 EHS 공지』*\n\n"
            
        notice_msg = (
            f"안녕하세요? 김포 클러스터 지게차 운전원 여러분!\n안전한 사업장 만들기를 위한 *지게차 안전작업수칙* 을 안내드립니다.\n\n"
            f"1️⃣  지게차 운행 전 포크가 상향되어 있지 않은지 확인해주세요.\n"        
            f"2️⃣  단독작업 시 유도자를 배치하여 주변 통제를 해주세요.\n"  
            f"3️⃣  핸드폰, 이어폰 등 운행 중에는 전자기기 사용을 금해주세요.\n" 
            f"4️⃣  지게차 운전원 개인별 지급된 PIN번호는 공유를 금해주세요.\n\n" 
            f"감사합니다.\n\n"
            f"*<https://static.wixstatic.com/media/70b014_0c1447fb020741ba825db0ef31685c52~mv2.png|지게차 운전원 안전작업수칙>*\n"
        )

        # 메시지 본문
        body = header + notice_msg
    
        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
