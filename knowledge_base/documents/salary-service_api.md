# salary-service — API Endpointlar


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

### GetCalculateByTimeTypeSelectlist [GET]
- Return: `IActionResult`

### GetCalculationMethodSelectlist [GET]
- Return: `IActionResult`

### GetCalculationTypeSelectlist [GET]
- Return: `IActionResult`

### GetRoundingTypeSelectlist [GET]
- Return: `IActionResult`

### GetStaffingTypeSelectlist [GET]
- Return: `IActionResult`

### GetPlasticCardTypeSelectlist [GET]
- Return: `IActionResult`

### GetLeaveCalcTypeSelectlist [GET]
- Return: `IActionResult`

### GetRequestReceivingCashTypeSelectlist [GET]
- Return: `IActionResult`

### GetPositionPeriodSelectlist [GET]
- Return: `IActionResult`

### GetEmployeeProfitRowTypeSelectlist [GET]
- Return: `IActionResult`

### GetLimitOperTypeSelectlist [GET]
- Return: `IActionResult`

### GetPayrollSheetTypeSelectlist [GET]
- Return: `IActionResult`

### GetBenefitTaxTypeSelectlist [GET]
- Return: `IActionResult`

### GetIvsTempCalcList [POST]
- Return: `IActionResult`

### InsertIvsSalary [POST]
- Return: `IActionResult`
- Tavsif: Ташкилий тузилма ҳужжатини таҳрирлаш

### GetLimitTypeSelectList [GET]
- Return: `IActionResult`

### GetCalculationClassificationTypeSelectlist [GET]
- Return: `IActionResult`

### GetSchoolYearList [GET]
- Return: `IActionResult`

### GetSchoolGradeGroupList [GET]
- Return: `IActionResult`

### GetSchoolGradeList [GET]
- Return: `IActionResult`

### GetSchoolGradeLetterList [GET]
- Return: `IActionResult`

### GetTarifficationTitlePeriodTypeSelectList [GET]
- Return: `IActionResult`

### GetFinanceSourceSelectList [GET]
- Return: `IActionResult`

### GetPaymentTypeSelectList [GET]
- Return: `IActionResult`

### GetSportTitleDefinationSelectList [GET]
- Return: `IActionResult`

### GetTaxBreakDirectionTypeSelectList [GET]
- Return: `IActionResult`

### GetTaxBreakPeriodSelectList [GET]
- Return: `IActionResult`

### ConstantSelectList [GET]
- Return: `IActionResult`

### GetTaxBreakTypeSelectList [GET]
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


## AppointEmployeeSalaryController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `AppointEmployeeSalaryView`
- Return: `PagedResult<AppointEmployeeSalaryListDto>`

### PrintGetListAppoint [POST]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`

### GetListNotAddSalary [POST]
- Permission: `AppointEmployeeSalaryView`
- Return: `IActionResult`

### Get [GET]
- Permission: `AppointEmployeeSalaryView`
- Return: `IActionResult`

### Get [GET]
- Permission: `AppointEmployeeSalaryView`
- Return: `IActionResult`

### RecalcAppointEmpSalaryTable [POST]
- Permission: `AppointEmployeeSalaryCreate`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш қайта ҳисоблаш

### GetAsSelectList [GET]
- Return: `IActionResult`

### GetLastAppointEmployeeSalaryTable [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `AppointEmployeeSalaryCreate`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш ҳужжатини яратиш

### Update [POST]
- Permission: `AppointEmployeeSalaryEdit`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `AppointEmployeeSalaryAccept`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `AppointEmployeeSalaryCancel`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `AppointEmployeeSalaryDelete`
- Return: `IActionResult`
- Tavsif: Ходимнинг иш ҳақини тайинлаш ҳужжатини ўчириш


## AppointQualCategoryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<AppointQualCategoryListDto>`

### GetListWithHistoryAsync [POST]
- Return: `AppointQualCategoryResultDto`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncFromErpAsync [POST]
- Return: `IActionResult`

### EmployeeSyncFromErpAsync [POST]
- Return: `IActionResult`

### Test [GET]
- Return: `IActionResult`


## AverageSalaryControlController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AverageSalaryControlView`
- Return: `PagedResult<AverageSalaryControlListDto>`

### GetAsync [GET]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`

### GetTablesAsync [POST]
- Permission: `AverageSalaryControlView`
- Return: `PagedResult<AverageSalaryControlTableDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AverageSalaryControlCreate`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `AverageSalaryControlEdit`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `AverageSalaryControlAccept`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `AverageSalaryControlCancel`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `AverageSalaryControlDelete`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини ўчириш

### FillAsync [POST]
- Permission: `AverageSalaryControlCreate`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `AverageSalaryControlCreate`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини тозалаш

### PrintAsExcelAsync [POST]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини печать килиш


## CalcLeavePayController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `PagedResult<CalcLeavePayListDto>`

### GetLaborLeaveListAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `PagedResult<CalcLeavePayListDto>`

### GetSickLeaveListAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `PagedResult<CalcLeavePayListDto>`

### GetCompensationListAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `PagedResult<CalcLeavePayListDto>`

### GetListNotAddSickLeaveAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`

### GetListNotAddCompensationAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`

### GetListNotAddLeaveOrderAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CalcLeavePayCreate`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини яратиш

### RecalcCalcLeavePayAsync [POST]
- Permission: `CalcLeavePayCreate`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини қайта ҳисоблаш

### ClearAsync [POST]
- Permission: `CalcLeavePayCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `CalcLeavePayEdit`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CalcLeavePayAccept`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CalcLeavePayCancel`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `CalcLeavePayDelete`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `CalcLeavePayView`
- Return: `IActionResult`


## CalcSendTrainController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CalcSendTrainView`
- Return: `PagedResult<CalcSendTrainListDto>`

### GetAsync [GET]
- Permission: `CalcSendTrainView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalcSendTrainView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CalcSendTrainCreate`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CalcSendTrainEdit`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини таҳрирлаш

### RecalcCalcSendTrainAsync [POST]
- Permission: `CalcSendTrainEdit`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CalcSendTrainAccept`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини тасдиқлаш

### ClearAsync [POST]
- Permission: `CalcLeavePayCreate`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `CalcSendTrainCancel`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `CalcSendTrainDelete`
- Return: `IActionResult`
- Tavsif: Малака ошириш даврида ўртача ойлик иш ҳақини ҳисоблаш ҳужжатини ўчириш


## CalculationKindSwitchController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CalculationKindSwitchView`
- Return: `PagedResult<CalculationKindSwitchListDto>`

### GetAsync [GET]
- Permission: `CalculationKindSwitchView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalculationKindSwitchView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CalculationKindSwitchCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `CalculationKindSwitchEdit`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини таҳрирлаш

### ClearAsync [POST]
- Permission: `CalculationKindSwitchCreate`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини тозалаш

### FillAsync [POST]
- Permission: `CalculationKindSwitchCreate`
- Return: `IActionResult`
- Tavsif: Ўртача иш ҳақини ҳисоблаш ҳужжатини тўлдириш

### DeleteAsync [POST]
- Permission: `CalculationKindSwitchDelete`
- Return: `IActionResult`

### Accept [POST]
- Permission: `CalculationKindSwitchAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `CalculationKindSwitchCancel`
- Return: `IActionResult`


## ChangeDocumentStatusController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChangeDocumentStatusView`
- Return: `PagedResult<ChangeDocumentStatusListDto>`

### GetAsync [GET]
- Permission: `ChangeDocumentStatusView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChangeDocumentStatusView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChangeDocumentStatusCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `ChangeDocumentStatusEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `ChangeDocumentStatusAccept`
- Return: `IActionResult`


## ChangeOrgSettlementAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountView`
- Return: `PagedResult<ChangeOrganizationSettlementAccountListDto>`

### GetAsync [GET]
- Permission: `ChangeOrganizationSettlementAccountView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChangeOrganizationSettlementAccountView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountEdit`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountAccept`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountCancel`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `ChangeOrganizationSettlementAccountDelete`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини ўчириш


## ChargesFromSalaryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChargesFromSalaryView`
- Return: `PagedResult<ChargesFromSalaryListDto>`

### GetAsync [GET]
- Permission: `ChargesFromSalaryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChargesFromSalaryView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `ChargesFromSalaryView`
- Return: `IActionResult`

### GetByOrgSettlementAccountIdAsync [GET]
- Permission: `ChargesFromSalaryView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChargesFromSalaryCreate`
- Return: `IActionResult`
- Tavsif: Ойликдан ушланмалар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ChargesFromSalaryEdit`
- Return: `IActionResult`
- Tavsif: Ойликдан ушланмалар ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ChargesFromSalaryDelete`
- Return: `IActionResult`
- Tavsif: Ойликдан ушланмалар ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `ChargesFromSalaryAccept`
- Return: `IActionResult`
- Tavsif: Ойликдан ушланмалар ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ChargesFromSalaryCancel`
- Return: `IActionResult`
- Tavsif: Ойликдан ушланмалар ҳужжатини бекор қилиш


## ChatBoxController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ChatBoxView`
- Return: `PagedResult<ChatBoxListDto>`

