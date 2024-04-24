# -*- coding: utf-8 -*-
"""Data_Mining_HW4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nIj_HV0wUfJ4HrL4IKSSGolGra-jxIbN
"""

#-------------------------------------------------------------------------
# AUTHOR: Nhi Nguyen
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990- Assignment #4
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
import pandas as pd

dbTraining = []
dbTest = []
X_training = []
y_training = []
classVotes = [] #this array will be used to count the votes of each classifier

#reading the training data from a csv file and populate dbTraining
#--> add your Python code here
dbTraining = pd.read_csv("optdigits.tra", header=None).values
dbTest = pd.read_csv("optdigits.tes", header=None).values

# initialize the variables to compute accuracy for single decision tree,
# ensemble classifier, and random forest classifier
single_tree_accuracy = ensemble_classifier_accuracy = random_forest_classifier_accuracy = 0

for _ in range(len(dbTest)):
    classVotes.append([0] * 10)

for k in range(20): #we will create 20 bootstrap samples here (k = 20). One classifier will be created for each bootstrap sample

  bootstrapSample = resample(dbTraining, n_samples=len(dbTraining), replace=True)

  #populate the values of X_training and y_training by using the bootstrapSample
  #--> add your Python code here
  X_training = bootstrapSample[:, :-1]
  y_training = bootstrapSample[:, -1]

  #fitting the decision tree to the data
  clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=None) #we will use a single decision tree without pruning it
  clf = clf.fit(X_training, y_training)

  for i, testSample in enumerate(dbTest):
    X_test, y_test = testSample[:-1], testSample[-1]
    class_predict = clf.predict([X_test])
    classVotes[i][class_predict[0]] += 1

    if k == 0: #for only the first base classifier, compare the prediction with the true label of the test sample here to start calculating its accuracy
      # --> add your Python code here
      single_tree_accuracy += 1 if class_predict == y_test else 0

  if k == 0: #for only the first base classifier, print its accuracy here
     #--> add your Python code here
     accuracy = single_tree_accuracy / len(dbTest)
     print("Finished my base classifier (fast but relatively low accuracy) ...")
     print("My base classifier accuracy: " + str(accuracy))
     print("")

  #now, compare the final ensemble prediction (majority vote in classVotes) for each test sample with the ground truth label to calculate the accuracy of the ensemble classifier (all base classifiers together)
  #--> add your Python code here
  for i, testSample in enumerate(dbTest):
    if classVotes[i].index(max(classVotes[i])) == testSample[-1]:
      ensemble_classifier_accuracy += 1

#printing the ensemble accuracy here
accuracy = ensemble_classifier_accuracy / (len(dbTest)*20)
print("Finished my ensemble classifier (slow but higher accuracy) ...")
print("My ensemble accuracy: " + str(accuracy))
print("")

print("Started Random Forest algorithm ...")
#Create a Random Forest Classifier
clf=RandomForestClassifier(n_estimators=20) #this is the number of decision trees that will be generated by Random Forest. The sample of the ensemble method used before

#Fit Random Forest to the training data
clf.fit(X_training,y_training)

#make the Random Forest prediction for each test sample. Example: class_predicted_rf = clf.predict([[3, 1, 2, 1, ...]]
#--> add your Python code here
for i, testSample in enumerate(dbTest):
    X_test, y_test = testSample[:-1], testSample[-1]
    y_predict = clf.predict([X_test])

    #compare the Random Forest prediction for each test sample with the ground truth label to calculate its accuracy
    #--> add your Python code here
    random_forest_classifier_accuracy += 1 if y_predict == y_test else 0

#printing Random Forest accuracy here
accuracy = random_forest_classifier_accuracy /  len(dbTest)
print("Random Forest accuracy: " + str(accuracy))

print("Finished Random Forest algorithm (much faster and higher accuracy!) ...")

