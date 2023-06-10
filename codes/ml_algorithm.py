from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

mldata = pd.DataFrame()


mldata['Gender'] = data['Gender'].replace({'Male': 0, 'Female': 1})

mldata['Age'] = data['Age'].replace({'0-18': 0, '18-30': 1, '30-50': 2, '50-60': 3, '60+': 4})

mldata['Region'] = data['Region'].replace({'Marmara': 0, 'Guneydogu': 1, 'Akdeniz': 2, 'Dogu Anadolu': 3, 'Ic Anadolu': 4, 'Ege' : 5, 'Karadeniz' : 6})


mldata['Education'] = data['Education'].replace({
    'Primary School': 0, 'Middle School': 1, 'Highschool': 2,
    'Associate Degree': 3, 'Bachelor Degree': 4, 'Masters Degree': 5
})


mldata['Party'] = data['Party'].replace({
    'AKP': 0, 'IYI PARTI': 1, 'CHP': 2, 'HDP': 3, 'MHP': 4, 'OTHER': 5
})


question_cols = ['GOOD_ECONOMY', 'SUPPORT_EDUCATIONAL_REFORM', 'STOP_PRIVATIZATION',
                 'DEATH_PENALTY', 'FREE_MEDIA', 'SUPPORT_ALCOHOL_BAN',
                 'SUPPORT_SECULARISM', 'SUPPORT_ABORTION_BAN', 'OHAL_LIMITS_FREEDOM',
                 'SUPPORT_NEW_PARTIES']

mldata[question_cols] = data[question_cols].replace({'Yes': 1, 'No': 0})

X = mldata.drop("Party", axis=1)
y = mldata['Party']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_classifier = GaussianNB()
dt_classifier = DecisionTreeClassifier()
rf_classifier = RandomForestClassifier()
knn_classifier = KNeighborsClassifier()
svm_classifier = SVC()


nb_classifier.fit(X_train, y_train)
dt_classifier.fit(X_train, y_train)
rf_classifier.fit(X_train, y_train)
knn_classifier.fit(X_train, y_train)
svm_classifier.fit(X_train, y_train)


nb_pred = nb_classifier.predict(X_test)
dt_pred = dt_classifier.predict(X_test)
rf_pred = rf_classifier.predict(X_test)
knn_pred = knn_classifier.predict(X_test)
svm_pred = svm_classifier.predict(X_test)

nb_accuracy = round(accuracy_score(y_test, nb_pred), 3)
dt_accuracy = round(accuracy_score(y_test, dt_pred), 3)
rf_accuracy = round(accuracy_score(y_test, rf_pred), 3)
knn_accuracy = round(accuracy_score(y_test, knn_pred), 3)
svm_accuracy = round(accuracy_score(y_test, svm_pred), 3)


print("Naive Bayes Classifier Accuracy:", nb_accuracy)
print("Decision Trees Accuracy:", dt_accuracy)
print("Random Forest Accuracy:", rf_accuracy)
print("K-Nearest Neighbors Accuracy:", knn_accuracy)
print("Support Vector Machines Accuracy:", svm_accuracy)

emir_voter_data = pd.DataFrame({
    'Gender': [0],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

ahmet_voter_data = pd.DataFrame({
    'Gender': [0],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

kagan_voter_data = pd.DataFrame({
    'Gender': [0],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

bora_voter_data = pd.DataFrame({
    'Gender': [1],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

sezin_voter_data = pd.DataFrame({
    'Gender': [1],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

nazli_voter_data = pd.DataFrame({
    'Gender': [1],
    'Age': [1],
    'Region': [0],
    'Education': [4],
    'GOOD_ECONOMY': [0],
    'SUPPORT_EDUCATIONAL_REFORM': [1],
    'STOP_PRIVATIZATION': [1],
    'DEATH_PENALTY': [0],
    'FREE_MEDIA': [1],
    'SUPPORT_ALCOHOL_BAN': [0],
    'SUPPORT_SECULARISM': [1],
    'SUPPORT_ABORTION_BAN': [0],
    'OHAL_LIMITS_FREEDOM': [1],
    'SUPPORT_NEW_PARTIES': [1]
})

party_prediction_emir = rf_classifier.predict(emir_voter_data)
party_prediction_ahmet = rf_classifier.predict(ahmet_voter_data)
party_prediction_kagan = rf_classifier.predict(kagan_voter_data)
party_prediction_bora = rf_classifier.predict(bora_voter_data)
party_prediction_sezin = rf_classifier.predict(sezin_voter_data)
party_prediction_nazli = rf_classifier.predict(nazli_voter_data)

predicted_party_emir = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_emir[0]]
predicted_party_ahmet = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_ahmet[0]]
predicted_party_kagan = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_kagan[0]]
predicted_party_bora = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_bora[0]]
predicted_party_sezin = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_sezin[0]]
predicted_party_nazli = ['AKP', 'IYI PARTI', 'CHP', 'HDP', 'MHP', 'OTHER'][party_prediction_nazli[0]]

print("")
print("Predicted Party for Emir:", predicted_party_emir)
print("Predicted Party for Ahmet:", predicted_party_ahmet)
print("Predicted Party for Kagan:", predicted_party_kagan)
print("Predicted Party for Bora:", predicted_party_bora)
print("Predicted Party for Sezin:", predicted_party_sezin)
print("Predicted Party for Nazlı:", predicted_party_nazli)
