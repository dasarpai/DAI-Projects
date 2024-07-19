# CapProject-CreditFraud-Detection
Credit Fraud Detection in Banking

Section 1: Exploratory data analysis
Getting data from kaggle to colab dataset. 
Analysis of Fraud against the Transaction Value
Let us see distribution of various columns
Here we will observe the distribution of our classes
Let us Check Coorelation Between Different Variables
Is there an relationship between variables and Class?
Let us see Distribution of data for the given 2 Classes
To observe the relation between amount and other variable for both the classes.
Standard Scale All the Fields Including Time and Amount
Plotting the distribution of a variable- After Scaling
Some fields are still skewed. So using PowerTransformer to fix that issue.
Plotting the distribution of a variable- After Correcting Skweness Issue
Check the outliers after fixing skewness & scale issue

Section 2: Splitting the data into Train & Test

Section 3: Visuzalise Results of Various Oversampling Methods
Random Oversampling
SMOTE : Synthetic Minority Over-sampling Technique
ADASYN : Adaptive Synthetic Sampling Method

Section 4: Select the Dataset Imbalancing Method

Section 5: Helper Functions for Model Building 

Section 6: Model Building 
folds = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 100)

Model 1: Logistic Regression
hyper_params = [{'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000] }]
LogisticRegression(C=.1,max_iter=1000, random_state=100)

Model 2: GLM

Model 3: KNeighborsClassifier
hyper_params = [{'n_neighbors': range(2,15,2) }]

KNeighborsClassifier(n_neighbors = 4, leaf_size=30, p=2)

Model 4: RandomForestClassifier
folds = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 100)
hyper_params=[{'n_estimators':range(4,20,2),'max_depth':range(8,25,2)}]

RandomForestClassifier(n_estimators=16, criterion="gini", max_depth=6, random_state=100)
	
Model 5: DecisionTreeClassifier
hyper_params=[{'max_depth': range(10,20,2),
                   'min_samples_leaf': range(1, 5, 1),
                   'min_samples_split': range(1, 5, 1) }]
				   
DecisionTreeClassifier(max_depth=16, min_samples_leaf=1, min_samples_split=2, random_state=100)

Model 6: LGBM
hyper_params=[{  'n_estimators': range(10,110,10)  }]
lgbmc.LGBMClassifier(n_estimators=100, random_state = 42)

Model 7: Perceptron
hyper_params=[{'n_iter_no_change': [ 5,6,7,8,9] }]
Perceptron(alpha=.00001,n_iter_no_change=7,random_state = 42, penalty="l2")

Model 8: SVC
hyper_params=[{'C': range(10,30,2) }]
SVC(C=20.0,random_state=100, probability=True).fit(X_train,y_train)


Model 9: XGBoost
hyper_params=[{'max_depth': range(10,15,1), 'n_estimators': range(95,120,2) }]
xgbc(max_depth=10, n_estimators=95, learning_rate=.01,random_state=100).fit(X_train,y_train)

Model 10: Adaboost
hyper_params=[{'learning_rate': range(1,5,1), 'n_estimators': range(40,71,10) }]
AdaBoostClassifier(learning_rate=1,random_state=100)

Model 11: CatboostClassifier
CatBoostClassifier(learning_rate=1,random_state=100)

Model 12: Naive Bayes

Model 13: Stochastic Gradient Descent Classifier
hyper_params = [{ 'alpha': [10 ** x for x in range(-3, 1)],
                        'l1_ratio': [0, 0.05, 0.1, 0.2, 0.5, 0.9, 0.95, 1] }]

sgd = SGDClassifier(max_iter=1000, alpha=0.0001, l1_ratio=0.2, random_state=100, penalty="elasticnet", class_weight='balanced',loss='hinge', )
			

Model 14: Dense Neural Network
    model = Sequential([
    Dense(units=16, input_dim=indput_dim, activation='relu'),
    Dropout(dropout),
    Dense(units=16, activation='relu'),
    Dropout(dropout),
    Dense(1, activation='sigmoid')])
	
	dnn = create_dnn(indput_dim=X_train.shape[1], dropout=0.2)
    dnn.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
    dnn.fit(X_train, y_train,batch_size=100, epochs=50)
	
	
Model 15: Convolution Neural Network
	cnn = Sequential()
    cnn.add(Conv1D(128, kernel_size = ( 5), activation='relu', padding="same",input_shape=(30, 1) ))
    cnn.add(layers.GlobalMaxPool1D())
    cnn.add(BatchNormalization())
    cnn.add(Dense(30,  activation='relu'))
    cnn.add(Dense(1, activation='sigmoid'))

    cnn = create_cnn(indput_dim=xtrain.shape[1], dropout=0.2)
    cnn.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
    cnn.fit(xtrain, y_train,batch_size=5000, epochs=50)
