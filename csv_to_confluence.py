
from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
from jira import JIRA

# Open the assessment_output.csv file in read mode
with open('C:\\Users\\PowerBI\\OneDrive - VMware, Inc\\Desktop\\Confluence\\assessment_output.csv', "r") as file1:
    # Create a csv reader object
    reader = csv.reader(file1)
    # Skip the header row
    next(reader)
    # Read the first data row
    row = next(reader)
    # Save the value of the pipeline column as pipeline variable
    assessment_pipeline_count=row[0]
    assessment_in_progress_count=row[1]
    # Print the pipeline variable

# Open the assessment_output.csv file in read mode
with open('C:\\Users\\PowerBI\\OneDrive - VMware, Inc\\Desktop\\Confluence\\migration_output.csv', "r") as file2:
    # Create a csv reader object
    reader = csv.reader(file2)
    # Skip the header row
    next(reader)
    # Read the first data row
    row = next(reader)
    # Save the value of the pipeline column as pipeline variable
    migration_pipeline_count=row[0]
    migration_in_progress_count=row[1]
    # Print the pipeline variable


# Create a Assessment Confluence page with your credentials and URL and with table excerpt
assessment_confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
assessment_page_id = "126594086"

# Define the ID of the existing confluence page
# Define the content of the table excerpt
assessment_table_content = f"""
<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1">
  <ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
  <ac:parameter ac:name="name">assessment_last_week_result</ac:parameter>
  <ac:rich-text-body>
    <table>
      <tbody>
        <tr>
          <th>Week</th>
          <th>Pipeline</th>
          <th>In Progress</th>
        </tr>
        <tr>
          <td style="text-align: center;">Last Week</td>
          <td style="text-align: center;">{assessment_pipeline_count}</td>
          <td style="text-align: center;">{assessment_in_progress_count}</td>
        </tr>
      </tbody>
    </table>
  </ac:rich-text-body>
</ac:structured-macro>
"""

# Create a Migration Confluence page with your credentials and URL and with table excerpt
migration_confluence = Confluence(url="https://confluence.pscoe.vmware.com", username="saldardery", password='@hly_91!Ahly_91!')
migration_page_id = "126594084"

# Define the ID of the existing confluence page
# Define the content of the table excerpt
migration_table_content = f"""
<ac:structured-macro ac:name="table-excerpt" ac:schema-version="1">
  <ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
  <ac:parameter ac:name="name">migration_last_week_result</ac:parameter>
  <ac:rich-text-body>
    <table>
      <tbody>
        <tr>
          <th>Week</th>
          <th>Pipeline</th>
          <th>In Progress</th>
        </tr>
        <tr>
          <td style="text-align: center;">Last Week</td>
          <td style="text-align: center;">{migration_pipeline_count}</td>
          <td style="text-align: center;">{migration_in_progress_count}</td>
        </tr>
      </tbody>
    </table>
  </ac:rich-text-body>
</ac:structured-macro>
"""

# Get the current version of the page
assessment_response = assessment_confluence.get_page_by_id(assessment_page_id,"body.storage")
migration_response = migration_confluence.get_page_by_id(migration_page_id,"body.storage")
#print(response)
#page_version = response["version"]["number"]

# Update the page with the table excerpt appended at the end of the body
assessment_response = assessment_confluence.update_page(
    page_id=assessment_page_id,
    title=assessment_response["title"],
    body=assessment_table_content,
    #version=page_version + 1,
)
migration_response = migration_confluence.update_page(
    page_id=migration_page_id,
    title=migration_response["title"],
    body=migration_table_content,
    #version=page_version + 1,
)
