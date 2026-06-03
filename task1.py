class student:
    def __init__(self,name,marks1,marks2):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
    def grade(self):
        sum=self.marks1+self.marks2
        avg=sum/2
        if avg>=90:
            print(f"the student {self.name} has grade A")
        elif avg>=75 and avg<90:
            print(f"the student {self.name} has grade B")
        elif avg>=50 and avg<75:
            print(f"the student {self.name} has grade C")
        elif avg<50:
            print(f"the student  {self.name} failed")
        else :
            print("invalid mark")
student1=student("amy",50,32)
student1.grade()
student2=student("emily",50,70)
student2.grade()
 
        