class Television:
    def __init__(self):
        self.__volume = 0
        self.__channel = 0
        self.__isOn = False

    def switchOn(self):
        if self.__isOn == False:
            self.__isOn = True
        else:
            self.__isOn = False

    def increase_volume(self):
        if self.__isOn == True:
            if self.__volume < 100:
                self.__volume += 1
            else:
                return f"You cant increase the volume to more than 100"

    def deccrease_volume(self):
        if self.__isOn == True:
            if self.__volume > 0:
                self.__volume -= 1
            else:
                return f"You cant decrease the volume to less than 0"

    def increase_channel(self):
        if self.__isOn == True:
            self.__channel += 1

    def decrease_channel(self):
        if self.__isOn == True:
            if self.__channel > 0:
                self.__channel -= 1
            else:
                return f"You cant have a negative channel"

    def set_channel(self, channel):
        if self.__isOn == True:
            if self.__channel > 0:
                self.__channel = channel
            else:
                return f"Channel cannot be less than 0"
