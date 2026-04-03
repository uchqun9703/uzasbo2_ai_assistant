# adm-service — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ManualController
Route: `Manual/[action]`

### GetPermissionSelectList [GET]
- Return: `IEnumerable<PermissionGroupSelectListDto`

### GetBankCodeSelectListAsync [GET]
- Return: `IActionResult`

### GetFinancingLevelSelectListAsync [GET]
- Return: `IActionResult`

### GetAppMessageTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetFileExtensionSelectListAsync [GET]
- Return: `IActionResult`

### GetMfyTypeSelectListAsync [GET]
- Return: `IActionResult`

### UserHeaderOrganizationSelectListAsync [GET]
- Return: `IActionResult`

### OrgSettlementSourceSelectListAsync [GET]
- Return: `IActionResult`

### GetOrganizationalStructureTypeAsync [GET]
- Return: `IActionResult`

### GetReportRecipientTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetSettlementAccountTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetStaffingTableTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetOrganizationFinancingTypeSelectList [GET]
- Return: `IActionResult`

### GetIntegrationTypeSelectList [GET]
- Return: `IActionResult`

### GetSysteamTypeSelectList [GET]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetOrganizationUsersAsync [POST]
- Permission: `OrganizationUsersView`
- Return: `DbPagedModel<GetOrganizationUsersDto>`

### PrintOrganizationUsersAsync [POST]
- Return: `IActionResult`

### GetRegistredUsersByOrganizationAsync [POST]
- Permission: `RegistredUsersByOrganizationView`
- Return: `DbPagedModel<GetRegistredUsersByOrganizationDto>`


## ControlController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ControlView`
- Return: `PagedResult<ControlListDto>`

### GetAsync [GET]
- Permission: `ControlView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ControlView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ControlCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `ControlEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `ControlAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `ControlCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `ControlDelete`
- Return: `IActionResult`

### UploadFileAsync [POST]
- Return: `IActionResult`

### DownloadFileAsync [GET]
- Return: `IActionResult`

### DeleteFileAsync [POST]
- Return: `IActionResult`


## DefectFindingController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<DefectFindingListDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DefectFindingEdit`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `DefectFindingDelete`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини ўчириш


## AnnouncementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AnnouncementView`
- Return: `PagedResult<AnnouncementListDto>`

### GetAsync [GET]
- Permission: `AnnouncementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AnnouncementView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AnnouncementCreate`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `AnnouncementEdit`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `AnnouncementDelete`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини ўчириш


## BankController
Route: `Bank/[action]`

### GetListAsync [POST]
- Permission: `BankView`
- Return: `PagedResult<BankListDto>`

### GetAsync [GET]
- Permission: `BankView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BankView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `BankCreate`
- Return: `IActionResult`
- Tavsif: Банк ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `BankEdit`
- Return: `IActionResult`
- Tavsif: Банк ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `BankDelete`
- Return: `IActionResult`
- Tavsif: Банк ҳужжатини ўчириш


## CameralController
Route: `Cameral/[action]`

### GetListAsync [POST]
- Permission: `CameralView`
- Return: `PagedResult<CameralListDto>`

### GetAsync [GET]
- Permission: `CameralView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CameralView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CameralCreate`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CameralEdit`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `CameralDelete`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини ўчириш

### CreateCalcKindTableAsync [POST]
- Permission: `CameralCreate`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `CameralEdit`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини таҳрирлаш

### DeleteTableAsync [POST]
- Permission: `CameralDelete`
- Return: `IActionResult`
- Tavsif: Камерал ҳужжатини таҳрирлаш

### GetCameralOrgAsync [POST]
- Permission: `OrganizationView`
- Return: `IActionResult`

### UploadFromExcelAsync [POST]
- Return: `IActionResult`
- Tavsif: Камерал фойдаланувчига эхселдан ташкилот бириктириш !


## ControlStructureController
Route: `ControlStructure/[action]`

### GetListAsync [POST]
- Permission: `ControlStructureView`
- Return: `PagedResult<ControlStructureListDto>`

