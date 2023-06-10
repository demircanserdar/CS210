abortion_support = data['SUPPORT_ABORTION_BAN'].value_counts(normalize=True) * 100
abortion_support.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Support for Abortion Ban')
plt.ylabel('')
plt.show()
support_abortion_ban_party = data[data['SUPPORT_ABORTION_BAN'] == 'Yes'].groupby('Party').size()
oppose_abortion_ban_party = data[data['SUPPORT_ABORTION_BAN'] == 'No'].groupby('Party').size()
total_by_party = data.groupby('Party').size()
percentage_support_party = (support_abortion_ban_party / total_by_party * 100).reset_index(name='Percentage')
percentage_oppose_party = (oppose_abortion_ban_party / total_by_party * 100).reset_index(name='Percentage')

percentage_support_party['Position'] = 'Support'
percentage_oppose_party['Position'] = 'Oppose'
percentage_data_party = pd.concat([percentage_support_party, percentage_oppose_party])


party_order = ['AKP', 'MHP', 'IYI PARTI', 'HDP', 'CHP']

percentage_data_party['Party'] = pd.Categorical(percentage_data_party['Party'], categories=party_order, ordered=True)
percentage_data_party = percentage_data_party.sort_values('Party')

plt.figure(figsize=(10, 6))
sns.barplot(y='Party', x='Percentage', hue='Position', data=percentage_data_party, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Parties')
plt.title('Percentage of Support and Opposition for Abortion Ban by Party Affiliation')
plt.legend(title='Position on Abortion Ban')
plt.show()
party_mapping = {party: i for i, party in enumerate(party_order)}
percentage_support_party['PartyMapped'] = percentage_support_party['Party'].map(party_mapping)

plt.figure(figsize=(10, 6))
sns.lmplot(data=percentage_support_party, x='PartyMapped', y='Percentage', order=1, ci=None, line_kws={'color':'red'}, scatter_kws={'alpha':0.5})
plt.xlabel('Parties')
plt.ylabel('Percentage of Support (%)')
plt.title('Percentage of Support for Abortion Ban by Party Affiliation')
plt.xticks(list(party_mapping.values()), list(party_mapping.keys()))
plt.show()
support_abortion_ban_age = data[data['SUPPORT_ABORTION_BAN'] == 'Yes'].groupby('Age').size()
oppose_abortion_ban_age = data[data['SUPPORT_ABORTION_BAN'] == 'No'].groupby('Age').size()
total_by_age = data.groupby('Age').size()
percentage_support_age = (support_abortion_ban_age / total_by_age * 100).reset_index(name='Percentage')
percentage_oppose_age = (oppose_abortion_ban_age / total_by_age * 100).reset_index(name='Percentage')

percentage_support_age['Position'] = 'Support'
percentage_oppose_age['Position'] = 'Oppose'
percentage_data_age = pd.concat([percentage_support_age, percentage_oppose_age])

plt.figure(figsize=(10, 6))
sns.barplot(y='Age', x='Percentage', hue='Position', data=percentage_data_age, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Age Group')
plt.title('Percentage of Support and Opposition for Abortion Ban by Age Group')
plt.legend(title='Position on Abortion Ban')
plt.show()
support_abortion_ban_edu = data[data['SUPPORT_ABORTION_BAN'] == 'Yes'].groupby('Education').size()
oppose_abortion_ban_edu = data[data['SUPPORT_ABORTION_BAN'] == 'No'].groupby('Education').size()
total_by_edu = data.groupby('Education').size()
percentage_support_edu = (support_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')
percentage_oppose_edu = (oppose_abortion_ban_edu / total_by_edu * 100).reset_index(name='Percentage')

percentage_support_edu['Position'] = 'Support'
percentage_oppose_edu['Position'] = 'Oppose'
percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])


education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')

support_abortion_ban_edu = data[data['SUPPORT_ABORTION_BAN'] == 'Yes'].groupby('Education').size()
oppose_abortion_ban_edu = data[data['SUPPORT_ABORTION_BAN'] == 'No'].groupby('Education').size()
total_by_edu = data.groupby('Education').size()

plt.figure(figsize=(10, 6))
sns.barplot(y='Education', x='Percentage', hue='Position', data=percentage_data_edu, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Education Level')
plt.title('Percentage of Support and Opposition for Abortion Ban by Education Level')
plt.legend(title='Position on Abortion Ban')
plt.show()
scatter_data = percentage_data_edu[percentage_data_edu['Position'] == 'Oppose']
education_mapping = {education: i for i, education in enumerate(education_order)}
scatter_data['Education_Num'] = scatter_data['Education'].map(education_mapping)

plt.figure(figsize=(10, 6))
sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None)
plt.xticks(ticks=range(len(education_order)), labels=education_order, rotation=45)
plt.xlabel('Education Level')
plt.ylabel('Percentage of Opposition (%)')
plt.title('Correlation between Education Level and Opposition to Abortion Ban')
plt.show()
