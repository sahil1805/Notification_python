from plyer import notification
import requests
from bs4 import BeautifulSoup


def notificationToMe(head, text):
    notification.notify(
        title=head,
        message=text,
        app_icon=None,
        timeout=3
    )


def notificationData(url):
    notifyData = requests.get(url)
    return notifyData.text


if __name__ == "__main__":
    siteData = notificationData(url='https://www.mohfw.gov.in/')
    siteData = siteData.replace('<!--<tbody>', '<tbody>')
    siteData = siteData.replace('</tr>-->', '</tr>')
    soup = BeautifulSoup(siteData, 'html.parser')
    myDataStr = ''
    for tbody in soup.find_all('tbody'):
        for tr in tbody.find_all('tr'):
            myDataStr += tr.get_text()
    myDataStr = myDataStr[1:].split('\n\n')
    dataAll = []
    for item in myDataStr[0:35]:
        dataAll.append(item.split('\n'))
    # print(dataAll)
    for i in range(len(dataAll)):
        print(dataAll[i])
    head = 'Notification About Covid'
    text = f'{dataAll[11][1]}\nTotal Active cases : {dataAll[11][2]}\nTotal Recovered : {dataAll[11][3]}\nTotal death : {dataAll[11][3]}'
    notificationToMe(head, text)
