import pyautogui
# mac은 화면 (retina) 비율이 좀 달라서 인식이 잘 안되는듯...

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.doubleClick(file_menu)

# min_icon = pyautogui.locateOnScreen("min_icon.png", confidence=0.8, grayscale=True)
# print(min_icon)
# pyautogui.moveTo(min_icon)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# 속도 개선
# 1. GrayScale (grayscale)
# 2. 정확도 조정 (confidence)
# 3. 범위 지정
# pyautogui.mouseInfo()
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=(320, 90, 500, 500))
# print(file_menu)
# pyautogui.moveTo(file_menu)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locate("file_menu_notepad.png")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locate("file_menu_notepad.png")
#     print("발견 실패")
#
# pyautogui.click(file_menu_notepad)
# 2. 일정 시간동안 기다리기 (Timeout)
import time
import sys

timeout = 10        # 10초 대기
start = time.time() # 시작 시간 설정
file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locate("file_menu_notepad.png")
    end = time.time()
    if end - start > timeout:   # 지정한 10초를 초과하면
        print("시간 종료")
        sys.exit()

pyautogui.click(file_menu_notepad)

# 함수화
def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate program.")
        sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

my_click("file_menu_notepad.png", 10)