i=0
NUM_DEV = 2
buf = (chr(0xAA)*2 + chr(0x55)*2) * NUM_DEV * 12

f = open("/dev/ttyUSB0", "w")

ENABLE_TEXT_SCROLLING = 0
DISABLE_TEXT_SCROLLING = 1
SEND_GRAPHICS_BUFFER = 2
SEND_LAMP_DATA = 3
SEND_TEXT_MESSAGE = 4
ONE_LINE_VERTICAL_CENTER = 5
TWO_LINES_OF_TEXT = 6

def send_frame(f, buf):
  global NUM_DEV
  f.write(SEND_GRAPHICS_BUFFER)
  for x in range(2*NUM_DEV*24):
    f.write(buf[x])

#def update_buffer(buf):
#  global i, NUM_DEV
#  i = (i+1)%256
#  for x in range(2*NUM_DEV*24):
#    buf[x] = chr(i)  

while True:
#  update_buffer(buf)
  send_frame(f,buf)

f.close()


