
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import autosklearn.classification
import sklearn.metrics

df = pd.read_csv('../heroku_bachmann/bachmannpreis/data/database_csvs/prediction_table.csv')

X_train = df[df.year < 2020].drop(columns=['price_won'])
X_test = df[df.year == 2020].drop(columns=['price_won'])
y_train = df[df.year < 2020]["price_won"]
y_test = df[df.year == 2020]["price_won"]

# rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
# rf_model.fit(X_train, y_train)
# print(rf_model.score(X_test, y_test))

automl = autosklearn.classification.AutoSklearnClassifier(
    include_estimators=["random_forest",],
    exclude_estimators=None,
    include_preprocessors=["no_preprocessing",],
    exclude_preprocessors=None,
)

automl.fit(X_train, y_train)

predictions = automl.predict(X_test)

print(automl.sprint_statistics())
print("Accuracy score:{}".format(
    sklearn.metrics.accuracy_score(y_test, predictions))
)