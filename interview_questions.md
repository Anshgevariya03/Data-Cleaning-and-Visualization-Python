# 👔 20 Interview Questions & Answers
**Role: Junior Data Analyst / Data Science Intern**

---

**1. Can you walk me through your Data Cleaning and Visualization project?**
> **Answer:** I developed an end-to-end data analysis pipeline in Python using Pandas, NumPy, and Seaborn. I started with a raw supermarket POS dataset that contained missing values, random duplicate rows, and extreme revenue outliers. I cleaned the data via median imputation and IQR capping, formatted inconsistent strings, and extracted over a dozen business insights through exploratory visual analysis, ultimately proving that standardizing loyalty programs and targeting high-revenue product lines could increase average cart profit margins.

**2. How did you handle the missing data in your project, and how do you usually decide which strategy to use?**
> **Answer:** I identified missing numeric constraints like 'Ratings' and categorical columns like 'Gender'. For categoricals, I imputed using the `mode()` (the most frequent value). For numerical columns, I avoided using the `mean()` because the dataset contained massive outlier spikes in Total Spending; instead, I used the robust `median()` so the imputation wouldn’t be artificially skewed. 

**3. What steps did you take to detect and handle outliers?**
> **Answer:** I used Matplotlib/Seaborn boxplots to visually detect outliers in the 'Total' spending column. I then programmed an algorithm using the Interquartile Range (IQR) boundaries (Q1-1.5*IQR and Q3+1.5*IQR). Instead of dropping out those heavy spenders which are valid business revenue, I capped/clipped them to the upper bound to normalize the distribution for plotting.

**4. Can you describe a specific business insight you derived from your Exploratory Data Analysis?**
> **Answer:** I plotted customer distribution against payment method preferences using Seaborn countplots. I observed a heavily surging shift towards E-Wallets over traditional credit cards. The actionable insight here is that supermarket management needs to ensure their E-Wallet and POS scanners are updated as the primary checkout requirement.

**5. How would you handle a dataset that had 60% of its data missing in a critical continuous column?**
> **Answer:** If 60% is missing, simple imputation like mean/median will destroy the variance and create massive bias. If the column is completely critical, I would look for ways to deduce the missing data using other proxy columns, or try K-Nearest Neighbor (KNN) imputation based on similar rows. If that fails, it might be safer to drop the column entirely from certain analyses to avoid mathematically misleading the stakeholders.

**6. Explain the difference between `loc` and `iloc` in Pandas.**
> **Answer:** `iloc` is strictly integer-position based (i stands for index/integer), meaning you use row and column numbers (e.g., `df.iloc[0:5, 1]`). `loc` is label-based, meaning you use the explicit names of the rows or columns (e.g., `df.loc[0:5, 'Total_Sales']`).

**7. Why is Data Normalization/Standardization important before certain analyses?**
> **Answer:** When variables in a dataset have different scales (e.g., age from 0-100 versus salaries from 0-100,000), algorithms that calculate distance (like KNN or K-Means clustering) will be disproportionately dominated by the larger numbers. Standardizing them scales them to equal footing.

**8. Have you used lambda functions in Pandas? Can you give an example?**
> **Answer:** Yes, lambda functions paired with the `apply()` method are excellent for column transformations. For example, in my project, I fixed negative quantities by applying: `df['Quantity'] = df['Quantity'].apply(lambda x: x if x > 0 else np.nan)`.

**9. How do you merge or join two DataFrames? What's the difference between inner and left joins?**
> **Answer:** We use `pd.merge()`. An 'inner join' returns only the rows that have matching keys in *both* DataFrames. A 'left join' returns *all* rows from the left DataFrame, and only the matching rows from the right DataFrame (filling non-matches with NaNs).

**10. What is a correlation coefficient and how did you use it?**
> **Answer:** It's a statistical measure between -1 and 1 indicating how heavily two numerical features move relative to each other. I plotted a Correlation Heatmap via `sns.heatmap()` to validate the math logic in my dataset—proving that 'Quantity', 'Tax', and 'Total' had a perfect positive correlation mathematically aligning with a POS receipt logic.

**11. What is the difference between a Bar plot and a Count plot in Seaborn?**
> **Answer:** A Countplot `sns.countplot()` automatically calculates the frequency (count) of occurrences of a categorical variable. A Bar plot `sns.barplot()` maps a categorical variable against an aggregated mathematical estimator (usually the mean or sum) of a second numerical variable.

**12. When would you use a Scatter Plot over a Line Chart?**
> **Answer:** Data points that represent entirely independent measurements of two numerical variables (like height vs weight) belong on a Scatter Plot to spot clusters or density. Line charts are used primarily when there is an intrinsic order, usually chronological Time-Series data, where drawing lines between dots indicates flow or transition over time.

**13. In your project notebook, you used `inplace=True`. What does this mean and what are the pros/cons?**
> **Answer:** `inplace=True` executes an operation (like `fillna()` or `drop()`) directly upon the variable stored in memory without needing reassignment (`df = df.drop()`). Pro: It saves memory. Con: It mutates the state permanently, making stepping backwards inside a Jupyter notebook harder without re-running the data-load cell.

**14. What exactly does it mean when data is skewed? Which plot shows this?**
> **Answer:** Skewness means the distribution of data is asymmetric. A right-skewed (positive) distribution has a long tail leaning towards higher values while mass bundles near zero. We visualize this easily using a Histogram or a KDE Density plot.

**15. If a stakeholder asked you to summarize the dataset to them in seconds, which pandas function tells you everything?**
> **Answer:** `df.describe()` for numerical aggregations (mean, standard deviation, quartiles), and `df.info()` to show memory footprint, non-null counts, and exact data types. Additionally, calling `df.nunique()` serves well to summarize nominal categorical counts.

**16. What is the difference between `isnull()` and `isna()`?**
> **Answer:** In Pandas, they behave identically. `isna()` is simply an alias for `isnull()`.

**17. How do you group data to find aggregates?**
> **Answer:** Using the `groupby()` method. For example, to find total revenue per branch, I would run `df.groupby('Branch')['Total'].sum()`.

**18. What is the purpose of `.dt` accessor in pandas?**
> **Answer:** The `.dt` accessor is needed when dealing with datetime objects in a Series. It unlocks properties like extracting the month, day, or year, for instance: `df['Date'].dt.month`.

**19. Describe a scenario where dropping duplicates is a BAD idea.**
> **Answer:** Dropping duplicates is bad if the rows are genuinely valid independent events that just happen to look similar. For example, two customers buying exactly 1 bottle of Coke at exactly 12:00 PM will look identical unless they have a unique transaction/invoice ID.

**20. After your EDA, you made actionable recommendations. What makes a good data analyst besides just writing Python code?**
> **Answer:** A great data analyst goes beyond just creating aesthetically pleasing charts—they perform data storytelling. They synthesize clean data into easily digested KPIs and connect observations explicitly to business outcomes, demonstrating exactly how a bar-chart directly influences the company's financial bottom line.
