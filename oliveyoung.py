import requests
from bs4 import BeautifulSoup

# 올리브영 스킨케어 인기 순위 페이지 URL
url = "https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=100000100010001"

# 헤더 추가 - User-Agent를 설정하여 봇이 아니라는 것을 서버에 알림
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

# 인기 순위 제품 리스트 추출 (여기서 정확한 CSS 선택자를 사용해야 합니다)
# 예시: 제품 항목이 'div.product-item'이라고 가정
products = soup.select('div.product-item')

# 제품 순위 출력
if not products:
    print("❌ 데이터를 찾을 수 없습니다. CSS 선택자를 확인하세요!")
else:
    print("\n🔥 올리브영 스킨케어 인기 순위 30위 🔥\n")
    for i, product in enumerate(products[:30]):  # 상위 30개 제품 가져오기
        try:
            name = product.select_one("div.product-name").get_text(strip=True)  # 제품명
            brand = product.select_one("div.product-brand").get_text(strip=True)  # 브랜드명
            price = product.select_one("span.product-price").get_text(strip=True)  # 가격
            link = product.select_one("a")["href"]  # 제품 상세 링크

            print(f"{i+1}위 | {brand} - {name} | 가격: {price}")
            print(f"   ▶ 링크: {link}\n")
        except Exception as e:
            print(f"Error: {e}")
            continue  # 오류 발생 시 건너뜀
