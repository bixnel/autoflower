import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect('Qwerty', '12345678')
print(sta_if.isconnected())


