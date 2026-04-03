# dashboard-service — API Endpointlar


## BankDocumentStatController
Route: `{lang}/[controller]/[action]`

### GetBankDocumentStatTotal [GET]
- Return: `ActionResult<BankDocumentStatTotalDto>`

### GetBankDocumentStatByRegion [GET]
- Return: `ActionResult<List<BankDocumentStatByRegionDto>>`

### GetBankDocumentStatByDistrict [GET]
- Return: `ActionResult<List<BankDocumentStatByDistrictDto>>`

### GetBankDocumentStatByOrgStructureType [GET]
- Return: `ActionResult<List<BankDocumentStatByOrgStructureTypeDto>>`

### GetBankDocumentStatByOrg [GET]
- Return: `ActionResult<List<BankDocumentStatByOrgDto>>`


## BankIndicatorController
Route: `{lang}/[controller]/[action]`

### GetBankIndicatorTotal [GET]
- Return: `ActionResult<BankIndicatorTotalDto>`

### GetBankIndicatorGroupTotal [GET]
- Return: `ActionResult<BankIndicatorGroupTotalDto>`

### GetBankIndicatorByRegion [GET]
- Return: `ActionResult<List<BankIndicatorByRegionDto>>`

### GetBankIndicatorByDistrict [GET]
- Return: `ActionResult<List<BankIndicatorByDistrictDto>>`

### GetBankIndicatorByIndicator [GET]
- Return: `ActionResult<List<BankIndicatorByIndicatorDto>>`

### GetBankIndicatorByOrg [GET]
- Return: `ActionResult<List<BankIndicatorByOrgDto>>`


## BudgetIndicatorController
Route: `{lang}/[controller]/[action]`

### GetBudgetIndicatorTotal [GET]
- Return: `ActionResult<BudgetIndicatorTotalDto>`

### GetBudgetIndicatorGroupTotal [GET]
- Return: `ActionResult<BudgetIndicatorGroupTotalDto>`

### GetBudgetIndicatorByRegion [GET]
- Return: `ActionResult<List<BudgetIndicatorByRegionDto>>`

### GetBudgetIndicatorByDistrict [GET]
- Return: `ActionResult<List<BudgetIndicatorByDistrictDto>>`

### GetBudgetIndicatorByIndicator [GET]
- Return: `ActionResult<List<BudgetIndicatorByIndicatorDto>>`

### GetBudgetIndicatorByOrg [GET]
- Return: `ActionResult<List<BudgetIndicatorByOrgDto>>`


## BudgetStatController
Route: `{lang}/[controller]/[action]`

### GetBudgetStatTotal [GET]
- Return: `ActionResult<BudgetStatTotalDto>`

### GetBudgetStatByRegion [GET]
- Return: `ActionResult<List<BudgetStatByRegionDto>>`

### GetBudgetStatByDistrict [GET]
- Return: `ActionResult<List<BudgetStatByDistrictDto>>`

### GetBudgetStatByOrgStructureType [GET]
- Return: `ActionResult<List<BudgetStatByOrgStructureTypeDto>>`

### GetBudgetStatByOrg [GET]
- Return: `ActionResult<List<BudgetStatByOrgDto>>`


## EmployeeManageStatController
Route: `{lang}/[controller]/[action]`

### GetEmployeeManageStatTotal [GET]
- Return: `ActionResult<EmployeeManageStatTotalDto>`

### GetEmployeeManageStatByRegion [GET]
- Return: `ActionResult<List<EmployeeManageStatByRegionDto>>`

### GetEmployeeManageStatByDistrict [GET]
- Return: `ActionResult<List<EmployeeManageStatByDistrictDto>>`

### GetEmployeeManageStatByOrgStructureType [GET]
- Return: `ActionResult<List<EmployeeManageStatByOrgStructureTypeDto>>`

### GetEmployeeManageStatByOrg [GET]
- Return: `ActionResult<List<EmployeeManageStatByOrgDto>>`


## EmployeeStatController
Route: `{lang}/[controller]/[action]`

### GetTotalLeaveStat [GET]
- Return: `ActionResult<TotalLeaveStatDto>`

### GetSickLeaveStat [GET]
- Return: `ActionResult<LeaveStatDto>`

### GetMaternityLeaveStat [GET]
- Return: `ActionResult<LeaveStatDto>`

### GetLeaveStat [GET]
- Return: `ActionResult<LeaveStatDto>`


## HealthController
Route: `[controller]/[action]`

### Get [GET]
- Return: `IActionResult`


## InventoryHoldingStatController
Route: `{lang}/[controller]/[action]`

