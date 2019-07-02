#python notebook

import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" ) 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

def printdom(doms):
  for i in doms:
    print(i.text)

###################################rank_left_content > div > div.TimecataRank_body > div > a:nth-child(5) > span.rank_left_name

b = webdriver.Chrome()
b.get("http://baike.baidu.com")
dom = b.find_element_by_css_selector("#query")
dom.send_keys("宋仲基")
dom = b.find_element_by_css_selector("#search")
dom.click()
allelements = b.find_elements_by_css_selector("div.lemma-summary")
for i in allelements:
    print(i.text)

allelements = b.find_elements_by_css_selector("div.basic-info.cmn-clearfix")
for i in allelements:
    print(i.text)

##################################

b = webdriver.Chrome()
url0 = "http://www.xunyee.cn/rank-person-index-0-page-"
for i in range(1,21):
  urli = "%s%d.html"%(url0,i)
  print(urli)
  b.get(urli)
  dom = b.find_elements_by_css_selector(".rank_left_name")
  printdom(dom)
  

  
b.get("http://www.xunyee.cn/rank-person-index-0-page-1.html")
dom = b.find_elements_by_css_selector(".rank_left_name")
for i in dom:
    print(i.text)

#rank_left_content > div > div.TimecataRank_body > div > a:nth-child(2) > span.rank_left_name
#rank_left_content > div > div.TimecataRank_body > div > a:nth-child(5) > span.rank_left_name
