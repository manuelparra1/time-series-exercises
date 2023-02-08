# Exercises

### The end result of this exercise should be a Jupyter notebook named model.
### Use either the SAAS dataset or the store data and:

# 1. Split data (train/validate/test) and resample by any period except daily. Aggregate using the sum.


```python
# split settings
train_size = int(len(df) * .5)
validate_size = int(len(df) * .3)
test_size = int(len(df) - train_size - validate_size)
validate_end_index = train_size + validate_size

# split into train, validation, test
train = df[: train_size]
validate = df[train_size : validate_end_index]
test = df[validate_end_index : ]
```


```python
# evaluation function to compute rmse
def evaluate(target_var):
    rmse = round(sqrt(mean_squared_error(validate[target_var], yhat_df[target_var])), 0)
    return rmse
```


```python
# plot and evaluate 
def plot_and_eval(target_var):
    plt.figure(figsize = (12,4))
    plt.plot(train[target_var], label = 'Train', linewidth = 1)
    plt.plot(validate[target_var], label = 'Validate', linewidth = 1)
    plt.plot(yhat_df[target_var])
    plt.title(target_var)
    rmse = evaluate(target_var)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))
    plt.show()
```


```python
# Create the empty dataframe
eval_df = pd.DataFrame(columns=['model_type', 'target_var', 'rmse'])

# function to store rmse for comparison purposes
def append_eval_df(model_type, target_var):
    rmse = evaluate(target_var)
    d = {'model_type': [model_type], 'target_var': [target_var], 'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)
```


```python
# Last Observed Value
# ===================

# Predictions
items = train['items_sold'][-1:][0]
dollars = round(train['dollars_sold'][-1:][0],2)

yhat_df = pd.DataFrame({'items_sold': [items], 'dollars_sold': [dollars]}, 
                       index = validate.index)

yhat_df.head(2)
```


```python
# Plot & Evaluate
plot_and_eval(col)
```


```python
# Append Metrics Eval DataFrame
for col in train.columns:
    eval_df = append_eval_df(model_type = 'last_observed_value', 
                             target_var = col)
```


```python
eval_df
```

# 2. Forecast, plot and evaluate using each of the 4 parametric based methods we discussed:

## a. Simple Average


```python

```

## b. Moving Average


```python

```

## c. Holt's Linear Trend Model


```python
def holt_linear_trend():
    for col in train.columns:
    model = Holt(train[col], exponential = False)
    model = model.fit(smoothing_level = .1, 
                      smoothing_slope = .1, 
                      optimized = False)
    yhat_items = model.predict(start = validate.index[0], 
                               end = validate.index[-1])
    yhat_df[col] = round(yhat_items, 2)

    for col in train.columns:
    plot_and_eval(target_var = col)

    for col in train.columns:
    eval_df = append_eval_df(model_type = 'Holts', 
                             target_var = col)
    eval_df

    
```

## d. Based on previous year/month/etc., this is up to you.


```python

```

# Bonus

### Using the store data:

## 1. Predict 2018 total monthly sales for a single store and/or item by creating a model.


```python

```

## 2. Return a dataframe with the month, store_id, y-hat, and the confidence intervals (y-hat lower, y-hat upper). The upper and lower bounds of the predictions are auto generated when using the facebook prophet model, or you could calculate your own using, for example, bollinger bands.


```python

```

## 3. Plot the 2018 monthly sales predictions.


```python

```
