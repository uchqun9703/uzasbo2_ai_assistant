# salary-report-service — API Endpointlar


## DashboardBudgetController
Route: `DashboardBudget/[action]`

### GetBudgetLoop [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetLoopNew [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetHeaderAll [GET]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetHeaderGroup [GET]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetListStaffingTariffication [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetEmployeeTariffication [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetLoaclBudgetStaffingByRegion [GET]
- Return: `IActionResult`

### GetFirstLevelPaymentsByOrgType [GET]
- Return: `IActionResult`

### GetLoaclBudgetStaffingByOrgType [GET]
- Return: `IActionResult`

### GetGenderBudgetByOrgType [GET]
- Return: `IActionResult`


## DashboardController
Route: `Dashboard/[action]`

### GetStaffingCount [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetVacansyPotsion [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetEmployeeSalary [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetRequestReceivingCashRequest [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetVacansyPotsionByOrg [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetStaffingPotsionByOrg [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetStaffingSortList [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDashTempSalaryCalcList [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataCountByGender [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### Tests [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByPositionClass [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByOrgType [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByRepublic [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### PersonPhoto [GET]
- Permission: `DashboardView`
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetEmployeeCardPrint [POST]
- Return: `IActionResult`

### PrintGetCalculationFormPrint [POST]
- Return: `IActionResult`

### PrintGetIncomeCardPrint [POST]
- Return: `IActionResult`

### GetBudgetStaffingCount [POST]
- Return: `IActionResult`

### GetStaffingCount [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion [POST]
- Return: `IActionResult`

### GetStaffingByStructure [POST]
- Return: `IActionResult`

### GetStaffingByStructure2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion3 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion3Print [POST]
- Return: `IActionResult`

### GetBudgetSumReport [POST]
- Return: `IActionResult`

### GetSalary [POST]
- Return: `IActionResult`

### GetBudgetSumReport2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion4 [POST]
- Return: `IActionResult`

### GetBudgetStaffSum [POST]
- Return: `IActionResult`

### GetAppointStatisticCount [POST]
- Return: `IActionResult`

### GetRequestResavingCash [POST]
- Return: `IActionResult`

### GetReportResavingCash [POST]
- Return: `IActionResult`

### GetPaymentOrdersAgroAsync [POST]
- Permission: `AGROBANK_PAYMENT_ORDER_VIEW`
- Return: `IActionResult`

### ExportToExcel [POST]
- Permission: `AGROBANK_PAYMENT_ORDER_VIEW`
- Return: `IActionResult`

### PrintReportResivingCash [POST]
- Return: `IActionResult`

### RepostStaffing2025 [POST]
- Return: `IActionResult`

### RepostStaffing2025Level [POST]
- Return: `IActionResult`

### PrintRepostStaffing2025Level [POST]
- Return: `IActionResult`

### PrintAppointStatistic [POST]
- Return: `IActionResult`

### PrintBudgetStaffing [POST]
- Return: `IActionResult`

### PrintEmployeeProfit [POST]
- Return: `IActionResult`

### GetPlasticCardSheetReport [POST]
- Return: `IActionResult`


## ReportVacancyTurnOverController
Route: `[controller]/[action]`

### GetPositionTurnover [GET]
- Return: `IActionResult`

### GetPositionVacancy [GET]
- Return: `IActionResult`

### GetPositionVacancyFast [GET]
- Return: `IActionResult`

### Print [GET]
- Return: `IActionResult`

### PrintByRegion [GET]
- Return: `IActionResult`

### GetPositionCard [GET]
- Return: `IActionResult`


## SalaryReportController
Route: `[controller]/[action]`

### GetSalaryInfoMonth [POST]
- Return: `IActionResult`

### GetSalaryTopCalc [POST]
- Return: `IActionResult`


## SportTarifficationReportController
Route: `SportTariffication/[action]`

### GetSportTarifficationVacancyAsync [POST]
- Return: `IActionResult`

### GetSportTarifficationTeacherHoursAsync [POST]
- Return: `IActionResult`


## TarifficationReportController
Route: `Tariffication/[action]`

### GetHeadOrgSchoolGradeReportAsync [POST]
- Return: `IActionResult`


## DashboardBudgetController
Route: `DashboardBudget/[action]`

### GetBudgetLoop [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetLoopNew [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetHeaderAll [GET]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetBudgetHeaderGroup [GET]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetListStaffingTariffication [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetEmployeeTariffication [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetLoaclBudgetStaffingByRegion [GET]
- Return: `IActionResult`

### GetFirstLevelPaymentsByOrgType [GET]
- Return: `IActionResult`

### GetLoaclBudgetStaffingByOrgType [GET]
- Return: `IActionResult`

