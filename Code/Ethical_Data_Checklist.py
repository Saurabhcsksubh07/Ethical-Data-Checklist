#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Project: Ethical Data Use Checklist
# Author: [Saurabh Rai]
# Date: 19-Aug-2025
# Description: A command-line tool to self-assess the ethical compliance
#              of a data analytics project, based on a predefined checklist.

# --- Program Configuration ---
ETHICS_CHECKS = [
    "1. Did you anonymize or de-identify personal data where possible?",
    "2. Did you obtain explicit and informed consent for data collection and use?",
    "3. Is your data collection limited to only what is necessary for the project's purpose?",
    "4. Have you checked your dataset for potential biases (e.g., gender, racial)?",
    "5. Is the data stored securely with access controls in place?",
    "6. Do you have a clear policy for data retention and deletion?",
    "7. Are the results of your analysis communicated in a fair and not misleading way?",
    "8. Is there a clear way for individuals to request access to or deletion of their data?",
    "9. Was the model's fairness and potential for discriminatory outcomes evaluated?",
    "10. Is the purpose of the data analysis clearly beneficial and not harmful?"
]
ACCEPTABLE_YES = {'yes', 'y'}
ACCEPTABLE_NO = {'no', 'n'}

# --- Core Functions ---
def start_checklist():
    """
    Runs the main interactive checklist for the user.
    Returns a list of answers (True for yes, False for no).
    """
    print("--- Data Analytics Ethics Self-Assessment ---")
    print("Answer the following with 'Yes' or 'No'.\n")
    
    user_choices = []
    
    for check in ETHICS_CHECKS:
        while True:
            reply = input(f"{check}\n> ").lower().strip()
            
            if reply in ACCEPTABLE_YES or reply in ACCEPTABLE_NO:
                user_choices.append(reply in ACCEPTABLE_YES)
                print()
                break
            else:
                print("--> Please use 'Yes' or 'No'.")
                
    return user_choices

def create_final_report(choices):
    """
    Analyzes the user's choices and prints the formatted summary.
    """
    compliance_score = 0
    points_to_address = []
    
    for i, choice_was_yes in enumerate(choices):
        if choice_was_yes:
            compliance_score += 1
        else:
            failed_check_text = ETHICS_CHECKS[i]
            points_to_address.append(failed_check_text)
            
    print("------------------------------------------")
    print("             Assessment Report            ")
    print("------------------------------------------")
    
    total_checks = len(ETHICS_CHECKS)
    print(f"Ethics score: {compliance_score}/{total_checks}")
    
    if compliance_score == total_checks:
        print("Message: Compliant")
    else:
        print("Message: Needs Attention")
        print("\nList of unchecked items:")
        for point in points_to_address:
            print(f"- {point}")
            
    print("------------------------------------------")


# --- Program Execution ---
def main():
    all_answers = start_checklist()
    create_final_report(all_answers)


if __name__ == "__main__":
    main()


# In[1]:


# --- Program Configuration ---
ETHICS_CHECKS = [
    "1. Did you anonymize or de-identify personal data where possible?",
    "2. Did you obtain explicit and informed consent for data collection and use?",
    "3. Is your data collection limited to only what is necessary for the project's purpose?",
    "4. Have you checked your dataset for potential biases (e.g., gender, racial)?",
    "5. Is the data stored securely with access controls in place?",
    "6. Do you have a clear policy for data retention and deletion?",
    "7. Are the results of your analysis communicated in a fair and not misleading way?",
    "8. Is there a clear way for individuals to request access to or deletion of their data?",
    "9. Was the model's fairness and potential for discriminatory outcomes evaluated?",
    "10. Is the purpose of the data analysis clearly beneficial and not harmful?"
]
ACCEPTABLE_YES = {'yes', 'y'}
ACCEPTABLE_NO = {'no', 'n'}

# --- Core Functions ---
def start_checklist():
    """
    Runs the main interactive checklist for the user.
    Returns a list of answers (True for yes, False for no).
    """
    print("--- Data Analytics Ethics Self-Assessment ---")
    print("Answer the following with 'Yes' or 'No'.\n")
    
    user_choices = []
    
    for check in ETHICS_CHECKS:
        while True:
            reply = input(f"{check}\n> ").lower().strip()
            
            if reply in ACCEPTABLE_YES or reply in ACCEPTABLE_NO:
                user_choices.append(reply in ACCEPTABLE_YES)
                print()
                break
            else:
                print("--> Please use 'Yes' or 'No'.")
                
    return user_choices

def create_final_report(choices):
    """
    Analyzes the user's choices and prints the formatted summary.
    """
    compliance_score = 0
    points_to_address = []
    
    for i, choice_was_yes in enumerate(choices):
        if choice_was_yes:
            compliance_score += 1
        else:
            failed_check_text = ETHICS_CHECKS[i]
            points_to_address.append(failed_check_text)
            
    print("------------------------------------------")
    print("             Assessment Report            ")
    print("------------------------------------------")
    
    total_checks = len(ETHICS_CHECKS)
    print(f"Ethics score: {compliance_score}/{total_checks}")
    
    if compliance_score == total_checks:
        print("Message: Compliant")
    else:
        print("Message: Needs Attention")
        print("\nList of unchecked items:")
        for point in points_to_address:
            print(f"- {point}")
            
    print("------------------------------------------")


# --- Program Execution ---
def main():
    all_answers = start_checklist()
    create_final_report(all_answers)


if __name__ == "__main__":
    main()


# In[3]:


get_ipython().system(' jupyter nbconvert --to scr')


# In[ ]:




