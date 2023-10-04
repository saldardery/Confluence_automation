from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
from jira import JIRA

# Open the assessment_output.csv file in read mode
with open("C:\\Users\\Administrator.NEXUS\\Desktop\\Confluence\\assessment_output.csv", "r") as file:
    # Create a csv reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Read the first data row
    row = next(reader)
    # Save the value of the pipeline column as pipeline variable
    assessment_pipeline_count=row[0]
    assessment_in_progress_count=row[1]
    # Print the pipeline variable

# Open the assessment_output.csv file in read mode
with open("C:\\Users\\Administrator.NEXUS\\Desktop\\Confluence\\migration_output.csv", "r") as file:
    # Create a csv reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Read the first data row
    row = next(reader)
    # Save the value of the pipeline column as pipeline variable
    migration_pipeline_count=row[0]
    migration_in_progress_count=row[1]
    # Print the pipeline variable


# Create a Assessment Confluence page with your credentials and URL and with table excerpt
confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
page_id = "126594086"

# Define the ID of the existing confluence page
# Define the content of the table excerpt
table_content = f"""
<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1">
  <ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
  <ac:parameter ac:name="name">assessment_last_week_result</ac:parameter>
  <ac:rich-text-body>
    <table>
      <tbody>
        <tr>
          <th>Pipeline</th>
          <th>In progress</th>
        </tr>
        <tr>
          <td>{assessment_pipeline_count}</td>
          <td>{assessment_in_progress_count}</td>
        </tr>
      </tbody>
    </table>
  </ac:rich-text-body>
</ac:structured-macro>
"""

# Create a Migration Confluence page with your credentials and URL and with table excerpt
confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
page_id = "126594084"

# Define the ID of the existing confluence page
# Define the content of the table excerpt
table_content = f"""
<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1">
  <ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
  <ac:parameter ac:name="name">migration_last_week_result</ac:parameter>
  <ac:rich-text-body>
    <table>
      <tbody>
        <tr>
          <th>Pipeline</th>
          <th>In progress</th>
        </tr>
        <tr>
          <td>{migration_pipeline_count}</td>
          <td>{migration_in_progress_count}</td>
        </tr>
      </tbody>
    </table>
  </ac:rich-text-body>
</ac:structured-macro>
"""

# Get the current version of the page
response = confluence.get_page_by_id(page_id,"body.storage")
#print(response)
#page_version = response["version"]["number"]

# Update the page with the table excerpt appended at the end of the body
response = confluence.update_page(
    page_id=page_id,
    title=response["title"],
    body=table_content,
    #version=page_version + 1,
)

