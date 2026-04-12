import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# -----------------------------
# MATRIX CONFIGURATION
# -----------------------------
keyboard.row_pins = (
    board.GP2,  # R0
    board.GP3,  # R1
    board.GP4,  # R2
    board.GP5,  # R3
    board.GP6,  # R4
    board.GP7,  # R5
)

keyboard.col_pins = (
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
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

# -----------------------------
# KEYMAP
# -----------------------------
keyboard.keymap = [
    [
        # ---------------- Row 0 ----------------
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7,
        KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.G, KC.G, KC.G,
        KC.NO,

        # ---------------- Row 1 ----------------
        KC.GRV, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7,
        KC._8, KC._9, KC._0, KC.MINS, KC.EQL, KC.BSPC, KC.INS, KC.HOME,
        KC.PGUP,

        # ---------------- Row 2 ----------------
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
        KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.DEL, KC.END, KC.PGDN,
        KC.NO,

        # ---------------- Row 3 ----------------
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J,
        KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT, KC.G, KC.G,
        KC.G,

        # ---------------- Row 4 ----------------
        KC.LSFT, KC.BSLS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N,
        KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.G, KC.UP, KC.G,
        KC.NO,

        # ---------------- Row 5 ----------------
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
        KC.LEFT, KC.DOWN, KC.RIGHT,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

# -----------------------------
# MAIN LOOP
# -----------------------------
if __name__ == '__main__':
    keyboard.go()
