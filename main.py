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
            f"*첨부:일: - <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_535ab3cc9a594f068a41b6d49fa98872.xlsx%7C셔틀 노선도>*\n"
        )

        # 메시지 본문
        body = header + notice_msg
    
        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
