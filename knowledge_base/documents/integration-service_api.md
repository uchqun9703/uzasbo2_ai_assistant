# integration-service — API Endpointlar


## GovermentAssetsController
Route: `[controller]/[action]`

### GetList [POST]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## IhmaController
Route: `[controller]/[action]`

### GetEmployeeManage [GET]
- Return: `IActionResult`

### GetEmployeeManageById [GET]
- Return: `IActionResult`

### GetEmployeeManagePeriod [GET]
- Return: `IActionResult`

### GetPostionIhma [GET]
- Return: `IActionResult`

### GetDepartmentIhma [GET]
- Return: `IActionResult`

### GetEmpAppointOrderTypeIhma [GET]
- Return: `IActionResult`

### GetOrganizationVacancy [POST]
- Return: `IActionResult`

### GetEmploymentTypeIhma [GET]
- Return: `IActionResult`

### GetWorkScheduleIhma [GET]
- Return: `IActionResult`

### GetAppointEmployeeById [GET]
- Return: `IActionResult`

### CheckIhmaOrg [POST]
- Return: `IActionResult`


## ManualController
Route: `[controller]/[action]`

### GetRegionList [GET]
- Return: `IActionResult`

### GetOrganizationList [GET]
- Return: `IActionResult`

### GetLeadershipList [GET]
- Return: `IActionResult`

### GetChildOrganization [GET]
- Return: `IActionResult`

### GetHeaderOrganization [GET]
- Return: `IActionResult`

### GetOrgStruct [GET]
- Return: `IActionResult`

### GetSendDocumentID [GET]
- Return: `IActionResult`

### GetOutSumByPinfl [POST]
- Return: `IActionResult`

### GetDepartamentsByInn [GET]
- Return: `IActionResult`

### GetPositionsByInn [GET]
- Return: `IActionResult`

### GetContractorSettlementAccount [GET]
- Return: `IActionResult`

### CheckAccPlanCalculationKind [GET]
- Return: `IActionResult`

### GetTreasBudget [POST]
- Return: `PagedResult<TreasBudgetListDto`

### GetTBudget [GET]
- Return: `IActionResult`

### GetReportFormN2 [GET]
- Return: `IActionResult`

### BankDocumentGetListTest [POST]
- Return: `BankDocumentNewPageGetList`

### BankDocumentIhmaGetList [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### BankDocumentIhmaByAccountGetList [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### BankDocumentDavmGetList [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### GetEreportForma1 [GET]
- Return: `IActionResult`

### GetEreportForma2 [GET]
- Return: `IActionResult`

### GetRestInfo [POST]
- Return: `IActionResult`


## PassportImvController
Route: `[controller]/[action]`

### GetOrganizationSettlemetAccount [GET]
- Return: `IActionResult`

### GetOrganizationStaffing [POST]
- Return: `IActionResult`

### GetPlasticCardNumber [POST]
- Return: `IActionResult`

### GetIncomeTaxPayment [POST]
- Return: `IActionResult`

### GetOrganizationStaffingPositions [POST]
- Return: `PagedResult<GetOrganizationStaffingPosition`

### GetOrganizationStaffingQualificationCategories [POST]
- Return: `IActionResult`

### GetVacacyStaffingPositionCount [POST]
- Return: `IActionResult`

### GetPedStaffingPositionCount [POST]
- Return: `IActionResult`

### GetOccupiedStaffingPositionCount [POST]
- Return: `IActionResult`

### GetOccupiedStaffingIndividualPositionCount [POST]
- Return: `IActionResult`

### GetMedicalStaffingPositionCount [POST]
- Return: `IActionResult`

### GetMedicalEmployeeCount [POST]
- Return: `IActionResult`

### GetAllOrgStructure [GET]
- Return: `IActionResult`

### GetOrgStructure [GET]
- Return: `IActionResult`

### GetSalaryInfo [GET]
- Return: `IActionResult`

### GetEmployeeInfoList [GET]
- Return: `IActionResult`

### GetEmployeeSalary [GET]
- Return: `IActionResult`

### GetPaySalaryInfo [GET]
- Return: `IActionResult`

### GetEmployeeInfo [GET]
- Return: `IActionResult`

### GetEmployeeInfoInn [GET]
- Return: `IActionResult`

### GetPropertyTaxPayment [POST]
- Return: `IActionResult`

### GetStaffingAndAppintInfo [POST]
- Return: `IActionResult`

### GetPermanentAssetAccountBookReportAutoMobileAsync [GET]
- Return: `IActionResult`

### GetOrganizationWithStructCode [GET]
- Return: `IActionResult`


## ZpUzasboController
Route: `[controller]/[action]`


## AppointQualCategoryController
Route: `[controller]/[action]`

### Delete [POST]
- Return: `IActionResult`


## BillingSalaryCalcController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`

### CreateStudentPayrollPlasticCardSheet [POST]
- Return: `IActionResult`

### GetOrganizationVacancyAsync [POST]
- Return: `IActionResult`

