# acc-service — API Endpointlar


## AccountPlanController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AccountPlanView`
- Return: `PagedResult<AccountPlanListDto>`

### PrintGetListAsync [POST]
- Permission: `AccountPlanView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AccountPlanView`
- Return: `IActionResult`

### Get [GET]
- Permission: `AccountPlanView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AccountPlanCreate`
- Return: `IActionResult`
- Tavsif: Хисоб режаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `AccountPlanEdit`
- Return: `IActionResult`
- Tavsif: Хисоб режаси ҳужжатини таҳрирлаш

### InitAsync [POST]
- Permission: `AccountPlanInit`
- Return: `IActionResult`
- Tavsif: Хисоб режаси ҳужжатини ишга тушуриш

### DeleteAsync [POST]
- Permission: `AccountPlanDelete`
- Return: `IActionResult`
- Tavsif: Хисоб режаси ҳужжатини ўчириш


## AllowedTransactionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AllowedTransactionView`
- Return: `PagedResult<AllowedTransactionListDto>`

### PrintGetList [POST]
- Permission: `AllowedTransactionView`
- Return: `IActionResult`
- Tavsif: Ўтказмалар ҳужжатини ўчириш

### GetAsync [GET]
- Permission: `AllowedTransactionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AllowedTransactionView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AllowedTransactionCreate`
- Return: `IActionResult`
- Tavsif: Ўтказмалар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `AllowedTransactionEdit`
- Return: `IActionResult`
- Tavsif: Ўтказмалар ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `AllowedTransactionDelete`
- Return: `IActionResult`
- Tavsif: Ўтказмалар ҳужжатини ўчириш


## CloseMonthController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CloseMonthView`
- Return: `PagedResult<CloseMonthListDto>`

### Get [GET]
- Permission: `CloseMonthView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CloseMonthView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CloseMonthCreate`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CloseMonthEdit`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CloseMonthAccept`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CloseMonthCancel`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `CloseMonthDelete`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини ўчириш

### GetCloseMonthsAsync [POST]
- Permission: `AccountBookView`
- Return: `IActionResult`
- Tavsif: Ҳисоб режасини қайта ҳисоблаш ҳужжатини ҳужжат бор ойларни текшириш.

### RefreshAccountBookAsync [POST]
- Permission: `AccountBookView`
- Return: `IActionResult`


## EnumController
Route: `[controller]/[action]`

### GetAccountPlanTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetAccountPlanTypeGroupSelectListAsync [GET]
- Return: `IActionResult`

### GetSubCountSelectListAsync [GET]
- Return: `IActionResult`

### GetFunctionValueAsync [GET]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## SubAccountPlanController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SubAccountPlanView`
- Return: `PagedResult<SubAccountPlanListDto>`

### PrintGetListAsync [POST]
- Permission: `SubAccountPlanView`
- Return: `IActionResult`
- Tavsif: Субсчет ҳужжатини ўчириш

### GetAsync [GET]
- Permission: `SubAccountPlanView`
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SubAccountPlanCreate`
- Return: `IActionResult`
- Tavsif: Субсчет ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SubAccountPlanEdit`
- Return: `IActionResult`
- Tavsif: Субсчет ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SubAccountPlanDelete`
- Return: `IActionResult`
- Tavsif: Субсчет ҳужжатини ўчириш


## SubCountController
Route: `[controller]/[action]`

### GetListByAllowedTransactionIdAsync [GET]
- Return: `IActionResult`

### GetListBySubAccountPlanIdAsync [GET]
- Return: `IActionResult`
