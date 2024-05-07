import requests

url = 'https://labour.gov.in/sites/default/files/mpr_december_2023.pdf'

response = requests.get(url)

if response.status_code == 200:
    filePath = 'monthlyProgressReport.pdf'

    f = open(filePath, 'wb')
    f.write(response.content)
    f.close()

else:
    print('error')