### GetAsync [GET]
- Permission: `ChatBoxView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ChatBoxView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ChatBoxCreate`
- Return: `IActionResult`
- Tavsif: Chat yaratish

### UpdateAsync [POST]
- Permission: `ChatBoxEdit`
- Return: `IActionResult`
- Tavsif: Chat tahrirlash

### AcceptAsync [POST]
- Permission: `ChatBoxAccept`
- Return: `IActionResult`
- Tavsif: Chat tasdiqlash

### CancelAsync [POST]
- Permission: `ChatBoxCancel`
- Return: `IActionResult`
- Tavsif: Chat bekor qilish

### DeleteAsync [POST]
- Permission: `ChatBoxDelete`
- Return: `IActionResult`
- Tavsif: Chat o'chirish

### GetMessagesAsync [POST]
- Permission: `ChatBoxView`
- Return: `IActionResult`

### SendMessageAsync [POST]
- Permission: `ChatBoxMessage`
- Return: `IActionResult`
- Tavsif: Xabar yuborish

### EditMessageAsync [POST]
- Permission: `ChatBoxMessage`
- Return: `IActionResult`
- Tavsif: Xabarni tahrirlash

### DeleteMessageAsync [POST]
- Permission: `ChatBoxMessage`
- Return: `IActionResult`
- Tavsif: Xabarni o'chirish


## CheckSalaryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CheckSalaryView`
- Return: `PagedResult<CheckSalaryListDto>`

### GetAsync [GET]
- Permission: `CheckSalaryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CheckSalaryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CheckSalaryCreate`
- Return: `IActionResult`

### CheckAsync [POST]
- Permission: `CheckSalaryCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `CheckSalaryEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `CheckSalaryAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `CheckSalaryCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `CheckSalaryDelete`
- Return: `IActionResult`


## CultureMusicTarifficationTitleController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `CultureMusicTarifficationTitleView`
- Return: `PagedResult<CultureMusicTarifficationTitleListDto`

### HeaderGetList [POST]
- Permission: `CultureMusicTarifficationTitleSentToRecive`
- Return: `PagedResult<CultureMusicTarifficationTitleListDto`

### Get [GET]
- Permission: `CultureMusicTarifficationTitleView`
- Return: `IActionResult`

### GetForHeader [GET]
- Permission: `CultureMusicTarifficationTitleSentToRecive`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `CultureMusicTarifficationTitleSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `CultureMusicTarifficationTitleSentToNotRecive`
- Return: `IActionResult`


## CurriculumController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurriculumView`
- Return: `PagedResult<CurriculumListDto>`

### GetAsync [GET]
- Permission: `CurriculumView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncFromErpAsync [POST]
- Return: `IActionResult`


## CurriculumOrgSchGradeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurriculumView`
- Return: `PagedResult<CurriculumOrgSchGradeListDto>`

### GetAsync [GET]
- Permission: `CurriculumView`
- Return: `IActionResult`

### GetTotalCurriculumOrgSchGradeAsync [POST]
- Permission: `CurriculumView`
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `CurriculumOrgSchGradeSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `CurriculumOrgSchGradeSentToNotRecive`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `CurriculumView`
- Return: `IActionResult`

### GetCurriculumOrgSchGradHours [GET]
- Permission: `CurriculumView`
- Return: `IActionResult`


## EduStudyCertificateController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurriculumView`
- Return: `PagedResult<EduStudyCertificateListDto>`

### GetAsync [GET]
- Permission: `CurriculumView`
- Return: `IActionResult`

### GetListWithPersonIdAsync [GET]
- Permission: `CurriculumView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncFromErpAsync [POST]
- Return: `IActionResult`


## EmployeeProfitController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeProfitView`
- Return: `PagedResult<EmployeeProfitListDto>`

### GetAsync [GET]
- Permission: `EmployeeProfitView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeProfitView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTableAsSelectListAsync [GET]
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `EmployeeProfitCreate`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeProfitCreate`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeProfitEdit`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EmployeeProfitAccept`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини таҳрирлаш

### CancelAsync [POST]
- Permission: `EmployeeProfitCancel`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини бекор қилиш

### ArchivedAsync [POST]
- Permission: `EmployeeProfitCancel`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини архиви холатга ўтказиш

### DeleteAsync [POST]
- Permission: `EmployeeProfitDelete`
- Return: `IActionResult`
- Tavsif: Aввалги даромадларни киритиш ҳужжатини ўчириш


## HeadOrgSchoolGradeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `HeadOrgSchoolGradeView`
- Return: `PagedResult<HeadOrgSchoolGradeListDto>`

### GetAsync [GET]
- Permission: `HeadOrgSchoolGradeView`
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `HeadOrgSchoolGradeRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `HeadOrgSchoolGradeNotRecive`
- Return: `IActionResult`


## HourlyPayController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `HourlyPayView`
- Return: `PagedResult<HourlyPayListDto>`

### GetAsync [GET]
- Permission: `HourlyPayView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `HourlyPayView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `HourlyPayCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `HourlyPayEdit`
- Return: `IActionResult`
- Tavsif: Меҳнат таътили, фойдаланилмаган меҳнат таътили учун компенсация ва меҳнатга лаёқатсизлик варақаси ҳисоби ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `HourlyPayAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `HourlyPayCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `HourlyPayDelete`
- Return: `IActionResult`


## IncomeInKindController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IncomeInKindView`
- Return: `PagedResult<IncomeInKindListDto>`

### GetAsync [GET]
- Permission: `IncomeInKindView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeInKindView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeInKindCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `IncomeInKindEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `IncomeInKindAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `IncomeInKindCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `IncomeInKindDelete`
- Return: `IActionResult`

### PrintGetListIncomeInKind [POST]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`


## IncomeTaxRegistryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeTaxRegistryCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `IncomeTaxRegistryCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `IncomeTaxRegistryDelete`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `IncomeTaxRegistryAccept`
- Return: `IActionResult`

### Accept [POST]
- Permission: `IncomeTaxRegistryAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `IncomeTaxRegistryCancel`
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### SentAsync [POST]
- Permission: `IncomeTaxRegistrySent`
- Return: `IActionResult`

### GetOrganizationTableAsync [GET]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### UpdateOrganizationTableAsync [POST]
- Permission: `IncomeTaxRegistryEdit`
- Return: `IActionResult`

### FillOrganizationTableAsync [POST]
- Permission: `IncomeTaxRegistryFill`
- Return: `IActionResult`

### ClearOrganizationTableAsync [POST]
- Permission: `IncomeTaxRegistryFill`
- Return: `IActionResult`

### GetTablesAsync [GET]
- Permission: `IncomeTaxRegistryView`
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `IncomeTaxRegistryFill`
- Return: `IActionResult`

### ClearTableAsync [POST]
- Permission: `IncomeTaxRegistryFill`
- Return: `IActionResult`


## IndexationOfSalaryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IndexationOfSalaryView`
- Return: `PagedResult<IndexationOfSalaryListDto>`

### UpdateForAdminAsync [POST]
- Permission: `SalaryCalcViewAdmin`
- Return: `IActionResult`

### GetListForAdminAsync [POST]
- Permission: `SalaryCalcViewAdmin`
- Return: `PagedResult<IndexationOfSalaryListDto>`

### GetAsync [GET]
- Permission: `IndexationOfSalaryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IndexationOfSalaryView`
- Return: `IActionResult`

### GetTablesAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<IndexationOfSalaryTableDto>`

### ClearTableAsync [POST]
- Permission: `IndexationOfSalaryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IndexationOfSalaryCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `IndexationOfSalaryEdit`
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `IndexationOfSalaryEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `IndexationOfSalaryDelete`
- Return: `IActionResult`

### DeleteTableAsync [POST]
- Permission: `IndexationOfSalaryEdit`
- Return: `IActionResult`

### TestAsync [GET]
- Return: `IActionResult`

### PrintAsExcelAsync [GET]
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `IndexationOfSalaryAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `IndexationOfSalaryCancel`
- Return: `IActionResult`


## InpsRegistryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InpsRegistryView`
- Return: `PagedResult<InpsRegistryListDto>`

### GetAsync [GET]
- Permission: `InpsRegistryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InpsRegistryView`
- Return: `IActionResult`

### GetTablesAsync [POST]
- Permission: `InpsRegistryView`
- Return: `PagedResult<InpsRegistryTableDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `InpsRegistryEdit`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `InpsRegistryEdit`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `InpsRegistryAccept`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InpsRegistryCancel`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `InpsRegistryDelete`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини ўчириш

### FillAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тўлдириш

### FillAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тўлдириш

### SendAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тозалаш

### ClearAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тозалаш

### FillOrganizationDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тўлдириш (ташкилот ҳужжатлари)

### ClearOrganizationDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини тозалаш (ташкилот ҳужжатлари)

### CancelOrganizationDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини бекор қилиш (ташкилот ҳужжатлари)

### PrintAsExcelAsync [GET]
- Permission: `InpsRegistryView`
- Return: `IActionResult`
- Tavsif: ИНПС реестри ҳужжатини печать килиш

### FillOrganizations [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`

