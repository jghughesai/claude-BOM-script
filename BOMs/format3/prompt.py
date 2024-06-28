# Format for IMG 5890 and 5891
prompt = """
System Prompt:  you are an expert at analyzing hand written Bill of material images.

Prompt:

Please extract the data from the handwritten bill of materials image and present it in a structured table format. Identify the column headers and populate the corresponding data accurately. If any information is unclear or illegible, indicate that in the respective cell.

Do not include any comments or any other text, just output the table and nothing else.

Please ensure the data is captured accurately and in the correct format.

Make the table tab delimited ('|').

Use the following example to aid you with formatting the table correctly:

Category | BOM Number | Subcategory | Part Number/ID | Paul Moore # Specify Length |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Stain. Steel 040" Thick x 1 1/2 x 72" LG-3/32 Pin | 01-093-001-7 | 55040024 |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Steel .060" Thick x 1 1/2" x 72"Lg 1/8 Pin | 01-093-002-7 | 5063024 |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Stain. Steel .060" Thick x 2" x72" LG 1/8 Pin | 01-093-003-7 | 55062032 |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Stain. Steel .060" Thick x 1 1/2" x 72" LG 3/16 Pin | 01-093-004-7 | 55065024 |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Stain. Steel .060" Thick x 1 1/2" x 72" LG 1/8 Pin | 01-093-005-7 | 55062024 |
Hinge-Continuous | 01-093-000 | Hinge-Continuous-Stain. Steel .050" Thick x 2" x 72" LG 1/8 Pin| 01-093-006-7 | 5052032 |
"""