# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:13:21 2018

@author: Shenghai

Clean up Wells Fargo statement scraper even further with more objects

There are two previous verions of this scraper.
Thi is most improved one with classes
"""
import os
import time
import zipfile

from selenium import webdriver as wd

class Constants:
    def __init__(self):
        self.ZERO = 0
        self.ONE  = 1
        self.TWO  = 2
        self.THREE = 3
        self.FOUR = 4
        self.FIVE = 5
        self.SIX  = 6
        self.EIGHT = 8
        self.TEN  = 10
        self.TWELVE = 12
        self.EIGHTEEN = 18
        self.THIRTY = 30

class LoginInfo:
    def __init__(self, login_page=None, username=None, password=None):
        self.login_page = login_page
        self.username = username
        self.password = password

class LoginAct:
    def __init__(self, info=None):
        self.constants = Constants()
        self.info = info
        self.driver = None

    def get_login_page(self):
        returnval = self.info
        while returnval is not None:
            return returnval.login_page

    def prompt_driver(self):
        driver = wd.Chrome()
        webpage = self.get_login_page()
        driver.get(webpage)

        # Doing the login action
        try:
            username = driver.find_element_by_id("user_id")
            password = driver.find_element_by_id("password")
            username.send_keys(self.info.username)
            password.send_keys(self.info.password)

            # Xpath copied from the Chrome developer mode
            login_attempt = driver.find_element_by_xpath("//*[@id='loginButton']")
            login_attempt.click()

        except:
            print("Exception happened in prompt_driver function!!!")
            print("Error handling happened in login.")
            print("Exiting the program now.")
            return

        self.driver = driver

    def link_page(self, links=None, dist_date=None):
        self.links = links
        self.dist_date = dist_date

        # find the main downlaod folder
        try:
            home = os.path.expanduser("~")
            home = os.path.join(home, "Downloads")
        except:
            print("Cannot find the users' Downloads folder")
            return

        for link in links:
            try:
                if link[-self.constants.EIGHTEEN:].find('=', self.constants.ZERO, len(link)) > -self.constants.ONE:
                    index = link[-self.constants.EIGHTEEN:].find("=", self.constants.ZERO, len(link))
                else:
                    print("Cannot find the equal sign in the url list!")

                # UMAC, UMLT, SMLT
                # 201632, 201836, etc.
                series_name = link[-self.constants.EIGHTEEN + index + \
                                   self.constants.ONE:][self.constants.ZERO:self.constants.FOUR]
                eti_numeric_name = link[-self.constants.EIGHTEEN + index + \
                                        self.constants.ONE:][self.constants.FIVE:-self.constants.FOUR]

                zip_file_name = "{}_{}_reports.zip".format(series_name, eti_numeric_name)

                if eti_numeric_name[-self.constants.TWO:] == 'RT':
                    if len(eti_numeric_name) == self.constants.EIGHT:
                        dealname = "{}-{}".format(eti_numeric_name[self.constants.ZERO:self.constants.FOUR], \
                                                  eti_numeric_name[self.constants.FOUR:self.constants.SIX])
                    else:
                        dealname = "{}-0{}".format(eti_numeric_name[self.constants.ZERO:self.constants.FOUR], \
                                                  eti_numeric_name[self.constants.FOUR:self.constants.FIVE])
                else:
                    if len(eti_numeric_name) == self.constants.SIX:
                        dealname = eti_numeric_name[self.constants.ZERO:self.constants.FOUR] + "-" + \
                                   eti_numeric_name[self.constants.FOUR:self.constants.SIX]
                    else:
                        dealname = eti_numeric_name[self.constants.ZERO:self.constants.FOUR] + "-0" + \
                                   eti_numeric_name[self.constants.FOUR:self.constants.FIVE]

                # searching for loop to find the user input dist_date and website dist_date
                # For Carrington deal it should be the 15th of every month unless is a holiday or weekends
                # //*[@id="seriesdocs"]/div/div/table/tbody/tr[3]/td[2]
                self.driver.get(link)

                for j in range(self.constants.ONE, self.constants.THIRTY):
                    try:
                        # //*[@id="seriesdocs"]/div/div/table/tbody/tr[3]/td[2]
                        # //*[@id="seriesdocs"]/div/div/table/tbody/tr[3]/td[2].

                        day_el = self.driver.find_element_by_xpath("//*[@id='seriesdocs']/div/div/table/tbody/tr[" + str(j) + "]/td[2]")
                    except:
                        pass
                    else:
                        if ((day_el.text[self.constants.ZERO:self.constants.TWO] == self.dist_date[-self.constants.TWO:]) and \
                            (day_el.text[-self.constants.TWO:] == self.dist_date[self.constants.ZERO:self.constants.TWO])):

                            day = day_el.text
                            break

                # will be appended into a list to unzip the file
                lst = [home + "\\" + zip_file_name, dealname]

                # this condition probably will never hit, since brian and i roll all the deals every month
                if "all" in self.dist_date:
                    checkbox1 = self.driver.find_element_by_xpath("//*[@id='" + "20" + \
                                                                  self.dist_date[-self.constants.TWO:] + "PDF']")
                    checkbox1.click()
                    checkbox2 = self.driver.find_element_by_xpath("//*[@id='" + "20" + \
                                                                  self.dist_date[-self.constants.TWO:] + "XLS']")
                    checkbox2.click()

                # Mostly for carrington SMLT deals
                else:
                    dist_day = day[self.constants.THREE:self.constants.FIVE]
                    # //*[@id="chk_2018PDF0"]
                    checkbox1 = self.driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle 20" + \
                                                                  self.dist_date[self.constants.ZERO:self.constants.TWO] + "-" + \
                                                                  self.dist_date[-self.constants.TWO:] + "-" + dist_day + " and format PDF')]")
                    checkbox1.click()
                    checkbox2 = self.driver.find_element_by_xpath("//input[contains(@aria-label, 'Select cycle 20" + \
                                                                  self.dist_date[self.constants.ZERO:self.constants.TWO] + "-" + \
                                                                  self.dist_date[-self.constants.TWO:] + "-" + dist_day + " and format XLS')]")
                    checkbox2.click()

                zip_download = self.driver.find_element_by_xpath("//*[@name='zip']")

                # if it is last file ensure download the file first before it closes out the browser
                if (links.index(link) == (len(links) - self.constants.ONE)):
                    zip_download.click()
                    print("File " + zip_file_name + " downloaded")
                    time.sleep(self.constants.THREE)

                elif(links.index(link) == (len(links) - self.constants.ONE)):
                    zip_download.click()
                    print("File " + zip_file_name + " downloaded")
                    time.sleep(self.constants.THREE)
                    print("Dowloading file(s) completed!!!")

                else:
                    zip_download.click()

                    print("File " + zip_file_name + " downloaded")

                self.unpack_unzipped(lst, self.driver.title)

            except:
                print("Error handling happened in link_page function!!!")


    def unpack_unzipped(self, zippedfile=None, title=None):
        self.zippedfile = zippedfile
        self.title = title

        try:
            while bool(self.title):
                try:
                    zip_ref = zipfile.ZipFile(zippedfile[self.constants.ZERO], 'r')
                    break
                except:
                    continue

            zip_ref.extractall("D:/deals/Carrington/aggdata/stmts/" + str(zippedfile[self.constants.ONE]))
            print("File is unzipped into " + "D:/deals/Carrington/aggdata/stmts/" + str(zippedfile[self.constants.ONE]))
            zip_ref.extractall("D:/deals/Carrington/SMAC/" + str(zippedfile[self.constants.ONE]) + "/stmts")
            print("File is unzipped into " + "D:/deals/Carrington/SMAC/" + str(zippedfile[self.constants.ONE]) + "/stmts")

            zip_ref.close()
            os.remove(zippedfile[self.constants.ZERO])

        except:
            print("Error handling happened in unpack_zippedfile function!!!")


class UserInput:
    def __init__(self):
        self.const = Constants()

    def user_input_yymm(self):
        # Asking user for year and month input as yymm
        # Retun the date as a 4-digit string as yymm
        try:
            while True:

                distribution_yymm = input("Please enter the distrituion month and year, " + \
                                               "(example 1701 for January 2017): ")
                try:
                    if (int(distribution_yymm[self.const.TWO:self.const.FOUR]) >= self.const.ONE) and \
                    (int(distribution_yymm[self.const.TWO:self.const.FOUR]) <= self.const.TWELVE) and \
                    (len(distribution_yymm) == self.const.FOUR):

                        month = int(distribution_yymm[self.const.TWO:self.const.FOUR])
                        year = int(distribution_yymm[self.const.ZERO:self.const.TWO])
                        if month < self.const.TEN:
                            month = "0{}".format(str(month))
                        else:
                            month = str(month)

                        distribution_yymm= "{}{}".format(str(year), str(month))
                        break
                    else:
                        print("Let's try this again!")
                        continue

                except:
                    print("Let's try this again!")
                    pass

            # return dist_date as a string like 1801 for Jan. 2018
            return distribution_yymm

        except:
            print("Error handling happened in user_input function!!!")


