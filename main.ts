input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    minutenhochzaehler += 1
    basic.showNumber(minutenhochzaehler)
    if (minutenhochzaehler == 60) {
        minutenhochzaehler = 0
    }
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    stunde = stundenhochzähler
    minute = minutenhochzaehler
    laufzeit_offset = input.runningTime()
    basic.showString("ok")
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    stundenhochzähler += 1
    if (stundenhochzähler == 12) {
        stundenhochzähler = 0
    }
    basic.showNumber(stundenhochzähler)
})
input.onGesture(Gesture.Shake, function () {
    stunde += Math.floor((input.runningTime() - laufzeit_offset) / 3600000)
    minute += (input.runningTime() - laufzeit_offset) % 60000
    basic.showString("S:")
    basic.showNumber(stunde % 12)
    basic.showString("M:")
    basic.showNumber(minute % 60)
})
let laufzeit_offset = 0
let minutenhochzaehler = 0
let minute = 0
let stundenhochzähler = 0
let stunde = 0
stunde = 0
stundenhochzähler = 0
minute = 0
minutenhochzaehler = 0
let lauf_sec = 0
laufzeit_offset = 0
