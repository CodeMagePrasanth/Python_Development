class pysipders:
    Branch_Name = 'Marathahail'
    Batch_code = '747E1'
    Course_Name = 'Python Full Stack Development'
s1 = pysipders()
s2 = pysipders()
s3 = pysipders()
def details(obj, Name, Mno, mail, mock):
    obj.Name = Name
    obj.Mno = Mno
    obj.mail =mail
    obj.mock = mock

details(s1, 'prasanth', '429847948', 'prasnth@gmail.com','p1')
details( s2, 'prasanth', '429847948', 'prasnth@gmail.com','p1')
details( s3, 'prasanth', '429847948', 'prasnth@gmail.com','p3')
print(s1.Name)

'''
# Ouptput --> 
    Marathahail
    Python Full Stack Development
    747E1
'''