who = "developer"
what = "to write code"
why = "I can build a product"

notes = "\n-".join([
    "I need to learn how to write code",
    "I need to learn how to run code"
])

acceptance_criteria = "\n- ".join([
    "I can run code",
    "I can test code",
    "I can deploy code",
])

context = f"""
Description: 

As a {who} I want {what} so that {why}.

Notes: 
{notes}

Acceptance Criteria:
{acceptance_criteria}
"""

plan_prompt = f"""
Given the following context, develop a plan to complete the work:

----------------------------------------
CONTEXT:
----------------------------------------
{context}
----------------------------------------
"""
