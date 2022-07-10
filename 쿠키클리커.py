# cls & python "쿠키클리커.py"

import pyautogui
from time import sleep
import keyboard


isPlaySound = True

def play():
    global isPlaySound

    while isPlaySound:
        # 뉴스피커 클릭
        pyautogui.click(x=1458, y=160)
        if keyboard.is_pressed('q'):
            break

        # # 주름벌레 터트리기
        # pyautogui.click(x=516, y=1322)
        # if keyboard.is_pressed('q'):
        #     break
        # # 전환 분노쿠키 안 나오는 거 클릭
        # pyautogui.click(x=2267, y=276)
        # if keyboard.is_pressed('q'):
        #     break
        # 모든 업그레이드 구매 # 스위치 탭 켜져있는 상태
        pyautogui.click(x=2306, y=438)
        if keyboard.is_pressed('q'):
            break
        # 빌딩 구매 # 스위치 탭 켜져있는 상태
        pyautogui.click(x=2513, y=597)
        if keyboard.is_pressed('q'):
            break

        # 용 쓰다듬기
        pyautogui.click(x=235, y=1224)
        if keyboard.is_pressed('q'):
            break

        # # 마법 쓰기.
        # pyautogui.click(x=1314, y=348)
        # if keyboard.is_pressed('q'):
        #     break

        # # 상점 구매
        # pyautogui.click(x=2314, y=194)
        # if keyboard.is_pressed('q'):
        #     break

        # pyautogui.click(x=2307, y=243)
        # if keyboard.is_pressed('q'):
        #     break

        # pyautogui.click(x=2320, y=193)
        # if keyboard.is_pressed('q'):
        #     break

        # pyautogui.click(x=2414, y=192)
        # if keyboard.is_pressed('q'):
        #     break

        # pyautogui.click(x=2323, y=286)
        # if keyboard.is_pressed('q'):
        #     break

        # pyautogui.click(x=2437, y=192)
        # if keyboard.is_pressed('q'):
        #     break

        # ! # 황금쿠키
        # pyautogui.click(x=114, y=89)
        # if keyboard.is_pressed('q'):
        #     break

def position():
    print(pyautogui.position())

print("q - 종료")
print("w - 루프 상점 3줄")
print("e - 포지션")

keyboard.add_hotkey('w', play)
keyboard.add_hotkey('e', position)
keyboard.wait('ctrl+shift+b')