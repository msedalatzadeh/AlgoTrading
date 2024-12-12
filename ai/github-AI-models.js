import ModelClient from "@azure-rest/ai-inference"
import { AzureKeyCredential } from "@azure/core-auth"
import OpenAI from "openai"
import config from "../config-private.json" with { type: "json" } // replace with your own config.json
//import { Mistral } from '@mistralai/mistralai'

export async function main() {
    const azureModels = [
        "Cohere-command-r",
        "AI21-Jamba-1.5-Large",
        "Meta-Llama-3.1-405B-Instruct",
        "jais-30b-chat"
    ]

    const prompt = JSON.parse(process.argv[2]) // could be another way of giving it prompt as input in process.run()

    const model = process.argv[3]
    const token = config["github-AI-models-api-keys"][model];
    let response
    if (azureModels.includes(model)) {
        const client = new ModelClient(
            "https://models.inference.ai.azure.com",
            new AzureKeyCredential(token)
        );

        response = await client.path("/chat/completions").post({
            body: {
                messages: prompt["messages"],
                model: model,
                temperature: 0.8,
                max_tokens: 2048,
                top_p: 0.1
            }
        });
    }
    else if (model === "gpt-4o") {
        const client = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com",
            apiKey: token
        });
    
        response = await client.chat.completions.create({
            messages: prompt["messages"],
            model: model,
            temperature: 1,
            max_tokens: 4096,
            top_p: 1
        });
    }
    else if (model === "Mistral-Nemo") {
        const client = new Mistral({
            apiKey: token,
            serverURL: "https://models.inference.ai.azure.com"
        });
        
        
        response = await client.chat.complete({
        model: model,
        messages: prompt["messages"],
        temperature: 0.8,
        max_tokens: 2048,
        top_p: 0.1
        });
    }

    if (response.status !== "200") {
        throw response.body.error;
    }

    console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
    console.error("The sample encountered an error:", err);
});
