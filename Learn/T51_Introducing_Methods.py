class Students(object):
    roll=""
    gpa=""
    def setValue(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"\nRoll : {self.roll}\nG.P.A : {self.gpa}")

joy=Students()
narayon=Students()
roy=Students()
joy.setValue(101,5.00)
narayon.setValue(102,4.86)
roy.setValue(103,4.5)
joy.display()
narayon.display()
roy.display()