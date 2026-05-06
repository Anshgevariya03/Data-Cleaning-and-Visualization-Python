# 🎓 30 Viva Questions & Answers
**Topic: Data Cleaning and Visualization using Python**

---

### Pandas & NumPy Basics
**Q1. What is Pandas and why is it used in data analysis?**  
**A:** Pandas is an open-source Python library used for data manipulation and analysis. It provides two main data structures: Series (1D) and DataFrame (2D), allowing easy handling of tabular data.

**Q2. What is the difference between a list and a NumPy array?**  
**A:** NumPy arrays are homogenous, meaning they store elements of the same data type, which makes them faster and more memory-efficient than Python lists. They also support vectorized operations.

**Q3. How do you view the top and bottom rows of a DataFrame?**  
**A:** Using the `head()` method for the top rows (default 5) and `tail()` method for the bottom rows.

**Q4. What does the `df.info()` function do?**  
**A:** It prints a concise summary of the DataFrame, including the number of non-null values, columns, data types, and memory usage.

**Q5. How do you check the shape of a DataFrame?**  
**A:** Using `df.shape`, which returns a tuple representing (number of rows, number of columns).

---

### Data Cleaning
**Q6. What are the common steps in Data Cleaning?**  
**A:** Handling missing values, removing duplicates, fixing wrong data types, handling outliers, and standardizing text/string formatting.

**Q7. How do you check for missing values in Pandas?**  
**A:** By using `df.isnull().sum()`. It returns the count of missing values in each column.

**Q8. What are the ways to handle missing data?**  
**A:** We can either drop them using `dropna()` if they are insignificant, or impute them using `fillna()` with the mean, median, or mode.

**Q9. When would you use Median over Mean for imputation?**  
**A:** We use the median when the feature has a skewed distribution or contains outliers, because the mean is heavily affected by outliers, whereas the median is robust.

**Q10. How do you find and drop duplicate rows?**  
**A:** Find them using `df.duplicated()` and remove them using `df.drop_duplicates(inplace=True)`.

**Q11. Why do we set `inplace=True` in pandas methods?**  
**A:** Because it modifies the DataFrame directly in memory rather than returning a newly modified copy of the DataFrame.

**Q12. How do you change the data type of a column?**  
**A:** Using the `astype()` function or `pd.to_numeric()`, `pd.to_datetime()`.

**Q13. How do you standardize strings in a column?**  
**A:** By using string accessors like `df['col'].str.lower()`, `str.strip()`, or `str.capitalize()`.

**Q14. How do you rename columns?**  
**A:** Using the `rename()` function and passing a dictionary: `df.rename(columns={'old_name': 'new_name'})`.

---

### Outlier Detection
**Q15. What is an Outlier?**  
**A:** An outlier is an abnormal observation that lies far away from other values in a dataset. It can skew statistical summaries.

**Q16. Name two methods to detect outliers?**  
**A:** The Z-Score method and the Interquartile Range (IQR) method (Boxplots).

**Q17. Explain the IQR method.**  
**A:** We calculate the 25th percentile (Q1) and the 75th percentile (Q3). IQR is Q3 - Q1. Any value below (Q1 - 1.5 * IQR) or above (Q3 + 1.5 * IQR) is evaluated as an outlier.

**Q18. Instead of dropping outliers, what else can we do?**  
**A:** We can cap/clip them. This means setting the extreme outliers to the maximum or minimum bounds calculated by the IQR formula.

**Q19. Which plot is best used to identify outliers?**  
**A:** The Boxplot. It clearly displays the median, quartiles, and dots representing outliers.

---

### Visualization
**Q20. What is Matplotlib?**  
**A:** Matplotlib is a comprehensive base library in Python used for creating static, animated, and interactive visualizations. 

**Q21. What is Seaborn and how is it different from Matplotlib?**  
**A:** Seaborn is built on top of Matplotlib. It provides a higher-level interface for creating attractive statistical graphics with fewer lines of code and better default themes.

**Q22. What is Univariate Analysis? Give an example.**  
**A:** It is the analysis of a single variable. Examples include plotting a Histogram to see data distribution or a Countplot for category frequencies.

**Q23. What is Bivariate Analysis? Give an example.**  
**A:** It analyzes the relationship between two variables. Examples include Scatter plots (Numerical vs Numerical) or Box plots (Categorical vs Numerical).

**Q24. When should you use a Bar Chart vs a Histogram?**  
**A:** Bar charts are used for mapping categorical data to numerical values, whereas Histograms are used to show the continuous frequency distribution of numerical data.

**Q25. What does a Correlation Heatmap show?**  
**A:** It shows the statistical correlation coefficient (-1 to +1) between all numerical columns in a dataset using color intensities.

**Q26. What does a value of `0.9` in correlation mean?**  
**A:** It indicates a very strong positive correlation; as one variable increases, the other reliably increases proportionally.

**Q27. How do you plot a pairplot and what is its use?**  
**A:** `sns.pairplot(df)`. It visualizes pairwise continuous relationships across an entire dataframe, essentially providing a multi-dimensional scatterplot matrix in a single grid.

---

### Project Specific
**Q28. Why did you choose this Supermarket Sales dataset?**  
**A:** It is a real-world mimic that contains multiple data types (currency, dates, categories) which flawlessly demonstrates a variety of cleaning needs and business storytelling applications.

**Q29. What was the most significant insight you found during your EDA?**  
**A:** The symmetric gender spending and the identical customer-type ratios indicated that pushing loyalty membership programs equally across all target groups is viable and necessary.

**Q30. What was the most challenging part of your data cleaning phase?**  
**A:** Properly handling the missing values without losing data mass. Dropping rows might skew analysis, so calculating an accurate median imputation strategy for outliers was crucial.
