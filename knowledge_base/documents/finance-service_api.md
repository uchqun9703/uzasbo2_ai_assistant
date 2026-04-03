# finance-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ChangeFinYearController
Route: `[controller]/[action]`

### ChangeFinYearAsync [POST]
- Permission: `FinYearChange`
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ManualController
Route: `[controller]/[action]`

### GetMoneyMeansMovementKindSelectListAsync [GET]
- Return: `IActionResult`

### GetBudgetTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetPaymentOrderTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetTreasuryMemOrderTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetContractCauseSelectListAsync [GET]
- Return: `IActionResult`

### GetContractCauseTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetContractTypeInfoSelectListAsync [GET]
- Return: `IActionResult`

### GetCommonSelectListAsync [GET]
- Return: `IActionResult`

### GetRestsImportTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetFuelTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetInvoiceListAsync [GET]
- Return: `IActionResult`

### GetSubAccDBListForChangeSubAccAsync [GET]
- Return: `IActionResult`

### GetIhmaInvoiceInfoAsync [GET]
- Return: `IActionResult`

### GetIsCheckedContractorInfoAsync [GET]
- Return: `IActionResult`

### GetIsPinflCheckedContractorInfoAsync [GET]
- Return: `IActionResult`

### GetSubSidiyaContractInfoAsync [GET]
- Return: `IActionResult`

### IsMibPaymentAsync [GET]
- Return: `IActionResult`

### GetMibDocPaymentInfoAsync [GET]
- Return: `IActionResult`

### SendPayAsync [POST]
- Return: `IActionResult`


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


## AdministrativeProtocolController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<AdministrativeProtocolListDto>`

### GetOrCreateDocAsync [POST]
- Return: `AdministrativeProtocolListDto`

### GetOrCreateMibDocAsync [POST]
- Return: `List<AdministrativeProtocolListDto>`

### CheckOrganizationAsync [POST]
- Return: `bool`

### UpdateAsync [POST]
- Return: `IActionResult`

### SignExplanatoryAsync [POST]
- Return: `IActionResult`

### DownloadPdfDocAsync [GET]
- Return: `IActionResult`

### DownloadExplantoryPdfDoc [GET]
- Return: `IActionResult`


## AuctionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AuctionView`
- Return: `PagedResult<AuctionListDto>`

### GetAsync [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AuctionCreate`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `AuctionEdit`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `AuctionDelete`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `AuctionAccept`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `AuctionCancel`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини бекор қилиш

### GetHashAsync [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `AuctionSend`
- Return: `IActionResult`

### CancelSendAsync [POST]
- Permission: `AuctionCancelSend`
- Return: `IActionResult`

### GetList [POST]
- Permission: `AuctionView`
- Return: `PagedResult<AuctionListDto`

### Get [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### Create [POST]
- Permission: `AuctionCreate`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини яратиш

### Update [POST]
- Permission: `AuctionEdit`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `AuctionDelete`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини ўчириш

### Accept [POST]
- Permission: `AuctionAccept`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `AuctionCancel`
- Return: `IActionResult`
- Tavsif: Касса харажати прогнози ҳужжатини бекор қилиш

### GetHash [GET]
- Permission: `AuctionView`
- Return: `IActionResult`

### Send [POST]
- Permission: `AuctionSend`
- Return: `IActionResult`

### CancelSend [POST]
- Permission: `AuctionCancelSend`
- Return: `IActionResult`


## BudgetController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `BudgetView`
- Return: `PagedResult<BudgetListDto>`

### BudgetGetListPowersAsync [GET]
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### BudgetPowersAsync [GET]
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### FillBudgetAsync [POST]
- Permission: `BudgetCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини тўлдириш

### GetAsync [GET]
- Permission: `BudgetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BudgetView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `BudgetCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `BudgetEdit`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `BudgetAccept`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини тасдиқлаш

### ReadyToSendAsync [POST]
- Permission: `BudgetReadyToSend`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини жўнатишга таёрлаш

### CancelReadyToSendAsync [POST]
- Permission: `BudgetCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини жўнатишни бекор қилиш

### GetHashAsync [GET]
- Permission: `BudgetView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `BudgetSend`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини жўнатиш

### CancelAsync [POST]
- Permission: `BudgetCancel`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `BudgetDelete`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `BudgetView`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш

### GetListSentToHeaderAsync [POST]
- Permission: `BudgetSentToHeader`
- Return: `PagedResult<BudgetListDto>`

### GetListSentToHeaderDepartmentAsync [POST]
- Permission: `StaffingViewToDepartment`
- Return: `PagedResult<BudgetRegionDepartmentListDto>`

### ReciveAsync [POST]
- Permission: `BudgetSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `BudgetSentToNotRecive`
- Return: `IActionResult`

### ApprovedAsync [POST]
- Permission: `BudgetSentToApproved`
- Return: `IActionResult`

