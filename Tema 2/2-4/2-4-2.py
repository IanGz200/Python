class Hotel:

    age:int
    student:bool
    unemployed:bool
    retired:bool
    large_family:bool

    def __init__(self, age:int, student:bool, unemployed:bool, retired:bool, large_family:bool):
        self.age = age
        self.student = student
        self.unemployed = unemployed
        self.retired = retired
        self.large_family = large_family

    def room_price(self):
        if self.age < 30:
            if self.student or self.unemployed:
                return 40
            return 50
        elif self.age > 55:
            if self.retired or self.unemployed:
                return 45
            return 60
        else:
            if self.large_family:
                return 65
            return 75

def main():
    hotel = Hotel(31,False,False,True,False)
    print("El precio de la habitación es: ",hotel.room_price(),"€",sep="")

if __name__ == '__main__':
    main()