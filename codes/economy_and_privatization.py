data_serdar=data[["Gender","Age","Region", "Education", "GOOD_ECONOMY", "STOP_PRIVATIZATION","Party"]]
fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
axes[0].pie(data_serdar["GOOD_ECONOMY"].value_counts(),labels=data_serdar["GOOD_ECONOMY"].value_counts().index, autopct='%1.1f%%')
axes[0].set_title("Do you believe we are economically stable?")
data_party=data_serdar[data_serdar['STOP_PRIVATIZATION']=='Yes']['Party'].value_counts()
axes[1].pie(data_serdar["STOP_PRIVATIZATION"].value_counts(),labels=data_serdar["STOP_PRIVATIZATION"].value_counts().index, autopct='%1.1f%%')
axes[1].set_title("Are you against privatization?")
plt.show()

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
data_party=data_serdar[data_serdar['GOOD_ECONOMY']=='No']['Party'].value_counts()
axes[0].pie(data_party,labels=data_party.index, autopct='%1.1f%%')
axes[0].set_title("Economy is bad")
data_party=data_serdar[data_serdar['STOP_PRIVATIZATION']=='Yes']['Party'].value_counts()
axes[1].pie(data_party,labels=data_party.index, autopct='%1.1f%%')
axes[1].set_title("Stop privatization")
plt.suptitle("Answers by party voters")
plt.show()

data_serdar=data[["Gender","Age","Region", "Education", "GOOD_ECONOMY", "STOP_PRIVATIZATION","Party"]]
list_attribute=["Age", "Education", "Region"]
list_q=["GOOD_ECONOMY", "STOP_PRIVATIZATION"]

fig, axes = plt.subplots(ncols=4, figsize=(20, 6))

data_attribute1 = data_serdar.groupby(["Age", 'GOOD_ECONOMY']).size().unstack()
data_attribute1.plot(kind='bar', stacked=True, ax=axes[0])
data_attribute2 = data_serdar.groupby(["Gender", 'GOOD_ECONOMY']).size().unstack()
data_attribute2.plot(kind='bar', stacked=True, ax=axes[1])
data_attribute3 = data_serdar.groupby(["Education", 'GOOD_ECONOMY']).size().unstack()
data_attribute3.plot(kind='bar', stacked=True, ax=axes[2])
data_attribute4 = data_serdar.groupby(["Region", 'GOOD_ECONOMY']).size().unstack()
data_attribute4.plot(kind='bar', stacked=True, ax=axes[3])
plt.suptitle("Do you believe that the economy is in a good condition?")
for i in range(0,4):
  axes[i].legend(title="Answers")
plt.show()

fig, axes = plt.subplots(ncols=4, figsize=(20, 6))

data_attribute1 = data_serdar.groupby(["Age", 'STOP_PRIVATIZATION']).size().unstack()
data_attribute1.plot(kind='bar', stacked=True, ax=axes[0])
data_attribute2 = data_serdar.groupby(["Gender", 'STOP_PRIVATIZATION']).size().unstack()
data_attribute2.plot(kind='bar', stacked=True, ax=axes[1])
data_attribute3 = data_serdar.groupby(["Education", 'STOP_PRIVATIZATION']).size().unstack()
data_attribute3.plot(kind='bar', stacked=True, ax=axes[2])
data_attribute4 = data_serdar.groupby(["Region", 'STOP_PRIVATIZATION']).size().unstack()
data_attribute4.plot(kind='bar', stacked=True, ax=axes[3])
plt.suptitle("Are you against privatization?")
for i in range(0,4):
  axes[i].legend(title="Answers")

plt.show()