### AgreedAsync [POST]
- Permission: `BudgetSentToAgreed`
- Return: `IActionResult`

### AgreedFinOrgAsync [POST]
- Permission: `BudgetSentToAgreedFinOrg`
- Return: `IActionResult`

### RegisteredAsync [POST]
- Permission: `BudgetSentToRegistered`
- Return: `IActionResult`


## BudgetRegisteryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `BudgetRegisteryView`
- Return: `PagedResult<BudgetRegisteryListDto>`

### GetByTreasBudgetAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### GetTableAsync [POST]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### GetSentToHeaderDepartmentAsync [GET]
- Permission: `StaffingViewToDepartment`
- Return: `IActionResult`

### GetBudgetAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `BudgetRegisteryCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `BudgetRegisteryEdit`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `BudgetRegisteryAccept`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `BudgetRegisteryCancel`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини бекор қилиш

### ChangeTreasSignOnAsync [POST]
- Permission: `BudgetRegisteryCreate`
- Return: `IActionResult`
- Tavsif: Смета санасини Ғазна санаси га ўзгартириш 

### DeleteAsync [POST]
- Permission: `BudgetRegisteryDelete`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини ўчириш

### FillBudgetRegisteryAsync [POST]
- Permission: `BudgetRegisteryCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини тўлдириш

### ClearTableAsync [POST]
- Permission: `BudgetRegisteryEdit`
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `BudgetRegisterySend`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини жўнатиш

### GetListSentToCenterAsync [POST]
- Permission: `BudgetRegisterySentToCenter`
- Return: `PagedResult<BudgetRegisteryListDto>`

### NotAcceptCenterAsync [POST]
- Permission: `BudgetRegisterySentToCancel`
- Return: `IActionResult`

### PrintAsync [GET]
- Permission: `BudgetRegisteryView`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш

### PrintSentToCenterAsync [GET]
- Permission: `BudgetRegisterySentToCenter`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш

### ApprovedAsync [POST]
- Permission: `BudgetRegisterySentToApproved`
- Return: `IActionResult`

### Registered [POST]
- Permission: `BudgetRegisterySentToRegistered`
- Return: `IActionResult`


## BudgetTotalController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `BudgetTotalView`
- Return: `PagedResult<BudgetTotalListDto>`

### GetAsync [GET]
- Permission: `BudgetTotalView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BudgetTotalView`
- Return: `IActionResult`

### GetForHeaderAsync [GET]
- Permission: `BudgetTotalView`
- Return: `IActionResult`

### GetBudgetAsync [GET]
- Permission: `BudgetTotalView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `BudgetTotalCreate`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини яратиш

### FillBudgetTotalAsync [POST]
- Permission: `BudgetTotalCreate`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини тўлдириш

### ClearTotalTableAsync [POST]
- Permission: `BudgetTotalEdit`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `BudgetTotalEdit`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `BudgetTotalAccept`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини тасдиқлаш

### GetHashAsync [GET]
- Permission: `BudgetTotalView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `BudgetTotalSend`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини жўнатиш

### CancelAsync [POST]
- Permission: `BudgetTotalCancel`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `BudgetTotalDelete`
- Return: `IActionResult`
- Tavsif: Смета йиғиш ҳужжатини ўчириш

### GetListSentToHeaderAsync [POST]
- Permission: `BudgetTotalSentToHeader`
- Return: `PagedResult<BudgetTotalListDto>`

### AcceptHeaderAsync [POST]
- Permission: `BudgetTotalSentToAccept`
- Return: `IActionResult`

### NotAcceptHeaderAsync [POST]
- Permission: `BudgetTotalSentToCancel`
- Return: `IActionResult`

### GetHashToDmbatAsync [GET]
- Permission: `BudgetTotalSentToDmbat`
- Return: `IActionResult`

### SendtoDmbatAsync [POST]
- Permission: `BudgetTotalSentToDmbat`
- Return: `IActionResult`

### ExternalReceiveAsync [POST]
- Return: `IActionResult`

### ApprovedAsync [POST]
- Permission: `BudgetTotalSentToApproved`
- Return: `IActionResult`

### AgreedAsync [POST]
- Permission: `BudgetTotalSentToAgreed`
- Return: `IActionResult`

### AgreedFinOrgAsync [POST]
- Permission: `BudgetTotalSentToAgreedFinOrg`
- Return: `IActionResult`

### RegisteredAsync [POST]
- Permission: `BudgetTotalSentToRegistered`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `BudgetTotalView`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш


## ChequeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChequeView`
- Return: `PagedResult<ChequeListDto>`

### GetAsync [GET]
- Permission: `ChequeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChequeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChequeCreate`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ChequeEdit`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ChequeAccept`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ChequeCancel`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `ChequeDelete`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини ўчириш

### GetHashAsync [GET]
- Permission: `ChequeView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `ChequeSend`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини жўнатиш

