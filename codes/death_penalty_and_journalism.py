# Mert Kağan AYCAN 29489


support_death_penalty_age = data[data['DEATH_PENALTY'] == 'Yes'].groupby('Age').size()
oppose_death_penalty_age = data[data['DEATH_PENALTY'] == 'No'].groupby('Age').size()
total_by_age = data.groupby('Age').size()
percentage_support_age = (support_death_penalty_age / total_by_age * 100).reset_index(name='Percentage')
percentage_oppose_age = (oppose_death_penalty_age / total_by_age * 100).reset_index(name='Percentage')

percentage_support_age['Position'] = 'Support'
percentage_oppose_age['Position'] = 'Oppose'
percentage_data_age = pd.concat([percentage_support_age, percentage_oppose_age])

plt.figure(figsize=(10, 6))
sns.barplot(y='Age', x='Percentage', hue='Position', data=percentage_data_age, orient='h', palette=['#68228B', '#00FF00'])
plt.xlabel('Percentage (%)')
plt.ylabel('Age Group')
plt.title('Percentage of Support and Opposition for Death Penalty by Age Group')
plt.legend(title='Position on Death Penalty')
plt.show()


support_death_ban = data[data['DEATH_PENALTY'] == 'Yes'].groupby('Party').size()
oppose_death_ban = data[data['DEATH_PENALTY'] == 'No'].groupby('Party').size()
total_by_party = data.groupby('Party').size()
percentage_support = (support_death_ban / total_by_party * 100).reset_index(name='Percentage')
percentage_oppose = (oppose_death_ban / total_by_party * 100).reset_index(name='Percentage')
percentage_support['Position'] = 'Support'
percentage_oppose['Position'] = 'Oppose'
percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Party', x='Percentage', hue='Position', data=percentage_data, orient='h', palette=['#68228B', '#00FF00'])
plt.xlabel('Percentage (%)')
plt.ylabel('Party')
plt.title('Percentage of Agreement and Disagreement on neutrality of journalists by Party')
plt.legend(title='Position on neutrality of journalists')
plt.show()


def calculate_percentage(position, position_label):
    party_position = data[data['FREE_MEDIA'] == position].groupby('Age').size()
    percentage = (party_position / total_by_party * 100).reset_index(name='Percentage')
    percentage['Position'] = position_label
    return percentage

total_by_party = data.groupby('Age').size()

percentage_support = calculate_percentage('Yes', 'Agree')
percentage_oppose = calculate_percentage('No', 'Disagree')

percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Age', x='Percentage', hue='Position', data=percentage_data, orient='h', palette=['#68228B', '#00FF00'])
plt.xlabel('Percentage (%)')
plt.ylabel('Age Group')
plt.title('Percentage of Agreement and Disagreement on neutrality of journalists by Age Group')
plt.legend(title='Position on Educational Reform')
plt.show()
support_death_penalty_party = data[data['DEATH_PENALTY'] == 'Yes'].groupby('Party').size()
oppose_death_penalty_party = data[data['DEATH_PENALTY'] == 'No'].groupby('Party').size()
total_by_party = data.groupby('Party').size()
percentage_support_party = (support_death_penalty_party / total_by_party * 100).reset_index(name='Percentage')
percentage_oppose_party = (oppose_death_penalty_party / total_by_party * 100).reset_index(name='Percentage')
percentage_support_party['Position'] = 'Support'
percentage_oppose_party['Position'] = 'Oppose'
percentage_data_party = pd.concat([percentage_support_party, percentage_oppose_party])

plt.figure(figsize=(10, 6))
sns.barplot(y='Party', x='Percentage', hue='Position', data=percentage_data_party, orient='h', palette=['#68228B', '#00FF00'])
plt.xlabel('Percentage (%)')
plt.ylabel('Party')
plt.title('Percentage of Support and Opposition for Death Penalty by Party')
plt.legend(title='Position on Death Penalty')
plt.show()
def calculate_percentage_for_group(condition, position_label):
    group = data[data['DEATH_PENALTY'] == condition].groupby('Education').size()
    total = data.groupby('Education').size()
    percentage_group = (group / total * 100).reset_index(name='Percentage')
    percentage_group['Position'] = position_label
    return percentage_group

def create_plot(scatter_data, education_order, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None, scatter_kws={'color': 'red'})
    plt.xticks(ticks=range(len(education_order)), labels=education_order, rotation=45)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_support_edu = calculate_percentage_for_group('Yes', 'Support')
percentage_oppose_edu = calculate_percentage_for_group('No', 'Oppose')

percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])
percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')

scatter_data = percentage_data_edu[percentage_data_edu['Position'] == 'Oppose']
education_mapping = {education: i for i, education in enumerate(education_order)}
scatter_data['Education_Num'] = scatter_data['Education'].map(education_mapping)

create_plot(scatter_data, education_order, 'Education Level', 'Percentage of Opposition (%)', 'Correlation between Education Level and Opposition to Death Penalty')
