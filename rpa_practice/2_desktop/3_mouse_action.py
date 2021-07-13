import pyautogui

# pyautogui.sleep(3)              # 3초 대기
# print(pyautogui.position())

# pyautogui.click(143, 10, duration=1)        # 1초 동안 (143, 10) 좌표로 이동 후 마우스 클릭

# pyautogui.click()               # 클릭
# pyautogui.mouseDown()           # 클
# pyautogui.mouseUp()             # 릭

# pyautogui.doubleClick()
# pyautogui.click(clicks=100)     # 클릭 횟수 지정

# pyautogui.rightClick()
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(413, 280)
# pyautogui.drag(100, 0, button='left')                  # 현재 위치 기준으로 x 100만큼, y 0만큼 드래그
# pyautogui.drag(100, 0, duration=0.25, button='left')   # 너무 빠른 동작으로 drag 수행이 안 될 때는 duration 값 설정
# pyautogui.dragTo(500, 400, button='left')               # 절대 좌표 기준으로 x 500, y 400 으로 드래그 (마찬가지로 duration 설정 가능)

pyautogui.scroll(300)           # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤
