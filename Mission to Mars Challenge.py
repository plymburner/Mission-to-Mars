#!/usr/bin/env python
# coding: utf-8

# In[50]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[51]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[52]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[53]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[54]:


slide_elem.find('div', class_='content_title')


# In[55]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# In[56]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[57]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[58]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[59]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[60]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[61]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[62]:


df.to_html()


# In[63]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[64]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for pict in range(4):
    # Browse through each article
    browser.links.find_by_partial_text('Hemisphere')[pict].click()
    
    # Parse the HTML
    html = browser.html
    mars_hemis_soup = soup(html,'html.parser')
    
    # Scraping
    title = mars_hemis_soup.find('h2', class_='title').text
    img_url = mars_hemis_soup.find('li').a.get('href')
    
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()


# In[65]:


hemisphere_image_urls


# In[66]:


# 5. Quit the browser
browser.quit()

