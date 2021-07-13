import pyautogui
# pyautogui.FAILSAFE = False          # <비추천> 동작하다가 멈추는 상황이 와도 끝까지 동작을 수행하겠다.
pyautogui.PAUSE = 1                 # 모든 동자게 1초씩 sleep 적용

# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)        # 동작 중 마우스를 맨 왼쪽 위로 가져가면 동작이 강제 종료된다.
    # pyautogui.sleep(1)