from func import m100, m50, m10, m_random, m_search, m_save

print("==============================")
print("| 1. 멜론 차트 TOP 100곡     |")
print("| 2. 멜론 차트 TOP 50곡      |")
print("| 3. 멜론 차트 TOP 10곡      |")
print("| 4. 멜론 차트 AI 추천곡     |")
print("| 5. 가수 이름으로 노래 검색 |")
print("| 6. 멜론 차트 CSV 저장      |")
print("==============================")

choice = input("메뉴 번호를 선택하세요: ")

if choice == '1':
    m100("<멜론 차트 TOP 100곡>")
elif choice == '2':
    m50("<멜론 차트 TOP 50곡>")
elif choice == '3':
    m10("<멜론 차트 TOP 10곡>")
elif choice == '4':
    m_random("<AI 추천곡>")
elif choice == '5':
    name = input("검색할 가수 이름을 입력하세요: ")
    m_search(name)
elif choice == '6':
    filename = input("저장할 파일명을 입력하세요 (예: melon_chart.csv): ")
    m_save(filename)
else:
    print("잘못된 선택입니다.")
