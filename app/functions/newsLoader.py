from datetime import datetime
import json

def loadNews():# Get the current date (without time)
    current_date = datetime.now().date()  
    print(current_date)  
    with open(f'data/news/{current_date}_news','r') as news:
        return json.load(news)


