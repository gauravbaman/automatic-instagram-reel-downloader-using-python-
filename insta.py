from instascrape import Reel
import pandas as pd
import time

# session id
SESSIONID = "use your own session id"

# Header with session id
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}


#Code
number = 0 
df = pd.read_csv("insta.csv")
while number < 1000:
    try:
        insta_reel = Reel(df.iloc[number-1,0])
        insta_reel.scrape(headers=headers)
        insta_reel.download(fp=f"%s 1.mp4" % number)
        print(number)
        print(df.iloc[number-1,0])
        number = number+1
        continue
    except:
        number = number+1
