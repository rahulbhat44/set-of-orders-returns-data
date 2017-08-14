
#### Install the libraries

Import
pandas as pd

import numpy as np

import matplotlib.mlab as mlab

import matplotlib.pyplot as plt


#### Load casper data set

casper = pd.read_excel('/Users/Bhat/Downloads/casper.xlsx')


#### Explore the data set

casper.head()

casper.tail()

casper.count()


#### Summary of the data set

casper.count()

casper.describe()


#### We can see that the total number of orders are 213 and minimum 1 order is returned out of 60 returns.


##### Order is either complete or return and lets see how many orders are complete and how many are returned.

complete_orders = casper[casper['orderstatus'] == 'complete']
complete_orders.count()

#### We have 153 complete orders without any return.


#### Summary of complete_orders (complete orders summary)

complete_orders.describe()

#### We can see that the average transaction orders are 6.751 and the median transaction is 6.00 orders.
#### We can say that the distribution of orders are right-skewed and the average size of the order is above the median.



#### Let's see how many orders are returned

return_orders = casper[casper['orderstatus'] == 'returned']
return_orders.count()
return_orders.describe()

#### We can see that the total of 60 orders are returned.



#### Check how many order dates are there and how many return dates are there

returns.nunique()

#### We can see that there are 39 order dates and 47 return dates.
#### We don't have more than one return and we have already seen that each sale transaction avg is for 6.75.
#### So this is the reason we have more return dates than the ordered dates.



#### Plot the histogram of complete_orders (complete orders)

plt.title('Histogram of Order Size')
plt.ylabel('Frequency')
plt.xlabel('No. of orders')
complete_orders['orders'].hist(bins=20, figsize=(8, 8));

#### From the histogram we can see that the average size of the order is above the median order size.


#### Lets see the size of the order over time

orders.plot(x='dateordered', y='orders',
            figsize=(8, 8), grid=True, title='Order Size over Time');

#### We can see that the orders are trending upward from the month of November



#### Check for any duplicate order in the complete_orders

len(complete_orders)

complete_orders['dateordered'].nunique()

#### We got one duplicate date in the complete_orders which is manageable.

#### We have already seen that the average transaction is 6.751 orders and the median transaction is 6.00 orders.
#### Each transaction contains number of orders (for example in one transaction there could be more than 1 order)
#### Let's plot the avg. transaction (one week avg order size)

d = complete_orders['orders'][::-1].rolling(7).mean()

d.plot(figsize=(10, 10), grid=True, color='blue', title='Average Order Size');

### from the plot we can say that at least one transaction is happening per day.


