from config import CLAUDE_OUTPUT_PATH, ANTHROPIC_API_KEY, BOM_DIRECTORY, PROMPT
from ai_image_analysis.interpreters import claude_interpreter as claude
from ai_image_analysis.core import process
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log")
    ]
)

def main():
    claude_obj = claude.ClaudeInterpreter(api_key=ANTHROPIC_API_KEY)

    process.process_dir(claude_obj, BOM_DIRECTORY, PROMPT, CLAUDE_OUTPUT_PATH)


if __name__== '__main__':
    main()