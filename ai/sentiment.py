import subprocess

result = subprocess.run(["node", "ai/gpt4o.js"], capture_output=True, text=True)

def remove_newlines(text: str) -> str:
    return text.replace('\n', '')

# Print the output
print("Output from API:", result.stdout)

# Save output to response.js file
response = f'{{ "response": "{remove_newlines(result.stdout)}" }}'
with open("ai/response.json", "w") as file:
    file.write(response)