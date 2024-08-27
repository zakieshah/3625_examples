from optimization_test_functions import ad_campaign_profit
import numpy as np


# build an array of 4 values in the range [0, 1] representing the $ spend on each of 4 ad campaigns
# call ad_campaign_profit to run the ads and get the *negative* profit
# like this:
test_spend = np.array([0.5, 0.5, 0.2, 0.9])
profit = ad_campaign_profit(test_spend)
print(profit)

# now, using scipy functions, find the optimum spend for each ad campaign
