from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
from jira import JIRA

## GET Asssessment VALUES FROM JIRA
jira = JIRA('https://jira.pscoe.vmware.com/', auth=('saldardery', 'Ahly_12345'))
assessment_in_progress = jira.search_issues('((project = MCOEA AND issuetype = Project AND status in (Backlog, Execution)) OR (project = "Project Atlantic - Modernization COE " AND "Migration Process" = Accelerated AND "Assessment Status" = In-progress AND status in (BACKLOG, EXECUTION)) )AND (product != "NSX - Standalone Migration") ',maxResults=1000)
assessment_pipeline=issues = jira.search_issues ('((project = MCOEA AND issuetype = Project AND status in (Approved, "SOW Prep", "SOW Approval & Signature")) OR (project = "Project Atlantic - Modernization COE " AND "Migration Process" = Accelerated AND ("Assessment Status" != In-progress OR "Assessment Status" != Completed))) AND created >= startOfWeek()',maxResults=1000)
assessment_pipeline_count=len(assessment_pipeline)
assessment_in_progress_count = len(assessment_in_progress)



## GET Migration VALUES FROM JIRA
jira = JIRA('https://jira.pscoe.vmware.com/', auth=('saldardery', 'Ahly_12345'))
migration_in_progress = jira.search_issues('project = MCOE AND Product in ("NSX - Standalone Migration",VCF) AND issuetype = Project AND status in (Execution) AND "Migration Detailed Status" in ("Live Migration", "Migration prep work") OR ( project = MCOE AND Product in (vRA) AND issuetype = Project AND status in (Execution))',maxResults=1000)
migration_pipeline=issues = jira.search_issues ('project = MCOE AND issuetype = Project AND Product in (vRA,VCF, "NSX - Standalone migration") AND status in (Approved, Backlog, "SOW Prep", "SOW Approval & Signature")',maxResults=1000)
migration_pipeline_count=len(migration_pipeline)
migration_in_progress_count = len(migration_in_progress)

# Create a Assessment csv file with the table columns pipeline and in progress
with open('C:\\Users\\PowerBI\\OneDrive - VMware, Inc\\Desktop\\Confluence\\assessment_output.csv', "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["pipeline", "in progress"])
    writer.writerow([assessment_pipeline_count, assessment_in_progress_count])

# Create a csv file with the table columns pipeline and in progress
with open('C:\\Users\\PowerBI\\OneDrive - VMware, Inc\\Desktop\\Confluence\\migration_output.csv', "w", newline="") as csvfile2:
    writer = csv.writer(csvfile2)
    writer.writerow(["pipeline", "in progress"])
    writer.writerow([migration_pipeline_count, migration_in_progress_count])
