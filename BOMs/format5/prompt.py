prompt = """
System Prompt: You are an expert at analyzing hand written Bill of material images.

Prompt:

Please extract the data from the handwritten bill of materials image and present it in a structured table format. Identify the column headers and populate the corresponding data accurately. If any information is unclear or illegible, indicate that in the respective cell.

Do not include any comments or any other text, just output the table and nothing else.

Please ensure the data is captured accurately and in the correct format.

Make the table tab delimited ('|').

Use the following example to aid you with formatting the table correctly:

Category | Subcategory | Part Number/ID |
Index | General For Rebuilding (FMC's Etc) | 10-000-000 |
Index | AmeriPak PFM 2000/2500 | 11-000-000 |
Index | AmeriPak PFM 50/80/200/30 | 12-000-000 |
Index | "LS" Quad - All Quads | 13-000-000 |
Index | Intermittent Cardboard Sheeter (FMC) | 14-000-000 |
Index | Gluers & Wrappers | 15-000-000 |
Index | Cioni Box Closer | 16-000-000 |
Index | Vipomat | 16-100-000 |
Index | Machines in Inventory | 17-000-000 |
Index | Sheet Metal | 17-500/501-000 |
Index | STS Polywrapper | 18-000-000 |
Index | AmeriPak Filled Tray Sealer Model "245" | 19-000-000 |
Index | AmeriPak 60/140/560 Wrapper | 20-000-000 |
Index | AmeriPak 3500 Wrapper | 21-000-000 |
Index | AmeriPak 3500 Servo Feeder | 22-000-000 |
Index | AmeriPak 40 | 23-000-000 |
Index | HWS | 24-000-000 |

The 'Category' column data from the above example is usually extracted from the top center of the Bill of Materials image, make sure to include all of the text from the image where you determine is the 'Category'. Also make sure to fill every row in the 'Category' column of the table.

Only use the 3 columns from the example: 'Category', 'Subcategory', and 'Part Number/ID'. If you are unable to identify any of the columns from the image, leave it blank.

Also pay close attention to each Part Number/ID as it may not be in numerical order always and if you do end up tripping up, ensure not to make each Part Number/ID after be wrong. Make sure you match each Part Number/ID with its corresponding Category individually and accurately.
"""