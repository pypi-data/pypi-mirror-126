# S T E R R A X C Y L
## OSINT via Instagram Followers / Following
Allows you to analyse someone's followers, following, and mutuals to determine the close social circle of your target.  
Also a great alternative to [Export List of Followers from Instagram](https://chrome-stats.com/d/hcdbfckhdcpepllecbkaaojfgipnpbpb), that has been killed.  

### Here is the result for the accounts followed by kyliejenner :
![](https://i.imgur.com/CeP9nSQ.png)

# Installation
```python
#via pypi
pip install sterratest
#sterraxcyl in official version

#via github (you can copy the whole line)
git clone https://github.com/novitae/sterraxcyl; cd sterraxcyl; python setup.py install
```

# Usage examples:
## Simple usage:
```python
#sterra or sterraxcyl can be both used to invoke the program
sterra -h
#print the help

sterra -u kyliejenner -t following -sssid SSSID
#will export on excel, in the /export direcotry of the module, the table of accounts kyliejenner follows

sterra -u kyliejenner -t following -sssid -e --all-infos
#same than before, but in express mode, and with a lot more details exported (see further will --all-infos)

sterra -u chrstianpedroza -t mutuals -sssid -a --do-not-export
#will not export, but will print probabilities for each account following and being followed back by chrstianpedroza of being personnal accounts.

sterra -u chrstianpedroza -t both -sssid -a -f csv -p desktop/OSINT/ --descending --size 30
#will export at desktop/OSINT/ in csv lists of followers and following of chrstianpedroza, and also print the 30 lowest probabilites of being personnal accounts in each lists.

*chrstianpedroza is my account, im not exposing random mexicans
```

## Arguments
```python
usage: sterra -t {followers,following,both,mutuals} (-u U | -id ID) (-lcrd U P | -ssid S)
              [--all-infos] [--do-not-export] [-e] [-f {excel,csv}] [-h] [--no-limit] [--no-btc]
              [-p P] [-a] [--pctg PCTG] [--size SIZE] [--url] [--descending]


required arguments:

  -t {followers,following,both,mutuals}, --target {followers,following,both,mutuals}
                        what do you want to export ("followers", "following", "both" or "mutuals")
  -u U, --username U    the instagram username of the aimed account
  -id ID                the instagram id of the aimed account

login arguments:

  -lcrd U P, --login-credentials U P
                        login by credentials: USERNAME PASSWORD (be sure to keep a space between them)
  -ssid S, --login-session-id S
                        login by SessionID

probabilities arguments:

  -a, --activate-data-analysis
                        activates a data analysis that prints, for each accounts in the target lists, the probabilities of being an account from the close circle of the target
  --pctg PCTG           percentage under wich we won't print results (between 0 and 98)
  --size SIZE           size of the most probable username list (will be by default the size of the followers/mutuals/following list filled in)
  --url                 instead of printing username, printing the url to the account
  --descending          instead of printing by highest probability, printing by lowest probability

optional arguments:

  --all-infos           writes down the account extra informations that the program originaly ignores
  --do-not-export       do not export to file
  -e, --express         sends ultra fast requests to get the table faster (deactivated if more than 109 total usernames to avoid blocking)
  -f {excel,csv}, --format {excel,csv}
                        format of the export, by default "excel"
  -h, --help            show this help message and exit
  --no-limit            disable the limitation for lists over 1000 follow(ers|ing); all errors you could get by doing this will not recieve help if you submit it at the issue page of sterraxcyl
  --no-btc              hides the invitation to donations printed at the end
  -p P, --path P        directory path where export the files (by default in your module path)
```