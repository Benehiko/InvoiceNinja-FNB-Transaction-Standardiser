import argparse
import pandas as pd


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, help="Specify the csv file path")
    return parser.parse_args()


def main(args):
    if args.csv is not None:
        colnames = ["Date", "Amount", "Balance", "Description"]
        df = pd.read_csv(args.csv, skiprows=7, sep=',', names=colnames, header=None)
        expenses = {"Date": [], "Amount": [], "Balance": [], "Description": []}
        income = {"Date": [], "Amount": [], "Balance": [], "Description": []}
        for i, row in df.iterrows():
            if row.Amount <= 0:
                df.at[i, 'Amount'] = abs(row.Amount)
                expenses["Date"].append(df.at[i, 'Date'])
                expenses["Amount"].append(df.at[i, 'Amount'])
                expenses["Balance"].append(df.at[i, 'Balance'])
                expenses["Description"].append(df.at[i, 'Description'])
            else:
                income["Date"].append(df.at[i, 'Date'])
                income["Amount"].append(df.at[i, 'Amount'])
                income["Balance"].append(df.at[i, 'Balance'])
                income["Description"].append(df.at[i, 'Description'])

        df_expenses = pd.DataFrame(expenses, columns=colnames)
        df_income = pd.DataFrame(income, columns=colnames)

        df_expenses.to_csv(args.csv.replace('.csv', '') + '_expenses.csv')
        df_income.to_csv(args.csv.replace('.csv', '') + '_income.csv')


if __name__ == "__main__":
    main(args_parser())