### PrintControlStructureAsync [POST]
- Permission: `ControlStructureView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ControlStructureView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ControlStructureView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Permission: `HeaderOrganizationView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ControlStructureCreate`
- Return: `IActionResult`
- Tavsif: Фойдаланувчига класс бириктириш яратиш

### UpdateAsync [POST]
- Permission: `ControlStructureEdit`
- Return: `IActionResult`
- Tavsif: Фойдаланувчига класс бириктириш таҳрирлаш

### DeleteAsync [POST]
- Permission: `ControlStructureDelete`
- Return: `IActionResult`
- Tavsif: Фойдаланувчига класс бириктириш ўчириш


## CountryController
Route: `Country/[action]`

### GetListTest [GET]
- Return: `IActionResult`

### GetListAsync [POST]
- Permission: `CountryView`
- Return: `PagedResult<CountryListDto>`

### GetAsync [GET]
- Permission: `CountryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CountryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CountryCreate`
- Return: `IActionResult`
- Tavsif: Давлат ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CountryEdit`
- Return: `IActionResult`
- Tavsif: Давлат ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `CountryDelete`
- Return: `IActionResult`
- Tavsif: Давлат ҳужжатини ўчириш


## CurrencyController
Route: `Currency/[action]`

### GetListAsync [POST]
- Permission: `CurrencyView`
- Return: `PagedResult<CurrencyListDto>`

### GetAsync [GET]
- Permission: `CurrencyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CurrencyView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Permission: `CurrencyView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CurrencyCreate`
- Return: `IActionResult`
- Tavsif: Валюта ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CurrencyEdit`
- Return: `IActionResult`
- Tavsif: Валюта ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `CurrencyDelete`
- Return: `IActionResult`
- Tavsif: Валюта ҳужжатини ўчириш


## CurrencyRateController
Route: `CurrencyRate/[action]`

### GetListAsync [POST]
- Permission: `CurrencyRateView`
- Return: `PagedResult<CurrencyRateListDto>`

### GetAsync [GET]
- Permission: `CurrencyRateView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CurrencyRateView`
- Return: `IActionResult`

### GetCurrencyRateAsync [GET]
- Permission: `CurrencyRateView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Permission: `CurrencyRateView`
- Return: `IActionResult`

### SyncWithCbuAsync [POST]
- Permission: `CurrencyRateSync`
- Return: `IActionResult`

### SyncWithCbuByDateAsync [POST]
- Permission: `CurrencyRateSync`
- Return: `IActionResult`

### Create [POST]
- Permission: `CurrencyRateCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `CurrencyRateEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `CurrencyRateDelete`
- Return: `IActionResult`


## DistrictCategoryController
Route: `DistrictCategory/[action]`

### GetListAsync [POST]
- Permission: `DistrictView`
- Return: `PagedResult<DistrictCategoryListDto>`

### GetAsync [GET]
- Permission: `DistrictView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DistrictView`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DistrictView`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `DistrictView`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини ўчириш


## DistrictController
Route: `District/[action]`

### GetListAsync [POST]
- Permission: `DistrictView`
- Return: `PagedResult<DistrictListDto>`

### GetAsync [GET]
- Permission: `DistrictView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DistrictView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListTreasCodeAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DistrictCreate`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DistrictEdit`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `DistrictDelete`
- Return: `IActionResult`
- Tavsif: Туман ҳужжатини ўчириш


## FunctionalItemOfExpenseController
Route: `FunctionalItemOfExpense/[action]`

### GetListAsync [POST]
- Permission: `FunctionalItemOfExpenseView`
- Return: `PagedResult<FunctionalItemOfExpenseListDto>`

### GetAsync [GET]
- Permission: `FunctionalItemOfExpenseView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FunctionalItemOfExpenseView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetGroupAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FunctionalItemOfExpenseCreate`
- Return: `IActionResult`
- Tavsif: Ҳаражатларнинг функционал таснифи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FunctionalItemOfExpenseEdit`
- Return: `IActionResult`
- Tavsif: Ҳаражатларнинг функционал таснифи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `FunctionalItemOfExpenseDelete`
- Return: `IActionResult`
- Tavsif: Ҳаражатларнинг функционал таснифи ҳужжатини ўчириш