### ReadyToSendAsync [POST]
- Permission: `ChequeReadyToSend`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини жўнатишга таёрлаш

### CancelReadyToSendAsync [POST]
- Permission: `CancelReadyToSendCheque`
- Return: `IActionResult`
- Tavsif: Чек ҳужжатини жўнатишни бекор қилиш

### PrintAsync [POST]
- Permission: `ChequeView`
- Return: `IActionResult`


## ChequeWarrantController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChequeWarrantView`
- Return: `PagedResult<ChequeWarrantListDto>`

### GetAsync [GET]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChequeWarrantCreate`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `ChequeWarrantAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `ChequeWarrantCancel`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `ChequeWarrantEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `ChequeWarrantDelete`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `ChequeWarrantSend`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### ExportDocxAsync [GET]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### UploadFileMinIO [POST]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### DeleteFile [POST]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### GetPdf [POST]
- Permission: `ChequeWarrantView`
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `ChequeWarrantReadyToSent`
- Return: `IActionResult`

### CancelReadyToSendAsync [POST]
- Permission: `CancelChequeWarrantReadyToSent`
- Return: `IActionResult`

### ArchiveAsync [POST]
- Permission: `ChequeWarrantSend`
- Return: `IActionResult`


## ContractController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ContractView`
- Return: `PagedResult<ContractListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `ContractView`
- Return: `ContractListWithHistoryDto`

### GetAsync [GET]
- Permission: `ContractView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ContractView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ContractCreate`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ContractEdit`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ContractDelete`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `ContractAccept`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини тасдиқлаш

### CreatePaymentOrder [POST]
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `ContractCancel`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини бекор қилиш

### PrintAsync [GET]
- Permission: `ContractPrint`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини печать қилиш

### FillContractSpecificationFromLotAsync [GET]
- Permission: `ContractCreate`
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `ContractView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `ContractSend`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини жўнатиш

### CancelSendAsync [POST]
- Permission: `ContractCancelSend`
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини жўнатишни бекор қилиш

### ContractByTreasContractAsync [POST]
- Permission: `ContractCreate`
- Return: `IActionResult`

### ContractByTreasContractByIsukAsync [POST]
- Permission: `ContractCreate`
- Return: `IActionResult`

### TestSyncContractAsync [POST]
- Permission: `ContractCreate`
- Return: `IActionResult`

### SyncWithOldContractsAsync [POST]
- Permission: `ContractCreate`
- Return: `IActionResult`

### RequestToSyncAllContractAsync [GET]
- Permission: `ContractCreate`
- Return: `IActionResult`

### CreateByTreasContractByMvd [POST]
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини жўнатиш MVD

### AcceptByMvd [POST]
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини Яратиш ва тасдиқлаш MVD

### CancelByMvd [POST]
- Return: `IActionResult`
- Tavsif: Шартнома ҳужжатини бекор қилиш ва ўчириш MVD


## CurrencyBuyController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurrencyBuyView`
- Return: `PagedResult<CurrencyBuyListDto>`

### GetAsync [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CurrencyBuyCreate`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CurrencyBuyEdit`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CurrencyBuyAccept`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CurrencyBuyCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `CurrencyBuyDelete`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини бекор қилиш

### GetHashAsync [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `CurrencyBuySend`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини жўнатиш

### UploadFileMinIO [POST]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### UploadPdf [POST]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### DownloadPdf [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### DeletePdf [DELETE]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### DownloadMinIOPdf [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`


## CurrencyReappraisalController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurrencyReappraisalView`
- Return: `PagedResult<CurrencyReappraisalListDto>`

### GetAsync [GET]
- Permission: `CurrencyReappraisalView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CurrencyReappraisalView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CurrencyReappraisalCreate`
- Return: `IActionResult`
- Tavsif: Валютани қайта баҳолаш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CurrencyReappraisalEdit`
- Return: `IActionResult`
- Tavsif: Валютани қайта баҳолаш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CurrencyReappraisalAccept`
- Return: `IActionResult`
- Tavsif: Валютани қайта баҳолаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CurrencyReappraisalCancel`
- Return: `IActionResult`
- Tavsif: Валютани қайта баҳолаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `CurrencyReappraisalDelete`
- Return: `IActionResult`
- Tavsif: Валютани қайта баҳолаш ҳужжатини ўчириш


## CurrencySaleController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurrencySaleView`
- Return: `PagedResult<CurrencySaleListDto>`

### GetAsync [GET]
- Permission: `CurrencySaleView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CurrencySaleView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CurrencySaleCreate`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CurrencySaleEdit`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CurrencySaleAccept`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CurrencySaleCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `CurrencySaleDelete`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини бекор қилиш

### GetHashAsync [GET]
- Permission: `CurrencySaleView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `CurrencySaleSend`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини жўнатиш

### UploadFileMinIO [POST]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`

