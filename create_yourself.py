who = "founder"
what = "to design a system that I can use to design systems"
why = "I can use it to develop my ideas including the system itself"

notes = "\n-".join([
    ""
])

acceptance_criteria = "\n- ".join([
    "",
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
    print(plan_prompt)
    # print(plan_to_code_prompt)
