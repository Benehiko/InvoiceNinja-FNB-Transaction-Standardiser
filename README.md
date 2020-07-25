# InvoiceNinja-FNB-Transaction-Standardiser

### Purpose

Standardise FNB transactions into `income`, `expenses` and `savings`.
`InvoiceNinja` can then import the expenses from the standardised expenses
file.

### Usage

Write all your categories (usually they stay the same throughout a couple of months) in
the `categories.json` file. Some examples have been added there, but can be changed.

``python3 convert.py --csv <path_to_transaction_history>``

This will produce the expenses CSV inside the `<path_to_transaction_history>` CSV.
