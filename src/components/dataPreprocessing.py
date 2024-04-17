from sklearn.pipeline import  Pipeline
numVal_Pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler())
    ]
)

categoricalVal_Pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer=(strategy="most_frequent")),
        ("", )
    ]
)