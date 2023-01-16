import pandas as pd                        
from pytrends.request import TrendReq
from datetime import datetime, timedelta

# Create a pandas dataframe with keywords
pytrend = TrendReq()
df = pytrend.trending_searches(pn='united_states')
df.head()

now = datetime.now()
last_hour = now - timedelta(hours=1)
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
last_hour_str = last_hour.strftime("%Y-%m-%d %H:%M:%S")

related_queries = pytrend.related_queries()
related_queries.values()

# Define a function to get the trend score for a keyword
def get_trend_score(keyword):
    pytrend.build_payload(kw_list=[keyword], timeframe='2022-01-15 2022-01-15', geo='US')
    df_trend = pytrend.interest_by_region()
    trend_score = df_trend[keyword].mean()
    related_queries = pytrend.related_queries()
    related_topics = pytrend.related_topics()
    return trend_score

# Apply the function to every row in the dataframe
df['trend_score'] = df[0].apply(get_trend_score)
df = df.sort_values('trend_score', ascending = False)
print(df.head(100))