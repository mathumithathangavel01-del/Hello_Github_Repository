import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={"Hours_studied":[2,5,3,7,1,6,4,8,5,3],
      "Attendance":[60,90,75,95,50,88,80,98,85,70],
      "Previous_score":[45,70,55,82,40,78,65,90,72,58],
      "Final_score":[45,76,58,88,35,82,68,94,79,60],
      "Assignments":[5,8,9,6,7,10,8,9,7,10],
      "Study_Material":[1,2,3,2,1,3,2,3,2,3],
      "Test_Attempts":[2,3,4,2,3,5,3,4,2,5],
      "Class_Participation":[70,80,90,60,75,95,85,90,70,98],
      "Revision_Hours":[1,2,3,1,2,4,2,3,2,5]
      }


df=pd.DataFrame(data)
print(df.head())
print("shape:",df.shape)
print(df.isnull().sum())
sns.barplot(data=df,x="Hours_studied",y="Final_score")
plt.title("Study Hours vs Final Score")
plt.show()
