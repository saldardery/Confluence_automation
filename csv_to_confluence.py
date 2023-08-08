from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import requests
# Create a Confluence object with your credentials and URL
confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
page_id = "126594086"
page_title= "test_Page"
table = pd.read_csv("table.csv")
# Convert the table to HTML format
table_html = table.to_html(index=False)

# Get the current page content in storage format
page = confluence.get_page_by_id(page_id, expand="body.storage")
page_content = page["body"]["storage"]["value"]

# Append the table HTML to the page content
page_content += table_html

# Update the page with the new content
confluence.update_page(page_id, page_title, page_content)