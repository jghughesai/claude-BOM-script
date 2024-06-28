from config import CLAUDE_OUTPUT_PATH, ANTHROPIC_API_KEY, BOM_DIRECTORY, PROMPT
from ai_image_analysis.interpreters import claude_interpreter as claude
from ai_image_analysis.core import process
import logging
import os
import re
import importlib.util

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log")
    ]
)

def load_prompt_from_subdir(sub_dir_path):
    prompt_path = os.path.join(sub_dir_path, 'prompt.py')
    spec = importlib.util.spec_from_file_location("prompt", prompt_path)
    prompt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prompt_module)
    return prompt_module.prompt
def main():
    claude_obj = claude.ClaudeInterpreter(api_key=ANTHROPIC_API_KEY)

    sub_dirs = [sub for sub in os.listdir(BOM_DIRECTORY) if sub.startswith('format')]
    sub_dirs.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    for sub_dir in sub_dirs:
        sub_dir_path = os.path.join(BOM_DIRECTORY, sub_dir)
        print(f'sub_dir being worked: {sub_dir_path}\n')

        prompt = load_prompt_from_subdir(sub_dir_path)
        print(f'prompt: {prompt}\n')

        process.process_dir(claude_obj, sub_dir_path, prompt, CLAUDE_OUTPUT_PATH)


if __name__== '__main__':
    main()