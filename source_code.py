import pandas as pd

# Step 1: Load data
df_borrow = pd.read_csv("borrow_history.csv")
df_read = pd.read_csv("read_log.csv")

# Step 2: Ensure Student_IDs are strings
df_borrow['Student_ID'] = df_borrow['Student_ID'].astype(str)
df_read['Student_ID'] = df_read['Student_ID'].astype(str)

# Step 3: Calculate borrow count
borrow_counts = df_borrow['Student_ID'].value_counts().reset_index()
borrow_counts.columns = ['Student_ID', 'Borrow_Count']

# Step 4: Convert In/Out time to datetime
df_read['In_Time_DT'] = pd.to_datetime(df_read['In_Time'], format='%H:%M:%S', errors='coerce')
df_read['Out_Time_DT'] = pd.to_datetime(df_read['Out_Time'], format='%H:%M:%S', errors='coerce')

# Step 5: Calculate study duration
df_read['Study_Duration'] = df_read['Out_Time_DT'] - df_read['In_Time_DT']

# Step 6: Aggregate study time and unique study days
read_summary = df_read.groupby('Student_ID').agg({
    'Study_Duration': 'sum',
    'Date': pd.Series.nunique
}).reset_index()
read_summary.columns = ['Student_ID', 'Total_Study_Time', 'Study_Days']

# Step 7: Merge borrow and study data
user_activity = pd.merge(borrow_counts, read_summary, on='Student_ID', how='outer')

# Step 8: Fill missing values for users with only borrow or only study data
user_activity['Borrow_Count'] = user_activity['Borrow_Count'].fillna(0).astype(int)
user_activity['Total_Study_Time'] = user_activity['Total_Study_Time'].fillna(pd.Timedelta(0))
user_activity['Study_Days'] = user_activity['Study_Days'].fillna(0).astype(int)

# Step 9: Convert study time to total study hours
user_activity['Total_Study_Hours'] = user_activity['Total_Study_Time'].dt.total_seconds() / 3600
# Step 9.5: Classify users based on borrow count and study hours
def classify_user(row):
    if row['Borrow_Count'] == 0 and row['Total_Study_Hours'] == 0:
        return 'Inactive'
    elif row['Borrow_Count'] >= 20 or row['Total_Study_Hours'] >= 80:
        return 'Frequent'
    elif row['Borrow_Count'] >= 10 or row['Total_Study_Hours'] >= 30:
        return 'Moderate'
    else:
        return 'Rare'

user_activity['User_Type'] = user_activity.apply(classify_user, axis=1)


# Step 10: Sort by borrow and study time
user_activity_sorted = user_activity.sort_values(by=['Borrow_Count', 'Total_Study_Hours'], ascending=False)


# Step 12 (optional): Also show who never borrowed or studied
inactive_users = user_activity[(user_activity['Borrow_Count'] == 0) & (user_activity['Study_Days'] == 0)]

# Step 13: Save full user activity to a CSV file
user_activity_sorted.to_csv("user_activity_report.csv", index=False)

