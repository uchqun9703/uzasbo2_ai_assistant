# finance-report-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## IntegrationController
Route: `Integration/[action]`

### GetInPaymentForBillingAsync [POST]
- Return: `IActionResult`

### GetRestByAccountAsync [POST]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetContractorRestAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetContractorAccountBookAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetContractorAccountBookActAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### PrintGetContractorAccountBookAsync [POST]
- Return: `IActionResult`

### PrintContractorAccountBookActAsync [POST]
- Return: `IActionResult`

### GetContractRestAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetContractAccountBookAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### PrintGetContractAccountBookAsync [POST]
- Return: `IActionResult`

### PrintGetContractAccountBookByRegionAsync [POST]
- Return: `IActionResult`

### GetYearExpenseBookAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetReportFormN2Async [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### PrintReportFormN2Async [POST]
- Return: `IActionResult`

### GetItemOfExpenseAccountBookAsync [POST]
- Permission: `ItemOfExpenseAccountBookView`
- Return: `IActionResult`

### PrintItemOfExpenseAccountBookAsync [POST]
- Return: `IActionResult`

### GetItemOfExpenseTurnoverBySubAccIdAsync [POST]
- Permission: `ItemOfExpenseTurnoverBySubAccIdView`
- Return: `IActionResult`

### PrintItemOfExpenseTurnoverBySubAccIdAsync [POST]
- Return: `IActionResult`

### GetAccountContractAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### PrintGetAccountContractAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetRegisterPaymentOrderAsync [POST]
- Permission: `RegisterPaymentOrder`
- Return: `IActionResult`

### PrintRegisterPaymentOrderAsync [POST]
- Permission: `AccountContractView`
- Return: `IActionResult`

### GetReportPaymentOrderAsync [POST]
- Permission: `RegisterPaymentOrder`
- Return: `IActionResult`

### PrintGetReportPaymentOrderAsync [POST]
- Return: `IActionResult`

### GetOnlinePaymentAsync [POST]
- Permission: `ChildComeView`
- Return: `IActionResult`
