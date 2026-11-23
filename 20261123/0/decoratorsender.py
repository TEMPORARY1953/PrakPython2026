class Sender:
    _first = True
    def report(cls):
        if cls._first:
            print("Greetings!")
            cls._first = False
        else:
            print("Get away!")
class Asker:
    def askall(lst):
        for item in lst:
            item.report()

s1, s2, s3 = Sender(), Sender(), Sender()
Asker.askall([s1, s2, s3])
