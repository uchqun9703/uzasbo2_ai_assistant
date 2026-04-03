# asset-report-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetPermanentAssetRest [POST]
- Permission: `RestByPermanentAssetView`
- Return: `IActionResult`

### GetPermanentAssetAccountBook [POST]
- Permission: `PermanentAssetView`
- Return: `IActionResult`

### PrintGetPermanentAssetAccountBook [POST]
- Return: `IActionResult`

### GetPermanentAssetAgeingAccountBook [POST]
- Permission: `PermanentAssetAgeingView`
- Return: `IActionResult`

### PrintGetPermanentAssetAgeingAccountBook [POST]
- Return: `IActionResult`

### PrintGetPermanentAssetAgeingAccountBookByOrg [POST]
- Return: `IActionResult`

### GetPermanentAssetAgeingDepartmentAccountBook [POST]
- Permission: `PermanentAssetAgeingView`
- Return: `IActionResult`

### PrintGetPermanentAssetAgeingDepartmentAccountBook [POST]
- Return: `IActionResult`

### GetPermanentAssetReappraisalAccountBook [POST]
- Permission: `PermanentAssetReappraisalIndexView`
- Return: `IActionResult`

### PrintGetPermanentAssetReappraisalAccountBook [POST]
- Return: `IActionResult`

### PrintAccountBookPermanentAssetInventory [POST]
- Return: `IActionResult`

### GetAccountBookAgeing [POST]
- Permission: `PermanentAssetView`
- Return: `IActionResult`

### GetAccountBookAgeingPrint [POST]
- Return: `IActionResult`


## ValuesController
Route: `Values/[action]`

### ErrorLog [GET]
- Return: `IActionResult`
