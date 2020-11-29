# IPriskIQ
IPriskIQ is a tiny python script used for host and reputation discovery.
This script uses the RiskIQ API to get the information, so you must register in their website and obtain a valid token (https://community.riskiq.com/login)

You can easily run the script using python 2.7 or above, giving the riskiq username followed by the token and providing a text file with all the IPs to be tested.

Example:
```sh
python ipriskiq.py <your_riskiq_username> <your_riskiq_token> file.txt
python ipriskiq.py your@email.com  b1dfd4b186941a3d4b18691eff7747582756d4b1869de120b3 ips.txt
```

The text file must contain the IPs line by line:

![ips](https://user-images.githubusercontent.com/36700364/100539880-c84dd200-3239-11eb-9152-db6b56584e94.png)


The output of the script will retrive all the different domains asociated to a single IP, the classification and the tags associated to each IP.

![ipriskiq](https://user-images.githubusercontent.com/36700364/100539798-20d09f80-3239-11eb-9177-0429cbc20fff.png)

