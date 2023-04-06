import pytrends as pytrend 
from pytrends.request import TrendReq

# Define a function to get the trend score for a keyword
def get_trend_score(keyword):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword], timeframe='2023-03-01 2023-03-01', geo='US')
    df_trend = pytrend.interest_by_region()
    trend_score = df_trend[keyword].mean()
    return trend_score

# Print the output for a sample keyword
sample_keyword = 'elon musk'
print(get_trend_score(sample_keyword))