### DownloadMinIOPdf [GET]
- Permission: `CurrencyBuyView`
- Return: `IActionResult`


## ExpenseReportController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ExpenseReportView`
- Return: `PagedResult<ExpenseReportListDto>`

### GetAsync [GET]
- Permission: `ExpenseReportView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ExpenseReportView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ExpenseReportCreate`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини яратиш

### FillTable [POST]
- Permission: `ExpenseReportCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `ExpenseReportEdit`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `ExpenseReportCanCLone`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `ExpenseReportDelete`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `ExpenseReportAccept`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ExpenseReportCancel`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини бекор қилиш

### PrintAsync [POST]
- Permission: `ExpenseReportView`
- Return: `IActionResult`
- Tavsif: Авансовый отчет ҳужжатини печать қилиш


## IncomeCalculationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IncomeCalculationView`
- Return: `PagedResult<IncomeCalculationListDto>`

### GetAsync [GET]
- Permission: `IncomeCalculationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeCalculationView`
- Return: `IActionResult`

### GetByOrgSettlementAccountId [GET]
- Permission: `InPaymentView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeCalculationCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `IncomeCalculationEdit`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `IncomeCalculationSend`
- Return: `IActionResult`

### Accept [POST]
- Permission: `IncomeCalculationAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `IncomeCalculationCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `IncomeCalculationDelete`
- Return: `IActionResult`

### AddIncomeCalculation [POST]
- Return: `IActionResult`

### UpdateIncomeCalculation [POST]
- Return: `IActionResult`


## InPaymentController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `InPaymentView`
- Return: `PagedResult<InPaymentListDto>`

### Get [GET]
- Permission: `InPaymentView`
- Return: `IActionResult`

### Get [GET]
- Permission: `InPaymentView`
- Return: `IActionResult`

### GetByOrgSettlementAccountId [POST]
- Permission: `InPaymentView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### UpdateIsRepayment [POST]
- Permission: `InPaymentEdit`
- Return: `IActionResult`

### UpdateIsTransit [POST]
- Permission: `InPaymentEdit`
- Return: `IActionResult`

### Create [POST]
- Permission: `InPaymentCreate`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини яратиш

### Update [POST]
- Permission: `InPaymentEdit`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини таҳрирлаш

### GetClone [GET]
- Permission: `InPaymentCanCLone`
- Return: `IActionResult`

### Accept [POST]
- Permission: `InPaymentAccept`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `InPaymentCancel`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `InPaymentDelete`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини ўчириш

### UpdateRjPosition [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`

### ImportByBankDocument [GET]
- Permission: `InPaymentCreate`
- Return: `IActionResult`

### Print [POST]
- Permission: `InPaymentView`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини печать қилиш

### Refresh [POST]
- Permission: `InPaymentCreate`
- Return: `IActionResult`

### Refresh [GET]
- Permission: `InPaymentCreate`
- Return: `IActionResult`


## InvoiceController
Route: `InvoiceDocument/[action]`

### SendToKafka [POST]
- Permission: `InvoiceDocumentView`
- Return: `SendToKafkaResultDto`


## MonthlyAllocationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `MonthlyAllocationView`
- Return: `PagedResult<MonthlyAllocationListDto>`

### GetAsync [GET]
- Permission: `MonthlyAllocationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `MonthlyAllocationView`
- Return: `IActionResult`

### GetListStaffingTableAsync [POST]
- Permission: `MonthlyAllocationView`
- Return: `PagedResult<MonthlyAllocationStaffingTableDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### FillAsync [POST]
- Permission: `MonthlyAllocationCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### ClearTableAsync [POST]
- Permission: `MonthlyAllocationEdit`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `MonthlyAllocationCreate`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `MonthlyAllocationEdit`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `MonthlyAllocationAccept`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `MonthlyAllocationCancel`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `MonthlyAllocationDelete`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини ўчириш

### Print [POST]
- Permission: `MonthlyAllocationView`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш


## PaymentCurrencyController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PaymentCurrencyView`
- Return: `PagedResult<PaymentCurrencyListDto>`

### GetAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PaymentCurrencyCreate`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PaymentCurrencyEdit`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PaymentCurrencyAccept`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentCurrencyCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини бекор қилиш

### SendAsync [POST]
- Permission: `PaymentCurrencySend`
- Return: `IActionResult`
- Tavsif: Чет эл валютасини сотиш ҳужжатини жўнатиш

### GetHashAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### GetChargePaidByList [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### GetPaymentOfSourceAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### GetTermsPaymentAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### GetFundsOfSourceAsync [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### DownloadMinIOPdf [GET]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### UploadFileMinIO [POST]
- Permission: `PaymentCurrencyView`
- Return: `IActionResult`

### PrintPaymentCurrency [POST]
- Return: `IActionResult`


