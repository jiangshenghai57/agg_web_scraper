# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:17:47 2018

@author: Shenghai
"""

import sys

from wells_stmts_scraper_misc_v3 import LoginInfo
from wells_stmts_scraper_misc_v3 import LoginAct
from wells_stmts_scraper_misc_v3 import UserInput

class DealUrl:
    def __init__(self):
        self.url = [
                    # Brian's Carrington deal list
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201320&doc=SMLT_201320_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201320RT&doc=SMLT_201320RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201321&doc=SMLT_201321_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201321RT&doc=SMLT_201321RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20141&doc=SMLT_20141_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20141RT&doc=SMLT_20141RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20144&doc=SMLT_20144_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20144RT&doc=SMLT_20144RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20153&doc=SMLT_20153_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20153RT&doc=SMLT_20153RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20154&doc=SMLT_20154_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20154RT&doc=SMLT_20154RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20155&doc=SMLT_20155_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20155RT&doc=SMLT_20155RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20157&doc=SMLT_20157_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20157RT&doc=SMLT_20157RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20165&doc=SMLT_20165_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20165RT&doc=SMLT_20165RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20166&doc=SMLT_20166_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20166RT&doc=SMLT_20166RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20167&doc=SMLT_20167_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20167RT&doc=SMLT_20167RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20168&doc=SMLT_20168_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20168RT&doc=SMLT_20168RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20169&doc=SMLT_20169_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20169RT&doc=SMLT_20169RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201610&doc=SMLT_201610_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201610RT&doc=SMLT_201610RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201611&doc=SMLT_201611_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201611RT&doc=SMLT_201611RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201612&doc=SMLT_201612_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201612RT&doc=SMLT_201612RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20171&doc=SMLT_20171_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20171RT&doc=SMLT_20171RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20172&doc=SMLT_20172_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20172RT&doc=SMLT_20172RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20173&doc=SMLT_20173_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20173RT&doc=SMLT_20173RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20174&doc=SMLT_20174_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20174RT&doc=SMLT_20174RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20175&doc=SMLT_20175_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20175RT&doc=SMLT_20175RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20176&doc=SMLT_20176_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20176RT&doc=SMLT_20176RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20179&doc=SMLT_20179_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20179RT&doc=SMLT_20179RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201721&doc=SMLT_201721_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201721RT&doc=SMLT_201721RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201731&doc=UMAC_201731_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201731RT&doc=UMAC_201731RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732&doc=UMAC_201732_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201732RT&doc=UMAC_201732RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733&doc=UMAC_201733_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201733RT&doc=UMAC_201733RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201734&doc=UMAC_201734_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201734RT&doc=UMAC_201734RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20181&doc=SMLT_20181_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20181RT&doc=SMLT_20181RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20182&doc=SMLT_20182_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20182RT&doc=SMLT_20182RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20184&doc=SMLT_20184_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20184RT&doc=SMLT_20184RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20183&doc=SMLT_20183_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20183RT&doc=SMLT_20183RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201831&doc=UMAC_201831_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201831RT&doc=UMAC_201831RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201832&doc=UMAC_201832_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201832RT&doc=UMAC_201832RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201833&doc=UMAC_201833_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201833RT&doc=UMAC_201833RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201834&doc=UMAC_201834_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201834RT&doc=UMAC_201834RT_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20185&doc=SMLT_20185_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20185RT&doc=SMLT_20185RT_RMT",
            
                    # Shenghai's deal list
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143&doc=SMLT_20143_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20143RT&doc=SMLT_20143RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145&doc=SMLT_20145_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20145RT&doc=SMLT_20145RT_RMT",    
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158&doc=SMLT_20158_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20158RT&doc=SMLT_20158RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159&doc=SMLT_20159_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20159RT&doc=SMLT_20159RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161&doc=SMLT_20161_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20161RT&doc=SMLT_20161RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164&doc=SMLT_20164_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20164RT&doc=SMLT_20164RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621&doc=SMLT_201621_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201621RT&doc=SMLT_201621RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623&doc=SMLT_201623_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=201623RT&doc=SMLT_201623RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631&doc=UMAC_201631_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201631RT&doc=UMAC_201631RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632&doc=UMAC_201632_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201632RT&doc=UMAC_201632RT_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201836&doc=UMAC_201836_RMT",
                    "https://www.ctslink.com/a/history.html?shelfId=UMAC&seriesId=201836RT&doc=UMAC_201836RT_RMT",
#                    
                    # Terminated deal
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151&doc=SMLT_20151_RMT",
#                    "https://www.ctslink.com/a/history.html?shelfId=SMLT&seriesId=20151RT&doc=SMLT_20151RT_RMT",
                ]

if __name__ == '__main__':
    login = LoginAct()
    login.info = LoginInfo(login_page = "http://www.ctslink.com", \
                           username = 'brianfilips', \
                           password = 'Suite82218!!')
    login.prompt_driver()
    UserInput = UserInput()
    dist_date = UserInput.user_input_yymm()
    login.link_page(links=DealUrl().url, dist_date=dist_date)
    login.driver.close()
    
    input("Press Enter to exit >>>")
    sys.exit()