Machine Learning-Subfield of AI



# what is machine Learning-
its a way to teach computer to LEARN from DATA,instead of assigning step by step RULES

ml=computer learning from patterns and getting better with experience

Ex-
1,000 pictures of cats
1,000 pictures of dogs
and computer on its own will figure it out if we ask it to indenitfy the animal based on picture

Ex-Netflix / YouTube → recommends videos
Gmail → spam filter
Phone face unlock
Amazon → suggests products


# application of ML
GPS-finding shortest path
perform web search, recognize human speech, diagnose diseases from X-rays or build a self-driving car.

# machine Learning AlGo-
1. supervised learning- used mostly in real world applictns,seen most rapid advancement 
2. unsupervised learning-

# ML overview-
what is ml-computer leraning by itself with patterns and getting better with experience
when to apply it-
If you can’t clearly explain the logic, ML is useful.
Example:
“Why is this email spam?”
“Why did this customer leave?”
“Why does this image look like a cat?”
used for guessing future or unknown,
ml is PROBABILITY

Professional Rule of Thumb

If you can explain the solution clearly in steps, don’t use ML.
If you can only show examples, ML might help.


# supervised learning
refers to algorithms that learn x to y or input to output label (mapping)

give ur learning algo examples to learn from;that includes the right answers,ie corrcet label y for given input x

from input x and desried output label y that the ;learning algo learns to take just the input alone without output label and gives a accurate prediction or guess the output

EX-
input(x)    output(y)     application
email       spam?(0/1)    spamfilterning
audio      texttranscript   speech recognition
english     spanish        machinetranslation
ad,userinfo   click?(0/1)  onlineadvertising
img,radarinfo   postnofothercars  selfdrivingcars 
imgofphone   defect?(0/1)   visual inspection
# type of supervised learning 
1. REGRESSION-regression is used when the output is a NUMBER from many possible outputs.
 Ex-Predicting house price → ₹5,200,000
Predicting temperature → 32.5°C
Predicting sales next month → 12,430 units
Predicting salary → ₹45,000

2. CLASSIFICTAION-
example- breast cancer detection
using patient medical record your ml system tries to figure out if tumor/lump is cancerous(maligant) or noncancerous(benign)

size     diagnosis
2          0
5          1
1          0
7          1


|1                   .   .
|
|
|
|
|
|0__.___._____________________
    1   2    3   4  5 6  7
or
malignnat-@
benign-#


____#____#____________@_____@___
    1   2    3   4  5 6  7

here only two possible output (0 or 1)


If canceroous lump is of two types
malignant type1@
malignant type 2$


____#____#___$___$______@_$____@__________
0cm    1   2    3   4  5 6  7       10cm
           diameter(cm)

if we compare it with regression then regression gives anyoutput ; when the output is a NUMBER from many possible outputs. 

in classification-
 the terms output classes and output categories are often used interchangeably. So what I say class or category when referring to the output, it means the same thing
classification algo predicts categories 
categories not need to be numbers it can ne any nonnumeric value too
Ex- it can predict if picture shown is cat or dog
    it can predct if tumor is benign or malignant
    it can be numers too - 0/1/2

it predicts small finite limited amt of output ie 0,1,2  but not all possbile number in between ie not 0.5 or 1.7


if INPUTS are 2 or more
tumor size and age of paitents
malignnat-@
benign-#
  |          
  |\         @
  |  \       @  @
  |    \      @ #  @
  |      \ \     @            
A |   # @  # \ 
g |- - # #     \
e |    # | #     \
  |______|________\_____________________
          tumor size

          here dr can mesure paitents tuor size and age to predict the result

      nd so given this, how can we predict if this patient's tumor is benign or malignant? 
      Well, given the day said like this, what the learning algorithm might do is find some boundary that separates out the malignant tumors from the benign one    
    

# RECAP-supervised learning
it maps input x to output y
learning algo learns from being given 'RIGHT ANSWERS"
two types
REGRESSION  -
  example predicting prices of houses
  learning algo has to  predict number from infinitely many possible outputs 
CLASSIFICATION - here predictions are made based on category
from small set of numbers of possible outputs





# Unsupervised learning   
we are given data that isnt associated with any output labels Y        

ex-you're given data on patients and their tumor size and the patient's age. But not whether the tumor was benign or malignant, so the dataset looks like this .

a|
g|
e|                      @
 |                          @     @
 |                          @         @
|     @                          @
 |       @   @
 |     @   @
 |     @
 |____________________________________
           tumor size


 We're not asked to diagnose whether the tumor is benign or malignant, because we're not given any labels. Why in the dataset, instead, our job is to find some structure or some pattern or just find something interesting in data

 its called UNSUPERVISED cuz we are not trying to supervise the algo.
To give some quote right answer for every input, instead, we asked the our room to figure out all by yourself what's interesting. Or what patterns or structures that might be in this data, with this particular data set

   so unspersvised learning algo ,might decidse that the data can be assigned two differnt grps or two diffrnt cluster


