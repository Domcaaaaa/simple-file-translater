import re
import yaml
import translators as ts

def translate_file(input_file, output_file):
    
    with open(input_file, 'r', encoding='utf-8') as file:
        yaml_data = yaml.safe_load(file)

   
    input_text = yaml_data['text']
    extracted_text = re.findall(r'"([^"]*)"', input_text)

    
    translated_text = input_text
    for text in extracted_text:
        translated = ts.translate_text(text, to_language='cs')
        translated_text = translated_text.replace(text, translated)


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print("Translation completed. The translated text is saved in the output file:", output_file)


input_file = ''    
output_file = ''  

translate_file(input_file, output_file)
