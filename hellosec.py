import threading


def printit():
    threading.Timer(1.0, printit).start()
    print("Happy New Second !")


printit()