### IsActualExpense [POST]
- Permission: `FunctionalItemOfExpenseView`
- Return: `IActionResult`

### IsCashExpense [POST]
- Permission: `FunctionalItemOfExpenseView`
- Return: `IActionResult`


## HeaderOrganizationController
Route: `HeaderOrganization/[action]`

### GetListAsync [POST]
- Permission: `HeaderOrganizationView`
- Return: `PagedResult<HeaderOrganizationListDto>`

### PrintHeaderOrganizationAsync [POST]
- Permission: `HeaderOrganizationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `HeaderOrganizationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `HeaderOrganizationView`
- Return: `IActionResult`

### GetByChildAsync [GET]
- Return: `IActionResult`

### GetByInnAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Permission: `HeaderOrganizationView`
- Return: `IActionResult`

### GetUsersAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `HeaderOrganizationCreate`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `HeaderOrganizationEdit`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `HeaderOrganizationDelete`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот ҳужжатини ўчириш


## IncomeUncController
Route: `IncomeUnc/[action]`

### GetListTestAsync [GET]
- Return: `IActionResult`

### GetListAsync [POST]
- Permission: `IncomeUncView`
- Return: `PagedResult<IncomeUncListDto>`

### GetAsync [GET]
- Permission: `IncomeUncView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeUncView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeUncCreate`
- Return: `IActionResult`
- Tavsif: УНС кодлари маълумоти ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `IncomeUncEdit`
- Return: `IActionResult`
- Tavsif: УНС кодлари маълумоти ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `IncomeUncDelete`
- Return: `IActionResult`
- Tavsif: УНС кодлари маълумоти ҳужжатини ўчириш


## IntegrationServiceController
Route: `[controller]/[action]`

### GetList [GET]
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`


## MfyController
Route: `Mfy/[action]`

### GetListAsync [POST]
- Permission: `MfyView`
- Return: `PagedResult<MfyListDto>`

### GetAsync [GET]
- Permission: `MfyView`
- Return: `IActionResult`

### GetHistoryListAsync [POST]
- Permission: `MfyView`
- Return: `IEnumerable<MfyHistoryListDto>`

### GetAsync [GET]
- Permission: `MfyView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `MfyCreate`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `MfyEdit`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `MfyDelete`
- Return: `IActionResult`
- Tavsif: Ма?алла фу?аролар йи?ини ҳужжатини ўчириш


## NationalityController
Route: `Nationality/[action]`

### GetListTest [GET]
- Return: `IActionResult`

### GetListAsync [POST]
- Permission: `NationalityView`
- Return: `PagedResult<NationalityListDto>`

### GetAsync [GET]
- Permission: `NationalityView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `NationalityView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `NationalityCreate`
- Return: `IActionResult`
- Tavsif: Миллати ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `NationalityEdit`
- Return: `IActionResult`
- Tavsif: Миллати ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `NationalityDelete`
- Return: `IActionResult`
- Tavsif: Миллати ҳужжатини ўчириш


## NumberController
Route: `Number/[action]`

### GetNextDocNumberAsync [GET]
- Return: `IActionResult`

### SaveNumberAsync [POST]
- Return: `IActionResult`


## OkedController
Route: `Oked/[action]`

### GetListAsync [POST]
- Permission: `OkedView`
- Return: `PagedResult<OkedListDto>`

### GetAsync [GET]
- Permission: `OkedView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OkedView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OkedCreate`
- Return: `IActionResult`
- Tavsif: ИФУТ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OkedEdit`
- Return: `IActionResult`
- Tavsif: ИФУТ ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OkedDelete`
- Return: `IActionResult`
- Tavsif: ИФУТ ҳужжатини ўчириш


## OrganizationActivityTypeController
Route: `OrganizationActivityType/[action]`

### GetListAsync [POST]
- Permission: `OrganizationActivityTypeView`
- Return: `PagedResult<OrganizationActivityTypeListDto>`