## PaymentForecastController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PaymentForecastView`
- Return: `PagedResult<PaymentForecastListDto>`

### GetAsync [GET]
- Permission: `PaymentForecastView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PaymentForecastView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PaymentForecastCreate`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PaymentForecastEdit`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини таҳрирлаш

### CreateMvdCassaPlanAsync [POST]
- Permission: `PaymentForecastEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `PaymentForecastAccept`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentForecastCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PaymentForecastDelete`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини бекор қилиш

### GetHashAsync [GET]
- Permission: `PaymentForecastView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `PaymentForecastSend`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини жўнатиш

### GetCloneAsync [GET]
- Permission: `PaymentForecastCreate`
- Return: `IActionResult`

### CancelSendAsync [POST]
- Permission: `PaymentForecastCancelSend`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини жўнатишни бекор қилиш

### UpdateArchivedAsync [POST]
- Permission: `PaymentForecastEdit`
- Return: `IActionResult`
- Tavsif: Пул воситалари тушуми ҳужжатини архивлаш

### Print [POST]
- Permission: `PaymentForecastPrint`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш

### PrintAsync [POST]
- Permission: `PaymentForecastPrint`
- Return: `IActionResult`
- Tavsif: Смета ҳужжатини печать қилиш


## PaymentOrderController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PaymentOrderView`
- Return: `PagedResult<PaymentOrderListDto>`

### ClearAsync [POST]
- Permission: `PaymentOrderCreate`
- Return: `IActionResult`

### FillTrip [POST]
- Permission: `PaymentOrderCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### GetListForCentralOrganizationAsync [POST]
- Permission: `PaymentOrderViewCentralizedSended`
- Return: `PagedResult<SentPaymentOrderListDto>`

### GetListForHeaderOrganizationAsync [POST]
- Permission: `PaymentOrderViewHeaderOrganizationSended`
- Return: `PagedResult<PaymentOrderListDto>`

### ReportAcceptedAsync [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### NotReportAcceptedAsync [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetByOrgSettlementAccountIdAsync [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PaymentOrderCreate`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини яратиш

### CreateMvdPaymentOrderAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PaymentOrderAccept`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentOrderCancel`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PaymentOrderDelete`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини ўчириш

### GetHashAsync [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### SendMib [POST]
- Return: `IActionResult`

### GetInvoiceCheckAsync [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `PaymentOrderSend`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини жўнатиш

### GetCloneAsync [GET]
- Permission: `PaymentOrderCreate`
- Return: `IActionResult`

### UpdateFinanceYearAsync [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`

### UpdateIsRepaymentAsync [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`

### UpdateRjPosition [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`

### UpdateIsTransitAsync [POST]
- Permission: `PaymentOrderEdit`
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `PaymentOrderReadyToSend`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини жўнатишга таёрлаш

### CancelReadyToSendAsync [POST]
- Permission: `PaymentOrderCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини жўнатишни бекор қилиш

### Print [GET]
- Permission: `PaymentOrderPrint`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини печать қилиш

### PrintGetList [POST]
- Return: `IActionResult`

### PrintGetListForCentralOrganization [POST]
- Return: `IActionResult`

### GetZpPayrollSheetListAsync [GET]
- Return: `IActionResult`

### CancelSendAsync [POST]
- Permission: `PaymentOrderCancelSend`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини жўнатишни бекор қилиш

### ChangeSubAccPaymentOrderAsync [POST]
- Permission: `PaymentOrderUpdateSubAcc`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини тасдиқлаш

### RefreshToBillingPaymentOrder [POST]
- Permission: `PaymentOrderView`
- Return: `ActionResult`
- Tavsif: Платежное поручение ҳужжатини тасдиқлаш

### GetListForChequeAsync [POST]
- Return: `PagedResult<PaymentOrderListDto>`

### ControlOrganizationSettlementAccountSelectListAsync [GET]
- Return: `IActionResult`


## PaymentRegistryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PaymentRegistryView`
- Return: `PagedResult<PaymentRegistryListDto>`

### GetAsync [GET]
- Permission: `PaymentRegistryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PaymentRegistryView`
- Return: `IActionResult`

### GetByOrgSettlementAccountIdAsync [GET]
- Permission: `PaymentRegistryCreate`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PaymentRegistryCreate`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PaymentRegistryEdit`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PaymentRegistryAccept`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentRegistryCancel`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PaymentRegistryDelete`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини ўчириш

### PrintAsync [GET]
- Permission: `PaymentRegistryPrint`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини печать қилиш

### FillTableAsync [POST]
- Permission: `PaymentRegistryCreate`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `PaymentRegistryCreate`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини тозалаш

### GetHashAsync [GET]
- Permission: `PaymentRegistryView`
- Return: `IActionResult`

### GetInvoiceCheckAsync [GET]
- Permission: `PaymentRegistryView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `PaymentRegistrySend`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `PaymentRegistryCreate`
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `PaymentRegistryReadyToSend`
- Return: `IActionResult`

