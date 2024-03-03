from openai import OpenAI

client = OpenAI(
    api_key='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') #Set as environ var in production

def gpt_response(prompt):
    chat_completion = client.chat.completions.create(
        messages = [
            {
            "role":"user",
            "content":prompt
            }
        ],
        model = "gpt-3.5-turbo"
    )
    output = chat_completion.choices[0].message.content
    return output

# takes the result of the OCR and makes it into a list of ingredients 
def ingredient_extractor(ocr_result):
    prompt = f"{ocr_result} Can you filter through this receipt (which has spelling mistakes) and try to find what was bought. Keep in mind, some of the values that are numbers (such as 200ml/600ml) may be read as SOOM, its not highly accurate, just try and best guess. Answer with a python list of strings (just the item/s), do not include any explanation."
    return (gpt_response(prompt))


# provides the recipes and how to make each of the items as a tuple, which we can use later idk i forgot
def recipe_maker(ingredients):  #this costs money btw
    prompt = f"I have these ingredients available: {ingredients}. Give me a python list with tuples of recipes that I can make, so (recipe name, how to make it)."
    return gpt_response(prompt)
