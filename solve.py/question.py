date=input("Enter the date: "):-
# 1:- iss line user se input liya ja raha hai date ka input liya ja raha hai"
dd,mm,yy=date.split('/'):-
# 2:- iss line ke code mein dd,mm,yy=date (dd ka matlab hai date aur mm ka matlab hai month aur yy ka mtlab hai year and then )and ye jo split likkha gaya hai code mein iska matlabb hai date and month and year ko alag alag space dekar print kar raha hai  
dd=int(dd):-
# 3:-  iss line mein dd(date ko intiger mein convert kiya ja raha hai)
mm=int(mm):-
# 4:- iss mein code mm (month ko intiger mein convert kitya ja raha hai)
yy=int(yy):-
# 5:- iss mein code yy (year ki value ko intiser maein convert kiya ja raha hai)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31:-
# 6:- iss line ke code mein (agar month ki value 1 hai to aur phir kah raha hai ki agar month value 3 hai ya 5 ya 7 ya 7 ya 8 10 ya 12 agar inn value mein se ek bhi value sahi hai inn ki   value jyada se jyada 31 one ho sakti hai)
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30:-
# 7:- iss line mein month ki value (4 ya 6 ya 9 ya 11 hai inamein se koi bhi month ki value input mein di jati hai )ousak jyada se jyada 30ho sakti hai 
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29:-
# 8:- iss line ke code mein agar (year ki value 4 se divide hoti hai aur remander zero bachta haito month ki las value 29 ho sakti hai aur agar year ki value 100 se divide nahi hota hai aur remander 0 bachta hai and aur year ki value 400 se dividde ho jati haiur remande zero bachta hai to month ki last value 29 ho sakti hai)
else:
    max1=28:-
# 9:- iss line ke code mein agar if wali conditon wrong hoti hai to else: wali condition ko excute karega jisaki last value  28 hogi
if(mm<1 or mm>12):
    print("Date is invalid."):-
# 10:- iss line ke code mein yeh kaha ja raha hai ki agar month ki value 1 se chtoi hai ya phir month ki value 12 se badi hai to print kar do date invalid hai 
elif(dd<1 or dd>max1):
    print("Date is invalid."):-
# 11:- iss line ke code mein yeh batya ja raha hai ki agar date ki value agar 11 se choti hai ya phir date ki value max1 1 se badi hai max1 ki char value hai in charon mein se ek bhi value excute nahi karta hai to (print kar do date invalid hai)
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yy)
# 12:- iss line ke code mein date ki value mein ek 1+ kiya jayega aur month  ki value mein 1jode diya jayega aur year ki value ko same print kiya ja raha hai  
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy):-
# 13:- iss line ke code mein agar date ki value 31 hai aur month 12 hai to date ki value mein ek + kar do aur month ki value mein bhi 1+ kar diya jayega aur year ki  value mein bhi ek + kiya ja raha hai
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)
# 14:- iss line ke code mein date ki value mein 1+ kar do (then after date ki value mein 1+ karne ke bad month aur year ki value mein ko same print kar do)
    
