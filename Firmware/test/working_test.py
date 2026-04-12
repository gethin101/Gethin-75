import board
import digitalio
import time

row_pins = [
    board.GP2,  # R0
    board.GP3,  # R1
    board.GP4,  # R2
    board.GP5,  # R3
    board.GP6,  # R4
    board.GP7,  # R5
]

col_pins = [
    board.GP8,   # C0
    board.GP9,   # C1
    board.GP10,  # C2
    board.GP11,  # C3
    board.GP12,  # C4
    board.GP13,  # C5
    board.GP14,  # C6
    board.GP15,  # C7
    board.GP16,  # C8
    board.GP17,  # C9
    board.GP18,  # C10
    board.GP19,  # C11
    board.GP20,  # C12
    board.GP21,  # C13
    board.GP22,  # C14
    board.GP26,  # C15
    board.GP27,  # C16
]

rows = []
for pin in row_pins:
    r = digitalio.DigitalInOut(pin)
    r.direction = digitalio.Direction.OUTPUT
    r.value = False
    rows.append(r)

cols = []
for pin in col_pins:
    c = digitalio.DigitalInOut(pin)
    c.direction = digitalio.Direction.INPUT
    c.pull = digitalio.Pull.DOWN
    cols.append(c)

print("17-column matrix test running...")

while True:
    for r_index, r in enumerate(rows):
        r.value = True
        time.sleep(0.0001)

        for c_index, c in enumerate(cols):
            if c.value:
                print(f"PRESS: R{r_index} C{c_index}")

        r.value = False

    time.sleep(0.01)
