import requests
from bs4 import BeautifulSoup

# 기상청 날씨 예보 페이지 URL (서울 기준)
url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"

# 헤더 추가 - User-Agent 설정
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

# 날씨 데이터를 추출할 수 있는 CSS 선택자
weather_data = soup.select('table > tbody > tr')

# 날씨 정보 출력
if not weather_data:
    print("❌ 데이터를 찾을 수 없습니다. CSS 선택자를 확인하세요!")
else:
    print("\n🔥 기상청 날씨 예보 🔥\n")
    for i, row in enumerate(weather_data[:10]):  # 상위 10개 지역 날씨 가져오기
        try:
            station = row.select_one("td:nth-of-type(1)").get_text(strip=True)  # 지역
            temp = row.select_one("td:nth-of-type(3)").get_text(strip=True)  # 기온
            humidity = row.select_one("td:nth-of-type(5)").get_text(strip=True)  # 습도
            wind_speed = row.select_one("td:nth-of-type(7)").get_text(strip=True)  # 풍속

            print(f"{station} | 기온: {temp}°C | 습도: {humidity}% | 풍속: {wind_speed}m/s")
        except Exception as e:
            print(f"Error: {e}")
            continue  # 오류 발생 시 건너뜀
        