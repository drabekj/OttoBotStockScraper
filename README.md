# OttoBot Stock Scraper

## Description:
Lambda function triggered everyday to add the newest stock information for all ticker from Quandal API to AWS RDS database.

## Components:
	1) CloudWatch (trigger)
	2) AWS Lambda (execution)
	3) AWS RDS (DB)
	4) Quandl API (data source API)

										 /- API
										/
	CloudWatch trigger - - - > Lambda <
									    \
										 \- DB

### 1) CloudWatch rule
* role: trigger for lambda
* name: ottobot-scrape-stock-daily
* region: Frankfurt

* description: triggers lambda everyday at 16:00:00 GMT

### 2) AWS Lambda 
* role: execution
* name: OttoBotStockScraperDaemon
* region: Frankfurt
* VPC: ottoBotVPC
* subnets: eu-central-1b, eu-central-1c (both private subnets inside ottoBotVPC, internet access via NAT Gateway)
* security group: ottoBotPrivateSG

* description: Pulls yesterday's data for all tickers from data source (Quandal API) and saves it to database (RDS). Gets triggered by CLoudWatch rule ottobot-scrape-stock-daily. Creating lambda function package for upload is done via archive_script.sh, packs dependencies and code into a zip file, which is ready to be uploaded either manually or via S3 (bucket: ottobotstockscraperdaemonbucket)

### 3) AWD RDS
* role: data storage (DB)
* name: myottobotdb
* region: Frankfurt
* VPC: ottoBotVPC
* security group: ottobotRDSsg (allows connection to DB from private subnets - that's where lambda runs)

### 4) Quandl API
* role: provide stock data (API)
* output: json data

* description: Quandl WIKI/PRICES database offers stock prices, dividends and splits for 3000 US publicly-traded companies. This database is updated at 9:15 PM EST every weekday (15:15 Prague).

## Infrastructure:

### VPC:
* name: ottoBotVPC
* CIDR: 10.0.0.0/16
* 3 subnets:
⋅⋅* 1 public: "10.0.1.0 - eu-central-1a"
⋅⋅* 2 private: "10.0.2.0 - eu-central-1b", "10.0.3.0 - eu-central-1c" => internet connection via NAT

### Security Groups:
1. default
2. ottoBotPublicSG: public security group inside ottoBotVPC for OttoBot, open SSH, HTTP and HTTPS from anywhere (0.0.0.0/0)
3. ottoBotPrivateSG: private security group inside ottoBotVPC for OttoBot, open ssh from public subnet (10.0.1.0/24)
4. ottobotRDSsg: for RDS in ottoBotVPC, opens MySQL/Aurora (3306) from private subnets (ottoBotPrivateSG, 10.0.2.0, 10.0.3.0)⋅⋅
!!! opened 3306 for ottoBotPublicSG to be able to DEBUG: inspect db from EC2 in public subnet => close when finished debugging
