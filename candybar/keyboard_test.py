from machine import Pin
import time

# define all GPIO pins as rows and outputs
pin_row = [9, 10, 11, 12]
pin_col = [0, 1, 2]

# instantiate all GPIO rows as outputs
rows = [Pin(pin, Pin.OUT) for pin in pin_row]

# instantiate all GPIO cols as inputs with pull-down resistors
cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in pin_col]

# matrix keypad layout
keypad = [
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6', '7', '8'],
    ['ast', '0', 'pou']
    ]

keypad2 = [
    [['A', 'B', 'C'], ['A', 'B', 'C'], ['D', 'E', 'F']],
    [['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O']],
    [['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']],
    [['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']]
    ]

def scan_keyboard():
    for row_idx, row in enumerate(rows):
        row = row.high()
        for col_idx, col in enumerate(cols):
            if col.value == 1:
                row.low()
                return keypad[row_idx][col_idx]
            else:
                row.low()
    return None

while True:
    key = scan_keyboard()
    if key:
        print(key)