from machine import Pin, I2C, UART
import time

# UART初期化
# UART番号とボーレートの設定
uart = UART(0, 9600)

print("Start!")
for i in range(1000):
    buf = uart.read(1)
    print(buf)
    
    time.sleep_ms(100)