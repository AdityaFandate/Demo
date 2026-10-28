import pandas as pd
# pyrefly: ignore[missing-import]
from scipy.stats import ttest_ind, chi2_contingency, f_oneway

# Creating the dataset
data = {
    "Gender": [
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male","Female","Male","Female","Male","Female"
    ],

    "Study_Method": [
        "Self-study","Self-study","Self-study","Self-study","Self-study",
        "Self-study","Self-study","Self-study","Self-study","Self-study",
        "Group Study","Group Study","Group Study","Group Study","Group Study",
        "Group Study","Group Study","Group Study","Group Study","Group Study",
        "Online Course","Online Course","Online Course","Online Course","Online Course",
        "Online Course","Online Course","Online Course","Online Course","Online Course"
    ],

    "Online_Class": [
        "Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes",
        "Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes",
        "Yes","Yes","Yes","Yes","No","Yes","Yes","Yes","No","Yes"
    ],

    "Marks": [
        78,82,65,85,70,80,68,88,72,84,
        76,79,73,81,69,77,71,83,75,80,
        90,92,88,95,85,91,89,94,87,93
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
online = df[df["Online_Class"] == "Yes"]["Marks"]
offline = df[df["Online_Class"] == "No"]["Marks"]

t_stat, t_pvalue = ttest_ind(online, offline)

print("\n--- Independent T-Test ---")
print("Online class mean:", online.mean())
print("No online class mean:", offline.mean())
print("t-statistic:", t_stat)
print("p-value:", t_pvalue)

if t_pvalue < 0.05:
    print("Reject H0: There is a significant difference in marks.")
else:
    print("Fail to reject H0: There is no significant difference in marks.")

contingency_table = pd.crosstab(df["Gender"], df["Online_Class"])

chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\n--- Chi-Square Test ---")
print("Contingency Table:")
print(contingency_table)

print("Chi-square statistic:", chi2)
print("p-value:", p)

if p < 0.05:
    print("Reject H0: Gender and online class participation are associated.")
else:
    print("Fail to reject H0: Gender and online class participation are independent.")

self_study = df[df["Study_Method"] == "Self-study"]["Marks"]
group_study = df[df["Study_Method"] == "Group Study"]["Marks"]
online_course = df[df["Study_Method"] == "Online Course"]["Marks"]

f_stat, anova_pvalue = f_oneway(
    self_study,
    group_study,
    online_course
)

print("\n--- One-Way ANOVA ---")
print("Self-study mean:", self_study.mean())
print("Group Study mean:", group_study.mean())
print("Online Course mean:", online_course.mean())

print("F-statistic:", f_stat)
print("p-value:", anova_pvalue)

if anova_pvalue < 0.05:
    print("Reject H0: At least one study method has a significantly different mean.")
else:
    print("Fail to reject H0: No significant difference among study methods.")