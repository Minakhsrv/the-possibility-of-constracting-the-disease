
print("hello we want to check your healthy against monkeypox, so you should enter a text to explain your problem")  #منوی ورودی
print("warrning: 1-type in english  2-only if following words are in your text make sure to type them between two cama(,) and just one space between every word:     Temporal pain, Mild pain, Severe pain, Muscle pain, Body pain, Back pain, Dizziness, Mild headache, Severe headache, Slight headache, Slightly tired, Mild fatigue, Excessive fatigue, Severe fatigue, Feeling weak, Severe weakness, Slight fever, Mild fever, High fever, High fever, Convulsions, Swelling of the neck, Swollen lymph nodes, Skin rash, Facial rash, Body rash")
import majul #فراخوانی ماژول
#majul.inputing()  #فراخوانی تابع دریافت مسئله

print('now its time to say about your self information') #منوی ورودی
x=input("enter your name")
y=input("enter your gender")
w=input("enter your age")
z=int(input("enter the number of your request"))

#کلاس اطلاعات مراجعه کننده
class USE():
    name=None
    gender=None
    age=None
    cost=None
    
    def __init__(self,name,gender,age,cost):  #تابع init ،  محاسبه هزینه
        self.name=name
        self.gender=gender
        self.age=age
        self.cost=cost*10    #محاسبه هزینه
    def display(self):   #تابع چاپ اطلاعات کاربر
        print(f"your info: \n name: {self.name}   gender: {self.gender}   age: {self.age}")
    def printbill(self):   #تابع چاپ فاکتور
        print(f"your bill:\n  name: {self.name}    gender: {self.gender}   age: {self.age}  cost in $: {self.cost}  ")

user=USE(x,y,w,z)   #تعریف یک شی از کلاس
user.display()   #فراخوانی تابع چاپ اطلاعات کلاس
user.printbill()   #فراخوانی تابع چاپ فاکتور کلاس

majul.answering(int)  #فراخوانی تابع چاپ پاسخ