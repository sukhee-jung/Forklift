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
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        
        # 메시지 제목 설정
        header = f"📢 *『김포 EHS 공지』*\n\n"
            
        notice_msg = (
            f"안녕하세요? 김포 클러스터 구성원 여러분!\n안전한 사업장 만들기를 위한 안전작업수칙을 안내드립니다.\n\n"
            f"감사합니다.\n"
            f"*첨부 : <https://static.wixstatic.com/media/70b014_af73a48c252a4a019d141818de2fe736~mv2.png|안전작업수칙>*\n"
        )

        # 메시지 본문
        body = header + notice_msg
    
        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
