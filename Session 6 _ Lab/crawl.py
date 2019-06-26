from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


# 1. Open connection
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode('utf8') # chuan utf8 (gg)

# print(content)

# 2. Find ROI (region of interest)
soup = BeautifulSoup(content, "html.parser") # khai bao du lieu
ul = soup.find("ul", "ul1 ulnew") # Only class can use only name. With other attribute, new full version
# print(ul.prettify())

# 3. Extract ROI
li_list = ul.find_all("li")
# print(li_list)

saved_list = []


for li in li_list:
   
    # # print(li.prettify())
    # a = li.h4.a
    # tittle = a.string.strip() # strip: bo khoang cach thua
    # # print(tittle) 
    # dic["Tittle"] = tittle
    # link = url + a["href"]
    # # print(link)
    # dic["Link"] = link
    # dic = OrderedDict(dic)
    # saved_list.append(dic)
    
    # Solution: techkid
    a = li.h4.a
    tittle = a.string.strip()
    link = url + a["href"]
    news = OrderedDict({
        "Tittle": tittle,
        "Link": link
    })
    saved_list.append(news)

print(*saved_list)

# 4. Save data
# from collections import OrderedDict


pyexcel.save_as(records=saved_list, dest_file_name="Link.xls")

