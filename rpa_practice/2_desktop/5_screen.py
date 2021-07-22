import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")              # 파일로 저장

pixel = pyautogui.pixel(30, 10)
print(pixel)

print(pyautogui.pixelMatchesColor(30, 10, (30, 60, 91)))
print(pyautogui.pixelMatchesColor(30, 10, pixel))