### GetPositionListAsync [POST]
- Return: `IActionResult`


## CultureMusicTarifficationTitleController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`


## CurriculumOrgSchGradeController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Ҳар бир синф кесимида соатлар сеткаси ҳужжатини яратиш


## EduStudyCertificateController
Route: `old/[controller]/[action]`

### SyncFromErpRemoveOld [POST]
- Return: `IActionResult`


## HeadOrgSchoolGradeController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Ҳар бир синф кесимида соатлар сеткаси ҳужжатини яратиш


## KindergardenTarifficationTitleController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## OrgSchoolParameterController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Ўқув йили бошига синф параметрлари ҳужжатини яратиш


## SportTarifficationTitleController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## TarifficationTitleController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## InventoryHoldingController
Route: `[controller]/[action]`

### GetAccountBookInventoryHoldingWithSubCounts [GET]
- Return: `IActionResult`


## PermanentAssetController
Route: `[controller]/[action]`

### GetAccountBookPermanentAsset [GET]
- Return: `IActionResult`

### GetPermanentAssetAccountBookReportAutoMobile [GET]
- Return: `IActionResult`


## MoliyachiNotificationController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`


## WorkScheduleController
Route: `[controller]/[action]`

### GetWorkDaysByScheduleAsync [GET]
- Return: `IActionResult`


## BankDocumentController
Route: `[controller]/[action]`

### BankDocumentGetList [GET]
- Return: `IActionResult`

### GetBankDocument [POST]
- Return: `IActionResult`


## DavAvtivBankDocumentController
Route: `[controller]/[action]`

### DavActivBankDocumentGetList [GET]
- Return: `IActionResult`


## InspectionBankDocumentController
Route: `[controller]/[action]`

### InspectionBankDocumentGetList [GET]
- Return: `IActionResult`


## TreasInfoController
Route: `[controller]/[action]`

### BankDocumentInfoList [GET]
- Return: `IActionResult`


## GovermentAssetsController
Route: `new/[controller]/[action]`

### GetList [POST]
- Return: `IActionResult`


## IhmaController
Route: `new/[controller]/[action]`

### GetEmployeeManageAsync [GET]
- Return: `IActionResult`

### GetEmployeeManageByIdAsync [GET]
- Return: `IActionResult`

### GetEmployeeManagePeriodAsync [GET]
- Return: `IActionResult`

### GetPostionIhmaAsync [GET]
- Return: `IActionResult`

### GetDepartmentIhmaAsync [GET]
- Return: `IActionResult`

### GetEmpAppointOrderTypeIhmaAsync [GET]
- Return: `IActionResult`

### GetOrganizationVacancyAsync [POST]
- Return: `IActionResult`

### GetEmploymentTypeIhmaAsync [GET]
- Return: `IActionResult`

### GetWorkScheduleIhmaAsync [GET]
- Return: `IActionResult`

### GetAppointEmployeeByIdAsync [GET]
- Return: `IActionResult`

### CheckIhmaOrgAsync [POST]
- Return: `IActionResult`


## ManualController
Route: `new/[controller]/[action]`

### GetRegionListAsync [GET]
- Return: `IActionResult`

### GetOrganizationListAsync [GET]
- Return: `IActionResult`

### GetLeadershipListAsync [GET]
- Return: `IActionResult`

### GetChildOrganizationAsync [GET]
- Return: `IActionResult`

### GetHeaderOrganizationAsync [GET]
- Return: `IActionResult`

### GetOrgStructAsync [GET]
- Return: `IActionResult`

### GetSendDocumentIDAsync [GET]
- Return: `IActionResult`

### GetOutSumByPinflAsync [POST]
- Return: `IActionResult`

### GetDepartamentsByInnAsync [GET]
- Return: `IActionResult`

### GetPositionsByInnAsync [GET]
- Return: `IActionResult`

### GetContractorSettlementAccountAsync [GET]
- Return: `IActionResult`

### CheckAccPlanCalculationKindAsync [GET]
- Return: `IActionResult`

### GetTreasBudgetAsync [POST]
- Return: `PagedResult<TreasBudgetListDto>`

### GetTBudgetAsync [GET]
- Return: `IActionResult`

### GetReportFormN2Async [GET]
- Return: `IActionResult`

### BankDocumentGetListTestAsync [POST]
- Return: `BankDocumentNewPageGetList`

### BankDocumentIhmaGetListAsync [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### BankDocumentIhmaByAccountGetListAsync [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### BankDocumentDavmGetListAsync [POST]
- Return: `DbPagedModel<BankDocumentPckListDto>`

### GetEreportForma1Async [GET]
- Return: `IActionResult`

### GetEreportForma2Async [GET]
- Return: `IActionResult`

### GetRestInfoAsync [POST]
- Return: `IActionResult`


## PassportImvController
Route: `new/[controller]/[action]`

### GetOrganizationSettlemetAccountAsync [GET]
- Return: `IActionResult`

