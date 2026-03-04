# KMK -  gethin101
#from kmk.bootcfg import bootcfg

#bootcfg(
    #usb_id={'manufacturer': "Gethin101", 'product': "Gethin-75"},
#)

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys


class Gethin75(KMKKeyboard):
    row_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    )

    col_pins = (
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
        board.GP26,
        board.GP27,
    )

    diode_orientation = DiodeOrientation.ROW2COL


keyboard = Gethin75()
keyboard.extensions.append(MediaKeys())

MAC1 = simple_key_sequence((KC.MPRV,))
MAC2 = simple_key_sequence((KC.MPLY,))
MAC3 = simple_key_sequence((KC.MNXT,))
MAC5 = simple_key_sequence((KC.VOLD,))
MAC6 = simple_key_sequence((KC.VOLU,))
MAC7 = simple_key_sequence((KC.LGUI, KC.L,))
MAC8 = simple_key_sequence((KC.LGUI, KC.E,))
MAC9 = simple_key_sequence((KC.LCTRL, KC.LSHIFT, KC.ESC,))

keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4,
        KC.F5, KC.F6, KC.F7, KC.F8,
        KC.F9, KC.F10, KC.F11, KC.F12,
        MAC1, MAC2, MAC3, KC.NO,
    ],

    [
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
    ],

    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I,
        KC.O, KC.P, KC.LBRC, KC.RBRC,
        KC.ENTER, KC.DEL, KC.END, KC.PGDN,
    ],

    [
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K,
        KC.L, KC.SCLN, KC.QUOT, KC.NUHS,
        MAC5, MAC6, MAC7, KC.NO,
    ],

    [
        KC.LSFT, KC.NUBS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M,
        KC.COMMA, KC.DOT, KC.SLSH, KC.RSFT,
        MAC8, KC.UP, MAC9, KC.NO,
    ],

    [
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,
        KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
        KC.LEFT, KC.DOWN, KC.RIGHT,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ],
]


if __name__ == '__main__':
    keyboard.go()
