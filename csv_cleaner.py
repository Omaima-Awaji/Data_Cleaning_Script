import pandas as pd
import json
import re
import os

with open("config.json", "r") as f:
    config = json.load(f)

df = pd.read_csv("messy_customer.csv")

print("Config loaded:", config)
print("\nRaw data:")
print(df)

df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

print("\nCleaned column names")
print(df.columns.tolist())

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

print("\nAfter stripping whitespace:")
print(df)

df["city"] = df["city"].str.title()

print("\nAfter fixing cities:")
print(df["city"])

fill_value = config["fill_missing_text"]
df = df.fillna(fill_value)

print("\nAfter filling missing values:")
print(df)

before = len(df)

if config["drop_duplicates"]:
    df = df.drop_duplicates()

after = len(df)

print(f"\nRemoved {before - after} duplicates rows")
print(f"Rows remaining: {after}")

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email.lower()))

df["email_valid"] = df["email"].apply(is_valid_email)

print("\nEmail validation:")
print(df[["email", "email_valid"]])

df["email"] = df["email"].str.lower()

print("\nAfter lowercasing emails:")
print(df[["email", "email_valid"]])

def clean_phone_number(phone):
    digits = re.sub(r"\D", "", phone)
    digits = digits.lstrip("1")
    if len(digits) == 10:
        return f"+1{digits}"
    return "invalid"

df["phone"] = df["phone"].apply(clean_phone_number)

print("\nAfter cleaning phones: ")
print(df[["phone"]])


def parse_date(datee_str):
    formats = ["%Y/%m/%d", "%d-%m-%Y", "%B %d %Y", "%Y-%m-%d"]
    for fmt in formats:
        try:
            return pd.to_datetime(datee_str, format=fmt).strftime(config["date_format"])
        except:
            continue
    return "invalid"

df["birth_date"] = df["birth_date"].apply(parse_date)


print("\nAfter cleaning dates:")
print(df[["birth_date"]])

report = {
    "total_rows_original": before,
    "total_rows cleaned": after,
    "duplicates_removed": before - after,
    "invalid_emails": int(df["email_valid"].value_counts().get(False, 0)),
    "invalid_phones": int((df["phone"] == "invalid").sum()),
    "invalid_dates": int((df["birth_date"] == "invalid").sum()),

}

print("\nCleaning Report:")
for key, value in report.items():
    print(f" {key}: {value}")

df.to_csv("cleaned_customers.csv", index=False)

with open("cleaning_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nFiles saved:")
print(" - cleaned_customer.csv")
print(" - cleaning_report.json")



















