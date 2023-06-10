def calculate_percentage(position, position_label):
    party_position = data[data['SUPPORT_EDUCATIONAL_REFORM'] == position].groupby('Party').size()
    percentage = (party_position / total_by_party * 100).reset_index(name='Percentage')
    percentage['Position'] = position_label
    return percentage

total_by_party = data.groupby('Party').size()

percentage_support = calculate_percentage('Yes', 'Support')
percentage_oppose = calculate_percentage('No', 'Oppose')

percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Party', x='Percentage', hue='Position', data=percentage_data, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Party')
plt.title('Percentage of Support and Opposition for Educational Reform by Party')
plt.legend(title='Position on Educational Reform')
plt.show()

def calculate_percentage(position, position_label):
    party_position = data[data['SUPPORT_EDUCATIONAL_REFORM'] == position].groupby('Age').size()
    percentage = (party_position / total_by_party * 100).reset_index(name='Percentage')
    percentage['Position'] = position_label
    return percentage

total_by_party = data.groupby('Age').size()

percentage_support = calculate_percentage('Yes', 'Support')
percentage_oppose = calculate_percentage('No', 'Oppose')

percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Age', x='Percentage', hue='Position', data=percentage_data, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Age Group')
plt.title('Percentage of Support and Opposition for Educational Reform by Age Group')
plt.legend(title='Position on Educational Reform')
plt.show()

def calculate_percentage_for_group(group_condition, position_label):
    group_data = data[data['SUPPORT_EDUCATIONAL_REFORM'] == group_condition].groupby('Education').size()
    total_data = data.groupby('Education').size()
    percentage_group = (group_data / total_data * 100).reset_index(name='Percentage')
    percentage_group['Position'] = position_label
    return percentage_group

education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_support_edu = calculate_percentage_for_group('Yes', 'Support')
percentage_oppose_edu = calculate_percentage_for_group('No', 'Oppose')
percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])

percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')

# Create subplots
fig, axs = plt.subplots(1, len(education_order), figsize=(len(education_order)*6, 6))

for i, edu in enumerate(education_order):
    data_for_edu = percentage_data_edu[percentage_data_edu['Education'] == edu]
    axs[i].pie(data_for_edu['Percentage'], labels=data_for_edu['Position'], autopct='%1.1f%%', startangle=90)
    axs[i].set_title(edu)

plt.suptitle('Percentage of Support and Opposition for Educational Reform by Education Level')
plt.show()

def calculate_percentage_for_group(condition, position_label):
    group = data[data['SUPPORT_EDUCATIONAL_REFORM'] == condition].groupby('Education').size()
    total = data.groupby('Education').size()
    percentage_group = (group / total * 100).reset_index(name='Percentage')
    percentage_group['Position'] = position_label
    return percentage_group

def create_plot(scatter_data, education_order, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None)
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

create_plot(scatter_data, education_order, 'Education Level', 'Percentage of Opposition (%)', 'Correlation between Education Level and Opposition for Educational Reform')	
def calculate_percentage(position, position_label):
    party_position = data[data['SUPPORT_NEW_PARTIES'] == position].groupby('Party').size()
    percentage = (party_position / total_by_party * 100).reset_index(name='Percentage')
    percentage['Position'] = position_label
    return percentage

total_by_party = data.groupby('Party').size()

percentage_support = calculate_percentage('Yes', 'Support')
percentage_oppose = calculate_percentage('No', 'Oppose')

percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Party', x='Percentage', hue='Position', data=percentage_data, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Party')
plt.title('Percentage of Support and Opposition for New Parties by Party')
plt.legend(title='Position on New Parties')
plt.show()

def calculate_percentage(position, position_label):
    party_position = data[data['SUPPORT_NEW_PARTIES'] == position].groupby('Age').size()
    percentage = (party_position / total_by_party * 100).reset_index(name='Percentage')
    percentage['Position'] = position_label
    return percentage

total_by_party = data.groupby('Age').size()

percentage_support = calculate_percentage('Yes', 'Support')
percentage_oppose = calculate_percentage('No', 'Oppose')

percentage_data = pd.concat([percentage_support, percentage_oppose])

plt.figure(figsize=(10, 6))
sns.barplot(y='Age', x='Percentage', hue='Position', data=percentage_data, orient='h')
plt.xlabel('Percentage (%)')
plt.ylabel('Age Group')
plt.title('Percentage of Support and Opposition for New Parties by Age Group')
plt.legend(title='Position on New Parties')
plt.show()

def calculate_percentage_for_group(group_condition, position_label):
    group_data = data[data['SUPPORT_NEW_PARTIES'] == group_condition].groupby('Education').size()
    total_data = data.groupby('Education').size()
    percentage_group = (group_data / total_data * 100).reset_index(name='Percentage')
    percentage_group['Position'] = position_label
    return percentage_group

education_order = ['Primary School', 'Middle School', 'Highschool', 'Associate Degree', 'Bachelor Degree', 'Masters Degree']

percentage_support_edu = calculate_percentage_for_group('Yes', 'Support')
percentage_oppose_edu = calculate_percentage_for_group('No', 'Oppose')
percentage_data_edu = pd.concat([percentage_support_edu, percentage_oppose_edu])

percentage_data_edu['Education'] = pd.Categorical(percentage_data_edu['Education'], categories=education_order, ordered=True)
percentage_data_edu = percentage_data_edu.sort_values('Education')

fig, axs = plt.subplots(1, len(education_order), figsize=(len(education_order)*6, 6))

for i, edu in enumerate(education_order):
    data_for_edu = percentage_data_edu[percentage_data_edu['Education'] == edu]
    axs[i].pie(data_for_edu['Percentage'], labels=data_for_edu['Position'], autopct='%1.1f%%', startangle=90)
    axs[i].set_title(edu)

plt.suptitle('Percentage of Support and Opposition for New Parties by Education Level')
plt.show()

def calculate_percentage_for_group(condition, position_label):
    group = data[data['SUPPORT_NEW_PARTIES'] == condition].groupby('Education').size()
    total = data.groupby('Education').size()
    percentage_group = (group / total * 100).reset_index(name='Percentage')
    percentage_group['Position'] = position_label
    return percentage_group

def create_plot(scatter_data, education_order, xlabel, ylabel, title):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Education_Num', y='Percentage', data=scatter_data, ci=None)
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

create_plot(scatter_data, education_order, 'Education Level', 'Percentage of Opposition (%)', 'Correlation between Education Level and Opposition to New Parties')
