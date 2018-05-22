class MulticastAddressGenerator:
    def __init__(self):
        self.__group_ip = "224.0.0."
        self.__current_last_ip = 0

    def __end_last_ip(self):
        return self.__current_last_ip >= 255

    def get_next_group(self):
        if self.__end_last_ip():
            self.__current_last_ip = 0
        returned_ip = self.__group_ip + str(self.__current_last_ip)
        self.__current_last_ip = self.__current_last_ip + 1
        return returned_ip
