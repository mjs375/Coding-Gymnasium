# LOGISTIC REGRESSION


## Classification
- **Classification:** *supervised machine learning that tries to predict which class or category some entity belongs to, based on its features, with some mathematical expression. E.g. analyzing company employees and trying to establish a dependence on some __feature__ or __variable___, like level of education, number of years in role, age, salary, &c.*
  - **Observation:** *the set of data related to one entity.*
  - **Variables:** *variables, of __features__, of the data.*
    - **Independent variables:** *inputs or predictors, these do not depend on other features. (E.g. level of education, age, time in current position.) Usually denoted with (x₁, x₂, ... xᵣ).*
    - **Dependent variables:** *outputs or reponses, these depend on the independent variables. (E.g. salary, odds for promotion.) Usually denoted with (y₀ or y₁).*
  - **Regression problems:** *these have continuous and usually unbounded outputs (e.g. estimating the salary as a function of experience and education level).*
  - **Classification problems:** *tend to have discrete and finite outputs, called __classes__ or __categories__.*
    - **Binary/Binomial Classification:** *exactly two classes to choose from (0/1, True/False, positive/negative).*
    - **Multiclass/Multinomial Classification:** *three or more classes of the outputs to choose from.*

### Understanding When to Classify
- Examples of when to use classification:
  - *Text classification algorithms separate legitimate and spam emails*
  - *Sorting positive and negative comments*
  - *Credit scoring, applications, biological classification...*
  - *Image recognition tasks (human face or not? mouse or elephant?*
- **Logistic Regression:** *a fundamental classification technique, belongs to a group of __linear classifiers__. Fast and relatively uncomplicated. Essentially a method for binary classification (but can be applied to multiclass problems too).*
  - **Sigmoid Function**: *a mathematical function having an "S-shaped" curve. All sigmoids have the property that they map the entire number line into a small range between 0<>1 or -1<>1 (such that the use of a sigmoid function to convert a real value to a value that can be interpreted as a __probability__. The commonest sigmoid is the __Logistic Function__, which maps any real value from 0<>1 (which maps the variables (x1, x2... xr).*
  - **Natural Logarithm Function**: *```log(x)```-> as x approaches 0, the natural log of 'x' drops toward negative infinity. When ```x=1, log(x)=0```. The opposite is true for ```log(1-x)```.*
    - ```math.log(x)```, ```numpy.log(x)``` => natural logarithm of 'x' in Python (it is otherwise often denoted with 'ln' instead of 'log').



### Problem Formulation
- Logistic regression applied to binary classification: implementing logistic regression of some dependent variable ```y``` on the set of independent variables x=```(x₁, x₂, ..., xᵣ)``` where 'r' is the number of predictors/inputs.
  - **Goal:** *find the __logistic regression function__ ```p(x)``` such that the __predicted responses__ ```p(xᵢ)``` are as close as possible to the __actual response__ ```yᵢ``` for each observation ```i=1, ..., n```. (Each ```p(xᵢ)``` should be close to either 0 or 1– convenient!). Once you have the function ```p(x)```, you can use it to predict the outputs for new and unseen inputs (assuming the underlying mathematical dependence is unchanged).*

### Methodology
- **Logit:** ```f(x) = b₀ + b₁x₁ + ... + bᵣxᵣ```
  - **Estimators:** *the variables b₀,b₁,...,bᵣ, also called __prediction weights__ or just __coefficients__.*
- The logistic regression function ```p(x)``` is the sigmoid function of ```f(x)```: ```p(x)=1/(1+exp(-f(x))```. As such, it is often close to 0 or 1. 
- The function ```p(x)``` is often interpreted as the __predicted probability__ that the output for a given ```x``` is equal to 1. (Inversely, ```1-p(x)``` is the probability that the output is 0.)
- Logistic Regression determines the best predicted weights b₀,b₁,...,bᵣ such that the function ```p(x)``` is as close as possible to all actual responses y₁,i=1,..,n where n is the number of observations. The process of calculating the best weights using available observations is called __model training__ or __fitting__.
- To get the best weights, you usually maximize the __log-likelihood function (LLF)__ for all observations i=1,...,n. This method is called the __maximum likelihood estimation__ and is represented by the equation:
  - ```LLF = Σᵢ(𝑦ᵢ log(𝑝(𝐱ᵢ)) + (1 − 𝑦ᵢ) log(1 − 𝑝(𝐱ᵢ)))```
- When ```𝑦ᵢ=0```, the LLF for the corresponding observation is equal to ```log(1-p(xᵢ))```.
  - If ```p(xᵢ)``` is close to ```𝑦₀=0```, then ```log(1-p(x))``` is close to 9. This is the result you want.
    - If ```p(xᵢ)``` is far from 0, then ```log(1-p(x))``` drops significantly. You don't want that b/c your goal is to obtain the max LLF.
- When ```𝑦ᵢ=0```, the LLF for the corresponding observation is equal to ```yᵢlog(1-p(xᵢ))```.
  - If ```p(xᵢ)``` is close to ```𝑦₁=0```, then ```log(p(xᵢ))``` is close to 9. 
    - If ```p(xᵢ)``` is far from 1, then ```log(p(xᵢ))``` is a large negative number.
- Use Python's logistic regression libraries to approach these problems!
  - Once you determine the best weights that define the function ```p(x)```, you can get the predicted outputs ```p(x)ᵢ``` for any given input ```xᵢ```.
    - For each observation i=1,...,n, the predicted output is 1 IF ```p(x)ᵢ``` > 0.5, else 0 (this is the *usual* threshold– you can raise/lower it).
- Finally, one more important relationship between ```p(x)``` and ```f(x)```:
  - ```log( p(x)/(1-p(x)) )  = f(x)```.
    - This explains why f(x) is the __logit__. It implies that p(x) = 0.5 when f(x) = 0, and that the predicted output is 1 if f(x)>0 and 0 otherwise.
    
    
### Classification Performance
- 4 Types of Results for binary classification:
  - **True negatives:** *correctly predicted negatives (0s)*
  - **True positives:** *correctly predicted positives (1s)*
  - **False negatives:** *incorrectly predicted negatives (0s)*
  - **False positives:** *incorrectly predicted positives (1s)*
    - You can evaluate the performance of your classififer by comparing the *actual* and *predicted* outputs and by counting the correct/incorrect predictions.
- **Classification Accuracy:** *ratio of correct predictions to the total number predictions (or observations). The most straightforward indicator.*
  - **Other Indicators of Binary Classifiers:**
    - **Positive Prediction value**: ratio of the number of true positives to the sum of the numbers of true & false positives.
    - **Negative Prediction value**: ratio of the number of true negatives to the sum of the numbers of true & false negatives.
    - **Sensitivity**: ratio of the number of true positives to the number of actual positives (also known as recall or true positive rate).
    - **Specificity**: ratio of number of true negatives to the number of actual negatives (true negative rate).


### Single-Variate Logistic Regression
- The most straightforward case of logistic regression, with only 1 independent variable (or feature), which is x=```x```.
![Single-Variate Logistic Regression](https://files.realpython.com/media/log-reg-2.e88a21607ba3.png)
- Here you have pairs of inputs-outputs (x-y pairs, the green circles). These are your __observations__. ```y``` can only be 0 or 1.
  - __Logistic regression__ finds the weights b₀ & b₁ that correspond to the maximum __LLF__. These weights define the __logit__ ```f(x) = b₀ + b₁x₁```, which is the dashed black line. They also define the predicted probability ```p(x) = 1 / (1 + exp(-f(x)))```, shown as the solid black line.

### Multi-Variate Logistic Regression
- more than one input variable. Below is an example of the classification with 2 independent variables, x₁ & x₂:
![Multi-Variate Logistic Regression](https://files.realpython.com/media/log-reg-3.b1634d335c4f.png)
- Here, both axes represent the inputs. The outputs differ in color: white circles are observations classified as 0s, and green circles are those classified as 1s.
  - Logistic regression determines the weights b₀, b₁ & b₂ that maximize the LLF. Once you have these, you can get:
    - __Logit__: ```f(x₁,x₂) = b₀ + b₁x₁ + b₂x₂```
    - __The probabilities__: ```p(x₁,x₂) = 1/(1+exp(-f(x₁,x₂)))
  - The dash-dotted line linearly separates the two classes. This line corresponds to ```p(x₁,x₂)=0.5``` and ```f(x₁,x₂)=0```.

### Regularization
- **Overfitting:** *a serious problem related to Machine Learning. It happens when a model learns the training data too well– then it learns not only the __relationships__ among data, but also the __noise__ in the data. This leads to good performance with the data used to __fit__ them (i.e. training data), but they behave poorly with unseen data (test data).*
  - __Regularization__ tries to reduce or penalize the complexity of a model (as overfitting usually occurs on complex models). Regularization techniques applied with logistic regression mostly tend to penalize large coefficients ```b₀,b₁,b₂, ... bᵣ```. Regularization significantly improves model performance on unseen data.
    - **L1 regularization**: penalizes the LFF with the scaled sum of the absolute values of the weights (```|b₀|+|b₁|+|b₂| ... +|bᵣ|```).
    - **L2 regularization**: penalizes the LFF with the scaled sum of the squares of the weights (```|b₀|+|b₁|+|b₂| ... +|bᵣ|```).
    - **Elastic-net regularization**: a linear combination of L1 & L2 regularization.

## Logistic Regression in Python

### Python Packages
- **```NumPy```**: *fundamental package for scientific and numerical computing in Python. It allows for high-performance operations on single- and multi-dimensional arrays.*
- **```scikit-learn```**: *data science/machine-learning library. It can: preprocess data, reduce dimensionality of problems, validate models, select the most appropriate model, solve regression and classification problems, and implement cluster analysis.*
- **```Matplotlib```**: *used to visualize your classification. Widely-used for high-quality plotting.*

### Ex 1: Logistic Regression w/ ```scikit-learn```
- A single-variate binary classification problem (the most straightforward kind). We'll need to: *import, get data to work with, create a classification model (and train it), and evaluate the model to see if its performance is satisfactory.*


<hr>
PAUSE: return to after 'Linear Regression'
