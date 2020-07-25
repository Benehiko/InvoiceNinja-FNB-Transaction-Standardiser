import argparse
import json

import pandas as pd


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, help="Specify the csv file path")
    return parser.parse_args()


def search_categories(search):
    with open('categories.json', 'r') as f:
        categories = json.load(f)

    for key, value in categories.items():
        for x in value:
            if x.lower() in search.lower():
                return key
    return "General"


def main(args):
    if args.csv is not None:
        colnames = ["Date", "Amount", "Balance", "Description", "Category"]
        df = pd.read_csv(args.csv, skiprows=7, sep=',', names=colnames, header=None)
        df["Category"] = df["Category"].astype(str)

        expenses = {"Date": [], "Amount": [], "Balance": [], "Description": [], "Category": []}
        income = {"Date": [], "Amount": [], "Balance": [], "Description": [], "Category": []}
        savings = {"Date": [], "Amount": []}

        for i, row in df.iterrows():
            df.at[i, 'Category'] = search_categories(df.at[i, 'Description'])
            if df.at[i, 'Category'].lower() != 'Savings'.lower():
                if row.Amount <= 0:
                    df.at[i, 'Amount'] = abs(row.Amount)
                    expenses["Date"].append(df.at[i, 'Date'])
                    expenses["Amount"].append(df.at[i, 'Amount'])
                    expenses["Balance"].append(df.at[i, 'Balance'])
                    expenses["Description"].append(df.at[i, 'Description'])
                    expenses["Category"].append(df.at[i, 'Category'])
                else:
                    income["Date"].append(df.at[i, 'Date'])
                    income["Amount"].append(df.at[i, 'Amount'])
                    income["Balance"].append(df.at[i, 'Balance'])
                    income["Description"].append(df.at[i, 'Description'])
                    income["Category"].append(df.at[i, 'Category'])
            else:
                savings["Date"].append(df.at[i, 'Date'])
                savings["Amount"].append(abs(df.at[i, 'Amount']))

        df_expenses = pd.DataFrame(expenses, columns=colnames)
        df_income = pd.DataFrame(income, columns=colnames)
        df_savings = pd.DataFrame(savings, columns=colnames)

        df_expenses.to_csv(args.csv.replace('.csv', '') + '_expenses.csv')
        df_income.to_csv(args.csv.replace('.csv', '') + '_income.csv')
        df_savings.to_csv(args.csv.replace('.csv', '') + '_savings.csv')


if __name__ == "__main__":
    main(args_parser())
