import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # 2021년 12월 3일 10시 08분 20초 ->_20211203_100820
    cuur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(cuur_time))


# 사용자가 ctrl+shift+s 키를 누르면 스크린 샷 저장
keyboard.add_hotkey("ctrl+shift+s", screenshot)

keyboard.wait("esc")  # 사용자가 esc 를 누를 때까지 프로그램 수행
