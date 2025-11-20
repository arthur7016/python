class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):



        '''
        Sets the defaults for the Television object
        args: None
        return: None
        '''

        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0


    def power(self):

        '''
        Turns the television on and off
        args: None
        return: None
        '''

        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self):

        '''
        Mutes the television
        args: None
        return: None
        '''

        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
    def channel_up(self):

        '''
        Changes the channel up
        args: None
        return: None
        '''

        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):



        '''
        Changes the channel down
        args: None
        return: None
        '''



        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):

        '''
        Changes the volume up
        args: None
        return: None
        '''

        if self.__status:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):

        '''
        Changes the volume down
        args: None
        return: None
        '''


        if self.__status:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1




    def __str__(self):

        '''
        Returns a string representation of the Television object
        args: None
        return: string
        '''

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"