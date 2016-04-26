import credentials
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import sys
# sys.argv = ["python", "/home/raquel/Downloads/hyphagooglesheets-1f05924cc945.json"]


def get_worklog():
    gs = credentials.authorise()
    worklog = gs.open("Work Log")
    return worklog.sheet1


def get_registry():
    gs = credentials.authorise()
    job_registry = gs.open("Job Registry")
    return job_registry.sheet1


def first_empty_row(worklog):
    search = re.compile('$^')
    empty_cells = worklog.findall(search)
    return empty_cells[0].row


def update_cell(start=None, week=None, duration=None, jobid=None, job_class=None,
                description=None, prep_time="", billed_time=""):
    worklog = get_worklog()
    empty_cell = first_empty_row(worklog)
    # keys = [x for x in worklog.row_values(1) if x != ""]
    vals = [start, week, duration, jobid, job_class, description, prep_time, billed_time]

    for idx, val in enumerate(worklog.row_values(empty_cell)):
        if worklog.cell(1, idx + 1) != "":
            worklog.update_cell(empty_cell, idx + 1, vals[idx])
    return get_worklog()

worksheet = pd.DataFrame(get_worklog().get_all_records())
worksheet = worksheet.replace("", np.nan, regex=True).dropna(thresh=1)
coded_jobs = worksheet[worksheet["Job class"] == "Coded Jobs"]

worksheet_byWeek = worksheet.sort(["Week", "Duration", "Job class"],
                                  ascending=[True, False, True])[["Week", "Duration", "Job ID"]]


latest_week = max(worksheet.Week)
week_cj = coded_jobs[coded_jobs["Week"] == latest_week]
week_work = worksheet[worksheet["Week"] == latest_week]
week_work_byID = week_work.sort(["Duration", "Job class"], ascending=[False, False])[["Duration", "Job ID"]]
coded_jobs_byID = coded_jobs.sort(["Week", "Duration", "Job class"],
                                  ascending=[True, False, True])[["Week", "Duration", "Job ID"]]

coded_jobs_byDuration = coded_jobs_byID.ix[:, coded_jobs_byID.columns != "Week"].groupby(by="Job ID").sum()




registrysheet = pd.DataFrame(get_registry().get_all_records())
registrysheet = registrysheet.replace("", np.nan, regex=True).dropna(thresh=2)

registrysheet["Duration"] = registrysheet["number"].map(coded_jobs_byDuration["Duration"])
duration_by_customer = registrysheet.groupby(['customer'])['Duration'].sum()
# duration_by_customer = registrysheet.groupby(['customer'])['Duration'].sum().reset_index(0)

myplot = duration_by_customer.plot(kind="bar")
myplot.set_xlabel("Customers")
myplot.set_ylabel("Hours")
plt.show()

duration_by_customerWeek = registrysheet.groupby(["customer", "Week"])["Duration"].sum()
my_plot = duration_by_customerWeek.unstack().plot(kind='bar', stacked=True, title="Total Hours/Week by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Hours")
plt.show()


