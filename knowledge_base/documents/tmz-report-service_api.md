# tmz-report-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ReportController
Route: `[controller]/[action]`

### GetInventoryHoldingRest [POST]
- Permission: `RestByInventoryHoldingView`
- Return: `IActionResult`

### GetInventoryHoldingAccountBook [POST]
- Permission: `InventoryHoldingView`
- Return: `IActionResult`

### PrintGetInventoryHoldingAccountBook [POST]
- Return: `IActionResult`

### PrintExportActInventory [POST]
- Return: `IActionResult`

### GetInventoryHoldingCard [POST]
- Permission: `InventoryHoldingView`
- Return: `IActionResult`

### PrintInventoryHoldingCard [POST]
- Return: `IActionResult`


## IntegrationController
Route: `Integration/[action]`

### GetInventoryHoldingRest [POST]
- Return: `IActionResult`

### GetAccountBook [POST]
- Return: `IActionResult`
