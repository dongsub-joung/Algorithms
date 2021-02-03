class Person:
    def __init__(self, name, age, address):
        self.hello= '안녕하세요.'
        self.name= name
        self.age= age
        self.address= address

    def greeting(self):
        print(f'{self.hello} 저는 {self.name}입니다.')

dongsub= Person('dongsub', 24, '강원도 인제군')
dongsub.greeting()