### GetInpsRegistriesFromChildsAsync [POST]
- Permission: `InpsRegistryView`
- Return: `IActionResult`

### CancelInpsRegistriesFromChildsAsync [POST]
- Permission: `InpsRegistryCancel`
- Return: `IActionResult`

### GetListForPaymentOrderAsync [POST]
- Permission: `InpsRegistryView`
- Return: `PagedResult<InpsRegistryListDto>`

### InsertDataAsync [POST]
- Permission: `InpsRegistryCreate`
- Return: `IActionResult`


## KindergardenTarifficationTitleController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `KindergardenTarifficationTitleView`
- Return: `PagedResult<KindergardenTarifficationTitleListDto>`

### GetAsync [GET]
- Permission: `KindergardenTarifficationTitleView`
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `KindergardenTarifficationTitleReciveNotRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `KindergardenTarifficationTitleReciveNotRecive`
- Return: `IActionResult`

### RejectAsync [POST]
- Permission: `KindergardenTarifficationTitleReciveNotRecive`
- Return: `IActionResult`


## LimitCalculationKindController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `LimitCalculationKindView`
- Return: `PagedResult<LimitCalculationKindListDto>`

### GetAsync [GET]
- Permission: `LimitCalculationKindView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `LimitCalculationKindView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `LimitCalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `LimitCalculationKindEdit`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `LimitCalculationKindAccept`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `LimitCalculationKindCancel`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `LimitCalculationKindDelete`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини ўчириш


## MandatoryCalcExclusionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `MandatoryCalcExclusionView`
- Return: `PagedResult<MandatoryCalcExclusionListDto>`

### GetAsync [GET]
- Permission: `MandatoryCalcExclusionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `MandatoryCalcExclusionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `MandatoryCalcExclusionCreate`
- Return: `IActionResult`
- Tavsif: Истисно ҳолатдаги ходимлар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `MandatoryCalcExclusionEdit`
- Return: `IActionResult`
- Tavsif: Истисно ҳолатдаги ходимлар ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `AppointEmployeeSalaryAccept`
- Return: `IActionResult`
- Tavsif: Истисно ҳолатдаги ходимлар ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `AppointEmployeeSalaryCancel`
- Return: `IActionResult`
- Tavsif: Истисно ҳолатдаги ходимлар ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `AppointEmployeeSalaryDelete`
- Return: `IActionResult`
- Tavsif: Истисно ҳолатдаги ходимлар ҳужжатини ўчириш


## OrgSchoolParameterController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `OrgSchoolParameterView`
- Return: `PagedResult<OrgSchoolParameterListDto>`

### GetAsync [GET]
- Permission: `OrgSchoolParameterView`
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `OrgSchoolParameterSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `OrgSchoolParameterSentToNotRecive`
- Return: `IActionResult`


## PayrollPlasticCardSheetController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetListDto>`

### PrintGetListCart [POST]
- Permission: `AverageSalaryControlView`
- Return: `IActionResult`

### GetListForAdminAsync [POST]
- Permission: `PayrollPlasticCardSheetViewAdmin`
- Return: `PagedResult<PayrollPlasticCardSheetListDto>`

### GetListFromOldAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetForSwitchAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### UpdateBankStatusStudentAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### UpdateBankStatusStudentAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetDocsAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IEnumerable<PayrollPlasticCardSheetDocDto>`

### GetTablesAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetTableDto>`

### GetTableSalariesAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetPayrollsFromChildsAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### CreateExternalAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини яратиш

### GetAndCreateExternalAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### UpdateStatusForAdminAsync [POST]
- Permission: `PayrollPlasticCardSheetViewAdmin`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини статусини админ тарафдан узгартириш

### ChangeCardAsync [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### CreateFromOldAsync [GET]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини табел кисмини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PayrollPlasticCardSheetDelete`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PayrollPlasticCardSheetAccept`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### FillOrganizationDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш (ташкилот ҳужжатлари)

### ClearOrganizationDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тозалаш (ташкилот ҳужжатлари)

### CancelOrganizationDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш (ташкилот ҳужжатлари)

### CancelPayrollsFromChildsAsync [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### Fill [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### FillDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### FillTrip [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### Upload [POST]
- Return: `IActionResult`

### RecalcByEmployee [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### ClearDocsAsync [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тозалаш

### PrintAsExcelAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини печать қилиш

### GetListForPaymentOrderAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetListDto>`

### CheckPaymentOrderAsync [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `PayrollPlasticCardSheetSend`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини жўнатиш

### CancelSendAsync [POST]
- Permission: `PayrollPlasticCardSheetCancelSend`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини жўнатишни бекор қилиш

### GetList [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetListDto`

### GetListForAdmin [POST]
- Permission: `PayrollPlasticCardSheetViewAdmin`
- Return: `PagedResult<PayrollPlasticCardSheetListDto`

### GetListFromOld [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### UpdateBankStatusStudent [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### UpdateBankStatusStudent [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetDocs [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IEnumerable<PayrollPlasticCardSheetDocDto`

### GetTables [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetTableDto`

### GetTableSalaries [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetPayrollsFromChilds [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### CreateExternal [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини яратиш

### GetAndCreateExternal [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`

### Create [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини яратиш

### Update [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### UpdateStatusForAdmin [POST]
- Permission: `PayrollPlasticCardSheetViewAdmin`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини статусини админ тарафдан узгартириш

### ChangeCard [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### UpdateTable [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини табел кисмини таҳрирлаш

### Delete [POST]
- Permission: `PayrollPlasticCardSheetDelete`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини ўчириш

### Accept [POST]
- Permission: `PayrollPlasticCardSheetAccept`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### FillOrganizationDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш (ташкилот ҳужжатлари)

### ClearOrganizationDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тозалаш (ташкилот ҳужжатлари)

### CancelOrganizationDocs [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш (ташкилот ҳужжатлари)

### CancelPayrollsFromChilds [POST]
- Permission: `PayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### Fill [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### FillDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### RecalcByEmployee [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`

### Clear [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### ClearDocs [POST]
- Permission: `PayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тозалаш

### PrintAsExcel [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини печать қилиш

### GetListForPaymentOrder [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollPlasticCardSheetListDto`

### CheckPaymentOrder [POST]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `IActionResult`

### Send [POST]
- Permission: `PayrollPlasticCardSheetSend`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини жўнатиш

### CancelSend [POST]
- Permission: `PayrollPlasticCardSheetCancelSend`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини жўнатишни бекор қилиш


## PayrollSalaryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PayrollSalaryView`
- Return: `PagedResult<PayrollSalaryListDto>`

### GetAsync [GET]
- Permission: `PayrollSalaryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollSalaryView`
- Return: `IActionResult`

### GetByOrgSettlementAccountIdAsync [GET]
- Permission: `PayrollSalaryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PayrollSalaryCreate`
- Return: `IActionResult`
- Tavsif: Иш ҳақи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollSalaryEdit`
- Return: `IActionResult`
- Tavsif: Иш ҳақи ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `PayrollSalaryCanCLone`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `PayrollSalaryAccept`
- Return: `IActionResult`
- Tavsif: Иш ҳақи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollSalaryCancel`
- Return: `IActionResult`
- Tavsif: Иш ҳақи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PayrollSalaryDelete`
- Return: `IActionResult`
- Tavsif: Иш ҳақи ҳужжатини ўчириш


## PayrollSheetController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PayrollSheetView`
- Return: `PagedResult<PayrollSheetListDto>`

### GetListForInPaymentAsync [POST]
- Permission: `PayrollSheetView`
- Return: `PagedResult<PayrollSheetListDto>`

### GetListFromOldAsync [POST]
- Permission: `PayrollSheetView`
- Return: `IActionResult`

### CreateFromOldAsync [GET]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш

### GetAsync [GET]
- Permission: `PayrollSheetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollSheetView`
- Return: `IActionResult`

### GetDocsAsync [GET]
- Permission: `PayrollSheetView`
- Return: `IEnumerable<PayrollSheetDocDto>`

### GetTablesAsync [GET]
- Permission: `PayrollPlasticCardSheetView`
- Return: `PagedResult<PayrollSheetTableDto>`

### CreateAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `PayrollSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини табел кисмини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PayrollSheetDelete`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PayrollSheetAccept`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини бекор қилиш

### Fill [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тўлдириш

### FillDocsAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тозалаш

### ClearDocsAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тозалаш

### FillOrganizationDocsAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тўлдириш (ташкилот ҳужжатлари)

### ClearOrganizationDocsAsync [POST]
- Permission: `PayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини тозалаш (ташкилот ҳужжатлари)

### CancelOrganizationDocsAsync [POST]
- Permission: `PayrollSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси ҳужжатини бекор қилиш (ташкилот ҳужжатлари)

### GetListForPaymentOrderAsync [POST]
- Permission: `PaymentOrderView`
- Return: `PagedResult<PayrollSheetListDto>`

### PrintAsExcelAsync [GET]
- Permission: `PayrollSheetView`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси қайдномаси ҳужжатини печать қилиш

### PrintBydepartmentAsync [GET]
- Permission: `PayrollSheetView`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси қайдномаси ҳужжатини печать қилиш


## PayrollSheetDeductionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PayrollSheetDeductionView`
- Return: `PagedResult<PayrollSheetDeductionListDto>`

### GetAsync [GET]
- Permission: `PayrollSheetDeductionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollSheetDeductionView`
- Return: `IActionResult`

### GetTablesAsync [POST]
- Permission: `PayrollSheetDeductionView`
- Return: `PagedResult<PayrollSheetDeductionTableDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PayrollSheetDeductionCreate`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollSheetDeductionEdit`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `PayrollSheetDeductionEdit`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PayrollSheetDeductionAccept`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollSheetDeductionCancel`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PayrollSheetDeductionDelete`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини ўчириш

### FillAsync [POST]
- Permission: `PayrollSheetDeductionCreate`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `PayrollSheetDeductionCreate`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини тозалаш

### PrintAsExcelAsync [GET]
- Permission: `PayrollSheetDeductionView`
- Return: `IActionResult`
- Tavsif: Ушланмалар бўйича ведомость ҳужжатини печать килиш


## PlanExecutionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PlanExecutionView`
- Return: `PagedResult<PlanExecutionListDto>`

### GetAsync [GET]
- Permission: `PlanExecutionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PlanExecutionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PlanExecutionCreate`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини яратиш

### ClearAsync [POST]
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини тозалаш

### UpdateAsync [POST]
- Permission: `PlanExecutionEdit`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PlanExecutionAccept`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PlanExecutionCancel`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PlanExecutionDelete`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини ўчириш

### FillTableAsync [POST]
- Permission: `PlanExecutionCreate`
- Return: `IActionResult`
- Tavsif: Тушум режаси ҳужжатини тўлдириш


## PlasticCardRequestController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PlasticCardRequestView`
- Return: `PagedResult<PlasticCardRequestListDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`

### AcceptAsync [POST]
- Return: `IActionResult`

### CancelAsync [POST]
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `PlasticCardRequestSend`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `PlasticCardRequestSend`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини жўнатиш


## PreferentialOrganizationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PreferentialOrganizationView`
- Return: `PagedResult<PreferentialOrganizationListDto>`

### GetAsync [GET]
- Permission: `PreferentialOrganizationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PreferentialOrganizationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PreferentialOrganizationCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PreferentialOrganizationEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `PreferentialOrganizationAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `PreferentialOrganizationCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PreferentialOrganizationDelete`
- Return: `IActionResult`


## RecalcOfSalaryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RecalcOfSalaryView`
- Return: `PagedResult<RecalcOfSalaryListDto>`

### GetAsync [GET]
- Permission: `RecalcOfSalaryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RecalcOfSalaryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### FillAsync [POST]
- Permission: `RecalcOfSalaryEdit`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RecalcOfSalaryCreate`
- Return: `IActionResult`
- Tavsif: Ўтган давр учун қайта ҳисоб-китоб ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RecalcOfSalaryEdit`
- Return: `IActionResult`
- Tavsif: Ўтган давр учун қайта ҳисоб-китоб ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `RecalcOfSalaryDelete`
- Return: `IActionResult`
- Tavsif: Ўтган давр учун қайта ҳисоб-китоб ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `RecalcOfSalaryAccept`
- Return: `IActionResult`
- Tavsif: Ўтган давр учун қайта ҳисоб-китоб тасдиқлаш

### CancelAsync [POST]
- Permission: `RecalcOfSalaryCancel`
- Return: `IActionResult`
- Tavsif: Ўтган давр учун қайта ҳисоб-китоб бекор қилиш


## RequestReceivingCashController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `PagedResult<RequestReceivingCashListDto>`

### GetListSentsAsync [POST]
- Permission: `RequestReceivingCashSentsView`
- Return: `PagedResult<RequestReceivingCashListDto>`

### GetListDeductionTableAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `PagedResult<RequestReceivingCashDeductionTableDto>`

### GetListOldAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### PostFromOldAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### GetAdminAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetRequestReceivingCashTableAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `PagedResult<RequestReceivingCashTableDto>`

### FillDocTable [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини тозалаш

### FillTableAsync [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини табел қисмини тўлдириш

### FillDeduction [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини табел қисмини тўлдириш

### GetByDocId [GET]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`

### GetRequesRecevingCashsFromChildsAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RequestReceivingCashEdit`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини ўчириш

### UpdateDeductionTableAsync [POST]
- Permission: `RequestReceivingCashEdit`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `RequestReceivingCashAccept`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини ўчириш

### CancelAsync [POST]
- Permission: `RequestReceivingCashCancel`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини ўчириш

### ClearOrganizationDocsAsync [POST]
- Permission: `RequestReceivingCashCreate`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини тозалаш (ташкилот ҳужжатлари)

### CancelOrganizationDocsAsync [POST]
- Permission: `RequestReceivingCashCancel`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини ўчириш (ташкилот ҳужжатлари)

### GetEmployeeListForDeductionAsync [GET]
- Permission: `RequestReceivingCashEdit`
- Return: `IActionResult`

### GetItemOfExpenceListForDeductionAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### CancelRequestRecevingCashsFromChildsAsync [POST]
- Permission: `RequestReceivingCashCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `RequestReceivingCashDelete`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини ўчириш

### UpdateControlAsync [POST]
- Permission: `UserView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатидан чекловни олиш

### AcceptByAdminAsync [POST]
- Permission: `UserView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатидан чекловни олиш

### GetHashAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `RequestReceivingCashSend`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини жўнатиш

### CancelSend [POST]
- Permission: `RequestReceivingCashCancelSend`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини жўнатишни бекор қилиш

### UpdateDocOnAsync [POST]
- Permission: `RequestReceivingCashUpdateDocOn`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини тахрирлаш

### PrintAsExcel [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини печать қилиш

### PrintAsExcelAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини печать қилиш

### PrintNewAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини печать қилиш

### TEstUpdateAsync [POST]
- Return: `IActionResult`

### GetListForPaymentOrderAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `PagedResult<RequestReceivingCashListDto>`

### GetReqReceivingCashTableAsync [POST]
- Permission: `RequestReceivingCashView`
- Return: `List<ReqReceivingCashTableDto>`

### PrintQuickAsync [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`
- Tavsif: Суровнома ҳужжатини печать қилиш

### GetDeductionTables [GET]
- Permission: `RequestReceivingCashView`
- Return: `IActionResult`


## SalaryCalcController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SalaryCalcView`
- Return: `PagedResult<SalaryCalcListDto>`

### GetListForAdminAsync [POST]
- Permission: `SalaryCalcViewAdmin`
- Return: `PagedResult<SalaryCalcListDto>`

### GetAsync [GET]
- Permission: `SalaryCalcView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SalaryCalcView`
- Return: `IActionResult`

### GetEnrolmentsAsync [POST]
- Permission: `SalaryCalcView`
- Return: `IActionResult`

### GetRowsByEnrolmentIdAsync [GET]
- Permission: `SalaryCalcView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SalaryCalcEdit`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `SalaryCalcAccept`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини тасдиқлаш

### Accept [POST]
- Permission: `SalaryCalcAccept`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `SalaryCalcCancel`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `SalaryCalcDelete`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини ўчириш

### UpdateStatusForAdminAsync [POST]
- Permission: `SalaryCalcViewAdmin`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини ўчириш

### FillAsync [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини тозалаш

### SalaryCalcReportAsExcelAsync [POST]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини печать қилиш

### SalaryCalcReportTotalAsExcelAsync [POST]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини печать қилиш

### SalaryCalcTotalReportAsExcelAsync [GET]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини жамланма печать қилиш

### SalaryCalcEnrolmentsReportAsExcelAsync [GET]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Ойлик ҳисоби ҳужжатини тўлиқ печать қилиш

### TotalMonthlySalaryCalcAsync [POST]
- Permission: `SalaryCalcView`
- Return: `IActionResult`

### TotalMonthlySalaryCalcAsExcelAsync [POST]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Ойлик умумий ҳисоби ҳужжатини печать қилиш

### ThePaySheetForMonthAsExcelAsync [POST]
- Permission: `SalaryCalcPrint`
- Return: `IActionResult`
- Tavsif: Расчетный листок за месяц

### FillIncomeTaxForOldCalcsAsync [POST]
- Permission: `SalaryCalcCreate`
- Return: `IActionResult`


## SalaryCalcRiskControlController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<SalaryCalcRiskControlListDto>`

### GetAsync [GET]
- Return: `IActionResult`


## SchoolHourlyPayRateController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolHourlyPayRateView`
- Return: `PagedResult<SchoolHourlyPayRateListDto>`

### GetAsync [GET]
- Permission: `SchoolHourlyPayRateView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SchoolHourlyPayRateView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SchoolHourlyPayRateCreate`
- Return: `IActionResult`
- Tavsif: Соатбай ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SchoolHourlyPayRateEdit`
- Return: `IActionResult`
- Tavsif: Соатбай ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SchoolHourlyPayRateDelete`
- Return: `IActionResult`
- Tavsif: Соатбай ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `SchoolHourlyPayRateAccept`
- Return: `IActionResult`
- Tavsif: Соатбай ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `SchoolHourlyPayRateCancel`
- Return: `IActionResult`
- Tavsif: Соатбай ҳужжатини бекор қилиш


## SportTarifficationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SportTarifficationView`
- Return: `PagedResult<SportTarifficationListDto>`
- Tavsif: Тарификация ҳужжатини кўриш

### GetAsync [GET]
- Permission: `SportTarifficationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SportTarifficationView`
- Return: `IActionResult`

### GetForHeaderAsync [GET]
- Permission: `SportTarifficationViewSendHeader`
- Return: `IActionResult`

### GetCalculationKindListAsync [GET]
- Permission: `SportTarifficationView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `SportTarifficationCreate`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини ҳужжатини тозалаш

### FillAsync [POST]
- Permission: `SportTarifficationAccept`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини тўлириш

### AcceptAsync [POST]
- Permission: `SportTarifficationAccept`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `SportTarifficationCancel`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `SportTarifficationDelete`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини ўчириш

### GetHashAsync [GET]
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `SportTarifficationView`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини марказга жўнатиш

### GetListSentToHeaderAsync [POST]
- Permission: `SportTarifficationViewSendHeader`
- Return: `PagedResult<SportTarifficationListDto>`

### ReciveSentToHeaderAsync [POST]
- Permission: `SportTarifficationReciveSendHeader`
- Return: `IActionResult`

### NotReciveSentToHeaderAsync [POST]
- Permission: `SportTarifficationNotReciveSendToHeader`
- Return: `IActionResult`

### ArchiveSentToHeaderAsync [POST]
- Permission: `SportTarifficationArchiveSendToHeader`
- Return: `IActionResult`

### PrintAsExcel [GET]
- Permission: `SportTarifficationPrint`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини печать килиш

### PrintForHeader [GET]
- Permission: `SportTarifficationViewSendHeader`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини печать килиш

### CreateCalcKindTableAsync [POST]
- Permission: `SportTarifficationCreate`
- Return: `IActionResult`
- Tavsif: Tarifikatsiya hujjatiga to'lov turini qo'shish

### DeleteCalcKindTableAsync [POST]
- Permission: `SportTarifficationDelete`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини ўчириш

### RecalcCalcKindAsync [POST]
- Permission: `SportTarifficationCreate`
- Return: `IActionResult`


## SportTarifficationTitleController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `SportTarifficationTitleView`
- Return: `PagedResult<SportTarifficationTitleListDto`

### HeaderGetList [POST]
- Permission: `SportTarifficationTitleSentToRecive`
- Return: `PagedResult<SportTarifficationTitleListDto`

### Get [GET]
- Permission: `SportTarifficationTitleView`
- Return: `IActionResult`

### GetForHeader [GET]
- Permission: `SportTarifficationTitleSentToRecive`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `SportTarifficationTitleSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `SportTarifficationTitleSentToNotRecive`
- Return: `IActionResult`

### GetGroupHours [GET]
- Permission: `SportTarifficationTitleView`
- Return: `IActionResult`


## StaffingController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingListDto>`

### GetAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### DoesNotRegisteredAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### FillAsync [POST]
- Permission: `StaffingView`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали ҳужжатини тўлириш

### GetAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetForViewAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали ҳужжатини тозалаш

### UpdateAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини таҳрирлаш

### GetAllStaffingPositionsAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetAllStaffingPositionsFromStructureAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetStaffingTemplateAsync [GET]
- Return: `IActionResult`

### GetAllStaffingPositionClassificationsAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### FillStaffingPositionsAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetStaffingPositionAsync [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetStaffingPositionFromStructureAsync [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### FillIndicatorAsync [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetListStaffingAdditionalPaymentForLongWork [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### CreateStaffingAdditionalPaymentForLongWorkAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingAdditionalPaymentForLongWorkAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingAdditionalPaymentForLongWorkAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### DeleteStaffingAdditionalPaymentForLongWorkAllAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### FillStaffingAdditionalPaymentForLongWorkAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetListStaffingAdditionalPersonalBenefitAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingAdditionalPersonalBenefitDto>`

### CreateStaffingAdditionalPersonalBenefitAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingAdditionalPersonalBenefitAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingAdditionalPersonalBenefitAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### FillStaffingAdditionalPersonalBenefitAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### DeleteStaffingAdditionalPersonalBenefitAllAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetListStaffingDayOffHolidayTableAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingDayOffHolidayTableDto>`

### CreateStaffingDayOffHolidayTableAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingDayOffHolidayTableAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingDayOffHolidayTableAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetListStaffingNightWorkTimeTableAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingNightWorkTimeTableDto>`

### CreateStaffingNightWorkTimeTableAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingNightWorkTimeTableAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingNightWorkTimeTableAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetListStaffingOtherCalculationsTableAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingOtherCalculationsTableDto>`

### CreateStaffingOtherCalculationsTableAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingOtherCalculationsTableAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingOtherCalculationsTableAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetListStaffingTarifficationAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingTarifficationDto>`

### CreateStaffingTarifficationAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### UpdateStaffingTarifficationAsync [POST]
- Permission: `StaffingEdit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteStaffingTarifficationAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetTarifficationType [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### GetPositionListAsync [POST]
- Permission: `StaffingView`
- Return: `PagedResult<StaffingPositionDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetPositionClassifierAsync [GET]
- Return: `IActionResult`

### GetAsSelectListForMonthLyAllocationAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### GetCloneAsync [GET]
- Permission: `StaffingCreate`
- Return: `IActionResult`

### RecalcStaffingCalcKindTablesAsync [POST]
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `StaffingAccept`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StaffingCancel`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingDelete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### CreateFromExcelAsync [POST]
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини печать қилиш

### PrintFullAsync [POST]
- Return: `IActionResult`

### PrintFullForViewAsync [POST]
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `StaffingReadyToSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишга таёрлаш

### CancelReadyToSendAsync [POST]
- Permission: `StaffingCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишни бекор қилиш

### GetHashAsync [GET]
- Permission: `StaffingView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `StaffingSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатиш

### GetListSentToHeader [POST]
- Permission: `StaffingSentToHeader`
- Return: `PagedResult<StaffingListDto>`

### GetListSentToHeaderDepartmentAsync [POST]
- Permission: `StaffingViewToDepartment`
- Return: `PagedResult<StaffingHeaderDepartmentListDto>`

### ReciveAsync [POST]
- Permission: `StaffingSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `StaffingSentToNotRecive`
- Return: `IActionResult`

### ApprovedAsync [POST]
- Permission: `StaffingSentToApproved`
- Return: `IActionResult`

### AgreedAsync [POST]
- Permission: `StaffingSentToAgreed`
- Return: `IActionResult`

### AgreedFinOrgAsync [POST]
- Permission: `StaffingSentToAgreedFinOrg`
- Return: `IActionResult`

### RegisteredAsync [POST]
- Permission: `StaffingSentToRegistered`
- Return: `IActionResult`

### GetReasonTemporaryTypeListAsync [GET]
- Return: `IActionResult`


## StaffingForm15Controller
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `StaffingForm15View`
- Return: `PagedResult<StaffingForm15ListDto`

### Get [GET]
- Permission: `StaffingForm15View`
- Return: `IActionResult`

### Get [GET]
- Permission: `StaffingForm15View`
- Return: `IActionResult`

### GetForView [GET]
- Permission: `StaffingForm15View`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StaffingForm15Create`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### Update [POST]
- Permission: `StaffingForm15Edit`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StaffingForm15Accept`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StaffingForm15Cancel`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StaffingForm15Delete`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### ReadyToSend [POST]
- Permission: `StaffingForm15ReadyToSend`
- Return: `ActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишга таёрлаш

### CancelReadyToSend [POST]
- Permission: `StaffingForm15CancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишни бекор қилиш

### GetHash [GET]
- Permission: `StaffingForm15View`
- Return: `IActionResult`

### Send [POST]
- Permission: `StaffingForm15Send`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатиш

### GetListSentToHeader [POST]
- Permission: `StaffingForm15SentToHeader`
- Return: `PagedResult<StaffingForm15ListDto`

### Recive [POST]
- Permission: `StaffingForm15SentToRecive`
- Return: `IActionResult`

### NotRecive [POST]
- Permission: `StaffingForm15SentToNotRecive`
- Return: `IActionResult`

### Approved [POST]
- Permission: `StaffingForm15SentToApproved`
- Return: `IActionResult`

### Agreed [POST]
- Permission: `StaffingForm15SentToAgreed`
- Return: `IActionResult`

### AgreedFinOrg [POST]
- Permission: `StaffingForm15SentToAgreedFinOrg`
- Return: `IActionResult`

### Registered [POST]
- Permission: `StaffingForm15SentToRegistered`
- Return: `IActionResult`

### GetActivePositionWithOrgStructure [POST]
- Permission: `StaffingForm15View`
- Return: `IActionResult`

### Print [GET]
- Return: `IActionResult`


## StaffingForm15RegisteryController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `StaffingForm15RegisteryView`
- Return: `PagedResult<StaffingForm15RegisteryListDto`

