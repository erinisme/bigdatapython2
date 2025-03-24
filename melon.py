import requests
from bs4 import BeautifulSoup

# 멜론 차트 페이지 URL
url = "https://www.melon.com/chart/index.htm"

# 헤더 추가 - User-Agent 설정 (웹 브라우저처럼 보이게 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# 페이지가 정상적으로 로드되었는지 확인
if response.status_code != 200:
    print(f"❌ 페이지 로드 실패: {response.status_code}")
else:
    print("✅ 페이지 로드 성공!")

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 멜론 차트 순위 데이터를 추출할 수 있는 CSS 선택자 (예시)
song_elements = soup.select('table > tbody > tr')

# 순위 출력
if not song_elements:
    print("❌ 데이터를 찾을 수 없습니다. CSS 선택자를 확인하세요!")
else:
    print("\n🔥 멜론 100위 차트 🔥\n")
    for i, song in enumerate(song_elements[:100]):  # 상위 100곡 가져오기
        try:
            rank = song.select_one('span.rank').get_text(strip=True)  # 순위
            title = song.select_one('div.ellipsis.rank01 a').get_text(strip=True)  # 곡 제목
            artist = song.select_one('div.ellipsis.rank02 a').get_text(strip=True)  # 아티스트

            print(f"{rank}위 | {title} - {artist}")
        except Exception as e:
            print(f"Error: {e}")
            continue  # 오류 발생 시 건너뜀
        