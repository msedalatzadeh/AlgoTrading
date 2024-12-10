import OpenAI from "openai";
import prompt from "./prompt.json" with { type: "json" }
import config from "../config-private.json" with { type: "json" }

const token = config["aiTokens"]["gpt4o"]

export async function main() {
    const client = new OpenAI({
        baseURL: "https://models.inference.ai.azure.com",
        apiKey: token
    });

    const response = await client.chat.completions.create({
        messages: [
        { role:"system", content: "" },
        { role:"user", content: prompt["prompt"] }
        ],
        model: "gpt-4o",
        temperature: 1,
        max_tokens: 4096,
        top_p: 1
    });

    console.log(response.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});