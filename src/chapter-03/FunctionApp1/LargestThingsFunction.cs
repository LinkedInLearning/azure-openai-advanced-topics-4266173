using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Extensions.OpenAI.TextCompletion;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace FunctionApp1;

public class LargestThingsFunction(ILogger<LargestThingsFunction> logger)
{
    [Function(nameof(LargestThingsFunction))]
    public async Task<HttpResponseData> Run([HttpTrigger(AuthorizationLevel.Function, "get", Route = "largest/{things}")] HttpRequestData req,
       [TextCompletionInput("What are the largest {things} in the world?",
        MaxTokens = "1000",
        Temperature = "0.6",
        Model = "%MODEL_NAME%")]  TextCompletionResponse response)
    {
        logger.LogInformation($"Total tokens: {response.TotalTokens}");
        var data = req.CreateResponse(System.Net.HttpStatusCode.OK);
        await data.WriteStringAsync(response.Content);
        return data;
    }
}