### Get [GET]
- Permission: `StaffingForm15RegisteryView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StaffingForm15RegisteryView`
- Return: `IActionResult`

### GetStaffingForm15 [GET]
- Permission: `StaffingForm15RegisteryView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StaffingForm15RegisteryCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `StaffingForm15RegisteryEdit`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StaffingForm15RegisteryAccept`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StaffingForm15RegisteryCancel`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StaffingForm15RegisteryDelete`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини ўчириш

### FillStaffingForm15Registery [POST]
- Permission: `StaffingForm15RegisteryCreate`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини тўлдириш

### ClearTable [POST]
- Permission: `StaffingForm15RegisteryEdit`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `StaffingForm15RegisteryView`
- Return: `IActionResult`

### Send [POST]
- Permission: `StaffingForm15RegisterySend`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини жўнатиш

### GetListSentToCenter [POST]
- Permission: `StaffingForm15RegisterySentToCenter`
- Return: `PagedResult<StaffingForm15RegisteryListDto`

### NotAcceptCenter [POST]
- Permission: `StaffingForm15RegisterySentToCancel`
- Return: `IActionResult`

### Print [GET]
- Permission: `StaffingForm15RegisteryView`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини печать қилиш

### PrintSentToCenter [GET]
- Permission: `StaffingForm15RegisterySentToCenter`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини печать қилиш

### Approved [POST]
- Permission: `StaffingForm15RegisterySentToApproved`
- Return: `IActionResult`


## StaffingForm15TotalController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `StaffingForm15TotalView`
- Return: `PagedResult<StaffingForm15TotalListDto`

### Get [GET]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`

### GetForView [GET]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`

### GetStaffingForm15 [GET]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `StaffingForm15TotalCreate`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини яратиш

### FillStaffingForm15Total [POST]
- Permission: `StaffingForm15TotalCreate`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини тўлдириш

### ClearTotalTable [POST]
- Permission: `StaffingForm15TotalEdit`
- Return: `IActionResult`

### Update [POST]
- Permission: `StaffingForm15TotalEdit`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StaffingForm15TotalAccept`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини тасдиқлаш

### GetHash [GET]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`

### GetListStaffingForm15TotalPosition [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### ReadyToSend [POST]
- Permission: `StaffingForm15TotalReadyToSend`
- Return: `IActionResult`
- Tavsif: 15- Илова ҳужжатини жўнатишга таёрлаш

### CancelReadyToSend [POST]
- Permission: `StaffingForm15TotalCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: 15- Илова ҳужжатини жўнатишни бекор қилиш

### Send [POST]
- Permission: `StaffingForm15TotalSend`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини жўнатиш

### Cancel [POST]
- Permission: `StaffingForm15TotalCancel`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StaffingForm15TotalDelete`
- Return: `IActionResult`
- Tavsif: 15- Илова йиғиш ҳужжатини ўчириш

### GetListSentToHeader [POST]
- Permission: `StaffingForm15TotalSentToHeader`
- Return: `PagedResult<StaffingForm15TotalListDto`

### AcceptHeader [POST]
- Permission: `StaffingForm15TotalSentToAccept`
- Return: `IActionResult`

### NotAcceptHeader [POST]
- Permission: `StaffingForm15TotalSentToCancel`
- Return: `IActionResult`

### Approved [POST]
- Permission: `StaffingForm15TotalSentToApproved`
- Return: `IActionResult`

### Agreed [POST]
- Permission: `StaffingForm15TotalSentToAgreed`
- Return: `IActionResult`

### AgreedFinOrg [POST]
- Permission: `StaffingForm15TotalSentToAgreedFinOrg`
- Return: `IActionResult`

### Registered [POST]
- Permission: `StaffingForm15TotalSentToRegistered`
- Return: `IActionResult`

### Print [POST]
- Permission: `StaffingForm15TotalView`
- Return: `IActionResult`


## StaffingForm4Controller
Route: `StaffingForm4/[action]`

### GetListAsync [POST]
- Permission: `StaffingForm4View`
- Return: `PagedResult<StaffingForm4ListDto>`

### GetAsync [GET]
- Permission: `StaffingForm4View`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingForm4View`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingForm4Create`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffingForm4Edit`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StaffingForm4Accept`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StaffingForm4Cancel`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини бекор қилиш

### RecalcStaffingForm4Async [POST]
- Permission: `StaffingForm4Cancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `StaffingForm4Delete`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини ўчириш

### Print [GET]
- Permission: `StaffingForm4View`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини печать қилиш

### FillAsync [POST]
- Permission: `StaffingForm4Create`
- Return: `IActionResult`
- Tavsif: Штат жадвали (4 - Илова) ҳужжатини тўлириш


## StaffingForm5Controller
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingForm5View`
- Return: `PagedResult<StaffingForm5ListDto>`
- Tavsif: Штат жадвали (5- Илова) ҳужжатини кўриш

### GetCalcKindListAsync [GET]
- Permission: `StaffingForm5View`
- Return: `List<StaffingForm5CalcKindDto>`

### GetAsync [GET]
- Permission: `StaffingForm5View`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingForm5View`
- Return: `IActionResult`

### GetTableAsync [GET]
- Permission: `StaffingForm5View`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `StaffingForm5Create`
- Return: `IActionResult`
- Tavsif: Штат жадвали (5 - Илова) ҳужжатини ҳужжатини тозалаш

### FillAsync [POST]
- Permission: `StaffingForm5Create`
- Return: `IActionResult`
- Tavsif: Штат жадвали (5 - Илова) ҳужжатини тўлириш

### AcceptAsync [POST]
- Permission: `StaffingForm5Accept`
- Return: `IActionResult`
- Tavsif: Штат жадвали (5 - Илова) ҳужжатини тасдиқлаш

### UpdateTableAsync [POST]
- Permission: `StaffingForm5Create`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `StaffingForm5Cancel`
- Return: `IActionResult`
- Tavsif: ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingForm5Delete`
- Return: `IActionResult`
- Tavsif: Штат жадвали (5 - Илова) ҳужжатини ўчириш

### RecalcCalcKindAsync [POST]
- Permission: `StaffingForm5Create`
- Return: `IActionResult`

### PrintAsync [GET]
- Permission: `StaffingForm5View`
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

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingPositionReplacementCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffingPositionReplacementEdit`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини таҳрирлаш

### GetVacansyStaffingPositionsAsync [POST]
- Permission: `StaffingPositionReplacementView`
- Return: `IActionResult`

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


## StaffingRegisteryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingRegisteryView`
- Return: `PagedResult<StaffingRegisteryListDto>`

### GetTable [POST]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`

### GetStaffingAsync [GET]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingRegisteryCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StaffingRegisteryEdit`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StaffingRegisteryAccept`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StaffingRegisteryCancel`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingRegisteryDelete`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини ўчириш

### FillStaffingRegisteryAsync [POST]
- Permission: `StaffingRegisteryCreate`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини тўлдириш

### ClearTableAsync [POST]
- Permission: `StaffingRegisteryEdit`
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `StaffingRegisterySend`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини жўнатиш

### GetListSentToCenterAsync [POST]
- Permission: `StaffingRegisterySentToCenter`
- Return: `PagedResult<StaffingRegisteryListDto>`

### NotAcceptCenterAsync [POST]
- Permission: `StaffingRegisterySentToCancel`
- Return: `IActionResult`

### Print [GET]
- Permission: `StaffingRegisteryView`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини печать қилиш

### PrintSentToCenter [GET]
- Permission: `StaffingRegisterySentToCenter`
- Return: `IActionResult`
- Tavsif: Штат ҳужжатини печать қилиш

### ApprovedAsync [POST]
- Permission: `StaffingRegisterySentToApproved`
- Return: `IActionResult`


## StaffingTemplateController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingTemplateView`
- Return: `PagedResult<StaffingTemplateListDto>`

### GetAsync [GET]
- Permission: `StaffingTemplateView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingTemplateView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTableAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingTemplateCreate`
- Return: `IActionResult`
- Tavsif: Намунавий штатлар жадвали ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffingTemplateEdit`
- Return: `IActionResult`
- Tavsif: Намунавий штатлар жадвали ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StaffingTemplateAccept`
- Return: `IActionResult`
- Tavsif: Намунавий штатлар жадвали ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StaffingTemplateCancel`
- Return: `IActionResult`
- Tavsif: Намунавий штатлар жадвали ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingTemplateDelete`
- Return: `IActionResult`
- Tavsif: Намунавий штатлар жадвали ҳужжатини ўчириш


## StaffingTotalController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingTotalView`
- Return: `PagedResult<StaffingTotalListDto>`

### GetAsync [GET]
- Permission: `StaffingTotalView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingTotalView`
- Return: `IActionResult`

### GetFastAndFuriousAsync [GET]
- Permission: `StaffingTotalView`
- Return: `IActionResult`

### GetStaffingAsync [GET]
- Permission: `StaffingTotalView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingTotalCreate`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини яратиш

### FillStaffingTotalAsync [POST]
- Permission: `StaffingTotalCreate`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини тўлдириш

