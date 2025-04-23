from machine import Timer,freq
from PA_SERVO import release
release()
freq(240000000)
#import _thread
import padog, time
from padog import uart6
t=Timer(1)

c_loop_speed_mode=0
i = 0
def loop(t):
  #LOOP JUDGE
  try:
    global c_loop_speed_mode
    padog.mainloop()
 #   if i % 2 == 0: 
      #  uart6.write(str(i) + "nihao\n")
#     padog.alarm_run()
    if padog.CC_M==1:
      padog.remote_run()
      padog.height(110)
      padog.X_goal=padog.in_y
    elif padog.CC_M==2:
      padog.UART_Run()
      padog.height(110)
      padog.X_goal=padog.in_y
  
    if padog.loop_speed_mode_sc==1:
      if padog.loop_speed_mode==0:
        print("Loop mode 1")
        t.deinit()
        t.init(period=30,mode=Timer.PERIODIC,callback=loop)
        padog.loop_speed_mode_sc=0
      elif padog.loop_speed_mode==1:
        print("Loop mode 2")                                                                                                                                                                                 
        t.deinit()
        t.init(period=100,mode=Timer.PERIODIC,callback=loop)
        padog.loop_speed_mode_sc=0
  except Exception as e:
#     t.deinit()
    import sys
    import io

    # 格式化异常信息
    buf = io.StringIO()
    sys.print_exception(e, buf)
    error_msg = buf.getvalue()
    buf.close()

    # 通过串口发送（带循环计数 i）
    uart6.write("错误信息:\n" + error_msg + "\n")  # 发送格式化后的异常信息

    print("致命错误，重新烧录程序")

def app_1():
  exec(open('web_c.py').read())

t.init(period=30,mode=Timer.PERIODIC,callback=loop)
padog.loop_speed_mode_sc=0

padog.start_ring()

while True:
    print(i)
    i = i + 1
    time.sleep(1)
