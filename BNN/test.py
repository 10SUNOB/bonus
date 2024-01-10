import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data.csv")
q1=df["ประเภทอาหารที่ชื่นชอบ"]
a1=list(df["น้ำที่ทานคู่"])
a2=list(df["ประมาณราคาอาหารรวมทั้งหมด"])
plotdata = pd.DataFrame(
    {
 "q1":a1,
    "q2":a2,
  }, 
    index=q1)
plotdata.plot(kind="bar")
plt.show()