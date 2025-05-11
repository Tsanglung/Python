import time


def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print("倒數 " + timeformat, end="\r")
        time.sleep(1)
        seconds -= 1


seconds = int(input("輸入秒數 : "))
countdown_timer(seconds)
print("down !")
