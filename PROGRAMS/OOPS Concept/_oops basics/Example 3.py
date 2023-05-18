class pysipders:
    Branch_Name = 'Marathahail'
    Batch_code = '747E1'
    Course_Name = 'Python Full Stack Development'

    def __init__(self, Name, Mno, Mail, Mock):
        self.Name = Name
        self.mno = Mno
        self.Mail = Mail
        self.Mock = Mock

s1 = pysipders('prasanth', '98285982', 'prasath@gmail.com', 'P1')
s2 = pysipders('ravi', '9828536382', 'ravi@gmail.com', 'P3')
s3 = pysipders('mathi', '9823582', 'mathi@gmail.com', 'P4')

print(s1.Mock)
print(s2.Mock)
print(s1.Mail)
print(s1.Name)

