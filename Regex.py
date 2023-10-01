
def clean_resume(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            resume_text = file.read()
        cleaned_resume = ' '.join(resume_text.split())


        with open(output_file, 'w') as file:
            file.write(cleaned_resume)

        print("Whitespace removed successfully!")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred:)
clean_resume('input_resume.txt', 'output_resume.txt')
