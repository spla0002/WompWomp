from openai import OpenAI

client = OpenAI(
    api_key='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')

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
    prompt = f"{ocr_result} Can you filter through this receipt (which has spelling mistakes) and try to find what was bought. Answer with a python list of strings (just the item/s), do not include any explanation."
    return (gpt_response(prompt))


# provides the recipes and how to make each of the items as a tuple, which we can use later idk i forgot
def recipe_maker(ingredients):  #this costs money btw
    prompt = f"I have these ingredients available: {ingredients}. Give me a python list with tuples of recipes that I can make, so (recipe name, how to make it)"
    return gpt_response(prompt)


ingredients = ingredient_extractor('''Coles s
128 Supermarkets
9 Thvoice ABN,

ore: 553
Store Manager

Australia Pt
Australia Pty Ltd
15 004 189 708

Coles

CS WAVERLEY GARDENS

Phor er; Michael

eh 2 py, 03.9548

Register: Tee moron

late 12/01/2024 ines 149
Description $
*RLISTERINE MEDIUM MOU SOOM, 4.00
Total for 1 item: $4.00
EFT
GST INCLUDED IN TOTAL $0.38
Coles VIC_AU
12/01/24 16:49 95097070 —NS5SB5
xxx 5474 Ee
CREDIT ACCOUNT NAB Visa Credit

ABSN 0000

ATC 0242 — AG000000051010

AUD$ 4.00

ie (00) APPROVED

RAN, 001150337800

AUTH, 768441 7.
NO BLN R SIGNATURE. REQUIRED

5 Card NO: 279*x*
x = Specials
y= Taxable items

EAR KREKIEIEISE

axanannnnts®*

Total Savings |

xx 4826,''')

ingredients = ingredients[1:-1].split(', ') #dont ask, its cus GPT outputs a list, but python thinks its a string, so have to convert it
ingredients = [ingredient.strip("'") for ingredient in ingredients]

print(ingredients)

print(recipe_maker(ingredients))