# Format for IMG 5881-5889 and from IMG 5894-1905 and IMG 5939-5942
# Put in prompt that the category is the name at the top of the handwritten BOM, so in the example 'HANDLES' is taken from the top
# Also include in prompt that if you can't identify a category, leave the column blank
prompt = """
System Prompt:  you are an expert at analyzing hand written Bill of material images.

Prompt:

Please extract the data from the handwritten bill of materials image and present it in a structured table format. Identify the column headers and populate the corresponding data accurately. If any information is unclear or illegible, indicate that in the respective cell.

Do not include any comments or any other text, just output the table and nothing else.

Please ensure the data is captured accurately and in the correct format.

Make the table tab delimited ('|').

If you are unable to find the BOM Number in the image, make the column blank for all rows.

The Subcategory column should include all the information you think is part of it.

Use the following example to aid you with formatting the table correctly:

Category | BOM Number | Subcategory | Part Number/ID |
HANDLES | 1-090-000 | KIPP-STANDARD ADJUSTABLE HANDLE STUD TYPE WITH 1/2-13 THREAD - 1.18 STUD LENGTH PART NO. HAS-.350 x 1/2-13 x 1.18 x 30° | 1-090-001 |
HANDLES | 1-090-000 | SOUTHCO NO 24 ADJUSTABLE GRIP FLUSH LATCH STANDARD MODEL -RH CAT NO 24-10-101-10 | 1-090-002 |
HANDLES | 1-090-000 | SOUTHCO NO 24 ADJUSTABLE GRIP FLUSH LATCH STANDARD MODEL -LH CAT NO 24-10-201-10 | 1-090-003 |
HANDLES | 1-090-000 | WROUGHT STEEL -BLACK FINISH MC MASTER - CARR CAT'L #1646A11 | 1-090-004 |
HANDLES | 1-090-000 | KIPP/ELESA ADJUSTABLE HANDLE STUD TYPE WITH M8 THD. - 30 MM STUD LG. #2 SIZE, PART NO. 39152 (PMT SUPPLY INC.) | 1-090-005 |
HANDLES | 1-090-000 | KIPP/ELESA ADJUSTABLE HANDLE WITH M6 TAP #2 SIZE, PART NO. 39011 (PMT SUPPLY INC.) | 1-090-006 |
HANDLES | 1-090-000 | SOUTHCO SPRING LATCH - SERIES 19 BLACK KNOB, MTG. STYLE RIVET PART # ST-10-401-10 | 1-090-007 |
HANDLES | 1-090-000 | KIPP/ELESA ADJUSTABLE HANDLE WITH M12 TAP #5 SIZE, PART NO. 39051 (PMT SUPPLY INC.) | 1-090-008 |
HANDLES | 1-090-000 | SOUTHCO SPRING LATCH - SERIES 30 BLACK KNOB - TAPPED HOLES (4-40) PART # ST-30-403-10 | 1-090-009 |
HANDLES | 1-090-000 | KIPP/ELESA ADJUSTABLE HANDLE WITH M10 TAP #4 SIZE, PART NO. 39041 (PMT SUPPLY INC.) | 1-090-010 |

The 'BOM Number' can usually be found in the top right of the handwritten Bill of Materials image, if you are unable to identify leave it empty.
"""