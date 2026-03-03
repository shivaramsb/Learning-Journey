# AWS Generative AI Learning Report

## Summary of Today's Learnings
Today, you explored the fundamentals of using the Amazon Bedrock API to interact with Amazon's Nova foundation models. Through a series of five Jupyter Notebooks, you learned how to programmatically generate text, stream responses, and even generate videos using AWS Generative AI services.

### Key Concepts & Skills Acquired:

1. **Basic Text Generation (`Invoking an Amazon Bedrock Foundation Model.ipynb` & `genai-exercise1-text1.ipynb`)**
   - **Concepts:** You learned how to initialize a `boto3` client for `bedrock-runtime` and invoke text models like `amazon.nova-lite-v1:0` and `amazon.nova-micro-v1:0`.
   - **Skills:** You used the `invoke_model` and `converse` APIs to send prompts in the "messages-v1" schema format. For example, you successfully tasked the models to rewrite sentences into a formal tone, controlling the output via `inferenceConfig` parameters (like `maxTokens`, `topK`, and `temperature`).
   - **Extras:** You also explored how to pass an experimental `guardrailVersion` in the parameters.

2. **Streaming AI Responses (`genai-exercise1-text2.ipynb`)**
   - **Concepts:** For longer text generation (such as explaining different types of dances), waiting for the entire response can take time. You learned how to handle streaming outputs.
   - **Skills:** Using the `invoke_model_with_response_stream` API, you were able to process the AI’s response in real-time as a stream of byte chunks, decoding and printing out each `contentBlockDelta` piece-by-piece as it was generated.

3. **Asynchronous Video Generation (`genai-exercise1-video.ipynb`)**
   - **Concepts:** Video generation is a heavy process that requires asynchronous execution instead of a synchronous wait.
   - **Skills:** You worked with the `amazon.nova-reel-v1:0` model to generate a video from a text prompt ("A person dancing on a mountain"). You learned how to:
     - Use `start_async_invoke` to kick off a video generation job.
     - Provide video configuration settings (like FPS, dimensions, standard duration, and seed).
     - Submit an S3 bucket URI (`s3://gen-ai-exercise-shivaram/video/`) as the destination for the generated output.
     - Check the status of your asynchronous task using `get_async_invoke`.

4. **Advanced Bedrock Configurations (`invoke_model.ipynb`)**
   - **Concepts:** You explored advanced authentication and regional configurations.
   - **Skills:** You learned how to use a specific `boto3.Session` (using the "default" profile) and explicit signature versions (`v4`). You also explored using an "inference-profile" ARN (`global.amazon.nova-2-lite-v1:0`) to efficiently route and invoke models across regions using the `converse` API to explain complex topics like "quantum computing."

## Conclusion
You have built a very solid foundation! You've transitioned from making standard API calls to handling real-time streaming data, and you've even expanded beyond text into asynchronous multi-media/video generation. Understanding the distinction between `invoke_model`, `invoke_model_with_response_stream`, and `start_async_invoke` equips you well for building full-fledged generative AI applications on AWS.
