###Title
With Google Scraper you can scrape search results and extract the contents.

###Descrption
* This google scraper will scrape title, a small description, link etc from the search result.
* For example if we search gulmarg in google search then it will give us the json data which contains the article name such as gulmarg and the link of the website such as wikipedia etc which can be seen below in json sample data.

### JSON sample data
```sh
{
    "Scraper_People_also_ask": [
        {
            "column_0": "https://en.wikipedia.org \u203a wiki \u203a Gulmarg",
            "column_1": "https://en.wikipedia.org \u203a wiki \u203a Gulmarg",
            "column_6": "Gulmarg - Wikipedia",
            "column_7": "Gulmarg known as Gulmarag in Kashmiri, is a town, a hill station, a popular skiing destination and a notified area committee in the Baramulla district of\u00a0...",
            "column_8": "Country: IndiaDistrict: Baramulla",
            "column_9": "Web results"
        },
        {
            "be_link": "/search?q=Is+Gulmarg+safe+for+tourists%3F&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQzmd6BAgpEAU",
            "column_8": "Is Gulmarg safe for tourists?Search for: Is Gulmarg safe for tourists?",
            "link_0": "/search?q=Is+Gulmarg+safe+for+tourists%3F&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQzmd6BAgpEAU",
            "link_1": "/search?q=What+is+the+best+time+to+visit+Gulmarg%3F&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQzmd6BAgZEAU",
            "link_2": "/search?q=Is+Gulmarg+safe+for+tourists%3F&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQzmd6BAgpEAU",
            "link_4": "/search?q=Is+Gulmarg+safe+for+tourists%3F&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQzmd6BAgpEAU"
        },
        {
            "column_0": "https://skigulmarg.com",
            "column_1": "https://skigulmarg.com",
            "column_6": "Skiing India \u2014 Ski Gulmarg, the Best Skiing in India ...",
            "column_7": "Most people come to Gulmarg Ski Resort for the incredible terrain access from the Gulmarg Gondola. It is important to understand that outside the resort\u00a0...",
            "column_8": "\u200eGulmarg Trail Map \u00b7 \u200eAbout Gulmarg \u00b7 \u200eGulmarg Weather \u00b7 \u200eGulmarg in Summer",
            "column_9": "Web results"
        },
        {
            "be_link": "/search?q=gulmarg&tbm=isch&source=iu&ictx=1&fir=zqEz3gJ7p8dZwM%252Cvj6zfiOc_gvR1M%252C_%253BUo87NmXul6Ka9M%252CydjH7Y-Ndmv20M%252C_%253B_ysWTmXGBPSJVM%252Cger8IWrnyAHeLM%252C_%253BLCr_wbxPyfenUM%252CXHlwtSCSfbpw5M%252C_%253BcAPBLInxWlVjiM%252CGIFJkwIC2DSKJM%252C_%253Bquv7pOtIHZ-mmM%252Cx-mml25N3onQuM%252C_%253Br2Luss7397R5kM%252CGy0ekCg1lPK4eM%252C_%253BeeLInKD7Sl1a2M%252Cv3Gon5ykQSzLZM%252C_%253BYbBjG3yl8juNNM%252CuMfgSwGZlKXMsM%252C_%253B48SQ7eHTRLvXQM%252CxGvIrp79BwyUNM%252C_&vet=1&usg=AI4_-kQvto3e6I_SZTpIEyX7nc7rhRXIIQ&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQ9QF6BAgOEAE#imgrc=zqEz3gJ7p8dZwM",
            "link_0": "/search?q=gulmarg&tbm=isch&source=iu&ictx=1&fir=zqEz3gJ7p8dZwM%252Cvj6zfiOc_gvR1M%252C_%253BUo87NmXul6Ka9M%252CydjH7Y-Ndmv20M%252C_%253B_ysWTmXGBPSJVM%252Cger8IWrnyAHeLM%252C_%253BLCr_wbxPyfenUM%252CXHlwtSCSfbpw5M%252C_%253BcAPBLInxWlVjiM%252CGIFJkwIC2DSKJM%252C_%253Bquv7pOtIHZ-mmM%252Cx-mml25N3onQuM%252C_%253Br2Luss7397R5kM%252CGy0ekCg1lPK4eM%252C_%253BeeLInKD7Sl1a2M%252Cv3Gon5ykQSzLZM%252C_%253BYbBjG3yl8juNNM%252CuMfgSwGZlKXMsM%252C_%253B48SQ7eHTRLvXQM%252CxGvIrp79BwyUNM%252C_&vet=1&usg=AI4_-kQvto3e6I_SZTpIEyX7nc7rhRXIIQ&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQ9QF6BAgOEAE#imgrc=zqEz3gJ7p8dZwM",
            "link_2": "/search?q=gulmarg&tbm=isch&source=iu&ictx=1&fir=zqEz3gJ7p8dZwM%252Cvj6zfiOc_gvR1M%252C_%253BUo87NmXul6Ka9M%252CydjH7Y-Ndmv20M%252C_%253B_ysWTmXGBPSJVM%252Cger8IWrnyAHeLM%252C_%253BLCr_wbxPyfenUM%252CXHlwtSCSfbpw5M%252C_%253BcAPBLInxWlVjiM%252CGIFJkwIC2DSKJM%252C_%253Bquv7pOtIHZ-mmM%252Cx-mml25N3onQuM%252C_%253Br2Luss7397R5kM%252CGy0ekCg1lPK4eM%252C_%253BeeLInKD7Sl1a2M%252Cv3Gon5ykQSzLZM%252C_%253BYbBjG3yl8juNNM%252CuMfgSwGZlKXMsM%252C_%253B48SQ7eHTRLvXQM%252CxGvIrp79BwyUNM%252C_&vet=1&usg=AI4_-kQvto3e6I_SZTpIEyX7nc7rhRXIIQ&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQ9QF6BAgOEAE#imgrc=zqEz3gJ7p8dZwM",
            "link_4": "/search?q=gulmarg&tbm=isch&source=iu&ictx=1&fir=zqEz3gJ7p8dZwM%252Cvj6zfiOc_gvR1M%252C_%253BUo87NmXul6Ka9M%252CydjH7Y-Ndmv20M%252C_%253B_ysWTmXGBPSJVM%252Cger8IWrnyAHeLM%252C_%253BLCr_wbxPyfenUM%252CXHlwtSCSfbpw5M%252C_%253BcAPBLInxWlVjiM%252CGIFJkwIC2DSKJM%252C_%253Bquv7pOtIHZ-mmM%252Cx-mml25N3onQuM%252C_%253Br2Luss7397R5kM%252CGy0ekCg1lPK4eM%252C_%253BeeLInKD7Sl1a2M%252Cv3Gon5ykQSzLZM%252C_%253BYbBjG3yl8juNNM%252CuMfgSwGZlKXMsM%252C_%253B48SQ7eHTRLvXQM%252CxGvIrp79BwyUNM%252C_&vet=1&usg=AI4_-kQvto3e6I_SZTpIEyX7nc7rhRXIIQ&sa=X&ved=2ahUKEwiikamrkYj0AhX4q3IEHWDSCKAQ9QF6BAgOEAE#imgrc=zqEz3gJ7p8dZwM"
        },
```



