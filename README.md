# YAML Text Translator

A Python script that extracts and translates text from a YAML file and saves the translated content to a new file. The script uses the `translators` library for translation and supports extracting text enclosed in double quotes (`" "`). This project is useful for translating localized content or other YAML-based text files to a different language.

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Setup](#setup)
- [Usage](#usage)
- [Example](#example)
- [Notes](#notes)

## Overview
This script reads a YAML file, extracts text enclosed in double quotes (`" "`), translates it into a specified language (Czech by default), and saves the translated content to a new output file. The script leverages the `translators` library to perform translations and the `yaml` library for parsing YAML files.

## How It Works
1. **Read YAML File**:
   - The script opens and reads a YAML file using the `yaml` library.
   - It looks for a specific key (`'text'`) in the YAML structure and extracts the text.
   
2. **Extract Text for Translation**:
   - The script uses a regular expression to find text enclosed in double quotes.
   
3. **Translate the Text**:
   - It translates each extracted text snippet to Czech (or another specified language) using the `translators` library (`translators.translate_text`).

4. **Save Translated Content**:
   - The translated content is then saved to the specified output file in YAML format.

## Setup

### Prerequisites
- Python 3.x installed on your system.
- Install the required Python libraries:
  ```bash
  pip install pyyaml translators
  ```

### Dependencies
- `pyyaml`: For parsing and writing YAML files.
- `translators`: For translating the extracted text.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yaml-translator.git
   cd yaml-translator
   ```

2. Modify the script to point to your input and output files:
   ```python
   input_file = 'path/to/your/input.yaml'
   output_file = 'path/to/your/output.yaml'
   ```

3. Run the script:
   ```bash
   python translate_yaml.py
   ```

4. The translated content will be saved in the specified output file.

## Example
### Input YAML File (`input.yaml`):
```yaml
text: "Hello, world! This is a test. \"Translate this sentence.\""
```

### Translated Output YAML File (`output.yaml`):
```yaml
text: "Ahoj, světe! Toto je test. \"Přeložte tuto větu.\""
```

*Note*: The actual translated output may vary depending on the translation service.

## Notes
- Ensure that the YAML file contains a key named `'text'` that holds the string to be translated. If the structure of your YAML file is different, you may need to modify the script accordingly.
- The script translates text found within double quotes (`" "`). If the text you want to translate is not enclosed in double quotes, modify the regular expression in the script.
- The default target language is Czech (`'cs'`). You can change the `to_language` parameter in the `ts.translate_text()` call to translate to another language (e.g., `'fr'` for French).
