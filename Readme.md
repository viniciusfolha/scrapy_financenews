# Project Scrapy for Finance

This project collects the finance news from the website InfoMoney. It is an initial development for evaluation purposes.

## Why scrapy?
I used the scrapy framework because it is async, makes the requests and does not need to wait for every request to be done to start to process. It also a fast high-level web crawling and scraping framework for Python.

## Getting Started

These instructions will help you to run this project on your machine. See deployment for notes on how to deploy the project on your environment.

### Prerequisites
    The project was made using MongoDB and Python, your libraries and frameworks.
    The main prerequisites is below, however, It can be found the entire list on requirements.txt:
```
Python 3
PIP
MongoDB
Virtualenv
Scrapy
Spidermon
Pymongo
```

### Installing

Install python, pip and some dependencies
```
sudo apt-get install python3 python3-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

Install and Update pip
```
pip3 install --upgrade pip --user
```

Install virtualenv and create env
```
python3 -m pip install --user virtualenv
python3 -m venv env
```

Active virtualenv and install Scrapy
```
source env/bin/activate
pip install scrapy --upgrade
```

Install spidermon for monitor
```
pip install "spidermon[monitoring,validation]"
```

Install pymongo for database communication
```
pip install pymongo
```

It`s necessary to install MongoDB on computer and start the service
```
This command only start, check some tutorial how to install
sudo service mongod start
```


### How to RUN:
With Env actived, run this command below and get the monitor result and populate the DB.
```
scrapy crawl Infomoney -s HTTPCACHE_ENABLED=1
Result:
2019-10-24 00:36:28 [scrapy.core.engine] INFO: Closing spider (finished)
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] ------------------------------ MONITORS ------------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] Item count/Minimum number of items... OK
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] NotFoundPage/Check not found page... OK
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] ----------------------------------------------------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] 2 monitors in 0.001s
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] OK
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] -------------------------- FINISHED ACTIONS --------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] ----------------------------------------------------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] 0 actions in 0.000s
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] OK
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] --------------------------- PASSED ACTIONS ---------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] ----------------------------------------------------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] 0 actions in 0.000s
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] OK
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] --------------------------- FAILED ACTIONS ---------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] ----------------------------------------------------------------------
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] 0 actions in 0.000s
2019-10-24 00:36:28 [Infomoney] INFO: [Spidermon] OK
2019-10-24 00:36:28 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 18427,
 'downloader/request_count': 53,
 'downloader/request_method_count/GET': 53,
 'downloader/response_bytes': 789022,
 'downloader/response_count': 53,
 'downloader/response_status_count/200': 49,
 'downloader/response_status_count/301': 4,
 'dupefilter/filtered': 14,
 'elapsed_time_seconds': 3.136442,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 10, 24, 3, 36, 28, 204742),
 'httpcache/firsthand': 29,
 'httpcache/hit': 24,
 'httpcache/miss': 29,
 'httpcache/store': 29,
 'item_dropped_count': 19,
 'item_dropped_reasons_count/DropItem': 19,
 'item_scraped_count': 25,
 'log_count/DEBUG': 124,
 'log_count/INFO': 28,
 'log_count/WARNING': 19,
 'memusage/max': 62316544,
 'memusage/startup': 62316544,
 'request_depth_max': 3,
 'response_received_count': 49,
 'robotstxt/request_count': 2,
 'robotstxt/response_count': 2,
 'robotstxt/response_status_count/200': 2,
 'scheduler/dequeued': 50,
 'scheduler/dequeued/memory': 50,
 'scheduler/enqueued': 50,
 'scheduler/enqueued/memory': 50,
 'start_time': datetime.datetime(2019, 10, 24, 3, 36, 25, 68300)}
2019-10-24 00:36:28 [scrapy.core.engine] INFO: Spider closed (finished)
```
## Authors

* **Vinicius Folha** - *Initial work* -

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Future work

Improve the monitor checks and generate reports

Save database URI on Environment Variable for security 

Solve the problem with infinity-scrolling

On settings, set better params for request

Enable proxy to avoid ban. :)

Create a job

