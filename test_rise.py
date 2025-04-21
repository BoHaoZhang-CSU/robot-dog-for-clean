def rise():
  pin2 = Pin(2, Pin.OUT)
  pin2.value(1)
  pin0 = Pin(0, Pin.OUT)
  pin0.value(0)
  pin4 = Pin(4)
  pwm = PWM(pin4, freq=1000, duty=800) 
  time.sleep(2)  # 短暂延时# duty 范围 0-1023，512 表示 50% 占空比
  pin2.value(0)

rise()