import subprocess
import json
import re

def getSentiment(ticker: str):
    prompt = createSentimentPrompt(ticker_symbol=ticker)
    savePromptIntoFile(prompt)
    models = [
    "gpt4o",
    "Phi-3.5-MoE",
    "AI21-Jamba-1.5-Large",
    "Cohere-command-r",
    "Meta-Llama-3.1-405B-Instruct",
    "MistralNemo",
    "jais-30b-chat"
    ]
    model = models[3]
    promptString = json.dumps(prompt, separators=(',', ':'))
    result = subprocess.run(["node", "ai/model.js", promptString, model], capture_output=True, text=True)
    result.stdout = remove_newlines(result.stdout)
    
    # Using regex to check if it’s purely a number
    if not onlyNumber(result.stdout):
        fallbackPrompt = create_number_extraction_prompt(result.stdout)
        fallbackPromptString = json.dumps(fallbackPrompt, separators=(',', ':'))
        result = subprocess.run(["node", "ai/model.js", fallbackPromptString, model], capture_output=True, text=True)
        result.stdout = remove_newlines(result.stdout)
        if not onlyNumber(result.stdout):
            result.stdout = ''
    
    print(f"Sentiment Score for {ticker}:", result.stdout)

    saveResponseIntoFile(result.stdout)
    return result.stdout

def onlyNumber(text: str) -> bool:
    return re.fullmatch(r"[-+]?(\d+(\.\d*)?|\.\d+)", text)

def remove_newlines(text: str) -> str:
    text = text.replace('.\n', '')
    text = text.replace('\n', '')
    return text.strip()

def saveResponseIntoFile(response):
    # Save output to response.js file
    response = f'{{ "response": "{response}" }}'
    with open("ai/response.json", "w") as file:
        file.write(response)

def savePromptIntoFile(prompt):
    # Write the prompt data to a JSON file
    with open("./ai/prompt.json", "w") as json_file:
        json.dump(prompt, json_file, indent=4)

def createSentimentPrompt(ticker_symbol: str):
    prompt_data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a financial expert with a deep understanding of stock market trends and sentiment analysis."
            },
            {
                "role": "user",
                "content": (
                    f"Analyze the overall market sentiment for the stock with ticker symbol '{ticker_symbol}' "
                    "based on recent news, social media, and financial reports. Output a sentiment score ranging "
                    "from -1 to +1, where -1 represents the most bearish sentiment and +1 represents the most bullish sentiment. The output must be just the sentiment number."
                )
            }
        ]
    }

    return prompt_data

def create_number_extraction_prompt(response: str) -> dict:
    prompt_data = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an assistant specializing in extracting precise numerical values from text."
                )
            },
            {
                "role": "user",
                "content": (
                    f"The previous response was: '{response}'. Extract only the numerical value from it "
                    "and provide it as the output without any additional explanation or text."
                )
            }
        ]
    }
    return prompt_data