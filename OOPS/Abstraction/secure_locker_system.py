class SecureLocker:
    def __init__(self, pin):
        self.__pin = pin
        self.is_locked = True
    def __verify_pin(self, pin):
        return self.__pin == pin
    def unlock(self, pin):
        if self.__verify_pin(pin):
            self.is_locked = False
            print("Unlocked")
        else:
            print("Incorrect")

    def lock(self):
        self.is_locked = True
        print("Locker is locked")

    def status(self):
        if self.is_locked:
            print("Locked")
        else:
            print("Unlocked")

if __name__ == "__main__":
    locker = SecureLocker(1234)
    locker.status()
    locker.unlock(1111)
    locker.unlock(1234)
    locker.status()
    print("\nLocking:")
    locker.lock()
    locker.status()
