# For IMG 1906-1938
prompt = """
System Prompt:  you are an expert at analyzing hand written Bill of material images.

Prompt:

Please extract the data from the handwritten bill of materials image and present it in a structured table format. Identify the column headers and populate the corresponding data accurately. If any information is unclear or illegible, indicate that in the respective cell.

Do not include any comments or any other text, just output the table and nothing else.

Please ensure the data is captured accurately and in the correct format.

Make the table tab delimited ('|').

Use the following example to aid you with formatting the table correctly:

Category | BOM Number | Length (in.) | Part No. |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | Close 3/4 | 001 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 1 1/2 | 002 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 2 | 003 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 2 1/2 | 004 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 3 | 005 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 3 1/2 | 006 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 4 | 007 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 4 1/2 | 008 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 5 | 009 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 5 1/2 | 010 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 6 | 011 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 7 | 012 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 8 | 013 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 9 | 014 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 10 | 015 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 11 | 016 |
1/8 N.P.T Black Iron Nipples | 1-102-000 To 1-102-049 | 12 | 017 |

The 'Category' column data from the above example is usually extracted from the top center of the Bill of Materials image. The 'BOM Number' column data from the above example is usually extracted from the numbers in the top right of the handwritten Bill of Materials paper in the image, if you are unable to clearly identify or deduce what the 'Category' or 'BOM Number' is then leave whichever column blank.

Also pay close attention to each Part No. as it may not be in numerical order always and if you do end up tripping up make sure not to make each Part Po. after be wrong. Make sure you match each Part No. with its corresponding lengths(in.) individually and accurately.
"""