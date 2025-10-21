					                                               LIBRARY USER CLASSIFICATION - PROJECT REPORT


1.	ABSTARCT:

	In academic settings, libraries serve as both study spaces and resource hubs. However, most usage analytics focus only on book borrowing.
This project provides a comprehensive view of student engagement by analyzing both borrowing records and in-library study logs.
By combining these data sources, students are categorized as Frequent, Moderate, Rare, or Inactive users — enabling libraries to make data-driven decisions and improve engagement.


2. OBJECTIVES :

Main Goals:

⦁ Data Collection and Processing
   * Read and analyze book borrowing and in-library study logs from CSV files.
   * Clean and preprocess data for consistency and accuracy.

⦁ User Behavior Analysis
   * Calculate number of books borrowed per student.
   * Compute total study hours in the library.
   * Determine unique study days for each student.

⦁ User Categorization
   * Frequent Users: High borrowing frequency or long study duration
   * Moderate Users: Medium activity
   * Rare Users: Low engagement
   * Inactive Users: No borrowing or study record

⦁ Visualization and Insights (Future Scope)
   * Display top active users by borrow count, study hours, and days.
   * Highlight inactive or single-activity users.

⦁ Actionable Insights
   * Help library admins identify highly engaged students.
   * Improve book circulation and space utilization.
   * Plan recognition programs or incentives.


3. TOOLS AND TECHNOLOGIES:

	    Category                  Tools / Libraries 
⦁	Programming Language   :	  Python
⦁	Libraries Used	        :	  Pandas, datetime, matplotlib/seaborn for visualization
⦁	Datasets	      	      :	  borrow_history.csv, read_log.csv
⦁	Output File	      	    :	  user_activity_report.csv


4. DATASET DESCRIPTION:

⦁	Borrowing History (borrow_history.csv)
	  Contains: Student_ID, Book_ID, Borrow_Date, Return_Date
⦁	Study Log (read_log.csv)
	  Contains: Student_ID, Date, In_Time, Out_Time


5. DATA CLEANING:

To Ensure accuracy:
⦁	Standardized Student_ID values as strings.
⦁	Converted In_Time and Out_Time to datetime format.
⦁	Calculated study durations in hours.
⦁	Removed missing or inconsistent values.


6. PURPOSE OF ANALYSIS:

⦁	Understand student usage patterns across reading and borrowing.
⦁	Identify top engaged and inactive users.
⦁	Support resource planning and book circulation improvements.
⦁	Recognize and reward consistently active students.

 
7. METHODOLGY:

⦁	Data Input:
	Loaded data from borrow_history.csv and read_log.csv using pandas.
⦁	Data Processing:
	Cleaned, formatted, and aggregated both datasets.
⦁	Feature Creation:
   	* Borrow_Count
   	* Total_Study_Hours
   	* Study_Days
⦁	Classification Logic:
	Based on thresholds of borrowing and study hours, users are labeled as:
	* Frequent
   	* Moderate
   	* Rare
   	* Inactive
⦁	Output:
	   Final results saved in user_activity_report.csv.


8. OVERALL PERFORMANCE:

	This project successfully integrates both borrowing and study activity to measure student engagement more accurately.
By identifying user patterns, libraries can:

⦁	Recognize and reward top users
⦁	Motivate casual and inactive readers
⦁	Plan better resource allocation and service improvements

This analysis forms a foundation for advanced analytics such as trend tracking, predictive modeling, and personalized reading recommendations.







