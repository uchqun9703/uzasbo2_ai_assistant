# multicast-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## TurnikateController
Route: `[controller]/[action]`

### GetTurnikateInfo [POST]
- Return: `IEnumerable<GetTurnikateInfoDto>`


## TreasInfoController
Route: `new/[controller]/[action]`

### BankDocumentInfoListAsync [GET]
- Return: `IActionResult`

### GetRestInfoAsync [POST]
- Return: `IActionResult`

### GetRestInfoOrgList [GET]
- Return: `IActionResult`

### GetRestAccountInfoAsync [POST]
- Return: `IActionResult`

### BankDocumentInfoMigAListAsync [GET]
- Return: `IActionResult`

### BankDocumentInfoMdoListAsync [GET]
- Return: `IActionResult`

### BankDoucmentAvtoYol [GET]
- Return: `IActionResult`

### GetTreasBankDocumentAsKarantin [GET]
- Return: `IActionResult`

### Organization [POST]
- Return: `IActionResult`

### GetInventoryHoldingAccountBookAsync [POST]
- Return: `IActionResult`

### GetTreasBySettlementAccountCode [GET]
- Return: `IActionResult`

### GetAccountbankDocument [POST]
- Return: `IActionResult`

### GetPdf [GET]
- Return: `IActionResult`

### GetPdfCurrencySale [GET]
- Return: `IActionResult`

### GetPdfPaymentCurrency [GET]
- Return: `IActionResult`

### GetPremanentAssetAccount [POST]
- Return: `IActionResult`

### GetPremanentAssetAccount [POST]
- Return: `IActionResult`


## GatewayImvController
Route: `[controller]/[action]`

### GetUserListAsync [POST]
- Return: `IActionResult`

### BankDocumentGetListAsync [POST]
- Return: `IActionResult`

### GetSalaryCalcAsync [POST]
- Return: `IActionResult`

### GetEmployeeInfoListAsync [GET]
- Return: `IActionResult`

### GetPayrollSheetAsync [POST]
- Return: `IActionResult`

### GetSettlementAccountListAsync [GET]
- Return: `IActionResult`

### GetOrgSignInfoAsync [POST]
- Return: `IActionResult`

### GetMaternityLeavePaymentListAsync [GET]
- Return: `IActionResult`


## GovermentAssetsController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `IActionResult`

### GetOrgInfoAsync [POST]
- Return: `IActionResult`

### GetOrgInfoMibAsync [GET]
- Return: `IActionResult`

### GetEmployeeInfoMibAsync [GET]
- Return: `IActionResult`

### GetOrgAccountInfoAsync [GET]
- Return: `IActionResult`

### GetOrgFullInfoAsync [GET]
- Return: `IActionResult`

### GetOrgNameByInnAsync [POST]
- Return: `IActionResult`

### GetOrgPositionAsync [GET]
- Return: `IActionResult`

### CheckWorking [GET]
- Return: `IActionResult`

### GetStudentStipend [POST]
- Return: `IActionResult`

### GetSocialBenefit [POST]
- Return: `IActionResult`


## MinistryOfInternalAffairsController
Route: `[controller]/[action]`

### GetSettlementAccountListAsync [POST]
- Return: `IActionResult`


## MoliyachiNotificationController
Route: `new/[controller]/[action]`

### Create [POST]
- Return: `IActionResult`

### CalculateSalary [POST]
- Return: `IActionResult`


## ProsecutorDepartmentController
Route: `[controller]/[action]`

### GetOrganizationInfo [GET]
- Return: `IActionResult`

### GeStaffing [GET]
- Return: `IActionResult`

### GetBudget [GET]
- Return: `IActionResult`

### GetRequestReceivingCash [GET]
- Return: `IActionResult`

### GetContractorBook [GET]
- Return: `IActionResult`

### GetAccountBook [GET]
- Return: `IActionResult`

### GetAccountBookByContractor [GET]
- Return: `IActionResult`

### GetSubAcc [GET]
- Return: `IActionResult`

### GetOrgSettlementAccount [GET]
- Return: `IActionResult`


## StudentContractInfoController
Route: `Integration/[action]`

### GetStudentContractInfo [POST]
- Return: `IActionResult`

### GetStudentStipend [POST]
- Return: `IActionResult`


## YammtController
Route: `[controller]/[action]`

### GetStaffingVacancy [POST]
- Return: `IActionResult`
