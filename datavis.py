import serial
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from collections import deque

# 🔌 Change this to your port
PORT = 'COM15'   # Windows
# PORT = '/dev/ttyUSB0'  # Linux
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

app = QtWidgets.QAppl   ication([])

win = pg.GraphicsLayoutWidget(title="Motor Real-Time Data")
win.resize(1000, 600)

# Create plots
plot1 = win.addPlot(title="Speed & Voltage")
curve_speed = plot1.plot(pen='r', name="Speed")
curve_vq = plot1.plot(pen='b', name="Vq")

win.nextRow()

plot2 = win.addPlot(title="Current & Temperature")
curve_iq = plot2.plot(pen='y', name="Iq")
curve_temp = plot2.plot(pen='g', name="Temp")

# Buffers (fast)
speed = deque(maxlen=200)
vq = deque(maxlen=200)
iq = deque(maxlen=200)
temp = deque(maxlen=200)

win.show()

def update():
    while ser.in_waiting:
        line = ser.readline().decode(errors='ignore').strip()

        # Skip header line
        if "SPD" in line:
            continue

        try:
            parts = line.split("|")

            if len(parts) != 7:
                return

            s = float(parts[0])
            v = float(parts[1])
            i = float(parts[2])
            t = float(parts[6])  # REAL TEMP

            speed.append(s)
            vq.append(v)
            iq.append(i)
            temp.append(t)

        except:
            pass

    # Update plots
    curve_speed.setData(speed)
    curve_vq.setData(vq)
    curve_iq.setData(iq)
    curve_temp.setData(temp)

# Timer → fast refresh
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)  # 10ms (~100 FPS)

app.exec()