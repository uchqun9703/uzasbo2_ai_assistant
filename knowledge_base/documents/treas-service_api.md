# treas-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ManualController
Route: `[controller]/[action]`

### BankDocumentGetListAsync [POST]
- Permission: `BankView`
- Return: `BankDocumentNewPageGetList`

### BankDocumentPrintAsync [POST]
- Return: `IActionResult`

### GetRestInfoAsync [POST]
- Return: `IActionResult`

### PrintDataHeaderAsync [POST]
- Return: `IActionResult`

### PrintIntlFinanceInstAsync [POST]
- Return: `IActionResult`

### PrintAllDataHeaderAsync [POST]
- Return: `IActionResult`

### PrintStatementAccount [POST]
- Return: `IActionResult`

### GetRestAccountInfoAsync [GET]
- Return: `IActionResult`

### GetItemOfExpenseListForENKTAsync [GET]
- Return: `IActionResult`

### FillContractSpecificationV2FromLotAsync [GET]
- Return: `IActionResult`

### GetENKTListTestAsync [POST]
- Return: `IActionResult`

### GetENKTPropertiesListTestAsync [GET]
- Return: `IActionResult`

### GetENKTPropertiesValuesListTestAsync [GET]
- Return: `IActionResult`

### GetENKTListAsync [GET]
- Return: `IActionResult`

### GetENKTPropertiesListAsync [GET]
- Return: `IActionResult`

### GetENKTPropertiesValuesListAsync [GET]
- Return: `IActionResult`

### GetTreasStatusAsync [GET]
- Return: `IActionResult`

### GetTreasStatusAsync [POST]
- Return: `IActionResult`

### ContractRegistrationPrintAsync [POST]
- Return: `IActionResult`

### GetContractSpecificationAsync [GET]
- Return: `IActionResult`

### GetContractSpecificationTableAsync [GET]
- Return: `IActionResult`

### GetTreasBudgetListAsync [POST]
- Return: `IActionResult`

### GetTreasChequeListAsync [POST]
- Permission: `TreasBudgetView`
- Return: `PagedResult<ChequeListDto>`

### TreasChequePrintAsync [POST]
- Return: `IActionResult`

### GetUzexDealsJsonAsync [POST]
- Permission: `TreasBudgetView`
- Return: `IActionResult`

### GetUzexDealsTableJsonAsync [GET]
- Return: `IActionResult`

### GetUzexBlackListAsync [POST]
- Permission: `TreasBudgetView`
- Return: `IActionResult`

### GetUzexTransactionJsonAsync [POST]
- Permission: `TreasBudgetView`
- Return: `IActionResult`

### GetUzexTransactionTableJsonAsync [GET]
- Return: `IActionResult`

### GetUzexReservationOfFundsJsonAsync [POST]
- Permission: `TreasBudgetView`
- Return: `IActionResult`

### GetUzexReservationOfFundsTableJsonAsync [GET]
- Return: `IActionResult`

### GetKafkaLogListAsync [POST]
- Return: `IActionResult`

### GetTableIdsListAsync [GET]
- Return: `IActionResult`

### GetVeoliaData [GET]
- Return: `IActionResult`

### GetSuvsozBalance [GET]
- Return: `IActionResult`

### GetGasInfo [GET]
- Return: `IActionResult`

### GetElectrAccoutInfo [GET]
- Return: `IActionResult`

### GetElectrAccout [GET]
- Return: `IActionResult`

### GetCadastrList [GET]
- Return: `IActionResult`

### GetGarbageBalance [GET]
- Return: `IActionResult`

### BankDocumentByQrCodePrintAsync [POST]
- Return: `IActionResult`

### DownloadBankDocumentAsync [GET]
- Return: `IActionResult`


## IncomeDocumentController
Route: `IncomeDocument/[action]`

### GetListAsync [POST]
- Permission: `IncomeDocumentView`
- Return: `PagedResult<IncomeDocumentListDto>`

### PrintAsync [POST]
- Permission: `IncomeDocumentView`
- Return: `IActionResult`

### PrintActAsync [POST]
- Permission: `IncomeDocumentView`
- Return: `IActionResult`


## IncomeSplitBudgetController
Route: `IncomeSplitBudget/[action]`

### GetListAsync [POST]
- Permission: `IncomeSplitBudgetView`
- Return: `PagedResult<IncomeSplitBudgetListDto>`

### PrintAsync [POST]
- Permission: `IncomeSplitBudgetView`
- Return: `IActionResult`


## IncomeSplitFundController
Route: `IncomeSplitFund/[action]`

### GetListAsync [POST]
- Permission: `IncomeSplitFundView`
- Return: `PagedResult<IncomeSplitFundListDto>`

### PrintAsync [POST]
- Permission: `IncomeSplitFundView`
- Return: `IActionResult`


## InvoiceController
Route: `InvoiceDocument/[action]`

