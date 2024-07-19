


def inputing():  #تابع دریافت مسئله

    problem =input("your text should be atleast 4 sentences about your feelings and body mood.    ")
    return(problem)


#دیکشنری های علائم     

inflation={"Swelling of the neck":4,"Swelling of the lymph nodes":5,"Skin rash":4,"Facial rash":4,"Body rash":5}
Slight={"Slight fever":1, "Slightly tired":2, "Slight headache":1,"Temporal pain":4,"Feeling weak":1, "body aches":1}
mild={"Mild pain":2, "Mild fatigue":2, "Mild headache":2 , "mild fever":2,"high fever":3}
severe={"severe fever":4, "Severe fatigue":4, "Severe pain":5, "Severe headache":5,"Severe weakness":3}
hurt={"Muscle pain":4, "back pain":3, "Dizziness":3, "Excessive fatigue":5,"Convulsions":5}

slightkeys=list(Slight.keys())   #زخیره کلید های دیکشنری در یک لیست
mildkeys=list(mild.keys()) #زخیره کلید های دیکشنری در یک لیست
severekeys=list(severe.keys()) #زخیره کلید های دیکشنری در یک لیست
hurtkeys=list(hurt.keys())  #زخیره کلید های دیکشنری در یک لیست
inflationkeys=list(inflation.keys())  #زخیره کلید های دیکشنری در یک لیست

u=inputing()
problemlist=u.split(",")  #تبدیل رشته مسئله به لیست

def finding(): #تابع یافتن پاسخ

     commons1 = list(set(slightkeys).intersection(problemlist))   # پیدا کردن لیستی از مشترکات بین لیست مسئله و لیست کلیدهای دیکشنری
     commons2 = list(set(mildkeys).intersection(problemlist))   #پیدا کردن لیستی از مشترکات بین لیست مسئله و لیست کلیدهای دیکشنری
     commons3 = list(set(severekeys).intersection(problemlist))   #پیدا کردن لیستی از مشترکات بین لیست مسئله و لیست کلیدهای دیکشنری
     commons4 = list(set(hurtkeys).intersection(problemlist))   #پیدا کردن لیستی از مشترکات بین لیست مسئله و لیست کلیدهای دیکشنری
     commons5 = list(set(inflationkeys).intersection(problemlist))   #پیدا کردن لیستی از مشترکات بین لیست مسئله و لیست کلیدهای دیکشنری
     answer=0
     answer+=len(commons1)
     answer+=len(commons2)*2
     answer+=len(commons3)*3
     answer+=len(commons4)*3
     answer+=len(commons5)*4
     return(answer)




a=finding()   #زخیره مقدار برگشتی تابع فراخوانی شده
#دیکشنری پاسخ
result ={1:"Your chances of getting sick are very low and there is no need to worry",
2:"You are less likely to get sick. If you have symptoms, try again",
3:"You are moderately likely to be sick, so stay in quarantine for a few days and rest. See your doctor if your symptoms worsen.",
4:" Most likely you are sick, be sure to stay in quarantine and see a doctor if symptoms persist", 
5:" You are very very likely to be sick, be sure to be in quarantine and see a doctor as soon as possible"}

#تابع چاپ پاسخ
def answering(int):
    if 0<=a<3:
         print(result.get(1))
    if 3<=a<6:
         print(result.get(2))
    if 6<=a<10:
         print(result.get(3))
    if 10<=a<=13:
         print(result.get(4))
    if a>13:
         print(result.get(5))