### GetAsync [GET]
- Permission: `OrganizationActivityTypeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationActivityTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationActivityTypeCreate`
- Return: `IActionResult`
- Tavsif: Ташкилот фаолият тури ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationActivityTypeEdit`
- Return: `IActionResult`
- Tavsif: Ташкилот фаолият тури ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OrganizationActivityTypeDelete`
- Return: `IActionResult`
- Tavsif: Ташкилот фаолият тури ҳужжатини ўчириш


## OrganizationalClassificationController
Route: `OrganizationalClassification/[action]`

### GetListAsync [POST]
- Permission: `OrganizationalClassificationView`
- Return: `PagedResult<OrganizationalClassificationListDto>`

### GetAsync [GET]
- Permission: `OrganizationalClassificationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationalClassificationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationalClassificationCreate`
- Return: `IActionResult`
- Tavsif: Ташкилот функционал таснифи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationalClassificationEdit`
- Return: `IActionResult`
- Tavsif: Ташкилот функционал таснифи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OrganizationalClassificationDelete`
- Return: `IActionResult`
- Tavsif: Ташкилот функционал таснифи ҳужжатини ўчириш


## OrganizationalStructureController
Route: `OrganizationalStructure/[action]`

### GetListAsync [POST]
- Permission: `OrganizationalStructureView`
- Return: `PagedResult<OrganizationalStructureListDto>`

### GetListForUserAsync [POST]
- Permission: `AppointEmployeeSalaryView`
- Return: `PagedResult<OrganizationalStructureListDto>`

### GetPositionListAsync [POST]
- Return: `PagedResult<OrganizationalStructureStaffingPositionListDto>`

### GetOrganizationCountAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetAllPositionListAsync [GET]
- Permission: `StaffingCreate`
- Return: `IActionResult`

### GetPositionListAsync [GET]
- Permission: `PositionSubstitutionCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetForUserAsync [GET]
- Permission: `AppointEmployeeSalaryView`
- Return: `IActionResult`

### GetForUser2Async [GET]
- Permission: `AppointEmployeeSalaryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetStructureNameAsync [GET]
- Return: `IActionResult`

### GetCorrCoefAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationalStructureCreate`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OrganizationalStructureDelete`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини ўчириш

### PrintOrganizationStructureAsync [GET]
- Return: `IActionResult`

### PrintOrganizationalStructureListAsync [POST]
- Return: `IActionResult`

### PrintOrganizationalStructureIndicatorListAsync [POST]
- Return: `IActionResult`

### PrintOrganizationalStructurePositionAsync [POST]
- Return: `IActionResult`

### PrintOrganizationalStructureRowPositionAsync [GET]
- Return: `IActionResult`

### PrintOrganizationalStructureDashboardAsync [POST]
- Return: `IActionResult`

### GetListForDashbordAsync [GET]
- Return: `IActionResult`

### GetListForDashbord2Async [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetListForDashbord3Async [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### UploadEcxelAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### PrintTempAsync [POST]
- Return: `IActionResult`

### UpdatePositionFromExcelStage1Async [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### UpdatePositionFromExcelStage2Async [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### WriteChangePositionFromExcelAsync [POST]
- Return: `IActionResult`

### GetOrganizationalCalcKindListAsync [POST]
- Return: `PagedResult<OrganizationalStructureCalculationKindDto>`

### GetCloneStructureCalcKindAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### CreateStructureCalcKindTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### CalcKindPositionCreateAsync [POST]
- Return: `IActionResult`

### CalcKindPositionUpdateAsync [POST]
- Return: `IActionResult`

### CalcKindPositionGetListAsync [POST]
- Return: `PagedResult<OrganizationalStructureCalculationKindPositionListDto>`

### DeleteStructureCalcKindTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### ArchiveStructureCalcKindTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма лавозимни архивлаш

### CreateCalcKindTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteCalcKindTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### GetOrganizationalPositionListAsync [POST]
- Return: `PagedResult<OrganizationalStructurePositionDto>`

### GetCloneStructurePositionAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### CreateStructurePositionTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### UpdateStructurePositionTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteStructurePositionTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### ArchiveStructurePositionTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма лавозимни архивлаш

