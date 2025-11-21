class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:



        '''
        Sets the defaults for the Television object
        args: None
        return: None
        '''

        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0
        self.__prev_volume = 0




    def power(self) -> None:

        '''
        Turns the television on and off
        args: None
        return: None
        '''

        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self) -> None:

        '''
        Mutes the television
        args: None
        return: None
        '''

        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            else:
                self.__muted = True
                self.__prev_volume = self.__volume
                self.__volume = self.MIN_VOLUME
    def channel_up(self) -> None:

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

    def channel_down(self) -> None:



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

    def volume_up(self) -> None:

        '''
        Changes the volume up
        args: None
        return: None
        '''

        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:

        '''
        Changes the volume down
        args: None
        return: None
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1




    def __str__(self) -> str:

        '''
        Returns a string representation of the Television object
        args: None
        return: string
        '''

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"