# type of unsupervised learning 
1. Clustering- above type is culstering type cuz
it places the unlabeld data,into diffrnt clusters and this turns out to be useful in many applications 
ex-
or example, clustering is used in google news, what google news does is every day it goes. And looks at hundreds of thousands of news articles on the internet, and groups related stories together. For example, here is a sample from Google News, where the headline of the top article, is giant panda gives birth to rear twin cubs at Japan's oldest zoo. This article has actually caught my eye, because my daughter loves pandas and so there are a lot of stuff panda toys. And watching panda videos in my house, and looking at this, you might notice that below this are other related articles.

 Notice that the word panda appears here here, here, here and here and notice that the word twin also appears in all five articles. And the word Zoo also appears in all of these articles, so the clustering algorithm is finding articles. All of all the hundreds of thousands of news articles on the internet that day, finding the articles that mention similar words and grouping them into clusters

 Now, what's cool is that this clustering algorithm figures out on his own which words suggest, that certain articles are in the same group. 
 What I mean is there isn't an employee at google news who's telling the algorithm to find articles that the word panda. And twins and zoo to put them into the same cluster, the news topics change every day.
  
 Instead the algorithm has to figure out on his own without supervision, what are the clusters of news articles today

Let's look at the second example of unsupervised learning applied to clustering genetic or DNA data. This image shows a picture of DNA micro array data, these look like tiny grids of a spreadsheet. And each tiny column represents the genetic or DNA activity of one person, So for example, this entire Column here is from one person's DNA. And this other column is of another person, each row represents a particular gene. 
So just as an example, perhaps this role here might represent a gene that affects eye color, or this role here is a gene that affects how tall someone is. Researchers have even found a genetic link to whether someone dislikes certain vegetables, such as broccoli, or brussels sprouts, or asparagus. So next time someone asks you why didn't you finish your salad, you can tell them, maybe it's genetic for DNA micro race. The idea is to measure how much certain genes, are expressed for each individual person. So these colors red, green, gray, and so on, show the degree to which different individuals do, or do not have a specific gene active. And what you can do is then run a clustering algorithm to group individuals into different categories. Or different types of people like maybe these individuals that group together, and let's just call this type one. 
And these people are grouped into type two, and these people are groups as type three. This is unsupervised learning, because we're not telling the algorithm in advance, that there is a type one person with certain characteristics. Or a type two person with certain characteristics, instead what we're saying is here's a bunch of data. I don't know what the different types of people are but can you automatically find structure into data. And automatically figure out whether the major types of individuals, since we're not giving the algorithm the right answer for the examples in advance. This is unsupervised learning


here's the third example, many companies have huge databases of customer information given this data. Can you automatically group your customers, into different market segments so that you can more efficiently serve your customers. 
Concretely the deep learning dot AI team did some research to better understand the deep learning dot AI community. And why different individuals take these classes, subscribed to the batch weekly newsletter, or attend our AI events. Let's visualize the deep learning dot AI community, as this collection of people running clustering. That is market segmentation found a few distinct groups of individuals, one group's primary motivation is seeking knowledge to grow their skills. Perhaps this is you, and so that's great, a second group's primary motivation is looking for a way to develop their career. Maybe you want to get a promotion or a new job, or make some career progression if this describes you, that's great too. And yet another group wants to stay updated on how AI impacts their field of work, perhaps this is u ,that great too
This is a clustering that our team used to try to better serve our community as we're trying to figure out. Whether the major categories of learners in the deeper and community, So if any of these is your top motivation for learning, that's great. And I hope I'll be able to help you on your journey, or in case this is you, and you want something totally different than the other three categories. That's fine too, and I want you to know, I love you all the same, 

so to summarize a clustering algorithm-Which is a type of unsupervised learning algorithm, takes data without labels and tries to automatically group them into clusters. And so maybe the next time you see or think of a panda, maybe you think of clustering as well. And besides clustering, there are other types of unsupervised learning as well. 


2. anomaly detection:
used to detect unusual events
usefull in fraud detection in financial system


3.dimensionality reduction-
big dataset comprssed to much smaller dataset:while lsoing as little info as possible






# Regression model
fitting a straight line to your data

predicitng price of the house based on the size of the house

# its called regression model cuz it predicts number


# regression problem- any supervised learning model that predicts a number example liner regression

inifite number of outputs




# classification  model- predicts categories or discrete categories
limited number /small number of possible outputs
example if model identifying if given pic is cat or dog the n their are two possible outputs


# NOTATIONS
dataset used to train the mmodel is training set

example is size in feets of house vs price in $

if ur client wants to know  at what price their house can be sold

we first train the model to learn from training set
and then  model can predict the price of ur client's house


x="input " variable feature or input feature
example- x= size in feet of the house

y='ouput 'variable/'target ' variable
example- price of the house

m=total number of training examples(number of rows)

(x,y)=single training example

(x^(i),y^(i))=for specific example(specific row)(ith trainung example)