### CancelReadyToSendAsync [POST]
- Permission: `PaymentRegistryCancelReadyToSend`
- Return: `IActionResult`

### PrintOrgsAsync [GET]
- Permission: `PaymentRegistryPrint`
- Return: `IActionResult`
- Tavsif: Тўлов топшириқнома(Реестр) ҳужжатини печать қилиш


## ProcurementPlanController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ProcurementPlanView`
- Return: `PagedResult<ProcurementPlanListDto>`

### GetAsync [GET]
- Permission: `ProcurementPlanView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ProcurementPlanView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `ProcurementPlanView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ProcurementPlanCreate`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ProcurementPlanEdit`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ProcurementPlanAccept`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ProcurementPlanCancel`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини бекор қилиш

### SendAsync [POST]
- Permission: `IncomeCalculationSend`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини жўнатиш

### DeleteAsync [POST]
- Permission: `ProcurementPlanDelete`
- Return: `IActionResult`
- Tavsif: Харид қилиш режаси ҳужжатини ўчириш


## RestsByAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RestsByAccountView`
- Return: `PagedResult<RestsByAccountListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `RestsByAccountView`
- Return: `RestsByAccountListWithHistoryDto`

### GetAsync [GET]
- Permission: `RestsByAccountView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestsByAccountView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestsByAccountCreate`
- Return: `IActionResult`
- Tavsif: Субсчетлар бўйича қолдиқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestsByAccountEdit`
- Return: `IActionResult`
- Tavsif: Субсчетлар бўйича қолдиқ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RestsByAccountDelete`
- Return: `IActionResult`
- Tavsif: Субсчетлар бўйича қолдиқ ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `RestsByAccountAccept`
- Return: `IActionResult`
- Tavsif: Субсчетлар бўйича қолдиқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestsByAccountCancel`
- Return: `IActionResult`
- Tavsif: Субсчетлар бўйича қолдиқ ҳужжатини бекор қилиш

### SyncWithBillingRestByAccountByStudent [POST]
- Permission: `RestsByAccountCreate`
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### ClearTableAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### ClearImportsAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### SyncRestsByAccountImportsAsync [GET]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### GetStudentInfoAsync [POST]
- Permission: `RestsByAccountView`
- Return: `IActionResult`

### PrintAsync [GET]
- Permission: `RestByPermanentAssetView`
- Return: `IActionResult`
- Tavsif: Остаток по счетам бўйича қолдиқ ҳужжатини печать қилиш


## RestsByContractorController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RestsByContractorView`
- Return: `PagedResult<RestsByContractorListDto>`

### GetAsync [GET]
- Permission: `RestsByContractorView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestsByContractorView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestsByContractorCreate`
- Return: `IActionResult`
- Tavsif: Ташкилотлар бўйича қолдиқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestsByContractorEdit`
- Return: `IActionResult`
- Tavsif: Ташкилотлар бўйича қолдиқ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RestsByContractorDelete`
- Return: `IActionResult`
- Tavsif: Ташкилотлар бўйича қолдиқ ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `RestsByContractorAccept`
- Return: `IActionResult`
- Tavsif: Ташкилотлар бўйича қолдиқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestsByContractorCancel`
- Return: `IActionResult`
- Tavsif: Ташкилотлар бўйича қолдиқ ҳужжатини бекор қилиш


## RestsByEmployeeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RestsByEmployeeView`
- Return: `PagedResult<RestsByEmployeeListDto>`

### GetAsync [GET]
- Permission: `RestsByEmployeeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestsByEmployeeView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestsByEmployeeCreate`
- Return: `IActionResult`
- Tavsif: Ҳодимлар бўйича қолдиқ қолдиқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestsByEmployeeEdit`
- Return: `IActionResult`
- Tavsif: Ҳодимлар бўйича қолдиқ қолдиқ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RestsByEmployeeDelete`
- Return: `IActionResult`
- Tavsif: Ҳодимлар бўйича қолдиқ қолдиқ ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `RestsByEmployeeAccept`
- Return: `IActionResult`
- Tavsif: Ҳодимлар бўйича қолдиқ қолдиқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestsByEmployeeCancel`
- Return: `IActionResult`
- Tavsif: Ҳодимлар бўйича қолдиқ қолдиқ ҳужжатини бекор қилиш


## RestsBySettlementAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RestsBySettlementAccountView`
- Return: `PagedResult<RestsBySettlementAccountListDto>`