### GetListWithHitoryAsync [POST]
- Permission: `InvoiceDocumentView`
- Return: `InvoiceResultDto`

### GetListAsync [POST]
- Permission: `InvoiceDocumentView`
- Return: `PagedResult<InvoiceListDto>`

### GetFileAsync [GET]
- Permission: `InvoiceDocumentView`
- Return: `IActionResult`

### Get [GET]
- Permission: `InvoiceDocumentView`
- Return: `InvoiceDto`


## EnktController
Route: `Enkt/[action]`

### GetListAsync [POST]
- Permission: `EnktView`
- Return: `PagedResult<EnktListDto>`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EnktCreate`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EnktEdit`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EnktDelete`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини ўчириш


## EnktPropertiesValueController
Route: `EnktPropertiesValue/[action]`

### GetListAsync [POST]
- Permission: `EnktView`
- Return: `PagedResult<EnktPropertiesValueListDto>`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EnktCreate`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EnktEdit`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EnktDelete`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини ўчириш


## EnktPropertyController
Route: `EnktProperty/[action]`

### GetListAsync [POST]
- Permission: `EnktView`
- Return: `PagedResult<EnktPropertyListDto>`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EnktView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EnktCreate`
- Return: `IActionResult`
- Tavsif: ЕНКТ ҳужжатини яратиш


## ChequeController
Route: `Cheque/[action]`

### GetListAsync [POST]
- Permission: `SysChequeView`
- Return: `PagedResult<ChequeListDto>`

### GetAsync [GET]
- Permission: `SysChequeView`
- Return: `IActionResult`

### GetListSyncAsync [POST]
- Permission: `SysChequeView`
- Return: `PagedResult<ChequeListDto>`


## EnergoIncomeController
Route: `EnergoIncome/[action]`

### GetListAsync [POST]
- Permission: `EnergoIncomeView`
- Return: `PagedResult<EnergoIncomeListDto>`

### GetAsync [GET]
- Permission: `EnergoIncomeView`
- Return: `IActionResult`

### Print [POST]
- Permission: `EnergoIncomeView`
- Return: `IActionResult`
- Tavsif: Печать қилиш

### PrintAsync [POST]
- Return: `IActionResult`


## EnergoIncomeGenerController
Route: `EnergoIncomeGener/[action]`

### GetListAsync [POST]
- Permission: `EnergoIncomeGenerView`
- Return: `PagedResult<EnergoIncomeGenerListDto>`

### GetAsync [GET]
- Permission: `SysEnergoIncomeView`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `EnergoIncomeGenerView`
- Return: `IActionResult`
- Tavsif: Печать қилиш


## EnergoOtchisController
Route: `EnergoOtchis/[action]`

### GetListAsync [POST]
- Permission: `EnergoOtchisView`
- Return: `PagedResult<EnergoOtchisListDto>`

### GetAsync [GET]
- Permission: `EnergoOtchisView`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `EnergoOtchisView`
- Return: `IActionResult`
- Tavsif: Печать қилиш


## EnergoPaydocController
Route: `EnergoPaydoc/[action]`

### GetListAsync [POST]
- Permission: `EnergoOtchisView`
- Return: `PagedResult<EnergoPaydocListDto>`

### GetAsync [GET]
- Permission: `EnergoPaydocView`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `EnergoOtchisView`
- Return: `IActionResult`
- Tavsif: Печать қилиш

### PrintGetListAsync [POST]
- Return: `IActionResult`
- Tavsif: Печать қилиш


## KafkaInController
Route: `KafkaIn/[action]`

### GetList [POST]
- Permission: `SysKafkaInView`
- Return: `PagedResult<KafkaInListDto`

### GetAsync [GET]
- Permission: `SysKafkaInView`
- Return: `IActionResult`


## KafkaLogController
Route: `KafkaLog/[action]`

### GetList [POST]
- Return: `PagedResult<KafkaLogListDto>`

### GetAsync [GET]
- Permission: `SysKafkaOutView`
- Return: `IActionResult`


## KafkaOutController
Route: `KafkaOut/[action]`

### GetList [POST]
- Permission: `SysKafkaOutView`
- Return: `PagedResult<KafkaOutListDto`

### GetAsync [GET]
- Permission: `SysKafkaOutView`
- Return: `IActionResult`


## MibExecutionOrgSheetController
Route: `MibExecutionOrgSheet/[action]`

### GetListExecutionOrgSheetAsync [POST]
- Return: `PagedResult<MibExecutionOrgSheetDlDto>`


## TreasBudgetController
Route: `TreasBudget/[action]`

### GetListAsync [POST]
- Permission: `TreasBudgetView`
- Return: `PagedResult<TreasBudgetListDto>`

### GetAsync [GET]
- Permission: `TreasBudgetView`
- Return: `IActionResult`
