class Person():
    #this function is to initialize the class, and make all the value default in N/A
    def __init__(self):
        self.name = "N/A"
        self.ID = "N/A"
        self.age = "N/A"
        self.weight = "N/A"
        self.height = "N/A"
        self.section = "N/A"

    #this function require user to input the data the class need
    def input_person_data(self,name,ID,age,weight,height,section):
        self.name = name
        self.ID = ID
        self.age = age
        self.weight = weight
        self.height = height
        self.section = section
    
    #this function is to print all the data out 
    def get_person_data(self):
        print("name: "+self.name+"\n"+"ID: "+self.ID+"\n"+"age: "+self.age+"\n"+"weight: "+self.weight+"\n"+"height: "+self.height+"\n"+"section: "+self.section+"\n")


def main():
    Isaac = Person()
    Isaac.input_person_data("Isaac","1130107","21","65kg","177cm","W01")

    Jack = Person()
    Jack.input_person_data("Jack","1131001","20","60kg","175cm","W02")

    person = Person()
    

    Isaac.get_person_data()
    Jack.get_person_data()
    person.get_person_data()

if __name__ == '__main__':
    main()