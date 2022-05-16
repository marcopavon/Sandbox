import re

string = "5,599,Skoda - Fabia Hatchback Modell,['Vollkasko'],2022-04-30 10:34:01,2022-04-30,1000,1970"

export = re.findall('([a-z]+)|([0-9]+-[0-9]+-[0-9]+)', string, re.IGNORECASE)
print(export)
#end

def update_csv_output():
        # reading line by line
    with open('../Scripts/prime.csv', 'r') as f:
    
        # store in text variable
        text = f.read()
        
        # getting the pattern for [],(),{}
        # brackets and replace them to empty string
        # creating the regex pattern & use re.sub()
        pattern = re.sub(r"[\[\]\"\']", "", text)
    
    
    # Appending the changes in new file
    # It will create new file in the directory
    # and write the changes in the file.
    with open('../Sandbox/prime_output.csv', 'w') as my_file:
        my_file.write(pattern)

with open('../Scripts/prime.csv', 'r') as f:
    
        # store in text variable
        text = f.readlines()[-5:]
        print(text, type(text))
