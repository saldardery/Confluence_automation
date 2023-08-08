from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
from jira import JIRA
jira = JIRA('https://jira.pscoe.vmware.com/', auth=('saldardery', 'Ahly_12345'))

in_progress = jira.search_issues('((project = MCOEA AND issuetype = Project AND status in (Backlog, Execution)) OR (project = "Project Atlantic - Modernization COE " AND "Migration Process" = Accelerated AND "Assessment Status" = In-progress AND status in (BACKLOG, EXECUTION)) )AND (product != "NSX - Standalone Migration") ',maxResults=1000)
pipeline=issues = jira.search_issues ('((project = MCOEA AND issuetype = Project AND status in (Approved, "SOW Prep", "SOW Approval & Signature")) OR (project = "Project Atlantic - Modernization COE " AND "Migration Process" = Accelerated AND ("Assessment Status" != In-progress OR "Assessment Status" != Completed))) AND created >= startOfWeek()',maxResults=1000)
pipeline_count=len(pipeline)
in_progress_count = len(in_progress)



# Create a list of lists containing the headers and the values
data = [["Pipeline", "In Progress"], [pipeline_count, in_progress_count]]

# Open a file in write mode
with open("table1.csv", "w") as file:
    # Create a csv writer object
    writer = csv.writer(file)
    # Write each row of data to the file
    for row in data:
        writer.writerow(row)

# Close the file
file.close()

# Create a Confluence object with your credentials and URL
confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
page_id = "126594086"
page_title= "test_Page"
table = pd.read_csv("table1.csv")
# Convert the table to HTML format
table_html = table.to_html(index=False)

# Get the current page content in storage format
page = confluence.get_page_by_id(page_id, expand="body.storage")
page_content = page["body"]["storage"]["value"]

# Append the table HTML to the page content
page_content = table_html

# Update the page with the new content
confluence.update_page(page_id, page_title, page_content)