### GetOrgStructNoStaffPositionListAsync [POST]
- Return: `PagedResult<OrganizationalStructureNoStaffingPositionDto>`

### UpdateStructureNoPositionTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### CreateStructureNoPositionTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteStructureNoPositionTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### ArchiveStructureNoPositionTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма лавозимни архивлаш

### GetCloneStructureNoPositionAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetOrgStructStafIndicatorListAsync [POST]
- Return: `PagedResult<OrganizationalStructureStaffingIndicatorDto>`

### CreateOrgStructStafIndicatorTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### RecalcOrgStructStafIndicatorTableAsync [GET]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteOrgStructStafIndicatorTableAsync [POST]
- Permission: `OrganizationalStructureEdit`
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### ArchiveOrgStructStafIndicatorTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма лавозимни архивлаш

### GetClonetOrgStructStafIndicatorAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### GetOrganizationalFunctionalItemOfExpenseListAsync [POST]
- Return: `PagedResult<OrganizationalStructureFunctionalItemOfExpenseDto>`

### GetCloneStructureFunctionalItemOfExpenseAsync [GET]
- Permission: `OrganizationalStructureView`
- Return: `IActionResult`

### CreateStructureFunctionalItemOfExpenseTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### DeleteStructureFunctionalItemOfExpenseTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### ArchiveStructureFunctionalItemOfExpenseTableAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма лавозимни архивлаш

### GetOrganizationalStructurePositionSpecialtyListAsync [POST]
- Return: `PagedResult<OrganizationalStructurePositionSpecialtyDto>`

### CreateOrganizationalStructurePositionSpecialtyAsync [POST]
- Return: `IActionResult`
- Tavsif: Лавозимга мутахассислик қўшиш

### DeleteOrganizationalStructurePositionSpecialtyAsync [POST]
- Return: `IActionResult`
- Tavsif: Лавозимдан мутахассисликни ўчириш

### InsertFormExcelAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### InsertIvsSalaryAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### GetChanegLogAsync [GET]
- Permission: `OrganizationalStructureEdit`
- Return: `IEnumerable<object`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш


## OrganizationController
Route: `Organization/[action]`

### GetListAsync [POST]
- Return: `PagedResult<OrganizationListDto>`

### GetCameralOrgAsync [POST]
- Return: `IActionResult`

### GetListForCameralAsync [POST]
- Return: `IActionResult`

### UpdateBySoliq [POST]
- Return: `IActionResult`

### PrintOrganizationAsync [POST]
- Return: `IActionResult`

### GetCentralizedListAsync [POST]
- Return: `PagedResult<OrganizationListDto>`

### GetAsync [GET]
- Permission: `OrganizationView`
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetByInnAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### ForHeaderSelectListAsync [GET]
- Return: `IActionResult`

### GetCentralAsSelectListAsync [GET]
- Return: `IActionResult`

### GetCentralizedAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSignSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSignTypeSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationCreate`
- Return: `IActionResult`
- Tavsif: Ташкилот ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationEdit`
- Return: `IActionResult`
- Tavsif: Ташкилот ҳужжатини таҳрирлаш

### UpdateControlAsync [POST]
- Permission: `OrganizationEdit`
- Return: `IActionResult`

### ChangeStateAsync [POST]
- Permission: `UserChangeState`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `OrganizationDelete`
- Return: `IActionResult`
- Tavsif: Ташкилот ҳужжатини ўчириш

### UpdateStructureAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилот ҳужжатини таҳрирлаш

### UpdateFinancingTypeAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилот ҳужжатини таҳрирлаш

### GetOrganizationFromUzasboByInnAsync [GET]
- Return: `IActionResult`

### GetOrganizationInfoAsync [GET]
- Return: `IActionResult`

### RequestToSyncEmployeeForAllOrganizationsAsync [GET]
- Return: `IActionResult`

### GetAsync [POST]
- Return: `IActionResult`

### UpdateCentralOrganizationAsync [POST]
- Permission: `OrganizationEdit`
- Return: `IActionResult`

### RestrictionOrganizationAsync [POST]
- Permission: `FinancialAuthority`
- Return: `IActionResult`

### ChangeSportOrgType [POST]
- Permission: `OrganizationEdit`
- Return: `IActionResult`

### RemovedJobHistory [POST]
- Permission: `OrganizationView`
- Return: `IActionResult`
- Tavsif: Tashkilotni jobdan tozalash


## OrganizationHeaderInfoController
Route: `OrganizationHeaderInfo/[action]`

### GetListAsync [POST]
- Permission: `OrganizationHeaderInfoView`
- Return: `PagedResult<OrganizationHeaderInfoListDto>`

### GetAsync [GET]
- Permission: `OrganizationHeaderInfoView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationHeaderInfoView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationHeaderInfoCreate`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот маълумотлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationHeaderInfoEdit`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот маълумотлари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OrganizationHeaderInfoDelete`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот маълумотлари ҳужжатини ўчириш

### PrintOrganizationAsync [POST]
- Permission: `OrganizationHeaderInfoView`
- Return: `IActionResult`


## OrganizationSettlementAccountController
Route: `OrganizationSettlementAccount/[action]`

### GetListAsync [POST]
- Permission: `OrganizationSettlementAccountView`
- Return: `PagedResult<OrganizationSettlementAccountListDto>`

### GetListByOrganizationsAsync [POST]
- Permission: `OrganizationSettlementAccountView`
- Return: `IEnumerable<OrganizationSettlementAccountListDto>`

### GetPagedListByOrganizationsAsync [POST]
- Permission: `OrganizationSettlementAccountView`
- Return: `PagedResult<OrganizationSettlementAccountListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `OrganizationSettlementAccountView`
- Return: `OrganizationSettlementAccountResultDto`

### PrintGetListWithHistoryAsync [POST]
- Return: `IActionResult`

### SyncOrgSettAccountsAsync [POST]
- Permission: `OrganizationSettlementAccountSync`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationSettlementAccountView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationSettlementAccountView`
- Return: `IActionResult`

### GetSettlementAccountSettingInfoAsync [GET]
- Permission: `OrganizationSettlementAccountView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`
- Tavsif: Ташкилот шахсий ғазна ҳисобрақами ҳужжатини таҳрирлаш

### OrganizationSettlementAccountInfoAsync [GET]
- Return: `IActionResult`

### SearchOrganizationSettlementAccount [GET]
- Return: `IActionResult`


## OrganizationSignController
Route: `OrganizationSign/[action]`

### GetListAsync [POST]
- Permission: `OrganizationSignView`
- Return: `PagedResult<OrganizationSignListDto>`

### GetAsync [GET]
- Permission: `OrganizationSignView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrganizationSignView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationSignCreate`
- Return: `IActionResult`
- Tavsif: Ташкилот имзолари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrganizationSignEdit`
- Return: `IActionResult`
- Tavsif: Ташкилот имзолари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `OrganizationSignDelete`
- Return: `IActionResult`
- Tavsif: Ташкилот имзолари ҳужжатини ўчириш


## OrganizationTypeController
Route: `OrganizationType/[action]`

### GetListAsync [POST]
- Permission: `OrganizationTypeView`
- Return: `PagedResult<OrganizationTypeListDto>`

### GetAsync [GET]
- Permission: `OrganizationTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrganizationTypeCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `OrganizationTypeEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `OrganizationTypeDelete`
- Return: `IActionResult`


## RegionController
Route: `Region/[action]`

### GetListAsync [POST]
- Permission: `RegionView`
- Return: `PagedResult<RegionListDto>`

### GetAsync [GET]
- Permission: `RegionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RegionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListTreasCodeAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RegionCreate`
- Return: `IActionResult`
- Tavsif: Вилоят ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RegionEdit`
- Return: `IActionResult`
- Tavsif: Вилоят ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RegionDelete`
- Return: `IActionResult`
- Tavsif: Вилоят ҳужжатини ўчириш


## RegulatoryDocumentController
Route: `RegulatoryDocument/[action]`

### GetListAsync [POST]
- Permission: `RegulatoryDocumentView`
- Return: `PagedResult<RegulatoryDocumentListDto>`