### GetAsync [GET]
- Permission: `RestsBySettlementAccountView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestsBySettlementAccountView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestsBySettlementAccountCreate`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestsBySettlementAccountEdit`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RestsBySettlementAccountDelete`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `RestsBySettlementAccountAccept`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestsBySettlementAccountCancel`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини бекор қилиш

### FillTableAsync [POST]
- Permission: `RestsBySettlementAccountCreate`
- Return: `IActionResult`
- Tavsif: ШҒҲ бўйича қолдиқ ҳужжатини толдириш

### GetRestsByDebitAmountAsync [POST]
- Permission: `RestsBySettlementAccountCreate`
- Return: `IActionResult`


## ReturnIncomeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ReturnIncomeView`
- Return: `PagedResult<ReturnIncomeListDto>`

### GetAsync [GET]
- Permission: `ReturnIncomeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ReturnIncomeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Permission: `ReturnIncomeView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ReturnIncomeCreate`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ReturnIncomeEdit`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ReturnIncomeDelete`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `ReturnIncomeAccept`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини тасдиқлаш

### GetHashAsync [GET]
- Permission: `ReturnIncomeView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `ReturnIncomeSend`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини жўнатиш

### ReadyToSendAsync [POST]
- Permission: `ReturnIncomeReadyToSend`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини жўнатишга таёрлаш

### CancelSendAsync [POST]
- Permission: `ReturnIncomeCancelSend`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини бекор қилиш

### CancelReadyToSendAsync [POST]
- Permission: `ReturnIncomeCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Платежное поручение ҳужжатини жўнатишни бекор қилиш

### PrintAsync [POST]
- Permission: `ReturnIncomePrint`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини печать қилиш

### CancelAsync [POST]
- Permission: `ReturnIncomeCancel`
- Return: `IActionResult`
- Tavsif: Ортиқча тўловларни қайтариш ҳулосаси ҳужжатини жўнатишни бекор қилиш


## WriteoffCostServiceController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `WriteoffCostServiceView`
- Return: `PagedResult<WriteoffCostServiceListDto>`

### GetAsync [GET]
- Permission: `WriteoffCostServiceView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `WriteoffCostServiceView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `WriteoffCostServiceCreate`
- Return: `IActionResult`
- Tavsif: Бажарилган иш ва хизматлар таннархини ҳисобдан чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `WriteoffCostServiceEdit`
- Return: `IActionResult`
- Tavsif: Бажарилган иш ва хизматлар таннархини ҳисобдан чиқариш ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `WriteoffCostServiceDelete`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `WriteoffCostServiceCanCLone`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `WriteoffCostServiceCancel`
- Return: `IActionResult`
- Tavsif: Бажарилган иш ва хизматлар таннархини ҳисобдан чиқариш ҳужжатини бекор қилиш


## WriteoffServiceController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `WriteoffServiceView`
- Return: `PagedResult<WriteoffServiceListDto>`

### GetAsync [GET]
- Permission: `WriteoffServiceView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `WriteoffServiceView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `WriteoffServiceView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `WriteoffServiceCreate`
- Return: `IActionResult`
- Tavsif: Бажарилган ишлар далолатномаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `WriteoffServiceEdit`
- Return: `IActionResult`
- Tavsif: Бажарилган ишлар далолатномаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `WriteoffServiceDelete`
- Return: `IActionResult`
- Tavsif: Бажарилган ишлар далолатномаси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `WriteoffServiceAccept`
- Return: `IActionResult`
- Tavsif: Бажарилган ишлар далолатномаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `WriteoffServiceCancel`
- Return: `IActionResult`
- Tavsif: Бажарилган ишлар далолатномаси ҳужжатини бекор қилиш

### GetSellerFacturaInfoAsync [GET]
- Return: `IActionResult`


## ErpRejectedDocumentController
Route: `[controller]/[action]`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetListAsync [POST]
- Return: `PagedResult<ErpRejectedDocumentListDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ErpRejectedDocumentCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`

### AcceptAsync [POST]
- Return: `IActionResult`

### CancelAsync [POST]
- Return: `IActionResult`

### PrintGetSentMessagesAsync [POST]
- Return: `IActionResult`

### GetSentMessagesAsync [POST]
- Permission: `ErpRejectedDocumentSentView`
- Return: `PagedResult<ErpRejectedDocumentListDto>`

### GetSentAsync [GET]
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `ChequeView`
- Return: `IActionResult`

### SendAsync [POST]
- Return: `IActionResult`
- Tavsif: Erp ҳужжатини жўнатиш

### ConsideredAsync [POST]
- Return: `IActionResult`

### UnderConsiderationAsync [POST]
- Return: `IActionResult`

### UpdateTreasDetailsAsync [POST]
- Return: `IActionResult`


## ContractorController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ContractorView`
- Return: `DbPagedModel<ContractorGetListDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetByInnAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ContractorView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ContractorCreate`
- Return: `IActionResult`
- Tavsif: Контрагент яратиш

### Create [POST]
- Permission: `ContractorCreate`
- Return: `IActionResult`
- Tavsif: Контрагент яратиш

