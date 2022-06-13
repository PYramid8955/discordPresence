from pypresence import Presence
import time
print("Code By PYramid#8955")
buttons = None
details = None
state = None
large_image = None
small_image = None
start = None
while 1:
    with open("settings.txt") as f:
        settings = f.read()
    settings = settings.replace("\n", "").split('"')
    for i in settings[::2]:
        settings[settings.index(i)] = i.replace(" ", "")
    if not ("id=" in settings[::2]):
        raise
    for i in settings[::2]:
        i = i.strip()
        if i == "id=":
            ID = settings[settings.index(i)+1]
        elif i == "title=":
            details = settings[settings.index(i)+1]
        elif i == "desc=":
            state = settings[settings.index(i)+1]
        elif i == "largeImage=":
            large_image = settings[settings.index(i)+1]
        elif i == "smallImage=":
            small_image = settings[settings.index(i)+1]
        elif i == "start=":
            if settings[settings.index(i)+1].lower() == "true":
                start = time.time()
        elif i == "button1=":
            x = eval('['+settings[settings.index(i)+1]+']')
            if type(buttons) != list:
                buttons = []
            buttons.insert(0, {"label":x[0], "url": x[1]})
        elif i == "button2=":
            x = eval(settings[settings.index(i)+1])
            if type(buttons) != list:
                buttons = []
            buttons.append({"label":x[0], "url": x[1]})

    presence = Presence(ID)
    presence.connect()
    presence.update(
      details = details,
      state = state,
      large_image = large_image,
      small_image = small_image,
      buttons = buttons,
      start = start
    )
    time.sleep(15)

