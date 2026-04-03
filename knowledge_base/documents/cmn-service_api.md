# cmn-service — API Endpointlar


## BankDocumentHistoryController
Route: `[controller]/[action]`

### GetListByDocumentIdAsync [POST]
- Return: `IActionResult`


## DmbatDocumentHistoryController
Route: `[controller]/[action]`

### GetListByDocumentIdAsync [GET]
- Return: `IActionResult`


## DocumentChangeLogController
Route: `[controller]/[action]`

### GetListByDocumentIdAsync [GET]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## InfoChangeLogController
Route: `[controller]/[action]`

### GetListByInfoIdAsync [GET]
- Return: `IActionResult`


## ManualController
Route: `Manual/[action]`

### GetStateSelectListAsync [GET]
- Return: `IActionResult`

### GetStatusSelectListAsync [GET]
- Return: `IActionResult`

### GetActivityTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetLanguageSelectListAsync [GET]
- Return: `IActionResult`

### GetTableSelectListAsync [GET]
- Return: `IActionResult`

### GetDocTableSelectListAsync [GET]
- Return: `IActionResult`

### GetGenderSelectListAsync [GET]
- Return: `SelectList<int>`

### GetMonthSelectListAsync [GET]
- Return: `SelectList<int>`

### GetPeriodSelectListAsync [GET]
- Return: `SelectList<int>`


## MibDocumentHistoryController
Route: `[controller]/[action]`

### GetPagedListAsync [GET]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetRegisterDocumentAsync [POST]
- Permission: `RegisterDocument`
- Return: `DbPagedModel<RegisterDocumentDto>`

### PrintRegisterDocumentAsync [POST]
- Return: `IActionResult`