### GetOrganizationStaffingAsync [POST]
- Return: `IActionResult`

### GetIncomeTaxPaymentAsync [POST]
- Return: `IActionResult`

### GetOrganizationStaffingPositionsAsync [POST]
- Return: `PagedResult<GetOrganizationStaffingPosition>`

### GetOrganizationStaffingQualificationCategoriesAsync [POST]
- Return: `IActionResult`

### GetVacacyStaffingPositionCountAsync [POST]
- Return: `IActionResult`

### GetPedStaffingPositionCountAsync [POST]
- Return: `IActionResult`

### GetOccupiedStaffingPositionCountAsync [POST]
- Return: `IActionResult`

### GetOccupiedStaffingIndividualPositionCountAsync [POST]
- Return: `IActionResult`

### GetMedicalStaffingPositionCountAsync [POST]
- Return: `IActionResult`

### GetMedicalEmployeeCountAsync [POST]
- Return: `IActionResult`

### GetAllOrgStructureAsync [GET]
- Return: `IActionResult`

### GetOrgStructureAsync [GET]
- Return: `IActionResult`

### GetSalaryInfoAsync [GET]
- Return: `IActionResult`

### GetEmployeeInfoListAsync [GET]
- Return: `IActionResult`

### GetEmployeeSalaryAsync [GET]
- Return: `IActionResult`

### GetPaySalaryInfoAsync [GET]
- Return: `IActionResult`

### GetEmployeeInfoAsync [GET]
- Return: `IActionResult`

### GetEmployeeInfoInnAsync [GET]
- Return: `IActionResult`

### GetPropertyTaxPaymentAsync [POST]
- Return: `IActionResult`


## ZpUzasboController
Route: `new/[controller]/[action]`


## ChildPaymentController
Route: `[controller]/[action]`

### GetSeries [GET]
- Return: `IActionResult`

### GetStatusInfo [GET]
- Return: `IActionResult`

### GetInfo [GET]
- Return: `IActionResult`

### CancelPayedInfo [GET]
- Return: `IActionResult`

### PayedInfo [POST]
- Return: `IActionResult`


## MibController
Route: `[controller]/[action]`

### PostDebtInfo [POST]
- Return: `IActionResult`

### GetOrgSheetDocAsPdfBase64 [GET]
- Return: `IActionResult`


## MvdController
Route: `[controller]/[action]`

### GetOperDate [GET]
- Return: `IActionResult`

### SendRequestReceivingCash [POST]
- Return: `IActionResult`

### SendPaymentOrder [POST]
- Return: `IActionResult`

### SendContract [POST]
- Return: `IActionResult`

### AcceptContractByMvd [POST]
- Return: `IActionResult`

### CancelContractByMvd [POST]
- Return: `IActionResult`

### GetContractor [GET]
- Return: `IActionResult`

### SendChequeWarrant [POST]
- Return: `IActionResult`


## GetOrganizationAccountInfoController
Route: `[controller]/[action]`

### GetOrganizationAccountInfo [POST]
- Return: `IActionResult`


## AppointQualCategoryController
Route: `new/[controller]/[action]`

### DeleteAsync [POST]
- Return: `IActionResult`


## BillingSalaryCalcController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`

### CreateStudentPayrollPlasticCardSheet [POST]
- Return: `IActionResult`


## CultureMusicTarifficationTitleController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## CurriculumOrgSchGradeController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Ҳар бир синф кесимида соатлар сеткаси ҳужжатини яратиш


## HeadOrgSchoolGradeController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Ҳар бир синф кесимида соатлар сеткаси ҳужжатини яратиш


## OrgSchoolParameterController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Ўқув йили бошига синф параметрлари ҳужжатини яратиш


## SportTarifficationTitleController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## TarifficationTitleController
Route: `new/[controller]/[action]`

### CreateAsync [POST]
- Return: `IActionResult`
- Tavsif: Титул варағи ҳужжатини яратиш


## InventoryHoldingController
Route: `new/[controller]/[action]`

### GetAccountBookInventoryHoldingWithSubCountsAsync [GET]
- Return: `IActionResult`


## PermanentAssetController
Route: `new/[controller]/[action]`

### GetAccountBookPermanentAssetAsync [GET]
- Return: `IActionResult`

### GetPermanentAssetAccountBookReportAutoMobileAsync [GET]
- Return: `IActionResult`


## WorkScheduleController
Route: `new/[controller]/[action]`

### GetWorkDaysByScheduleAsync [GET]
- Return: `IActionResult`


## BankDocumentController
Route: `new/[controller]/[action]`

### BankDocumentGetListAsync [GET]
- Return: `IActionResult`


## DavAvtivBankDocumentController
Route: `new/[controller]/[action]`

### DavActivBankDocumentGetList [GET]
- Return: `IActionResult`


## InspectionBankDocumentController
Route: `new/[controller]/[action]`

### InspectionBankDocumentGetList [GET]
- Return: `IActionResult`
