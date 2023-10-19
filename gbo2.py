import random
import time
import psutil
import pyautogui
import pygetwindow as click_window
def find_processes():
    processes = psutil.process_iter()
    # 遍历进程列表并找到指定的进程
    target_process_name = "MSGBO2.exe"  # 指定进程名称
    target_process = None
    for process in processes:  # 在所有进程中查找MSGBO2.exe
        try:
            process_name = process.name()
            if process_name == target_process_name:
                target_process = process
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if target_process is not None:
        print("GBO2已在运行:",time_now())
        create_room()
    else:
        print("GBO2未达到要求！请打开至自定义界面",time_now())
def window_click():                                     # 点击窗口，保证在顶端
    title = 'GUNDAM BATTLE OPERATION 2'
    window=click_window.getWindowsWithTitle(title)[0]
    window.activate()
    link_test()
def link_test():                                        # 连接测试
    if pyautogui.locateOnScreen('sc/unstable connection.png', grayscale=True, confidence=0.70) is not None:
        print('连接不稳定',time_now())
        time.sleep(6)

def right(i):                                           # 右方向键
    window_click()
    for a in range(i):
        pyautogui.typewrite(['right'])

def down(i):                                            # 下方向键
    window_click()
    for a in range(i):
        pyautogui.typewrite(['down'])

def left(i):                                            # 左方向键
    window_click()
    for a in range(i):
        pyautogui.typewrite(['left'])

def up(i):                                              # 上方向键
    window_click()
    for a in range(i):
        pyautogui.typewrite(['up'])

def enter(i):                                           # 回车键/确定键
    window_click()
    for a in range(i):
        pyautogui.typewrite(['enter'])

def space(i):                                           # 空格键
    window_click()
    for a in range(i):
        pyautogui.typewrite(' ')
def right_click(i):
    window_click()
    for a in range(i):
        pyautogui.rightClick()
        time.sleep(1)
def hold_f(i):
    window_click()
    pyautogui.keyDown('f')
    time.sleep(i)
    pyautogui.keyUp('f')

def hold_shift(i):
    window_click()
    pyautogui.keyDown('shift')
    time.sleep(i)
    pyautogui.keyUp('shift')

def f12():
    window_click()
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f1')
    pyautogui.press('f12')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f1')
def timesleep(i,j):
    time.sleep(random.uniform(i,j))

def time_now():
    now=time.localtime(time.time())
    return time.strftime('%y-%m-%d-%H:%M:%S',now)
def create_room():
    window_click()
    link_test()
    try:
        if pyautogui.locateOnScreen('sc/create room.png', grayscale=True, confidence=0.70) is not None:
            print('创建AB房中...',time_now())
            enter(1)
            timesleep(1,2)
            right(4)
            print('选择模式：混合编组:',time_now())
            down(1)
            right(7)
            print('选择地图：北极基地:',time_now())
            down(2)
            left(9)
            print('解除段位限制:',time_now())
            down(4)
            enter(1)
            up(1)
            space(1)
            # pyautogui.typewrite('A WIN Random')
            pyautogui.typewrite('A WIN I AWAYS B')
            print('输入房间备注:',time_now())
            timesleep(3,4)
            enter(1)
            down(6)
            enter(1)
            print('创建完毕:',time_now())
            timesleep(0.5,1)
            link_test()
    except Exception as e:
        print("GBO2未达到要求！请打开至自定义界面:",time_now())
        print(e)
def always_b():
    window_click()
    enter(1)
    timesleep(1,1.5)
    window_click()
    right(1)
    enter(1)
    enter(1)
    timesleep(0.5,1.5)
    link_test()
def random_room():
    window_click()
    enter(1)
    timesleep(1,1.5)
    window_click()
    enter(1)
    enter(1)
    link_test()

def start():
    window_click()
    while(True):
        while(True):
            if pyautogui.locateOnScreen('sc/quit.png', grayscale=True, confidence=0.70) is not None:
                print('已返回出击室:',time_now())
                right_click(1)
            if pyautogui.locateOnScreen('sc/start.png', grayscale=True, confidence=0.70) is not None:
                always_b()
                # random_room()
                if pyautogui.locateOnScreen('sc/cant start.png', grayscale=True, confidence=0.70) is not None:
                    print('编组失败:',time_now())
                else:
                    print('编组成功:',time_now())
                    ab_room()
                    break
            else:
                print('人员未齐:',time_now())
                timesleep(1,1.5)
                continue
        game_start()
def ab_room():
    while(True):
        if pyautogui.locateOnScreen('sc/start.png', grayscale=True, confidence=0.70) is not None:
            print('玩家退出:',time_now())
            break
        if pyautogui.locateOnScreen('sc/unit selected.png', grayscale=True, confidence=0.90) is not None:
            print('已返回出击室:',time_now())
            break
        if pyautogui.locateOnScreen('sc/mission start.png', grayscale=True, confidence=0.80) is not None:
            print('地面对局开始:', time_now())
            break
        if pyautogui.locateOnScreen('sc/mission start_space.png', grayscale=True, confidence=0.80) is not None:
            print('宇宙对局开始:',time_now())
            break
        if pyautogui.locateOnScreen('sc/group.png', grayscale=True, confidence=0.90) is None:
            window_click()
            enter(1)
            if pyautogui.locateOnScreen('sc/get ready.png', grayscale=True, confidence=0.90) is not None:
                window_click()
                enter(1)
                print('准备完成:',time_now())
                break
            else:
                continue
