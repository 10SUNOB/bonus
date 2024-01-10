import matplotlib as mlt
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('data.csv')

#ใส่ Font ภาษาไทย
mlt.font_manager.fontManager.addfont('Sarabun-Regular.ttf')
mlt.rc('font', family='Sarabun',size=7)

#นับจำนวน
def count(k,l):
  m = list(df[l])
  x = 0
  for t in m :
    if k == t :
      x = x + 1
  return x

#ประเภทอาหาร
menu = ['ข้าวหมกไก่','ข้าวมันไก่','ข้าวขาหมู','ข้าวไก่เทอริยากิ','ข้าวยำ','เมนูเส้น','เกาเหลา','ข้าวราดแกง']
cag = []

for j in menu :
  cag.append(count(j,'ประเภทอาหารที่ชื่นชอบ'))

color = ['lightblue', 'blue', 'purple', 'red', 'black']


plt.bar(menu,cag,color=color)
plt.title('ประเภทอาหารที่ชื่นชอบ')
plt.ylabel('จำนวนคน')
plt.xlabel('ประเภทอาหาร')
plt.show()

df.head(0)

#น้ำที่ทานคู่
drink = ['น้ำเปล่า','โกโก้','ชาเย็น','ชาเขียว','ชาดำเย็น','ชามะนาว','น้ำแดง','แดงมะนาวโซดา','โอริโอ้ปั่น','โยเกิร์ตปั่น','นมปั่น','ไมโล']
cagdrink = []

for j in drink :
  cagdrink.append(count(j,'น้ำที่ทานคู่'))

plt.plot(drink,cagdrink)
plt.title('น้ำที่ทานคู่')
plt.show()
print(cagdrink)

#ประมาณราคาอาหารรวมทั้งหมดที่ทาน
money = ['35-45 บาท','45-55 บาท','55-65 บาท','65-75 บาท','75-85 บาท','85-100 บาท']
cagmoney = []

for j in money :
  cagmoney.append(count(j,'ประมาณราคาอาหารรวมทั้งหมด'))

plt.pie(cagmoney,labels=money)
plt.title('ประมาณราคาอาหารรวมทั้งหมดที่ทาน')
plt.show()
print(cagdrink)

#ของว่างที่ชอบทาน
desert = ['ไก่ทอด','มันเกลียว','โตเกียว','ขนมปังปิ้ง','คอร์นด็อก','ผลไม้','ไอศครีม']
cagdesert = []

for j in desert :
  cagdesert.append(count(j,'ของว่างที่ชอบทาน'))

plt.bar(desert,cagdesert,color=color)
plt.title('ของว่างที่ชอบทาน')
plt.ylabel('จำนวนคน')
plt.xlabel('ประเภทของว่าง')
plt.show()

#อาคารที่นำอาหารไปรับประทาน
builting = ['อาคาร 6','อาคาร 9','อาคาร 84','สระว่ายน้ำ']
cagbuilting = []

for j in builting :
  cagbuilting.append(count(j,'อาคารที่นำอาหารไปรับประทาน'))

plt.bar(builting,cagbuilting,color=color)
plt.title('อาคารที่นำอาหารไปรับประทาน')
plt.ylabel('จำนวนคน')
plt.xlabel('สถานที่')
plt.show()