### GetInventoryHoldingStatTotal [GET]
- Return: `ActionResult<InventoryHoldingStatTotalDto>`

### GetInventoryHoldingStatByRegion [GET]
- Return: `ActionResult<List<InventoryHoldingStatByRegionDto>>`

### GetInventoryHoldingStatByDistrict [GET]
- Return: `ActionResult<List<InventoryHoldingStatByDistrictDto>>`

### GetInventoryHoldingStatByOrgStructureType [GET]
- Return: `ActionResult<List<InventoryHoldingStatByOrgStructureTypeDto>>`


## ManualController
Route: `{lang}/[controller]/[action]`

### GetCurrentYear [GET]
- Return: `ActionResult<CurrentYearDto>`


## OrganizationController
Route: `{lang}/[controller]/[action]`

### GetOrganizationCount [GET]
- Return: `ActionResult<OrganizationCountDto>`

### GetOrgCountByRegion [GET]
- Return: `ActionResult<List<OrgCountByRegionDto>>`

### GetOrgCountByDistrict [GET]
- Return: `ActionResult<List<OrgCountByDistrictDto>>`

### GetOrgCountByOrgStructureType [GET]
- Return: `ActionResult<List<OrgCountByOrgStructureTypeDto>>`


## PermanetAssetStatController
Route: `{lang}/[controller]/[action]`

### GetPermanetAssetStatTotal [GET]
- Return: `ActionResult<PermanetAssetStatTotalDto>`

### GetPermanetAssetStatByRegion [GET]
- Return: `ActionResult<List<PermanetAssetStatByRegionDto>>`

### GetPermanetAssetStatByDistrict [GET]
- Return: `ActionResult<List<PermanetAssetStatByDistrictDto>>`

### GetPermanetAssetStatByOrgStructureType [GET]
- Return: `ActionResult<List<PermanetAssetStatByOrgStructureTypeDto>>`

### GetPermanetAssetStatByOrg [GET]
- Return: `ActionResult<List<PermanetAssetStatByOrgDto>>`


## PersonalStatController
Route: `{lang}/[controller]/[action]`

### GetLeaveOrderTotal [GET]
- Return: `ActionResult<LeaveOrderStatDto>`

### GetLeaveOrderStat [GET]
- Return: `ActionResult<LeaveOrderStatDto>`

### GetMaternityStat [GET]
- Return: `ActionResult<LeaveOrderStatDto>`

### GetSickStat [GET]
- Return: `ActionResult<LeaveOrderStatDto>`

### GetWorkingPersonByType [GET]
- Return: `ActionResult<List<WorkingPersonByTypeDto>>`

### GetVacancyByCategory [GET]
- Return: `ActionResult<List<VacancyByCategoryDto>>`

### GetWorkingPensionerByCategory [GET]
- Return: `ActionResult<List<WorkingPensionerByCategoryDto>>`

### GetWorkingPersonByCategory [GET]
- Return: `ActionResult<List<WorkingPersonByCategoryDto>>`

### GetWorkingPersonByRate [GET]
- Return: `ActionResult<List<WorkingPersonByRateDto>>`


## PersonStatController
Route: `{lang}/[controller]/[action]`

### GetPersonStatTotal [GET]
- Return: `ActionResult<PersonStatTotalDto>`

### GetPersonStatByRegion [GET]
- Return: `ActionResult<List<PersonStatByRegionDto>>`

### GetPersonStatByDistrict [GET]
- Return: `ActionResult<List<PersonStatByDistrictDto>>`

### GetPersonStatByOrgStructureType [GET]
- Return: `ActionResult<List<PersonStatByOrgStructureTypeDto>>`

### GetPersonStatByAge [GET]
- Return: `ActionResult<List<PersonStatByAgeDto>>`


## SalaryBudgetStatController
Route: `{lang}/[controller]/[action]`

### GetSalaryBudgetStatTotal [GET]
- Return: `ActionResult<SalaryBudgetStatTotalDto>`

### GetSalaryBudgetStatByRegion [GET]
- Return: `ActionResult<List<SalaryBudgetStatByRegionDto>>`

### GetSalaryBudgetStatByDistrict [GET]
- Return: `ActionResult<List<SalaryBudgetStatByDistrictDto>>`

### GetSalaryBudgetStatByOrgStructureType [GET]
- Return: `ActionResult<List<SalaryBudgetStatByOrgStructureTypeDto>>`

### GetSalaryBudgetStatByOrg [GET]
- Return: `ActionResult<List<SalaryBudgetStatByOrgDto>>`


## SalaryDetailController
Route: `{lang}/[controller]/[action]`

