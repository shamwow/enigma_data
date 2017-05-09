- `primary_id`: Must be an integer.
- `drug_name`: Must be a non blank, capitalized string.
- `validated_verbatim_drugname`: Must be an integer.
- `dose_verbatim`: Can be any string.
- `patient_gender`: Must be blank, M, or F.
- `patient_weight`: Must be a number.
- `weight_unit`: Can be blank if `patient_weight` is 0. Otherwise must be either LBS or KG
- `report_date`: Must be a date in the format `YYYYMMdd` or `YYYY-MM-dd`.
- Each row must contain exactly 8 columns.

Assuming the constraints described above, these are the problems the script outputted (column titles are in row #0):

```
More than 8 columns on row #3
Less than 8 columns on row #11
Less than 8 columns on row #12
report_date not formated as YYYYMMdd or YYYY-MM-dd on row #36
report_date not formated as YYYYMMdd or YYYY-MM-dd on row #45
Less than 8 columns on row #101
More than 8 columns on row #107
Less than 8 columns on row #502
```

Possible reasons for data problems:

- Row 3: Extra commas in column 4 and 5, after "20 MG" and "SINGLE". (Assumes "20 MG SINGLE INTRAVENOUS" is a valid dose_verbatim)
- Row 12 - 13: Line break in middle of 4th column
- Row 101: Unnecessary quotation marks in 3rd row. Two extra commas after "256.30 MG (DAILY DOSE)"
- Row 107: Extra comma in rows 4 and 5, after "20 MG" and "DAILY" (Assumes "20 MG  DAILY 25.9 G CUMULATIVE DOSE" is a valid dose_verbatim)
