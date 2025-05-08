import pandas as pd
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm
import seaborn as sns


def analyze_pk_data(csv_file):
  # we read the data using pandas
  pk_data= pd.read_csv(csv_file)

  # we calculate important PK values
  # cmax that is maximum concentration
  cmax = pk_data['Conc'].max()
  tmax = pk_data['Time'].max()

  cmax_row = pk_data[pk_data['Conc'] == cmax].index.values[0] + 2
  tmax_row = pk_data[pk_data['Time'] == tmax].index.values[0] + 2

  # Assignment print all the lines with tmax == 24
  print(cmax_row)
  print(tmax_row)

  #  print the cmax and tmax line from csv
  print(f"Cmax: {cmax} ug/mL on line {cmax_row}  and tmax: {tmax} hr(s) on line {tmax_row}")

  # # Plot 1: Time vs Concentration with regression line
  # plt.figure(figsize=(10, 5))
  # plt.plot(pk_data['Time'], pk_data['Conc'], marker='o', linestyle='-')
  # plt.title('Concentration-Time Profile Mentorship')
  # plt.xlabel('Time (hr)')
  # plt.ylabel('Concentration (ug/mL)')
  # plt.grid(True)
  # plt.show()

  # Assignment 1: Get all row line number in the CSV where Cmax and tmax occurs
  # cmax_rows = pk_data[pk_data['Conc'] == cmax]
  # print("rows with Cmax:")
  # print(cmax_rows)
  # tmax_rows = pk_data[pk_data['Time'] ==tmax]
  # print('Rows with tmax are: ')
  # print(tmax_rows)

  # Assigment 1: Get 1-based row numbers with Cmax
  # cmax_row_lines = (pk_data[pk_data['Conc'] == cmax].index + 2).tolist()
  #
  # #Get 1- based row numbers with Tmax
  # tmax_row_lines = (pk_data[pk_data["Time"] == tmax]. index + 2).tolist()

  #Cmax/tmax with Cmax(x) is found in : rows (a, b, x, y) shows other columns
  # print(f"Rows with Cmax ({cmax}) is found in: {', '.join(map(str, cmax_row_lines))}")
  # print(f"Rows with Tmax ({tmax}) is found in : {', '.join(map(str, tmax_row_lines))}")

  # Cmax/tmax value (x) is found in (x) row(s): a, b,x, y
  # print(f"Cmax value ({cmax}) is found in {len(cmax_row_lines)} row(s): {', '.join(map(str, cmax_row_lines))}")
  # print(f"Tmax value ({tmax}) is found in {len(tmax_row_lines)} row(s): {', '.join(map(str, tmax_row_lines))}")

 # Assignment 2, Plot 2: Weight vs Concentration with regression line
 #  plt.figure(figsize=(10, 5))
 #  plt.plot(pk_data['WGTkg'], pk_data['Conc'], marker='o', linestyle='-')
 #  plt.title('Weight-Concentration Profile Mentorship')
 #  plt.xlabel('Weight (kg)')
 #  plt.ylabel('Concentration (ug/mL)')
 #  plt.grid(True)
 #  plt.show()

  # Assignment 3:Calculates Pearson correlation btw wt & conc
  # runs a linear regression using statsmodel.ols
  # prints a full regression summaryincluding R2,coefficints and p-values
  # scatter plot to visualize correlation
  # Check that both columns exist and drop missing values
  if 'WGTkg' in pk_data.columns and 'Conc' in pk_data.columns:
    clean_data = pk_data[['WGTkg', 'Conc']].dropna()

    # Add constant for regression intercept
    X = sm.add_constant(clean_data['WGTkg'])
    y = clean_data['Conc']

    # Fit linear model
    model = sm.OLS(y, X).fit()

  #   # Print correlation and summary
    correlation = clean_data['WGTkg'].corr(clean_data['Conc'])
    print(f"Correlation between Weight and Concentration: {correlation:.3f}")
    print(model.summary())
  else:
    print("Columns 'WGTkg' and/or 'Conc' not found in the CSV.")

 # Scatter plot with regression line
    plt.figure(figsize=(8, 6))
    sns.regplot(x='WGTkg', y='Conc', data=clean_data, ci=95, line_kws={'color': 'red'})
    plt.title('Correlation between Weight and Concentration')
    plt.xlabel('Weight (kg)')
    plt.ylabel('Concentration (ug/mL)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
  # else:
  #   print("Columns 'Weight' and/or 'Conc' not found in the CSV.")

  print(clean_data.shape)
  print(clean_data.head())

if __name__ == "__main__":
  file_directory = os.path.dirname(os.path.abspath(__file__))
  print(file_directory)
  csv_file = file_directory + "/pk_data.csv"
  analyze_pk_data(csv_file)