### GetSalaryDetailTotal [GET]
- Return: `ActionResult<SalaryDetailTotalDto>`

### GetSalaryDetailByRegion [GET]
- Return: `ActionResult<List<SalaryDetailByRegionDto>>`

### GetSalaryDetailByDistrict [GET]
- Return: `ActionResult<List<SalaryDetailByDistrictDto>>`

### GetSalaryDetailByOrgStructureType [GET]
- Return: `ActionResult<List<SalaryDetailByOrgStructureTypeDto>>`

### GetSalaryDetailByOrgStructureTotal [GET]
- Return: `ActionResult<List<SalaryDetailByOrgStructureTotalDto>>`

### GetSalaryDetailByOrg [GET]
- Return: `ActionResult<List<SalaryDetailByOrgDto>>`


## SalaryStatController
Route: `{lang}/[controller]/[action]`

### GetSalaryStatTotal [GET]
- Return: `ActionResult<SalaryStatTotalDto>`

### GetSalaryStatByRegion [GET]
- Return: `ActionResult<List<SalaryStatByRegionDto>>`

### GetSalaryStatByDistrict [GET]
- Return: `ActionResult<List<SalaryStatByDistrictDto>>`

### GetSalaryStatByOrgStructureType [GET]
- Return: `ActionResult<List<SalaryStatByOrgStructureTypeDto>>`

### GetSalaryStatByOrg [GET]
- Return: `ActionResult<List<SalaryStatByOrgDto>>`


## StaffingController
Route: `{lang}/[controller]/[action]`

### GetStaffingStatTotal [GET]
- Return: `ActionResult<StaffingStatTotalDto>`

### GetMedStaffingStatTotal [GET]
- Return: `ActionResult<MedStaffingStatTotalDto>`

### GetStaffingStatByRegion [GET]
- Return: `ActionResult<List<StaffingStatByRegionDto>>`

### GetStaffingStatByDistrict [GET]
- Return: `ActionResult<List<StaffingStatByDistrictDto>>`

### GetStaffingStatByOrgStructureType [GET]
- Return: `ActionResult<List<StaffingStatByOrgStructureTypeDto>>`

### GetStaffingStatByOrg [GET]
- Return: `ActionResult<List<StaffingStatByOrgDto>>`

### GetMedStaffingStatByGroup [GET]
- Return: `ActionResult<List<MedStaffingStatByGroupDto>>`

### GetMedStaffingStatByExpertise [GET]
- Return: `ActionResult<List<MedStaffingStatByExpertiseDto>>`


## TarifficationStatController
Route: `{lang}/[controller]/[action]`

### GetTarifficationStatTotal [GET]
- Return: `ActionResult<TarifficationStatTotalDto>`

### GetTarifficationStatByRegion [GET]
- Return: `ActionResult<List<TarifficationStatByRegionDto>>`

### GetTarifficationStatByDistrict [GET]
- Return: `ActionResult<List<TarifficationStatByDistrictDto>>`

### GetTarifficationStatByOrgStructureType [GET]
- Return: `ActionResult<List<TarifficationStatByOrgStructureTypeDto>>`

### GetTarifficationStatByOrg [GET]
- Return: `ActionResult<List<TarifficationStatByOrgDto>>`


## TeacherHourStatController
Route: `{lang}/[controller]/[action]`

### GetTeacherHourStatTotal [GET]
- Return: `ActionResult<TeacherHourStatTotalDto>`

### GetTeacherHourStatByRegion [GET]
- Return: `ActionResult<List<TeacherHourStatByRegionDto>>`

### GetTeacherHourStatByDistrict [GET]
- Return: `ActionResult<List<TeacherHourStatByDistrictDto>>`

### GetTeacherHourStatByOrgStructureType [GET]
- Return: `ActionResult<List<TeacherHourStatByOrgStructureTypeDto>>`

### GetTeacherHourStatByOrg [GET]
- Return: `ActionResult<List<TeacherHourStatByOrgDto>>`


## XaridController
Route: `{lang}/[controller]/[action]`

### GetXaridStatTotal [GET]
- Return: `ActionResult<string>`

### GetXaridStatByRegion [GET]
- Return: `ActionResult<string>`

### GetXaridStatByDistrict [GET]
- Return: `ActionResult<string>`

### GetXaridStatByOrgStructureType [GET]
- Return: `ActionResult<string>`

### GetXaridStatByOrg [GET]
- Return: `ActionResult<string>`


## DefaultController
Route: `[controller]`

### Get [GET]
- Return: `ActionResult<string`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `ActionResult<string`
