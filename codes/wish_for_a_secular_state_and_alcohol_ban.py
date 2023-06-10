subset = data[['SUPPORT_ALCOHOL_BAN', 'SUPPORT_SECULARISM']]

count_yes_no = subset.apply(pd.Series.value_counts)

count_yes_no.plot(kind='bar', rot=0)

plt.xlabel('Response')
plt.ylabel('Count')
plt.title('Number of "Yes" and "No" Responses')

plt.xticks([0, 1], ['No', 'Yes'])


plt.show()


education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

grouped_question6 = data.groupby(['Education', 'SUPPORT_ALCOHOL_BAN']).size().unstack()

grouped_question6 = grouped_question6.reindex(education_order, axis=0)

grouped_question6.plot(kind='bar')

plt.xlabel('Education Level')
plt.ylabel('Count')
plt.title('Relationship between Education and Alcohol Ban')

plt.show()

grouped_question7 = data.groupby(['Education', 'SUPPORT_SECULARISM']).size().unstack()

grouped_question7 = grouped_question7.reindex(education_order, axis=0)

grouped_question7.plot(kind='bar')

plt.xlabel('Education Level')
plt.ylabel('Count')
plt.title('Relationship between Education and Wish for a Secular State')

plt.show()

education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

grouped = data.groupby(['Education', 'SUPPORT_ALCOHOL_BAN', 'SUPPORT_SECULARISM']).size().unstack().unstack()

grouped = grouped.reindex(education_order)

grouped.plot(kind='bar', stacked=True)

plt.xlabel('Education Level')
plt.ylabel('Count')
plt.title('Relationship between Education, Alcohol Ban, and Wish for a Secular State')

plt.show()

grouped = data.groupby(['Party', 'SUPPORT_ALCOHOL_BAN']).size().unstack()

grouped.plot(kind='bar', stacked=True)

plt.xlabel('Political Party')
plt.ylabel('Count')
plt.title('Relationship between Alcohol Ban and Political Party')

plt.show()

grouped_question7 = data.groupby(['Party', 'SUPPORT_SECULARISM']).size().unstack()

grouped_question7.plot(kind='bar', stacked=True)

plt.xlabel('Political Party')
plt.ylabel('Count')
plt.title('Relationship between Wish for a Secular State and Political Party')

plt.show()

support_abortion_ban_edu = data[data['SUPPORT_ALCOHOL_BAN'] == 'Yes'].groupby('Education').size()
oppose_abortion_ban_edu = data[data['SUPPORT_ALCOHOL_BAN'] == 'No'].groupby('Education').size()
total_by_edu = data.groupby('Education').size()
percentage_support_edu = (support_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')
percentage_oppose_edu = (oppose_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')

percentage_support_edu['Position'] = 'Support'
percentage_oppose_edu['Position'] = 'Oppose'
percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])


education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')
scatter_data = percentage_data_edu[percentage_data_edu['Position'] == 'Oppose']
education_mapping = {education: i for i, education in enumerate(education_order)}
scatter_data['Education_Num'] = scatter_data['Education'].map(education_mapping)

plt.figure(figsize=(10, 6))
sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None)
plt.xticks(ticks=range(len(education_order)), labels=education_order, rotation=45)
plt.xlabel('Education Level')
plt.ylabel('Percentage of Opposition (%)')
plt.title('Correlation between Education Level and Opposition to Alcohol Ban')
plt.show()


support_abortion_ban_edu = data[data['SUPPORT_SECULARISM'] == 'Yes'].groupby('Education').size()
oppose_abortion_ban_edu = data[data['SUPPORT_SECULARISM'] == 'No'].groupby('Education').size()
total_by_edu = data.groupby('Education').size()
percentage_support_edu = (support_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')
percentage_oppose_edu = (oppose_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')

percentage_support_edu['Position'] = 'Support'
percentage_oppose_edu['Position'] = 'Oppose'
percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])

education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')
scatter_data = percentage_data_edu[percentage_data_edu['Position'] == 'Support']
education_mapping = {education: i for i, education in enumerate(education_order)}
scatter_data['Education_Num'] = scatter_data['Education'].map(education_mapping)

plt.figure(figsize=(10, 6))
sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None)
plt.xticks(ticks=range(len(education_order)), labels=education_order, rotation=45)
plt.xlabel('Education Level')
plt.ylabel('Percentage of Support (%)')
plt.title('Correlation between Education Level and Support for a Secular State')
plt.show()
