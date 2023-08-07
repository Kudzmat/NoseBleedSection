from bs4 import BeautifulSoup
import requests


def get_ringer_links():
    url = 'https://www.theringer.com/nba'

    the_ringer_news = {}

    # Get url result
    result = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(result.content, "html.parser")

    # Find the <main> element on the page
    main_element = soup.find("main")

    # Create new variable headlines which finds the h2 elements on the page
    headlines = main_element.find_all('h2')

    for num, topic in enumerate(headlines):
        # Check if an <a> tag exists within the <h2> tag
        if topic.find('a'):
            # Retrieve the href link using the 'a' tag within the 'h2' tag
            link = topic.find('a')['href']

            # Retrieve the text content of the 'h2' tag
            text = topic.get_text()

            # Begin writing to file
            the_ringer_news[num + 1] = [text, link]
        #  'TypeError: 'NoneType' object is not subscriptable' error will pop up if no href link is found so we need to handle error
        else:
            the_ringer_news[num + 1] = [text, "https://www.theringer.com/nba"]

    return the_ringer_news