### UpdateAsync [POST]
- Permission: `ContractorEdit`
- Return: `IActionResult`
- Tavsif: Контрагентни таҳрирлаш

### DeleteAsync [POST]
- Permission: `ContractorDelete`
- Return: `IActionResult`
- Tavsif: Контрагентни ўчириш

### UpdateNetDocAsync [POST]
- Permission: `ContractorCreate`
- Return: `IActionResult`
- Tavsif: Контрагентни таҳрирлаш

### SyncContractorSetllementAccountInfoAsync [POST]
- Permission: `ContractorCreate`
- Return: `IActionResult`
- Tavsif: Контрагент ҳисоб-рақамлари маълумотларини синхронизациялаш

### CreateContractByLotAsync [POST]
- Permission: `ContractorCreate`
- Return: `IActionResult`
- Tavsif: Контрагентни яратиш (лот бўйича)


## ContractorSettlementAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ContractorSettlementAccountView`
- Return: `PagedResult<ContractorSettlementAccountListDto>`

### GetAsync [GET]
- Permission: `ContractorSettlementAccountView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ContractorSettlementAccountView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetContractorAccountList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ContractorSettlementAccountCreate`
- Return: `IActionResult`
- Tavsif: Доcументларда молия йилини ўзгартириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ContractorSettlementAccountEdit`
- Return: `IActionResult`
- Tavsif: Доcументларда молия йилини ўзгартириш ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ContractorSettlementAccountDelete`
- Return: `IActionResult`
- Tavsif: Доcументларда молия йилини ўзгартириш ҳужжатини ўчириш

### UpdateTreas [POST]
- Return: `IActionResult`


## IncomeSettlementAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IncomeSettlementAccountView`
- Return: `PagedResult<IncomeSettlementAccountListDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeSettlementAccountView`
- Return: `IActionResult`

### GetAsSelectDBListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeSettlementAccountCreate`
- Return: `IActionResult`
- Tavsif: Статья расходов ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `IncomeSettlementAccountEdit`
- Return: `IActionResult`
- Tavsif: Статья расходов ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `IncomeSettlementAccountDelete`
- Return: `IActionResult`
- Tavsif: Статья расходов ҳужжатини ўчириш


## InfoContractorExceptController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<ContractorExceptListDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `InfoContractorExceptCreate`
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`


## ItemOfExpenseController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ItemOfExpenseView`
- Return: `PagedResult<ItemOfExpenseListDto>`

### GetAsync [GET]
- Permission: `ItemOfExpenseView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ItemOfExpenseView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### GetAsSelectListNoAssetAsync [POST]
- Return: `IActionResult`

### GetAsSelectChildListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ItemOfExpenseCreate`
- Return: `IActionResult`
- Tavsif: Даромад ШҒҲ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ItemOfExpenseEdit`
- Return: `IActionResult`
- Tavsif: Даромад ШҒҲ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ItemOfExpenseDelete`
- Return: `IActionResult`
- Tavsif: Даромад ШҒҲ ҳужжатини ўчириш


## MoneyMeansMovementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `MoneyMeansMovementView`
- Return: `PagedResult<MoneyMeansMovementListDto>`

### GetAsync [GET]
- Permission: `MoneyMeansMovementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `MoneyMeansMovementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `MoneyMeansMovementCreate`
- Return: `IActionResult`
- Tavsif: Пул воситалари ҳаракати ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `MoneyMeansMovementEdit`
- Return: `IActionResult`
- Tavsif: Пул воситалари ҳаракати ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `MoneyMeansMovementDelete`
- Return: `IActionResult`
- Tavsif: Пул воситалари ҳаракати ҳужжатини ўчириш


## OperDateController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `OperDateView`
- Return: `PagedResult<OperDateListDto>`

### GetAsync [GET]
- Permission: `OperDateView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OperDateView`
- Return: `IActionResult`

### GetCurrentAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OperDateCreate`
- Return: `IActionResult`
- Tavsif: Амалиёт вақти ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OperDateEdit`
- Return: `IActionResult`
- Tavsif: Амалиёт вақти ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OperDateDelete`
- Return: `IActionResult`
- Tavsif: Амалиёт вақти ҳужжатини ўчириш


## OutOfBalansBranchController
Route: `[controller]/[action]`


## DmbatIncomeCalculationController
Route: `[controller]/[action]`

### ReceiveAsync [POST]
- Return: `IActionResult`


## InternalController
Route: `[controller]/[action]`

### GetByInnInternalAsync [GET]
- Return: `IActionResult`

### SendChequeWarrant [POST]
- Return: `IActionResult`


## SoliqHelperController
Route: `[controller]/[action]`

### GetOrganizationAccounts [GET]
- Return: `IActionResult`

### GetVillages [GET]
- Return: `IActionResult`


## UzasboHelperController
Route: `[controller]/[action]`

### ReceiveOperDateAsync [POST]
- Return: `IActionResult`
