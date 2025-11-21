from television import Television

def test_init():
    tv = Television()
    tv.__str__()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    tv.power()
    tv.__str__()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    tv.__str__()
    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.__str__()
def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"
    tv.channel_down()
    tv.channel_down()
    tv.channel_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.__str__()
def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"
    tv.__str__()
def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.__str__()

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"
    tv.mute()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"
    tv.__str__()