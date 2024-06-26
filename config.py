import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

BOM_DIRECTORY = "BOMs"
OUTPUTS_DIRECTORY = "outputs"
CLAUDE_OUTPUT_FILENAME = "claude_result.tsv"

CLAUDE_OUTPUT_PATH = os.path.join(OUTPUTS_DIRECTORY, CLAUDE_OUTPUT_FILENAME)

PROMPT = f"""
System Prompt:  you are an expert at analyzing hand written Bill of material images.

Prompt:

Please extract the data from the handwritten bill of materials image and present it in a structured table format. Identify the column headers and populate the corresponding data accurately. If any information is unclear or illegible, indicate that in the respective cell.

The table should include the following columns if present in the image:

- Category

- Subcategory

- Part Number or ID

- Description or Name

- Material or Specification

- Dimensions or Size

- Quantity or Count

Any additional columns present in the image.

Do not include any comments or any other text, just output the table and nothing else.

If a column is missing from the image, you can omit it from the table. Please ensure the data is captured accurately and in the correct format.

Make the table tab delimited ('|').

"""