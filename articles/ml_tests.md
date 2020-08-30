https://www.jeremyjordan.me/testing-ml/
lib for data assertions: https://greatexpectations.io/

# Highlights

## Model tests

### Pre-train tests:
* check the shape of your model output and ensure it aligns with the labels in your dataset
* check the output ranges and ensure it aligns with our expectations (eg. the output of a classification model should be a distribution with class probabilities that sum to 1)
* ? make sure a single gradient step on a batch of data yields a decrease in your loss
* make assertions about your datasets
* check for label leakage between your training and validation datasets

### Stability test

Make sure, that pertubation in sample doesn't affect the predition.

### Directional expectations test

Confirm some assertation about model predictions. For example if we had a housing price prediction model we might assert the following.
Increasing the number of bathrooms (holding all other features constant) should not cause a drop in price.
Lowering the square footage of the house (holding all other features constant) should not cause an increase in price.

### Minimum functionality test

Special cases with known output. Reference data set.

## Model evaluation

Report with metrics and plots indicating the model performance.

# Open questions

* What special tests could be for time series problems? For prediction problems?