### GetFileAsync [GET]
- Permission: `RegulatoryDocumentView`
- Return: `IActionResult`

### GetFileInfoAsync [GET]
- Permission: `RegulatoryDocumentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RegulatoryDocumentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RegulatoryDocumentView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RegulatoryDocumentCreate`
- Return: `IActionResult`
- Tavsif: Meyoriy hujjat yaratish

### UpdateAsync [POST]
- Permission: `RegulatoryDocumentEdit`
- Return: `IActionResult`
- Tavsif: Meyoriy hujjat таҳрирлаш

### DeleteAsync [POST]
- Permission: `RegulatoryDocumentDelete`
- Return: `IActionResult`
- Tavsif: Meyoriy hujjat ўчириш


## SettlementAccountPropertyController
Route: `SettlementAccountProperty/[action]`

### GetListAsync [POST]
- Permission: `SettlementAccountPropertyView`
- Return: `PagedResult<SettlementAccountPropertyListDto>`

### GetAsync [GET]
- Permission: `SettlementAccountPropertyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SettlementAccountPropertyView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SettlementAccountPropertyCreate`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SettlementAccountPropertyEdit`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SettlementAccountPropertyDelete`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини ўчириш


## SettlementAccountSettingController
Route: `SettlementAccountSetting/[action]`

### GetListAsync [POST]
- Permission: `SettlementAccountSettingView`
- Return: `PagedResult<SettlementAccountSettingListDto>`

### GetAsync [GET]
- Permission: `SettlementAccountSettingView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SettlementAccountSettingView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SettlementAccountSettingCreate`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SettlementAccountSettingEdit`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SettlementAccountSettingDelete`
- Return: `IActionResult`
- Tavsif: Шахсий ғазна ҳисобварағи созламалари ҳужжатини ўчириш


## StructOrgHeaderInfoController
Route: `StructOrgHeaderInfo/[action]`

### GetListAsync [POST]
- Permission: `StructOrgHeaderInfoView`
- Return: `PagedResult<StructOrgHeaderInfoListDto>`

### GetAsync [GET]
- Permission: `StructOrgHeaderInfoView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StructOrgHeaderInfoView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StructOrgHeaderInfoCreate`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот маълумотлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StructOrgHeaderInfoEdit`
- Return: `IActionResult`
- Tavsif: Юқори турувчи ташкилот маълумотлари ҳужжатини таҳрирлаш

### GetOrgsStructureListAsync [GET]
- Return: `IActionResult`

### PrintOrganizationAsync [POST]
- Permission: `OrganizationHeaderInfoView`
- Return: `IActionResult`


## SysteamTypeController
Route: `Systeam/[action]`

### GetListSysteamTypeAsync [POST]
- Return: `IActionResult`

### GetSysteamTypeAsync [GET]
- Return: `IActionResult`

### CreateSysteamTypeAsync [POST]
- Return: `IActionResult`

### UpdateSysteamTypeAsync [POST]
- Return: `IActionResult`

### DeleteSysteamTypeAsync [POST]
- Return: `IActionResult`


## UnitOfMeasureController
Route: `UnitOfMeasure/[action]`

### GetListAsync [POST]
- Permission: `UnitOfMeasureView`
- Return: `PagedResult<UnitOfMeasureListDto>`

### GetAsync [GET]
- Permission: `UnitOfMeasureView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `UnitOfMeasureView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `UnitOfMeasureCreate`
- Return: `IActionResult`
- Tavsif: Ўлчов бирлиг ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `UnitOfMeasureEdit`
- Return: `IActionResult`
- Tavsif: Ўлчов бирлиг ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `UnitOfMeasureDelete`
- Return: `IActionResult`
- Tavsif: Ўлчов бирлиг ҳужжатини ўчириш


## OrganizationForAsboController
Route: `organizationforasbo/[action]`

### PostInAsbo [POST]
- Return: `IActionResult`

### UpdateInAsbo [POST]
- Return: `IActionResult`


## ProviderBindingController
Route: `ProviderBinding/[action]`

### GetProviderBindingStatusAsync [GET]
- Return: `IActionResult`

### GetProviderBindingSubscriptionSignDataAsync [GET]
- Return: `IActionResult`

### ProviderBindingSubscriptionAsync [POST]
- Return: `IActionResult`


## AccountController
Route: `Account/[action]`

### GetPersonNameAsync [GET]
- Return: `IActionResult`

### CheckOrganizationAsync [GET]
- Return: `IActionResult`

### GetOrganizationInfoAsync [GET]
- Return: `IActionResult`

### CheckUserAsync [POST]
- Return: `IActionResult`

### ResendVerificationCodeAsync [POST]
- Return: `IActionResult`

### ConfirmRegisterUserAsync [POST]
- Return: `IActionResult`

### ChangeLanguageAsync [POST]
- Return: `IActionResult`

### GetAuthInfoAsync [GET]
- Return: `IActionResult`

### GetAuthInfoAsync [GET]
- Return: `IActionResult`


## AppMessageController
Route: `AppMessage/[action]`

### GetListAsync [POST]
- Permission: `AppMessageView`
- Return: `PagedResult<AppMessageListDto>`

### GetAsync [GET]
- Permission: `AppMessageView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AppMessageView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AppMessageCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `AppMessageEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `AppMessageDelete`
- Return: `IActionResult`


## DocumentBlockController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `DocumentBlockView`
- Return: `PagedResult<DocumentBlockListDto>`

### GetAsync [GET]
- Permission: `DocumentBlockView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DocumentBlockView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DocumentBlockCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `DocumentBlockEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `DocumentBlockDelete`
- Return: `IActionResult`


## RoleController
Route: `Role/[action]`

### GetListAsync [POST]
- Permission: `RoleView`
- Return: `PagedResult<RoleListDto>`

### GetAsync [GET]
- Permission: `RoleView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RoleView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### GetAsPermisSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListForOrganizationAsyncAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RoleCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `RoleEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `RoleDelete`
- Return: `IActionResult`


