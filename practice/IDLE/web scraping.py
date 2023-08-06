import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata

edatas = ""
edata1 = ""

surl = "https://www.flipkart.com/search?q=machine%20learning%20books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
soup1 = soup(surl)
# print(soup1)

count = soup1.findAll("a", {"class" : "s1Q9rs"})
print((len(count)))

for record in soup1.findAll("div", {"class": "_13oc-S"}):
    for record2 in record.findAll("div", {"class": "_4ddWXP"}):
        for record3 in record2.findAll("a", {"class": "s1Q9rs"}):
            title = record3.text.replace(',','..')

        for record4 in record2.findAll("div",{"class": "_30jeq3"}):
            price = record4.text.replace(',','')
            data = title + "," + price
        edatas = edatas + "\n" +data

print(edatas)

header = "book name,Price"
file = open(os.path.expanduser("out.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors="ignore"))
file.write(bytes(edatas, encoding="ascii", errors="ignore"))

# o/p-->
'''
book name,Price
Machine Learning Using Python,593
Machine Learning 1 Edition,518
Machine Learning,627
AI and Machine Learning,1977
Understanding Machine Learning,1080
Machine Learning with Python Course,351
NII Testbeds and Community for Information Access Resea...,4327
Superintelligence,500
Data Science and Machine Learning with R,637
Introduction to Machine Learning,160
Machine Learning,299
The Machine is Learning,320
Mathematics for Machine Learning,3720
Mathematics for Machine Learning,7541
Scale Space and Variational Methods in Computer Vision,8654
Machine Learning,899
Deep IV in Law,1508
Testing and Assessment of Interpreting,11563
Data Analysis.. Machine Learning and Knowledge Discovery,12982
Machine Learning and Knowledge Discovery in Databases. ...,8481
A Machine Learning Based Model of Boko Haram,12116
Hands-On Machine Learning with Scikit-Learn.. Keras.. and...,3000
AI and Machine Learning for Coders: A Programmer's Guid...,1500
Designing Machine Learning Systems: An Iterative Proces...,1600
Machine Learning and Algorithms,218
Machine Learning and Knowledge Discovery in Databases,10385
Optimization for Data Analysis,3820
Weapons of Math Destruction,476
Large-Scale Machine Learning in the Earth Sciences,4544
Advances in Artificial Intelligence.. Software and Syste...,19040
Machine Learning,4533
Big Data,1508
Algebraic Geometry and Statistical Learning Theory,6938
Frontiers in Data Science,4533
An Introduction to Machine Learning,222
The StatQuest Illustrated Guide to Machine Learning (Fu...,1158
Machine Learning for BE Anna University R21CBCS (IV - A...,195
Machine Learning and Applications For B.E. Pune Univers...,150
Just Enough R!,4029
Imitation in Animals and Artifacts illustrated edition ...,3115
'''