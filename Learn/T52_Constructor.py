class Students:
    roll=""
    gpa=""
    def __init__(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"\nRoll : {self.roll}\nG.P.A : {self.gpa}")

joy=Students(101,5.00)
narayon=Students(102,4.86)
roy=Students(103,4.5)
joy.display()
narayon.display()
roy.display()