## TableFileConfigController
Route: `TableFileConfig/[action]`

### GetListAsync [POST]
- Permission: `TableFileConfigView`
- Return: `PagedResult<TableFileConfigListDto>`

### GetAsync [GET]
- Permission: `TableFileConfigView`
- Return: `IActionResult`

### Get [GET]
- Permission: `TableFileConfigView`
- Return: `IActionResult`

### GetByTableIdAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TableFileConfigCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `TableFileConfigEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `TableFileConfigDelete`
- Return: `IActionResult`


## UserController
Route: `User/[action]`

### GetListAsync [POST]
- Permission: `UserView`
- Return: `PagedResult<UserListDto>`

### PrintUsersAsync [POST]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `UserView`
- Return: `IActionResult`

### GetForOrganizationAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Permission: `UserView`
- Return: `IActionResult`

### GetPersonalInfoAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `UserCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `UserEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`

### ChangeStateAsync [POST]
- Return: `IActionResult`

### GetUserOrganizationsAsync [GET]
- Return: `IActionResult`

### SetUserOrganizationsAsync [POST]
- Return: `IActionResult`

### GetListForOrganizationAsync [POST]
- Permission: `UserForOrganizationView`
- Return: `PagedResult<UserListDto>`

### CreateForOrganizationAsync [POST]
- Permission: `UserForOrganizationCreate`
- Return: `IActionResult`

### UpdateForOrganizationAsync [POST]
- Permission: `UserForOrganizationEdit`
- Return: `IActionResult`

### GetOldUzasboUserList [GET]
- Permission: `UserForOrganizationView`
- Return: `IActionResult`

### UpdateOldUserPassword [POST]
- Permission: `UserForOrganizationView`
- Return: `IActionResult`


## UserIncomeUncController
Route: `UserIncomeUnc/[action]`

### GetListAsync [POST]
- Permission: `UserIncomeUncView`
- Return: `PagedResult<UserIncomeUncListDto>`

### GetAsync [GET]
- Permission: `UserIncomeUncView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `UserIncomeUncView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `UserIncomeUncCreate`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `UserIncomeUncDelete`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `UserIncomeUncDelete`
- Return: `IActionResult`
