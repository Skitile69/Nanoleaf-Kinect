from nanoleafapi import discovery
from nanoleafapi import Nanoleaf, NanoleafDigitalTwin
from nanoleafapi import RED, ORANGE, BLUE, YELLOW, WHITE, GREEN

ip1 = "192.168.1.14"
ip2 = "192.168.1.13"
ip3 = "192.168.1.12"
ip4 = "192.168.1.10"
ip5 = "192.168.1.11"
ip6 = "192.168.1.9"
ip7 = "192.168.1.4"
ip8 = "192.168.1.5"
ip9 = "192.168.1.28"
ip10 = "192.168.1.2"

auth1="LKI439ILyLPOZ73i0fOodP3rgxObe2eO"
auth2="Vu9ggkGI9RNQ2SDaFPNfUIa7kX9r86nq"
auth3="Q6hNMymIYPtuJmc8c3Ok4roVjFlFO3F7"
auth4="Vu9ggkGI9RNQ2SDaFPNfUIa7kX9r86nq"
auth5="LKI439ILyLPOZ73i0fOodP3rgxObe2eO"
auth6="RBjc55LQniYPHOTsTgQW5Yoh792AINRl"
auth7="ALf4TvPrNiK4hxEVdjtbc5Gl0X2l0NCl"
auth8="eRTQpXfNZh4KLdvnJXsdQMsSzspSerPu"
auth9="8Wd6krYZG8bpcOkN8zvfbsFG69b2G4QL"
auth10="5lzrK08d5urKlI7pXeIKkWt2H4XtyGoe"

n1 = Nanoleaf(ip1, auth1)
n2 = Nanoleaf(ip2,auth2)
n3 = Nanoleaf(ip3,auth3)
n4 = Nanoleaf(ip4,auth4)
n5 = Nanoleaf(ip5,auth5)
n6 = Nanoleaf(ip6, auth6)
n7 = Nanoleaf(ip7,auth7)
n8 = Nanoleaf(ip8,auth8)
n9 = Nanoleaf(ip9,auth9)
n10 = Nanoleaf(ip10,auth10)

dt1 = NanoleafDigitalTwin(n1)
dt2 = NanoleafDigitalTwin(n2)
dt3 = NanoleafDigitalTwin(n3)
dt4 = NanoleafDigitalTwin(n4)
dt5 = NanoleafDigitalTwin(n5)
dt6 = NanoleafDigitalTwin(n6)
dt7 = NanoleafDigitalTwin(n7)
dt8 = NanoleafDigitalTwin(n8)
dt9 = NanoleafDigitalTwin(n9)
dt10 = NanoleafDigitalTwin(n10)


def allOn(color) -> None:
    dt1.set_all_colors(color)
    dt2.set_all_colors(color)
    dt3.set_all_colors(color)
    dt4.set_all_colors(color)
    dt5.set_all_colors(color)
    dt6.set_all_colors(color)
    dt7.set_all_colors(color)
    dt8.set_all_colors(color)
    dt9.set_all_colors(color)
    dt10.set_all_colors(color)

    dt1.sync()
    dt2.sync()
    dt3.sync()
    dt4.sync()
    dt5.sync()
    dt6.sync()
    dt7.sync()
    dt8.sync()
    dt9.sync()
    dt10.sync()


def allSetBright(brightness) -> None:
    n1.set_brightness(brightness)
    n2.set_brightness(brightness)
    n3.set_brightness(brightness)
    n4.set_brightness(brightness)
    n5.set_brightness(brightness)
    n6.set_brightness(brightness)
    n7.set_brightness(brightness)
    n8.set_brightness(brightness)
    n9.set_brightness(brightness)
    n10.set_brightness(brightness)

def specOn(num, color) -> None:
    if num == 1:
        n1.set_color(color)
        dt1.sync()
    elif num == 2:
        n2.set_color(color)
        dt2.sync()
    elif num == 3:
        n3.set_color(color)
        dt3.sync()
    elif num == 4:
        n4.set_color(color)
        dt4.sync()
    elif num == 5:
        n5.set_color(color)
        dt5.sync()
    elif num == 6:
        n6.set_color(color)
        dt6.sync()
    elif num == 7:
        n7.set_color(color)
        dt7.sync()
    elif num == 8:
        n8.set_color(color)
        dt8.sync()
    elif num == 9:
        n9.set_color(color)
        dt9.sync()
    elif num == 10:
        n10.set_color(color)
        dt10.sync()

def specBright(num, brightness) -> None:
    if num == 1:
        n1.set_brightness(brightness)
    elif num == 2:
        n2.set_brightness(brightness)
    elif num == 3:
        n3.set_brightness(brightness)
    elif num == 4:
        n4.set_brightness(brightness)
    elif num == 5:
        n5.set_brightness(brightness)
    elif num == 6:
        n6.set_brightness(brightness)
    elif num == 7:
        n7.set_brightness(brightness)
    elif num == 8:
        n8.set_brightness(brightness)
    elif num == 9:
        n9.set_brightness(brightness)
    elif num == 10:
        n10.set_brightness(brightness)