### ClearTotalTableAsync [POST]
- Permission: `StaffingTotalEdit`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StaffingTotalEdit`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StaffingTotalAccept`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини тасдиқлаш

### GetHashAsync [GET]
- Permission: `StaffingTotalView`
- Return: `IActionResult`

### GetListStaffingTotalPositionAsync [POST]
- Permission: `StaffingView`
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `StaffingTotalReadyToSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишга таёрлаш

### CancelReadyToSendAsync [POST]
- Permission: `StaffingTotalCancelReadyToSend`
- Return: `IActionResult`
- Tavsif: Шатат жадвали ҳужжатини жўнатишни бекор қилиш

### SendAsync [POST]
- Permission: `StaffingTotalSend`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини жўнатиш

### CancelAsync [POST]
- Permission: `StaffingTotalCancel`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StaffingTotalDelete`
- Return: `IActionResult`
- Tavsif: Штатлар жадвали йиғиш ҳужжатини ўчириш

### GetListSentToHeaderAsync [POST]
- Permission: `StaffingTotalSentToHeader`
- Return: `PagedResult<StaffingTotalListDto>`

### AcceptHeaderAsync [POST]
- Permission: `StaffingTotalSentToAccept`
- Return: `IActionResult`

### NotAcceptHeaderAsync [POST]
- Permission: `StaffingTotalSentToCancel`
- Return: `IActionResult`

### ApprovedAsync [POST]
- Permission: `StaffingTotalSentToApproved`
- Return: `IActionResult`

### AgreedAsync [POST]
- Permission: `StaffingTotalSentToAgreed`
- Return: `IActionResult`

### AgreedFinOrgAsync [POST]
- Permission: `StaffingTotalSentToAgreedFinOrg`
- Return: `IActionResult`

### RegisteredAsync [POST]
- Permission: `StaffingTotalSentToRegistered`
- Return: `IActionResult`

### PrintAsync [POST]
- Return: `IActionResult`

### PrintFastAsync [POST]
- Return: `IActionResult`


## TarifficationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TarifficationView`
- Return: `PagedResult<TarifficationListDto>`
- Tavsif: Тарификация ҳужжатини кўриш

### GetAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`

### GetForHeaderAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`

### GetCalculationKindListAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `TarifficationCreate`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини ҳужжатини тозалаш

### FillAsync [POST]
- Permission: `TarifficationAccept`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини тўлириш

### AcceptAsync [POST]
- Permission: `TarifficationAccept`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `TarifficationCancel`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `TarifficationDelete`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини ўчириш

### GetTarifficationVacansyHoursAsync [POST]
- Permission: `TarifficationTeacherVacancyReport`
- Return: `IActionResult`

### GetTarifficationVacansyHoursByOrgSchGradeAsync [POST]
- Permission: `TarifficationTeacherVacancyReport`
- Return: `IActionResult`

### GetTarifficationTeacherHoursAsync [POST]
- Permission: `TarifficationTeacherHoursReport`
- Return: `IActionResult`

### GetTeacherHoursBySchoolGradeAsync [POST]
- Permission: `TarifficationTeacherHoursReport`
- Return: `IActionResult`

### PrintAsExcelAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини печать килиш

### PrintDividedAsExcelAsync [GET]
- Permission: `TarifficationView`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини печать килиш

### GetListSentToCenterAsync [POST]
- Permission: `TarifficationViewSendToCenter`
- Return: `PagedResult<TarifficationListDto>`
- Tavsif: Тарификация ҳужжатини марказга юборилганларни кўриш

### SendAsync [POST]
- Permission: `TarifficationView`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини марказга жўнатиш

### GetHashAsync [GET]
- Return: `IActionResult`

### ReciveSentToCenterAsync [POST]
- Permission: `TarifficationReciveSendToCenter`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини марказ қабул қилиш

### NotReciveSentToCenterAsync [POST]
- Permission: `TarifficationNotReciveSendToCenter`
- Return: `IActionResult`
- Tavsif: Тарификация ҳужжатини марказ қабул қайтариш

### GetListSentToHeaderAsync [POST]
- Permission: `TarifficationViewSendHeader`
- Return: `PagedResult<TarifficationListDto>`

### GetListSentToHeaderAsync2 [POST]
- Permission: `TarifficationViewSendHeader`
- Return: `PagedResult<GetListForHeaderDto>`

### ReciveSentToHeaderAsync [POST]
- Permission: `TarifficationReciveSendHeader`
- Return: `IActionResult`

### NotReciveSentToHeaderAsync [POST]
- Permission: `TarifficationNotReciveSendToHeader`
- Return: `IActionResult`

### ArchiveSentToHeaderAsync [POST]
- Permission: `TarifficationArchiveSendToHeader`
- Return: `IActionResult`


## TarifficationTitleController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TarifficationTitleView`
- Return: `PagedResult<TarifficationTitleListDto>`

### HeaderGetListAsync [POST]
- Permission: `TarifficationTitleSentToRecive`
- Return: `PagedResult<TarifficationTitleListDto>`

### GetAsync [GET]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`

### GetForHeaderAsync [GET]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`

### GetStudentCountAsync [GET]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetGroupSelectListAsync [GET]
- Return: `IActionResult`

### ReciveAsync [POST]
- Permission: `TarifficationTitleSentToRecive`
- Return: `IActionResult`

### NotReciveAsync [POST]
- Permission: `TarifficationTitleSentToNotRecive`
- Return: `IActionResult`

### ChangeOrgStuctureAsync [POST]
- Return: `IActionResult`

### ChangeOrgStructureWithChildCountAsync [POST]
- Return: `IActionResult`

### GetTarifficationTitleByOnDateAsync [POST]
- Return: `IActionResult`

### GetTarifficationTitleHistoryByOnDateAsync [POST]
- Return: `IActionResult`

### PrintAsync [POST]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`

### PrintForHeaderAsync [POST]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`

### TarifficationTitleByOnDatePrintAsync [POST]
- Permission: `TarifficationTitleView`
- Return: `IActionResult`


## TaxRateController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `TaxRateView`
- Return: `PagedResult<TaxRateListDto>`

### Get [GET]
- Permission: `TaxRateView`
- Return: `IActionResult`

### Get [GET]
- Permission: `TaxRateView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `TaxRateCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `TaxRateEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `TaxRateAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `TaxRateCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `TaxRateDelete`
- Return: `IActionResult`


## TeacherHourController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TeacherHourView`
- Return: `PagedResult<TeacherHourListDto>`

### GetAsync [GET]
- Permission: `TeacherHourView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TeacherHourView`
- Return: `IActionResult`

### GetAmountAsync [GET]
- Permission: `TeacherHourView`
- Return: `IActionResult`

### GetTarifSacelAsync [GET]
- Permission: `TeacherHourView`
- Return: `IActionResult`

### GetPostionCategoryIdAsync [GET]
- Permission: `TeacherHourView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TeacherHourCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини яратиш

### UpdateTableAsync [POST]
- Permission: `TeacherHourCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини таҳрирлаш

### ClearAsync [POST]
- Permission: `TeacherHourCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳисобини тозалаш

### RecalcTeacherHourAsync [POST]
- Permission: `TeacherHourCreate`
- Return: `IActionResult`
- Tavsif: Пед. ходимларга иш ҳақини қайта ҳисоблаш

### UpdateAsync [POST]
- Permission: `TeacherHourEdit`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `TeacherHourAccept`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `TeacherHourCancel`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `TeacherHourDelete`
- Return: `IActionResult`
- Tavsif: Пед. ходимлар иш ҳақи ҳужжатини ўчириш


## ConstantValueController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ConstantValueView`
- Return: `PagedResult<ConstantValueListDto>`

### GetAsync [GET]
- Permission: `ConstantValueView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ConstantValueView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ConstantValueCreate`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ConstantValueEdit`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ConstantValueDelete`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини ўчириш


## HlCalculationKindTransactionController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `HlCalculationKindTransactionView`
- Return: `PagedResult<HlCalculationKindTransactionListDto>`

### GetAsync [GET]
- Permission: `HlCalculationKindTransactionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `HlCalculationKindTransactionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `HlCalculationKindTransactionCreate`
- Return: `IActionResult`
- Tavsif: Ҳисоб-китоб тури Битим ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `HlCalculationKindTransactionEdit`
- Return: `IActionResult`
- Tavsif: Ҳисоб-китоб тури Битим ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `HlCalculationKindTransactionDelete`
- Return: `IActionResult`
- Tavsif: Ҳисоб-китоб тури Битим ҳужжатини ўчириш


## PaymentTransferAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<PaymentTransferAccountListDto>`

