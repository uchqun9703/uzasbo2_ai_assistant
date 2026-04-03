# staff-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ManualController
Route: `[controller]/[action]`

### GetIvsTempCalcList [POST]
- Return: `IActionResult`

### InsertIvsSalary [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш


## PerformanceController
Route: `[controller]/[action]`

### Diagnostics [GET]
- Return: `IActionResult`

### ServerStatus [GET]
- Return: `IActionResult`

### AspNetStatus [GET]
- Return: `IActionResult`

### GCStatus [GET]
- Return: `IActionResult`

### ThreadPoolStatus [GET]
- Return: `IActionResult`

### ProcessStatus [GET]
- Return: `IActionResult`


## StaffingPositionReplacementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingPositionReplacementView`
- Return: `PagedResult<StaffingPositionReplacementListDto>`

### GetAsync [GET]
- Permission: `StaffingPositionReplacementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingPositionReplacementView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffingPositionReplacementEdit`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини таҳрирлаш

### GetTableListAsync [POST]
- Permission: `StaffingPositionReplacementView`
- Return: `PagedResult<StaffingPositionReplacementTableDto>`

### CreateTableAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`

### CreateCalcKindTableAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`

### DeleteCalcKindTableAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`

### DeleteTableAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`

### GetCalcKindListAsync [POST]
- Permission: `StaffingPositionReplacementView`
- Return: `List<StaffingPositionReplacementCalcKindDto>`

### AcceptAsync [POST]
- Permission: `StaffingPositionReplacementAccept`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StaffingPositionReplacementCancel`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingPositionReplacementDelete`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини ўчириш

### PrintAsync [POST]
- Return: `IActionResult`
