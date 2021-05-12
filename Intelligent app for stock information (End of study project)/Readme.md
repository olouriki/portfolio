# I - Presentation

My project is to build a cross-platform dashboard (web site, mobile application, …) for the finance domain which will propose many functionalities using AI. The application is aimed to respond to the increasing growth and popularity of the cryptocurrency market. 

The recent event related to the GameStop short squeeze by the reddit community, and the exponential value increase of Bitcoin led to this project idea.
The application will propose many functionalities which the main one will be to predict a score about a certain company using web scraping, Machine Learning and/or Deep Learning. You will find the detailed list of functionalities below.

# II – Datasets

The main source of data will be the web. So, my application will use web scraping to scrape data about a certain company or a certain share. The other source will be open source data about companies.

## Open-Source data:
* http://finance.yahoo.com/

* https://stats.oecd.org/index.aspx

* https://home.treasury.gov/

* https://db.nomics.world/

* https://www.assetmacro.com/

* http://www.forecasts.org/

* http://www.statistics.gov.uk/

* https://www.ssa.gov/

* https://www.bls.gov/

* https://www.census.gov/

* http://www.iasg.com/managed-futures/market-quotes

* http://www.ivolatility.com/

* http://www.optionmetrics.com/

* http://www.livevol.com/
 
## Data from Web Scraping:

- News

- Company websites

* Forum

* Social network (Tweeter, Facebook, LinkedIn, …)

# III – Functionalities

Here is the non-exhaustive list of functionalities:

* Web scraping / Crawler: Scrap data (pictures, texts, news, numerical data…) of a certain company chosen by the user.

* Tendency summary of a target company: Generate a summary of the scraped data for a targeted company using NLP techniques.

* Tendencies prediction of a target company: Predict tendencies of the targeted company using one or multiple models.

* Real time company ranking per domain:  Rank the companies of a certain domain chosen by the user based on their tendency at time t.

* Company ranking predictor per domain:  Predict the top ranked companies of a certain domain chosen by the user at time t+1.

* Dashboard: User-friendly graphical interface to synthesize results coming from the models.

# IV – Technical environment

<img align="left" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" alt="python_logo" width="50"/> Python will be the main language I will use to scrape data (tweepy, PRAW...), prepare my datasets (Pandas, numpy...), and create my models (scikit-learn, Bert, Pytorch…)

<img align="left" src="https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png" alt="python_logo" width="50"/> 
<br>I will use React JS to create my cross platform application<br>
<br>
<img align="left" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh8krcz53Tvpur6TAkE0YHVsLtmKou9j6qSzFmkmODP1qMu5mBZ-_CH9NFAhA0_m9mJL8&usqp=CAU" width="50"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cloud: AWS (EC2, Sagemaker, S3...) or GCP.  

