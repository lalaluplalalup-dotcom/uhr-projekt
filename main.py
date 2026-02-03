def on_button_a():
    global minutenhochzaehler
    minutenhochzaehler += 1
    if minutenhochzaehler == 60:
        minutenhochzaehler = 0
    basic.show_number(minutenhochzaehler)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    global stunde, minute, laufzeit_offset
    stunde = stundenhochzähler
    minute = minutenhochzaehler
    laufzeit_offset = input.running_time()
    basic.show_string("ok")
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    global stundenhochzähler
    stundenhochzähler += 1
    if stundenhochzähler == 12:
        stundenhochzähler = 0
    basic.show_number(stundenhochzähler)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_gesture_shake():
    global lauf_sec, stunde, minute
    lauf_sec = 0 / 1000
    stunde += Math.floor((input.running_time() - laufzeit_offset) / 3600000)
    minute += Math.floor((input.running_time() - laufzeit_offset) / 60000)
    basic.show_string("S:")
    basic.show_number(stunde % 12)
    basic.pause(1000)
    basic.show_string("M:")
    basic.show_number(minute % 60)
    basic.pause(1000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_pin_touch_p0():
    pass
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

laufzeit_offset = 0
lauf_sec = 0
minutenhochzaehler = 0
minute = 0
stundenhochzähler = 0
stunde = 0
stunde = 0
stundenhochzähler = 0
minute = 0
minutenhochzaehler = 0
lauf_sec = 0
laufzeit_offset = 0