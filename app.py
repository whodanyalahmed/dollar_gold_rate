import requests,os,datetime,csv,time
from bs4 import BeautifulSoup
from gold import sendEmail
logFile = open("log.txt","a+")
logFile.write("\nStarted at: " + str(datetime.datetime.now()))
print("info : processing ")
logFile.write("\ninfo : processing ")
def getGoldRate():
    url = "https://hamariweb.com/finance/gold_rate/"
    # url = "https://hamariweb.com/finance/forex/gbp-to-pkr.aspx"

    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    # div = soup.findChild("div",attrs={'id':"main-content"})
    # div_soup = BeautifulSoup(str(div),'lxml')
    # divs = div_soup.find_all("div")
    input = soup.find_all("tr")[2].text.split("\n")[2]

    return input

def getDollarRate():

    url = "https://hamariweb.com/finance/forex/usd-to-pkr.aspx"
    # url = "https://hamariweb.com/finance/forex/gbp-to-pkr.aspx"

    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    # div = soup.findChild("div",attrs={'id':"main-content"})
    # div_soup = BeautifulSoup(str(div),'lxml')
    # divs = div_soup.find_all("div")
    input = soup.find("input",attrs={'id':"currency2"})

    return input['value']

def Process():
    goldrate = getGoldRate()
    dollarrate = getDollarRate()
    if os.path.isfile('file.csv'):
        print ("info : File already exist")
        logFile.write("\ninfo : File already exist")
    else:
        with open("file.csv","w+",newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Date','Dollar_Rate',"Gold_Rate"])
            print ("info : File not exist... will create new file")
            logFile.write("\ninfo : File not exist... will create new file")
    row = []
    row.append(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
    row.append(dollarrate)
    row.append(goldrate)
    with open('file.csv',"a+",newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(row)
    print("success : complete")
    logFile.write("\nsuccess : complete")
    if(eval(dollarrate) >= 159):
        print("info : sending email")
        logFile.write("info : sending email")
        sendEmail("Dollar rate is: "+dollarrate + " and gold rate is: " + goldrate)
while True:
    Process()
    time.sleep(3600)