def game_start():
    while(True):
        if pyautogui.locateOnScreen('sc/start.png', grayscale=True, confidence=0.70) is not None:
            print('玩家退出:',time_now())
            break
        if pyautogui.locateOnScreen('sc/unit selected.png', grayscale=True, confidence=0.90) is not None:
            print('玩家退出:',time_now())
            break
        if pyautogui.locateOnScreen('sc/mission start.png', grayscale=True, confidence=0.80) is not None:
            print('地面对局开始:',time_now())
            time.sleep(6)
            window_click()
            hold_f(2)
        if pyautogui.locateOnScreen('sc/mission start_space.png', grayscale=True, confidence=0.80) is not None:
            print('宇宙对局开始:',time_now())
            time.sleep(20)
            window_click()
            hold_shift(0.2)
            timesleep(2,3)
            hold_f(2)
        if pyautogui.locateOnScreen('sc/mission completed.png', grayscale=True, confidence=0.90) is not None:
            print('对局结束—胜利:',time_now())
            while (True):
                right_click(1)
                if pyautogui.locateOnScreen('sc/result.png', grayscale=True, confidence=0.90) is not None:
                    right_click(1)
                    time.sleep(1)
                    right_click(2)
                if pyautogui.locateOnScreen('sc/box.png', grayscale=True, confidence=0.70) is not None:
                    print('发现物资:', time_now())
                    window_click()
                    right_click(1)
                    f12()
                    right_click(1)
                    continue
                if pyautogui.locateOnScreen('sc/unit selected.png', grayscale=True, confidence=0.90) is not None:
                    print('已返回出击室:', time_now())
                    break
                if pyautogui.locateOnScreen('sc/room lost.png', grayscale=True, confidence=0.70) is not None:
                    print('房间消失:', time_now())
                    right_click(1)
                    break
                if pyautogui.locateOnScreen('sc/link lost.png', grayscale=True, confidence=0.70) is not None:
                    print('连接丢失:', time_now())
                    right_click(1)
                    break
                if pyautogui.locateOnScreen('sc/quit.png', grayscale=True, confidence=0.70) is not None:
                    print('已返回出击室:', time_now())
                    right_click(1)
                    break
                else:
                    window_click()
            break
        if pyautogui.locateOnScreen('sc/mission failed.png', grayscale=True, confidence=0.90) is not None:
            print('对局结束—失败:',time_now())
            while(True):
                right_click(1)
                if pyautogui.locateOnScreen('sc/result.png', grayscale=True, confidence=0.90) is not None:
                    right_click(1)
                    time.sleep(1)
                    right_click(2)
                if pyautogui.locateOnScreen('sc/box.png', grayscale=True, confidence=0.70) is not None:
                    print('发现物资:',time_now())
                    window_click()
                    right_click(1)
                    f12()
                    right_click(1)
                    break
                if pyautogui.locateOnScreen('sc/unit selected.png', grayscale=True, confidence=0.90) is not None:
                    print('已返回出击室:',time_now())
                    break
                if pyautogui.locateOnScreen('sc/room lost.png', grayscale=True, confidence=0.70) is not None:
                    print('房间消失:',time_now())
                    right_click(1)
                    break
                if pyautogui.locateOnScreen('sc/link lost.png', grayscale=True, confidence=0.70) is not None:
                    print('连接丢失:',time_now())
                    right_click(1)
                    break
                if pyautogui.locateOnScreen('sc/quit.png', grayscale=True, confidence=0.70) is not None:
                    print('已返回出击室:',time_now())
                    right_click(1)
                    break
                else:
                    window_click()
            break
        if pyautogui.locateOnScreen('sc/room lost.png', grayscale=True, confidence=0.70) is not None:
            print('房间消失:',time_now())
            break
        if pyautogui.locateOnScreen('sc/link lost.png', grayscale=True, confidence=0.70) is not None:
            print('连接丢失:',time_now())
            break
        else:
            continue
def startab():
    try:
        while(True):
            if pyautogui.locateOnScreen('sc/room.png', grayscale=True, confidence=0.70) is not None:
                print('已创建房间:',time_now())
                start()
            else:
                find_processes()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    # print('请关注作者bilibili 雨辰official')
    # print('此程序完全免费，只作为自动化测试编程交流学习之用')
    # print('切勿用做商业用途！请在学习完成后自行删除')
    # print('若有违反，后果自负！')
    # input('按回车键开始程序')
    startab()
    # input('程序运行结束!',time_now())