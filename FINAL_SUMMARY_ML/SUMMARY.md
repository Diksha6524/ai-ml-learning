# SUMMARY ABOUT ML

1. types of models
supervised,unsupervised,semi-supervised,reinforcement

2. REGRESSION
(supervised)
relationshipe between continuous target variable and exploratory features

types of regrission
simple-single independent variable and a dependent variable
(this can be -linear or non linear)

multiple-uses two or more independent variable and a dependent variable

3. LOGISTICAL REGRESSION
looks for parameters that maps fatures to outcomes

Objective-used to predict classes with minimal error

4. CLASSIFICATION
(supervised)
uses fully train model to predict labels on new data
​The labels in classification form a categorical variable with discrete values
applictaion-
email filtering
speech to text
handwriting recognition
biometric identification

5. KNN
(supervised)
takes grp of labeled data points and use them to label other data pointsused for btoh classification and regression

6. SVM
(supervised)
maps data instance as a point in multidimensional space
used in classification and regression 
applctaion-speech recognition,anomaly detection and noise filtering

7. DECISION TREE(predicts Discrete(countable) classes)
used fo classifying datapoints
each internal node corresponds to test
each branch-result of corresponding test
leaf node-assigned data to a class
its built by condidering data set features one by one

8. REGRESSION TREE(predicts continous values)
similar to decision tree
Predicts CONTINUOUS VALUES rather then classes
​The distinguishing feature between classification and regression is the characteristic of the ​target, or labeled data

its created but recursively splitting dataset into subsets to MAXIMIZE INFO GAINED FROM SPLITTIG
This process generates a tree-like structure and minimizes the randomness of the classes ​assigned to the split nodes

9. clustering,dimension reduction and feature enggineering
works together to imporve model performance ,quality,and interpretability
culstering- automatically grps data points based on similarties
appl-identifying music genre,user segmentation,analysing market segments
dimension red- simplifies visulaization of high-dimenson cluster
aids feature enginnering and improves model quality
reduces no. of features required fo data model
reduces dataset features without sacrificing ciritical info
high dimension data-difficult to analyze and visulaize
therefore dimensionality reduction -simplifies dataset for ml models

10. classification metrics and evalutaion techniques

classification metrics -how well model can predict the outcomes from unseen data
essential for understanding of model effectivness
metrics-accuracy,confusion metrics,precision ,recall,f1score
10. 10.1   rgerssion method- they make prediction errors

regression evalution technique-
how accurately a model can predict numerical values(exam grades).

unspervised techniques like clustering and dimensionality reduction- aims to discover hidden patterns and structure in data
therfore evalution metrics assists the quality of this patterns(how affectively teh model can grp similar datapoints)

11. cross validtaion and advanced validation techniques

model validtaion- optimizing ml models(without compramising its ability to predict weel on unseen data)
it helps prevent overfitting when selecting the best model config by tunning hyperparameters checking performance on test data before you are done optimizing your model this is called data snooping from data leakage


validation-Validation means toning your model on the training data, but only testing it on unseen ​test data once you are satisfied that it is well trained. ​There is no snooping involved.