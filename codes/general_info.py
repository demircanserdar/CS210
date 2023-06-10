party_counts = data['Party'].value_counts()


plt.figure(figsize=(6, 6))
plt.pie(party_counts, labels=party_counts.index, autopct='%1.1f%%', startangle=90,)
plt.title('Political Party Distribution')
plt.axis('equal') 
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(10, 10))


axs[0, 0].pie(data['Gender'].value_counts(), labels=data['Gender'].unique(), autopct='%.1f%%')
axs[0, 0].set_title("Gender Distribution")


axs[0, 1].pie(data['Age'].value_counts(), labels=data['Age'].unique(), autopct='%.1f%%')
axs[0, 1].set_title("Age Distribution")


axs[1, 0].pie(data['Region'].value_counts(), labels=data['Region'].unique(), autopct='%.1f%%')
axs[1, 0].set_title("Region Distribution")


axs[1, 1].pie(data['Education'].value_counts(), labels=data['Education'].unique(), autopct='%.1f%%')
axs[1, 1].set_title("Distribution of Educational Levels")

plt.tight_layout()


plt.show()


education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']


pivot_table = data.pivot_table(index='Party', columns='Education', aggfunc='size', fill_value=0)
percentage_table = pivot_table.apply(lambda x: x / x.sum() * 100, axis=1)


percentage_table = percentage_table.reindex(columns=education_order)


percentage_table.plot(kind='bar', stacked=True)
plt.xlabel('Party')
plt.ylabel('Percentage')
plt.title('Percentage of Education Values for Each Party')
plt.legend(title='Education')
plt.show()

pivot_table = data.pivot_table(index='Party', columns='Age', aggfunc='size', fill_value=0)
percentage_table = pivot_table.apply(lambda x: x / x.sum() * 100, axis=1)

percentage_table.plot(kind='bar', stacked=True)
plt.xlabel('Party')
plt.ylabel('Percentage')
plt.title('Percentage of Parties by Age Group')
plt.legend(title='Age')
plt.show()


pivot_table = data.pivot_table(index='Party', columns='Gender', aggfunc='size', fill_value=0)
percentage_table = pivot_table.apply(lambda x: x / x.sum() * 100, axis=1)

percentage_table.plot(kind='bar', stacked=True)
plt.xlabel('Party')
plt.ylabel('Percentage')
plt.title('Percentage of Gender Values for Each Party')
plt.legend(title='Gender')
plt.show()