### Run Scraper
```sh
from google_scraper_dk import *
link="https://www.google.com/search?q=gulmarg&sxsrf=AOaemvIicejw7VKgxoU621evbbfFgltrHg%3A1633101464052&source=hp&ei=lyZXYdHqPNGTr7wPjMOF4Ag&iflsig=ALs-wAMAAAAAYVc0qCoMYl7y9-lMnkZgA5PnNEovKB-e&gs_ssp=eJzj4tTP1TcwNaksNjBg9GJPL83JTSxKBwA5ugYF&oq=gulmarg&gs_lcp=Cgdnd3Mtd2l6EAEYADILCC4QgAQQsQMQkwIyCAgAEIAEELEDMgUIABCRAjIOCC4QgAQQsQMQxwEQrwEyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEMkDMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6DQguEMcBEK8BEOoCECc6BAgjECc6CwgAELEDEIMBEJECOhEILhCABBCxAxCDARDHARDRAzoFCC4QgAQ6CAguELEDEIMBOggILhCABBCxAzoICAAQsQMQgwE6CwguEIAEEMcBEK8BUIItWP84YPpKaAFwAHgAgAHUA4gBnQuSAQcyLTMuMS4xmAEAoAEBsAEK&sclient=gws-wiz"
data=run_google_scraper(link)
```

### How it works?
* It takes URL of google page to scrape the data.
* We can scrape any search result just by changing URL from above code.
* It generates the json data which contains the information of the google search result.
* It gives the title, link , a small description etc in the form of json data.


### Examples
Below are some of the examples of URLs using which you can scrape:

1. [Example 1](https://www.google.com/search?q=gulmarg&sxsrf=AOaemvIicejw7VKgxoU621evbbfFgltrHg%3A1633101464052&source=hp&ei=lyZXYdHqPNGTr7wPjMOF4Ag&iflsig=ALs-wAMAAAAAYVc0qCoMYl7y9-lMnkZgA5PnNEovKB-e&gs_ssp=eJzj4tTP1TcwNaksNjBg9GJPL83JTSxKBwA5ugYF&oq=gulmarg&gs_lcp=Cgdnd3Mtd2l6EAEYADILCC4QgAQQsQMQkwIyCAgAEIAEELEDMgUIABCRAjIOCC4QgAQQsQMQxwEQrwEyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEMkDMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6DQguEMcBEK8BEOoCECc6BAgjECc6CwgAELEDEIMBEJECOhEILhCABBCxAxCDARDHARDRAzoFCC4QgAQ6CAguELEDEIMBOggILhCABBCxAzoICAAQsQMQgwE6CwguEIAEEMcBEK8BUIItWP84YPpKaAFwAHgAgAHUA4gBnQuSAQcyLTMuMS4xmAEAoAEBsAEK&sclient=gws-wiz)

2. [Example2](https://www.google.com/search?q=phelgam+kashmir&sxsrf=AOaemvLYYWz0se2p5fQQEAE0b5y0GOxw5Q%3A1633101475907&ei=oyZXYbXpNpKf4-EPpMKowAo&gs_ssp=eJzj4tTP1TdIMy0vzzNg9OIvyEjNSU_MVchOLM7IzSwCAH_mCX0&oq=phelgam+kashmir&gs_lcp=Cgdnd3Mtd2l6EAEYADIICC4QkQIQkwIyBQgAEJECMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BwgAEEcQsAM6BwgAELADEEM6DQguEMgDELADEEMQkwI6CgguEMgDELADEEM6EAguEMcBEK8BEMgDELADEEM6BwgjEOoCECc6BwguEOoCECc6DQguEMcBEK8BEOoCECc6BAgjECc6BAguEEM6BAgAEEM6DQguEMcBEK8BEEMQkwI6BQguEJECOgoILhDHARCvARBDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQ0QNKBQg4EgExSgQIQRgAUJ-ZAViVsgFg28IBaANwAngAgAG5A4gB1weSAQcyLTIuMC4xmAEAoAEBsAEKyAEPwAEB&sclient=gws-wiz)


### Queries/ Feedback
If you have some queries or feedback please contact us at following    
[Telegram](https://t.me/datakund)  
[Email](abhishek@datakund.com)