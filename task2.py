class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        sum=self.marks["malayalam"]+self.marks["hindi"]
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
student1=student("jason",{"malayalam":45,"hindi":50})
student1.grade()
student2=student("boss",{"malayalam":60,"hindi":50})
student2.grade()