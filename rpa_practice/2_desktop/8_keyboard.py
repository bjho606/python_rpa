import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]       # 메모장 1개 띄운 상태에서 가져옴
w.activate()

pyautogui.write("12345")
pyautogui.write("MyCoding", interval=0.25)
# write는 기본적으로는 숫자와 영문만 지원한다. 한글을 사용하려면 pyperclip 사용해보길...

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력
# 사이트 참고 - automate the boring stuff with python

# 특수 문자
# shift 4 -> $
pyautogui.keyDown("shift")          # shift 키를 누른 상태에서
pyautogui.press("4")                # 숫자 4를 입력하고
pyautogui.keyUp("shift")            # shift 키를 뗀다.

# 조합키 (Hot Key)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")                # = press("a")
pyautogui.keyUp("ctrl")             # Ctrl + a

# 간편한 조합키
pyautogui.hotkey("ctrl", "alt", "shift", "a")
# 순서 : ctrl 누르고 > alt 누르고 > shift 누르고 > a 누르고 > a 떼고 > shift 떼고 > alt 떼고 > ctrl 떼기

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q