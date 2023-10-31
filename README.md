# azure-function-openai

This repository containes sample code to test openai chat deployment with azure functions.

Setup azure credentials
```
az login
```
Create a new resource group
```
az group create --name YourResourceGroup --location YourLocation
```
Create storage account
```
az storage account create --name YourStorageAccountName --resource-group YourResourceGroup --location YourLocation --sku Standard_LRS
```
Create a new frunction
```
az functionapp create --resource-group YourResourceGroup --name YourFunctionAppName --consumption-plan-location YourLocation --runtime python --runtime-version 3.9 --functions-version 4 --os-type Linux
```
Set environment variables
```
az functionapp config appsettings set --name YourFunctionAppName --resource-group YourResourceGroup --settings OPENAI_API_KEY=YourOpenAIKey
```
Deploy the function with cli or using VScode
```
func azure functionapp publish openai-poc-prompt-api
```
Get function endpoint
```
az functionapp show --name YourFunctionAppName --resource-group YourResourceGroup --query "defaultHostName" --output tsv
```
List functions in the function app
```
az functionapp function list --name YourFunctionAppName --resource-group YourResourceGroup
```
Make an HTTP request to test
```
curl -X POST "https://YourFunctionAppName.azurewebsites.net/api/YourFunctionName" -d "{\"prompt\":\"YourPromptText\"}"
```