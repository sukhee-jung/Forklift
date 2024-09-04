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
        header = f"📢 *『인사총무팀 공지』* @channel\n\n"
            
        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분\n건강하고 안전한 우리 클러스터를 만들기 위해 아래와 같이 구성원 여러분들의 몇가지 협조를 요청 드리오니 꼭 협조 바랍니다!\n\n"
            f"✔ 수도 동파 및 온도 저하 우려로 출입문과 오버헤드도어 는 *꼭 사용 후 폐쇄* 바랍니다.\n"
            f"✔ 냉기 유출로 인한 상품 변질 등 우려로 냉장 / 냉동 방열도어 (챔버) 는 *꼭 사용 후 폐쇄* 바랍니다.\n"
            f"✔ 1번 / 7번 게이트 외부 (도로) <-> 복도 출입문 은 *꼭 사용 후 폐쇄* 바랍니다.\n"
            f"✔ 전열기구는 관리실에서 확인 후 사용, 그 외 *비인가 전열기구는 사용 금지* 바랍니다.\n"
            f"✔ 각 층 사무실,휴게공간 미 사용 콘센트, 냉난방기기 (에어컨 등) 는 *미 사용 시 OFF* 바랍니다.\n"
            f"관련 시설물 이슈 발생 시 *#11_시설안전이슈_평택* 채널 이용 부탁드립니다.\n\n"
            f"감사합니다.\n"
        )

        # 메시지 본문
        body = header + notice_msg
    
        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
