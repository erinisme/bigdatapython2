import requests
from bs4 import BeautifulSoup
import random
import time
import csv

def m000(a, c):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        for index, song in enumerate(songs):
            if index >= c:
                break
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요 | 상태 코드: {response.status_code}]')

def m100(a): m000(a, 100)
def m50(a): m000(a, 50)
def m10(a): m000(a, 10)

def m_random(d):
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print("[두구두구둥...]")

    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        song_list = []

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))

        random_song = random.choice(song_list)
        time.sleep(1)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')

def m_search(artist_name):
    print(f"[{artist_name}님의 노래를 찾아볼게요!]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        found = False

        for song in songs:
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            if artist_name.lower() in artist.lower():
                found = True
                rank = song.select_one('span.rank').text.strip()
                print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

        if not found:
            print("[해당 가수의 노래는 현재 차트에 없어요.]")
    else:
        print(f"[검색 실패 | 상태 코드: {response.status_code}]")

def m_save(filename):
    print(f"[멜론 TOP100 데이터를 '{filename}'으로 저장 중...]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['순위', '제목', '아티스트'])

            for song in songs:
                rank = song.select_one('span.rank').text.strip()
                title = song.select_one('div.ellipsis.rank01 a').text.strip()
                artist = song.select_one('div.ellipsis.rank02 a').text.strip()
                writer.writerow([rank, title, artist])

        print("[저장 완료!]")
    else:
        print(f"[저장 실패 | 상태 코드: {response.status_code}]")
