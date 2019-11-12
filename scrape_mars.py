#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from splinter import Browser

def init_browser():
        executable_path = {'executable_path': 'chromedriver.exe'}
        return Browser('chrome', **executable_path, headless=False)

def scrape_info():
        url = "https://mars.nasa.gov/news/"
        browser = init_browser()
        browser.visit(url)


        html = browser.html

        # Create BeautifulSoup object; parse with 'html.parser'
        soup = BeautifulSoup(html, "html.parser")

        # results are returned as an iterable list
        results = soup.find_all("li", class_="slide")
        type(results)


        # Collect the latest news title and paragraph text

        news_title = soup.find(class_="content_title").a.text
        news_p = soup.find(class_="rollover_description_inner").text


        print(news_title)
        print(news_p)

        mars_data = {"news_title": news_title, "news_p": news_p}
        
        browser.quit()

        for result in results:
                # Identify and return title of listing
                title = result.find(class_="content_title").a.text

                # Print results only if title, price, and link are available
                print('-------------')
                print(title)


        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)


        jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(jpl_url)

        # Create BeautifulSoup object; parse with 'html.parser'
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        # Collect the featured image url

        featured_image_partial = soup.footer.a['data-fancybox-href']

        featured_image_url = (f"https://www.jpl.nasa.gov{featured_image_partial}")

        print(featured_image_url)

        mars_data.update({"featured_image_url": featured_image_url})

        browser.quit()

        # Open up chrome with chrome driver
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)

        # Navigate to the mars weather twitter page
        mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(mars_twitter_url)

        # Create a beautiful soup object from the mars twitter weather page
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        # Collect the the latest tweet
        mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
        mars_twitter_link = mars_weather.find("a")
        mars_twitter_link.extract()
        mars_weather = mars_weather.text

        print(mars_weather)

        mars_data.update({"mars_weather": mars_weather})

        brows
        # Mars facts url
        mars_facts_url = "https://space-facts.com/mars/"

        #Use pandas to parse the html
        table = pd.read_html(mars_facts_url)

        facts_df = table[1]

        facts_df.head()


        html_table = facts_df.to_html()
        html_table

        html_table.replace("\n", "")

        facts_df.to_html("mars_facts_table.html")


        # Open up chrome with chrome driver
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)

        # Create a list of the four hemisphere urls
        hemisphere_urls = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced", "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
                "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced", "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

        hemisphere_image_urls = {}
        hemisphere_image_urls["title"] = []
        hemisphere_image_urls["img_url"] = []

        # loop through each link and pull the desired information 
        for hemisphere in hemisphere_urls:
        
                browser.visit(hemisphere)
                
                # create a beautiful soup object
                html = browser.html
                soup = BeautifulSoup(html, 'html.parser')
                
                img_url = soup.li.find("a")['href']
                title = soup.find("h2", class_="title").text
                title = title.replace(" Enhanced", "")

                hemisphere_image_urls["title"].append(title)
                hemisphere_image_urls["img_url"].append(img_url)

                # hemisphere_dict = {"title": title, "img_url": img_url}

                # hemisphere_image_urls.append(hemisphere_dict)
        
        browser.quit()

        mars_data.update(hemisphere_image_urls)

        return mars_data

        
