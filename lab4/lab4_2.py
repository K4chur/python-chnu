input_file_name = 'input.txt'
output_file_name = 'output.txt'

with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
    for line in input_file:
        line_with_exclamation = line.strip() + '!'
        output_file.write(line_with_exclamation + '\n')  

print(f"Added exclamation marks to {input_file_name} and saved the result in {output_file_name}.")