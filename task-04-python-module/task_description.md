Task 1 (required). Study the CSV dataset "sneaker_sales_dataset.csv", which I shared in the zip file with the materials for the Python topic:

1. Study the header of the dataset (in unclear cases you can also use the OLTP schema, which you can find in the zip file for the second lesson!).
   Describe the number of columns, the number of rows, and the data types of the columns.
   Use Python scripts for this.

2. Check the quality of the data – if there are missing values, duplicate transactions, or anomalies in numerical data (for example, unexpected shoe sizes).
   Use Python scripts and also box plots (for analyzing numerical data).

3. Choose one entity from the list: cities, stores, customers, sneaker brands, and find:
   - the number of unique objects of this entity,
   - how many times each unique object of this entity appears in the dataset.
     Use Python scripts and bar charts to visualize each result.

4. Choose one of the entities from point 3 and find:
   - the total amount of money connected with each of its objects in the transactions,
   - the TOP 3 objects by the amount of money connected with them,
   - the monthly dynamics for this entity by total monthly amounts of money (there is an example in the lesson materials on how to convert a transaction date into a month!).
     Use Python scripts and also one suitable type of chart (linear, bar, or pie) to visualize each result.

5. Create a report (ipynb/html) based on the results of this research (do not forget to write your short explanations and conclusions for each point!).


Task 2 (optional). Based on the weather database (explained in Valeriy’s part, and located in Dropbox):

1. Choose one geolocation and one year.

2. With an SQL query, calculate for this geolocation two average temperatures for each month of the year – the first average temperature should be calculated from the maximum daily temperature, and the second from the minimum daily temperature.

3. Create charts with these temperatures (linear or bar type), using the Python material we studied.

4. Create a report (ipynb/html) based on the results of this research (do not forget to write your short explanations and conclusions).