### GetListAsync [POST]
- Return: `DbPagedModel<PaymentTransferAccountTablePckDto>`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`

### AcceptAsync [POST]
- Return: `IActionResult`

### CancelAsync [POST]
- Return: `IActionResult`

### UpdateTable [POST]
- Return: `IActionResult`


## SportGroupController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SportGroupView`
- Return: `PagedResult<SportGroupListDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAsync [GET]
- Permission: `SportGroupSync`
- Return: `IActionResult`


## AllowanceByOrganizationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `AllowanceByOrganizationView`
- Return: `PagedResult<AllowanceByOrganizationListDto>`

### GetAsync [GET]
- Permission: `AllowanceByOrganizationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AllowanceByOrganizationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AllowanceByOrganizationCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `AllowanceByOrganizationEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `AllowanceByOrganizationDelete`
- Return: `IActionResult`

### CreateTableAsync [POST]
- Permission: `AllowanceByOrganizationCreate`
- Return: `IActionResult`

### GetTableListAsync [POST]
- Permission: `AllowanceByOrganizationView`
- Return: `PagedResult<AllowanceByOrganizationTableDto>`

### DeleteTableAsync [POST]
- Permission: `AllowanceByOrganizationView`
- Return: `IActionResult`


## ArgosOrganizationTempController
Route: `[controller]/[action]`

### UploadExcel [POST]
- Permission: `ArgosOrganizationTempCreate`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини яратиш

### GetListAsync [POST]
- Permission: `ArgosOrganizationTempView`
- Return: `PagedResult<ArgosOrganizationTempListDto>`

### GetAsync [GET]
- Permission: `ArgosOrganizationTempView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ArgosOrganizationTempView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ArgosOrganizationTempCreate`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ArgosOrganizationTempEdit`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `ArgosOrganizationTempDelete`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини ўчириш


## CalculationKindController
Route: `[controller]/[action]`

### GetTransactionCrSubAccAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetListAsync [POST]
- Return: `IActionResult`

### GetListAllAsync [POST]
- Return: `PagedResult<CalculationKindListDto>`

### GetListAll2Async [POST]
- Return: `PagedResult<CalculationKindListDto>`

### GetListAll3Async [POST]
- Return: `PagedResult<CalculationKindListDto>`

### GetListAll4Async [POST]
- Return: `PagedResult<CalculationKindListDto>`

### GetAsync [GET]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetNewAsync [GET]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetByAllowedDocAsSelectListAsync [GET]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetNewAsync [GET]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetCalcKindPersentageListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### CreateCalcKindPersentageAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`

### UpdateCalcKindPersentageAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteCalcKindPersentageAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetCalcKindUsedTableListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### CreateCalcKindUsedTableAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`

### UpdateCalcKindUsedTableAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteCalcKindUsedTableAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetCalcKindAllowedDocListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### CreateCalcKindAllowedDocAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`

### UpdateCalculationKindAllowedDocAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteCalculationKindAllowedDocAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetCalcKindTransactionListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### CreateCalcKindTransactionAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`

### UpdateCalcKindTransactionAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteCalcKindTransactionAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetCalcKindAllowedSettlementAccListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### CreateCalcKindAllowedSettlementAccAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`

### UpdateCalcKindAllowedSettlementAccAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини яратиш

### DeleteCalcKindAllowedSettlementAccAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Кадрлар билан таъминлаш ҳужжатини ўчириш

### GetCalculationKindDeductionUsedTableListAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### AsSelectListSalaryByDayAndSalaryByHourAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CalculationKindCreate`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CalculationKindEdit`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `CalculationKindDelete`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини ўчириш

### CalculationKindReportAsExcelAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини печать қилиш

### CalculationKindUsedReportAsExcelAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури, тўлов турлари билан

### GetCalculationKindThatDeductionAsync [POST]
- Permission: `CalculationKindView`
- Return: `IActionResult`

### AttachingCalculationKindToUsed [POST]
- Permission: `CalculationKindEdit`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини таҳрирлаш

### AddCalculationKindToUsedAsync [POST]
- Permission: `CalculationKindEdit`
- Return: `IActionResult`
- Tavsif: Ҳисоблаш тури ҳужжатини таҳрирлаш

### GetAllCalculationKindCoreAsync [GET]
- Return: `ActionResult<List<CalculationKindCore>>`


## CurriculumTypeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `CurriculumTypeView`
- Return: `PagedResult<CurriculumTypeListDto>`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncFromErpAsync [POST]
- Return: `IActionResult`


## LevelCodeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `LevelCodeView`
- Return: `PagedResult<LevelCodeListDto>`

### GetAsync [GET]
- Permission: `LevelCodeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `LevelCodeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `LevelCodeCreate`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `LevelCodeEdit`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `LevelCodeDelete`
- Return: `IActionResult`
- Tavsif: Бюджет даражаси ҳужжатини ўчириш


## QualificationCategoryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `QualificationCategoryView`
- Return: `PagedResult<QualificationCategoryListDto>`

### GetAsync [GET]
- Permission: `QualificationCategoryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `QualificationCategoryView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetSumSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `QualificationCategoryCreate`
- Return: `IActionResult`
- Tavsif: Малака тоифаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `QualificationCategoryEdit`
- Return: `IActionResult`
- Tavsif: Малака тоифаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `QualificationCategoryDelete`
- Return: `IActionResult`
- Tavsif: Малака тоифаси ҳужжатини ўчириш


## SchoolGroupContingentController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolGroupContingentView`
- Return: `PagedResult<SchoolGroupContingentListDto>`

### GetAsync [GET]
- Permission: `SchoolGroupContingentCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SchoolGroupContingentView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SchoolGroupContingentCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `SchoolGroupContingentEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `SchoolGroupContingentDelete`
- Return: `IActionResult`


## SchoolingShiftController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolingShiftView`
- Return: `PagedResult<SchoolingShiftListDto>`

### GetAsync [GET]
- Permission: `SchoolingShiftView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`


## SchoolTypeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolTypeView`
- Return: `PagedResult<SchoolTypeListDto>`

### GetAsync [GET]
- Permission: `SchoolTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`


## SourceCodeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SourceCodeView`
- Return: `PagedResult<SourceCodeListDto>`

### GetAsync [GET]
- Permission: `SourceCodeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SourceCodeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SourceCodeCreate`
- Return: `IActionResult`
- Tavsif: Манбаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SourceCodeEdit`
- Return: `IActionResult`
- Tavsif: Манбаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SourceCodeDelete`
- Return: `IActionResult`
- Tavsif: Манбаси ҳужжатини ўчириш


## SportLevelController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SportLevelView`
- Return: `PagedResult<SportLevelListDto>`

### GetAsync [GET]
- Permission: `SportLevelView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAsync [GET]
- Permission: `SportLevelSync`
- Return: `IActionResult`


## SportTypeClassifierController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `SportTypeClassifierView`
- Return: `PagedResult<SportTypeClassifierListDto>`

### GetAsync [GET]
- Permission: `SportTypeClassifierView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAsync [GET]
- Permission: `SportTypeClassifierSync`
- Return: `IActionResult`


## StaffingIndicatorController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffingIndicatorView`
- Return: `PagedResult<StaffingIndicatorListDto>`

### GetAsync [GET]
- Permission: `StaffingIndicatorView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffingIndicatorView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffingIndicatorCreate`
- Return: `IActionResult`
- Tavsif: Штат жадвали кўрсатгичлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffingIndicatorEdit`
- Return: `IActionResult`
- Tavsif: Штат жадвали кўрсатгичлари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `StaffingIndicatorDelete`
- Return: `IActionResult`
- Tavsif: Штат жадвали кўрсатгичлари ҳужжатини ўчириш


## TaxBreakSettlementAccountController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TaxBreakSettlementAccountView`
- Return: `PagedResult<TaxBreakSettlementAccountListDto>`

### GetAsync [GET]
- Permission: `TaxBreakSettlementAccountCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TaxBreakSettlementAccountView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TaxBreakSettlementAccountCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `TaxBreakSettlementAccountEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `TaxBreakSettlementAccountDelete`
- Return: `IActionResult`

### PrintAsExcelAsync [POST]
- Permission: `TaxBreakSettlementAccountView`
- Return: `IActionResult`


## TaxBreakTypeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TaxBreakTypeView`
- Return: `PagedResult<TaxBreakTypeListDto>`

### GetAsync [GET]
- Permission: `TaxBreakTypeCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TaxBreakTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectList2Async [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TaxBreakTypeCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `TaxBreakTypeEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `TaxBreakTypeDelete`
- Return: `IActionResult`

### PrintAsExcelAsync [POST]
- Permission: `TaxBreakTypeView`
- Return: `IActionResult`


## TaxCodeIncomeTypeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `TaxCodeIncomeTypeView`
- Return: `PagedResult<TaxCodeIncomeTypeListDto>`

### GetAsync [GET]
- Permission: `TaxCodeIncomeTypeCreate`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TaxCodeIncomeTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TaxCodeIncomeTypeCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `TaxCodeIncomeTypeEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `TaxCodeIncomeTypeDelete`
- Return: `IActionResult`


## ExternalInpsRegistryController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`

### Cancel [POST]
- Return: `IActionResult`


## ExternalPayrollPlasticCardSheetController
Route: `[controller]/[action]`

### Accept [POST]
- Return: `IActionResult`

### Cancel [POST]
- Return: `IActionResult`


## ExternalPayrollSheetController
Route: `[controller]/[action]`

### Accept [POST]
- Return: `IActionResult`

### Cancel [POST]
- Return: `IActionResult`


## ExternalRequestReceivingCashController
Route: `[controller]/[action]`

### Create [POST]
- Return: `IActionResult`

### Cancel [POST]
- Return: `IActionResult`
