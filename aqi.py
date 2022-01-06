#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class AQI():
    def __init__(self):
        pass
    
    def AQI_bucket(x):
            if x <= 50:
                return "AQI_bucket=Good, Air contains little or no pollutants.It is safe to live in.Minimal Impact on health"
            elif x <= 100:
                return "AQI_bucket=Satisfactory,May cause minor breathing discomfort to sensitive people.It is acceptable situation."
            elif x <= 200:
                return "AQI_bucket=Moderate, May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults. It is advised to wear mask for the sensitive people."
            elif x <= 300:
                return "AQI_bucket=Poor, May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease.Pregnant women are advised to stay at home. "
            elif x <= 400:
                return "AQI_bucket=Very Poor, May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases. Stay at home, go out when it is urgent, as place is near to risky time."
            elif x > 400:
                return "AQI_bucket=Severe, May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity. It is advised to use air purifer and take care of yourself as it is a risky time period."
            else:
                return "Give Valid AQI"


