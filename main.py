who = "data engineer"
what = "a data pipeline that can download and extract the NPPES data file"
why = "so I can use it in my data pipeline"

notes = "\n-".join([
    "download url: https://download.cms.gov/nppes/NPPES_Data_Dissemination_April_2023.zip",
    "the file is updated monthly",
    "the download url is mostly static but the month and year change",
])

acceptance_criteria = "\n- ".join([
    "the code downloads the file to my downloads folder (~/Downloads)",
    "the code checks if the file is available to download weekly",
    "if the file is available, the code downloads the file",
])

context = f"""
Description: 

As a {who} I want {what} so {why}.

Notes: 
{notes}

Acceptance Criteria:
{acceptance_criteria}
"""

plan_prompt = f"""
Given the following context, develop a plan to complete the work.

----------------------------------------
CONTEXT:
----------------------------------------
{context}
----------------------------------------
"""

plan = """
1. Create a script to check if the file is available to download each week.
2. Create a script to download the file if available. 
3. Create a script to extract the file contents.
4. Schedule the scripts to run weekly.
5. Test the scripts and debug as necessary.
"""

plan_to_code_prompt = f"""
Given the following plan and context that led to the plan, develop code to complete the work.

----------------------------------------
Context:
----------------------------------------
{context}

----------------------------------------
PLAN:
----------------------------------------
{plan}
"""

if __name__ == "__main__":
    # print(plan_prompt)
    print(plan_to_code_prompt)