### GetGenderBudgetByOrgType [GET]
- Return: `IActionResult`


## DashboardController
Route: `Dashboard/[action]`

### GetStaffingCount [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetVacansyPotsion [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetEmployeeSalary [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetRequestReceivingCashRequest [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetVacansyPotsionByOrg [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetStaffingPotsionByOrg [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetStaffingSortList [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDashTempSalaryCalcList [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataCountByGender [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### Tests [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByPositionClass [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByOrgType [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### GetDataByRepublic [POST]
- Permission: `DashboardView`
- Return: `IActionResult`

### PersonPhoto [GET]
- Permission: `DashboardView`
- Return: `IActionResult`


## MibController
Route: `[controller]/[action]`

### GetListExecutionPerson [POST]
- Return: `MibExecutionPersonPagedResponse`

### GetListExecutionOrgSheet [POST]
- Return: `PagedResult<MibExecutionOrgSheetDlDto>`

### GetDocAsPdf [GET]
- Return: `IActionResult`

### GetOrgSheetDocAsPdf [GET]
- Return: `IActionResult`

### PrintExecutionPerson [POST]
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetEmployeeCardPrint [POST]
- Return: `IActionResult`

### GetEmployeeCardPrintV2 [POST]
- Return: `IActionResult`

### PrintGetCalculationFormPrint [POST]
- Return: `IActionResult`

### PrintGetIncomeCardPrint [POST]
- Return: `IActionResult`

### GetBudgetStaffingCount [POST]
- Return: `IActionResult`

### GetStaffingCount [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion [POST]
- Return: `IActionResult`

### GetStaffingByStructure [POST]
- Return: `IActionResult`

### GetStaffingByStructure2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion3 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion3Print [POST]
- Return: `IActionResult`

### GetBudgetSumReport [POST]
- Return: `IActionResult`

### GetSalary [POST]
- Return: `IActionResult`

### GetBudgetSumReport2 [POST]
- Return: `IActionResult`

### GetBudgetStaffingCrossSectionByRegion4 [POST]
- Return: `IActionResult`

### GetBudgetStaffSum [POST]
- Return: `IActionResult`

### GetAppointStatisticCount [POST]
- Return: `IActionResult`

### GetRequestResavingCash [POST]
- Return: `IActionResult`

### GetReportResavingCash [POST]
- Return: `IActionResult`

### GetPaymentOrdersAgroAsync [POST]
- Permission: `AGROBANK_PAYMENT_ORDER_VIEW`
- Return: `IActionResult`

### ExportToExcel [POST]
- Permission: `AGROBANK_PAYMENT_ORDER_VIEW`
- Return: `IActionResult`

### PrintReportResivingCash [POST]
- Return: `IActionResult`

### RepostStaffing2025 [POST]
- Return: `IActionResult`

### RepostStaffing2025Level [POST]
- Return: `IActionResult`

### RepostStaffing2025Level4013 [POST]
- Return: `IActionResult`

### PrintRepostStaffing2025Level [POST]
- Return: `IActionResult`

### PrintReportStaffing2025LevelPrintByRegion [GET]
- Return: `IActionResult`

### PrintAppointStatistic [POST]
- Return: `IActionResult`

### PrintBudgetStaffing [POST]
- Return: `IActionResult`

### PrintEmployeeProfit [POST]
- Return: `IActionResult`

### GetPlasticCardSheetReport [POST]
- Return: `IActionResult`

### PrintGetPlasticCardSheetReport [POST]
- Return: `IActionResult`

### ExportPlasticCardSheetReportToExcel [POST]
- Return: `IActionResult`


## ReportVacancyTurnOverController
Route: `[controller]/[action]`

### GetPositionTurnover [GET]
- Return: `IActionResult`

### GetPositionVacancy [GET]
- Return: `IActionResult`

### GetPositionVacancyFast [GET]
- Return: `IActionResult`

### Print [GET]
- Return: `IActionResult`

### PrintByRegion [GET]
- Return: `IActionResult`

### GetPositionCard [GET]
- Return: `IActionResult`


## SalaryReportController
Route: `[controller]/[action]`

### GetSalaryInfoMonth [POST]
- Return: `IActionResult`

### GetSalaryTopCalc [POST]
- Return: `IActionResult`


## SportTarifficationReportController
Route: `SportTariffication/[action]`

### GetSportTarifficationVacancyAsync [POST]
- Return: `IActionResult`

### GetSportTarifficationTeacherHoursAsync [POST]
- Return: `IActionResult`


## TarifficationReportController
Route: `Tariffication/[action]`

### GetHeadOrgSchoolGradeReportAsync [POST]
- Return: `IActionResult`
