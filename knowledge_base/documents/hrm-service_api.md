# hrm-service — API Endpointlar


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

### GetDocumentTypeSelectList [GET]
- Return: `IActionResult`

### GetTimeSheetTypeSelectList [GET]
- Return: `IActionResult`

### GetEmpAppointOrderTypeSelectList [GET]
- Return: `IActionResult`

### GetReasonsOfDismissionSelectList [GET]
- Return: `IActionResult`

### GetEmploymentTypeSelectList [GET]
- Return: `IActionResult`

### GetMinimumValueTypeSelectList [GET]
- Return: `IActionResult`

### GetTariffScaleTypeSelectList [GET]
- Return: `IActionResult`

### GetPositionClassifiert [GET]
- Return: `IActionResult`

### GetTimeSheetIndicatorSelectList [GET]
- Return: `IActionResult`

### GetPositionTypeSelectList [GET]
- Return: `IActionResult`

### GetPositionCategorySelectList [GET]
- Return: `IActionResult`

### GetEmployeeSendTrainTypeSelectList [GET]
- Return: `IActionResult`

### GetTarifficationOrgTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetEmployeeSendTrainOrderTypeSelectList [GET]
- Return: `IActionResult`

### GetEmpApplicationTypeSelectList [GET]
- Return: `IActionResult`

### GetDepartmentTypeSelectList [GET]
- Return: `IActionResult`


## AppointEmployeeController
Route: `[Controller]/[action]`

### GetAsync [GET]
- Permission: `AppointEmployeeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `AppointEmployeeView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `AppointEmployeeCreate`
- Return: `IActionResult`
- Tavsif: Ходимни тайинлаш ҳужжатини яратиш

### GetListDismisalEmployeeAsync [GET]
- Permission: `AppointEmployeeView`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `AppointEmployeeEdit`
- Return: `IActionResult`
- Tavsif: Ходимни тайинлаш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `AppointEmployeeAccept`
- Return: `IActionResult`
- Tavsif: Ходимни тайинлаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `AppointEmployeeCancel`
- Return: `IActionResult`
- Tavsif: Ходимни тайинлаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `AppointEmployeeDelete`
- Return: `IActionResult`
- Tavsif: Ходимни тайинлаш ҳужжатини ўчириш

### AppointEmployeeDashboardAsync [POST]
- Permission: `DashboardMinistryView`
- Return: `PagedResult<AppointEmployeeDashboardListDto>`

### PrintAsync [GET]
- Permission: `DashboardMinistryView`
- Return: `IActionResult`

### GetListAsExcelAsync [POST]
- Permission: `DashboardMinistryView`
- Return: `IActionResult`

### PrintAsQuickAsync [GET]
- Return: `IActionResult`


## EmployeeApplicationController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeApplicationView`
- Return: `PagedResult<EmployeeApplicationListDto>`

### GetAsync [GET]
- Permission: `EmployeeApplicationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeApplicationView`
- Return: `IActionResult`

### GetDepartmentCodeSelectList [GET]
- Permission: `EmployeeApplicationView`
- Return: `IActionResult`

### GetDepartmentSubDevisionSelectList [GET]
- Permission: `EmployeeApplicationView`
- Return: `IActionResult`

### GetDepartmentPositionsAsync [GET]
- Permission: `EmployeeApplicationView`
- Return: `ActionResult<DepartmentPositionDto>`

### CreateAsync [POST]
- Permission: `EmployeeApplicationCreate`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeApplicationEdit`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EmployeeApplicationDelete`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини ўчириш

### ReadyToSendAsync [POST]
- Permission: `EmployeeApplicationReadyToSign`
- Return: `IActionResult`
- Tavsif: Аризани ҳужжатини имзолаш

### CancelAsync [POST]
- Permission: `EmployeeApplicationCancel`
- Return: `IActionResult`
- Tavsif: Аризани ҳужжатини имзолаш

### SignAsync [POST]
- Permission: `EmployeeApplicationSign`
- Return: `IActionResult`
- Tavsif: Аризани ҳужжатини имзолаш

### GetHash [GET]
- Return: `IActionResult`

### GetListForManage [POST]
- Permission: `EmployeeManageView`
- Return: `PagedResult<EmployeeManageListDto>`


## EmployeeLayoffController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeLayoffView`
- Return: `PagedResult<EmployeeLayoffListDto>`

### GetAsync [GET]
- Permission: `EmployeeLayoffView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeLayoffView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeLayoffCreate`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeLayoffEdit`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EmployeeLayoffAccept`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `EmployeeLayoffCancel`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `EmployeeLayoffDelete`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини ўчириш


## EmployeeLeaveOrderController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeLeaveOrderView`
- Return: `PagedResult<EmployeeLeaveOrderListDto>`

### GetListForRecallAsync [POST]
- Permission: `EmployeeLeaveOrderView`
- Return: `IActionResult`

### GetUnpaidListAsync [POST]
- Permission: `EmployeeLeaveOrderView`
- Return: `PagedResult<UnpaidEmployeeLeaveOrderListDto>`

### GetAsync [GET]
- Permission: `EmployeeLeaveOrderView`
- Return: `IActionResult`

### PrintAllAsync [POST]
- Permission: `EmployeeLeaveOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeLeaveOrderView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTableAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeLeaveOrderCreate`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeLeaveOrderEdit`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EmployeeLeaveOrderAccept`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `EmployeeLeaveOrderCancel`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `EmployeeLeaveOrderDelete`
- Return: `IActionResult`
- Tavsif: Ходимни ишдан бўшатиш тўғрисида хабарнома ҳужжатини ўчириш

### GetCalculatedDaysAsync [GET]
- Permission: `EmployeeLeaveOrderCreate`
- Return: `IActionResult`


## EmployeeSendTrainController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeSendTrainView`
- Return: `PagedResult<EmployeeSendTrainListDto>`

### GetListMaternityAsync [POST]
- Permission: `EmployeeSendTrainView`
- Return: `PagedResult<EmployeeSendTrainListDto>`

### GetListForSocialHolidayAsync [POST]
- Permission: `EmployeeSendTrainView`
- Return: `IActionResult`

### GetUnCalcListAsync [POST]
- Permission: `EmployeeSendTrainView`
- Return: `PagedResult<EmployeeSendTrainListDto>`

### GetAsync [GET]
- Permission: `EmployeeSendTrainView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeSendTrainView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeSendTrainCreate`
- Return: `IActionResult`
- Tavsif: Малака оширишга юбориш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeSendTrainEdit`
- Return: `IActionResult`
- Tavsif: Малака оширишга юбориш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EmployeeSendTrainAccept`
- Return: `IActionResult`
- Tavsif: Малака оширишга юбориш ҳужжатини тасдиқлаш

### GetListAsExcelAsync [POST]
- Permission: `DashboardMinistryView`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `EmployeeSendTrainCancel`
- Return: `IActionResult`
- Tavsif: Малака оширишга юбориш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `EmployeeSendTrainDelete`
- Return: `IActionResult`
- Tavsif: Малака оширишга юбориш ҳужжатини ўчириш


## EmployeeSickLeaveController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeSickLeaveView`
- Return: `PagedResult<EmployeeSickLeaveListDto>`

### GetUnpaidListAsync [POST]
- Permission: `EmployeeLeaveOrderView`
- Return: `PagedResult<UnpaidEmployeeSickLeaveListDto>`

### GetAsync [GET]
- Permission: `EmployeeSickLeaveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeSickLeaveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetInfoFromHrMfAsync [GET]
- Return: `IActionResult`

### GetInfoAdmSickLeaveAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeSickLeaveCreate`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeSickLeaveEdit`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EmployeeSickLeaveAccept`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `EmployeeSickLeaveCancel`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `EmployeeSickLeaveDelete`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини ўчириш

### PrintGetListAsync [POST]
- Permission: `EmployeeSickLeaveView`
- Return: `IActionResult`
- Tavsif: Касаллик варақаси ҳужжатини печать қилиш

### FillHrmfSickEmployeeLeaveAsync [GET]
- Permission: `EmployeeSickLeaveReView`
- Return: `ActionResult`

### GetHrmfSickEmployeeLeaveAsync [POST]
- Permission: `EmployeeSickLeaveView`
- Return: `PagedResult<SickLeaveStorageInfoDto>`

### PrintHrmfSickEmployeeAsync [POST]
- Permission: `EmployeeSickLeaveView`
- Return: `IActionResult`
- Tavsif: Xодимларниг касаллик варақаси рўйҳати печать қилиш

### ConsumeHrmfSickEmployeeAsync [POST]
- Return: `IActionResult`

### UpdateDocumentId [GET]
- Return: `IActionResult`

### JobHistoryGetListAsync [POST]
- Permission: `EmployeeSickLeaveReView`
- Return: `PagedResult<JobHistoryInfoDto>`


## ManagementCertificateController
Route: `[Controller]/[action]`

### GetList [POST]
- Permission: `EmployeeView`
- Return: `PagedResult<ManagementCertificateListDto>`

### Sync [GET]
- Permission: `EmployeeEdit`
- Return: `IActionResult`


## MassPlannedCalculationController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `MassPlannedCalculationView`
- Return: `PagedResult<MassPlannedCalculationListDto>`

### GetAsync [GET]
- Permission: `MassPlannedCalculationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `MassPlannedCalculationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `MassPlannedCalculationCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари умумий ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `MassPlannedCalculationEdit`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари умумий ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `MassPlannedCalculationAccept`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари умумий ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `MassPlannedCalculationCancel`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари умумий ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `MassPlannedCalculationDelete`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари умумий ҳужжатини ўчириш


## OrderToSendBusinessTripController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `OrderToSendBusinessTripView`
- Return: `PagedResult<OrderToSendBusinessTripListDto>`

### GetAsync [GET]
- Permission: `OrderToSendBusinessTripView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OrderToSendBusinessTripView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OrderToSendBusinessTripCreate`
- Return: `IActionResult`
- Tavsif: Ходимни ҳизмат сафарига юбориш буйруғи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OrderToSendBusinessTripEdit`
- Return: `IActionResult`
- Tavsif: Ходимни ҳизмат сафарига юбориш буйруғи ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `OrderToSendBusinessTripAccept`
- Return: `IActionResult`
- Tavsif: Ходимни ҳизмат сафарига юбориш буйруғи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `OrderToSendBusinessTripCancel`
- Return: `IActionResult`
- Tavsif: Ходимни ҳизмат сафарига юбориш буйруғи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `OrderToSendBusinessTripDelete`
- Return: `IActionResult`
- Tavsif: Ходимни ҳизмат сафарига юбориш буйруғи ҳужжатини ўчириш

### PrintAsExcelAsync [POST]
- Return: `IActionResult`


## PlannedCalculationController
Route: `[Controller]/[action]`

### GetList [POST]
- Permission: `PlannedCalculationView`
- Return: `PagedResult<PlannedCalculationListDto>`

### GetAsync [GET]
- Permission: `PlannedCalculationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PlannedCalculationView`
- Return: `IActionResult`

### GetFastAsync [GET]
- Permission: `PlannedCalculationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTablesByDocId [GET]
- Permission: `PlannedCalculationView`
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `PlannedCalculationCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини тўлдириш

### UpdateTableAsync [POST]
- Permission: `TempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини таҳрирлаш

### ClearAsync [POST]
- Permission: `PlannedCalculationCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини тозалаш

### CreateAsync [POST]
- Permission: `PlannedCalculationCreate`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PlannedCalculationEdit`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PlannedCalculationAccept`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PlannedCalculationCancel`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PlannedCalculationDelete`
- Return: `IActionResult`
- Tavsif: Доимий тўлов турлари (ходимлар кесимида) ҳужжатини ўчириш

### PrintAsync [GET]
- Permission: `EmployeeManageView`
- Return: `IActionResult`


## PositionSubstitutionController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PositionSubstitutionView`
- Return: `PagedResult<PositionSubstitutionListDto>`

### GetAsync [GET]
- Permission: `PositionSubstitutionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PositionSubstitutionView`
- Return: `IActionResult`

### AsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PositionSubstitutionCreate`
- Return: `IActionResult`
- Tavsif: Ўрнига ишлашга рухсат этилган лавозимлар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PositionSubstitutionEdit`
- Return: `IActionResult`
- Tavsif: Ўрнига ишлашга рухсат этилган лавозимлар ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PositionSubstitutionAccept`
- Return: `IActionResult`
- Tavsif: Ўрнига ишлашга рухсат этилган лавозимлар ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PositionSubstitutionCancel`
- Return: `IActionResult`
- Tavsif: Ўрнига ишлашга рухсат этилган лавозимлар ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `PositionSubstitutionDelete`
- Return: `IActionResult`
- Tavsif: Ўрнига ишлашга рухсат этилган лавозимлар ҳужжатини ўчириш


## RecallLeaveController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `RecallLeaveView`
- Return: `PagedResult<RecallLeaveListDto>`

### GetAsync [GET]
- Permission: `RecallLeaveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RecallLeaveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RecallLeaveCreate`
- Return: `IActionResult`
- Tavsif: Меҳнат таътилидан ёки ўз ҳисобидан таътилдан чақириб олиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RecallLeaveEdit`
- Return: `ActionResult`
- Tavsif: Меҳнат таътилидан ёки ўз ҳисобидан таътилдан чақириб олиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `RecallLeaveAccept`
- Return: `IActionResult`
- Tavsif: Меҳнат таътилидан ёки ўз ҳисобидан таътилдан чақириб олиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RecallLeaveCancel`
- Return: `IActionResult`
- Tavsif: Меҳнат таътилидан ёки ўз ҳисобидан таътилдан чақириб олиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `RecallLeaveDelete`
- Return: `IActionResult`
- Tavsif: Меҳнат таътилидан ёки ўз ҳисобидан таътилдан чақириб олиш ҳужжатини ўчириш


## TaxBenefitController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TaxBenefitView`
- Return: `PagedResult<TaxBenefitListDto>`

### GetAsync [GET]
- Permission: `TaxBenefitView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TaxBenefitView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TaxBenefitCreate`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёз ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TaxBenefitEdit`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёз ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `TaxBenefitAccept`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёз ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `TaxBenefitCancel`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёз ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `TaxBenefitDelete`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёз ҳужжатини ўчириш


## TempCalcKindController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TempCalcKindView`
- Return: `PagedResult<TempCalcKindListDto>`

### GetAsync [GET]
- Permission: `TempCalcKindView`
- Return: `IActionResult`

### GetTablesByDocId [GET]
- Permission: `TempCalcKindView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TempCalcKindView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `TempCalcKindView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `TempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тўлдириш

### FillTempTableAsync [POST]
- Permission: `TempCalcKindCreate`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `TempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тозалаш

### CreateAsync [POST]
- Permission: `TempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `TempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `TempCalcKindAccept`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `TempCalcKindCancel`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `TempCalcKindDelete`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини ўчириш

### PrintAsync [GET]
- Permission: `TempCalcKindView`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини Печать қилиш

### PrintAllAsync [GET]
- Permission: `TempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини Печать қилиш

### InsertDataAsync [POST]
- Permission: `TempCalcKindEdit`
- Return: `IActionResult`


## TimeSheetController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TimeSheetView`
- Return: `PagedResult<TimeSheetListDto>`

### GetAsync [GET]
- Permission: `TimeSheetView`
- Return: `IActionResult`

### TestApiAsync [POST]
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TimeSheetView`
- Return: `IActionResult`

### GetTableAsync [GET]
- Permission: `TimeSheetView`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини тозалаш

### FillTimeSheetAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`

### FillTimeSheetEmployeeManageIdAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TimeSheetCreate`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини таҳрирлаш

### CreateTableAsync [POST]
- Permission: `TimeSheetEdit`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини таҳрирлаш

### SignAsync [POST]
- Permission: `TimeSheetSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини имзолаш

### AcceptAsync [POST]
- Permission: `TimeSheetCreate`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини Тасдиклаш

### CancelAsync [POST]
- Permission: `TimeSheetCancel`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини бекор қилиш

### CancelReadyToSendAsync [POST]
- Permission: `TimeSheetCancelReadyToSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини бекор қилиш

### GetHashAsync [GET]
- Permission: `TimeSheetSign`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `TimeSheetSend`
- Return: `IActionResult`
- Tavsif: KADR TABLENI BUGALTERGA YUBORISH

### ReceiveAsync [POST]
- Permission: `TimeSheetReceive`
- Return: `IActionResult`
- Tavsif: BUGALTERGA TABELNI QABUL QILISHI

### DeleteAsync [POST]
- Permission: `TimeSheetDelete`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини ўчириш

### RejectedAsync [POST]
- Permission: `TimeSheetRejected`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини тасдиқлашга тайёрлашни қайтариш

### ReadyToSignAsync [POST]
- Permission: `TimeSheetReadyToSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини тасдиқлашга тайёрлашни қайтариш

### TimeSheetPrintAsync [POST]
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини ўчириш

### TimeSheetGetListTablePrintAsync [POST]
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини ўчириш


## TimeSheetEduController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TimeSheetEduView`
- Return: `PagedResult<TimeSheetEduListDto>`

### GetAsync [GET]
- Permission: `TimeSheetEduView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TimeSheetEduView`
- Return: `IActionResult`

### GetTableAsync [GET]
- Permission: `TimeSheetEduView`
- Return: `IActionResult`

### FillTimeSheetEduAsync [POST]
- Permission: `TimeSheetEduEdit`
- Return: `IActionResult`

### ClearAsync [POST]
- Permission: `TimeSheetEduEdit`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини тозалаш

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TimeSheetEduCreate`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TimeSheetEduEdit`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `TimeSheetEduEdit`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `TimeSheetEduAccept`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `TimeSheetEduCancel`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `TimeSheetEduDelete`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) ҳужжатини ўчириш

### PrintWithSubjectAsync [POST]
- Permission: `TimeSheetEduView`
- Return: `IActionResult`
- Tavsif: Табел (Таълим муассасалари учун) 

### GetHashAsync [GET]
- Permission: `TimeSheetEduSign`
- Return: `IActionResult`

### ReadyToSignAsync [POST]
- Permission: `TimeSheetEduReadyToSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини тасдиқлашга тайёрлашни қайтариш

### CancelReadyToSignAsync [POST]
- Permission: `TimeSheetEduCancelReadyToSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини бекор қилиш

### SignAsync [POST]
- Permission: `TimeSheetEduSign`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини имзолаш

### SendAsync [POST]
- Permission: `TimeSheetEduSend`
- Return: `IActionResult`
- Tavsif: KADR TABLENI BUGALTERGA YUBORISH

### RejectedAsync [POST]
- Permission: `TimeSheetEduRejected`
- Return: `IActionResult`
- Tavsif: Табел ҳужжатини тасдиқлашга тайёрлашни қайтариш

### ReceiveAsync [POST]
- Permission: `TimeSheetEduReceive`
- Return: `IActionResult`
- Tavsif: BUGALTERGA TABELNI QABUL QILISHI


## TypicalOrgStructureController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TypicalOrgStructureView`
- Return: `PagedResult<TypicalOrgStructureListDto>`

### GetAsync [GET]
- Permission: `TypicalOrgStructureView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TypicalOrgStructureView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `TypicalOrgStructureEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `TypicalOrgStructureDelete`
- Return: `IActionResult`

### GetTempListAsync [POST]
- Permission: `TypicalOrgStructureView`
- Return: `PagedResult<TypicalOrgStructureTempListDto>`

### CreateTempAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### DeleteTempAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### ClearTableAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### GetOrgTableListAsync [POST]
- Permission: `TypicalOrgStructureView`
- Return: `PagedResult<TypicalOrgStructureOrgListDto>`

### CreateOrgTableAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### DeleteOrgTableAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### GeStructurePositionListAsync [GET]
- Permission: `TypicalOrgStructureView`
- Return: `List<StructurePositionListDto>`

### GetOrgPositionListAsync [GET]
- Permission: `TypicalOrgStructureView`
- Return: `TypicalOrgStructureOrgDto`

### GetTempPositionListAsync [GET]
- Permission: `TypicalOrgStructureView`
- Return: `TypicalOrgStructureOrgDto`

### CreateOrUpdateTableAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `TypicalOrgStructureCreate`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `TypicalOrgStructureAccept`
- Return: `IActionResult`

### CancelAsync [POST]
- Permission: `TypicalOrgStructureCancel`
- Return: `IActionResult`


## WorkDayOffController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `WorkDayOffView`
- Return: `PagedResult<WorkDayOffListDto>`

### GetAsync [GET]
- Permission: `WorkDayOffView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `WorkDayOffView`
- Return: `IActionResult`

### AsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `WorkDayOffCreate`
- Return: `IActionResult`
- Tavsif: Байрам (ишланмайдиган) кунлари ишга жалб этиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `WorkDayOffEdit`
- Return: `IActionResult`
- Tavsif: Байрам (ишланмайдиган) кунлари ишга жалб этиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `WorkDayOffAccept`
- Return: `IActionResult`
- Tavsif: Байрам (ишланмайдиган) кунлари ишга жалб этиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `WorkDayOffCancel`
- Return: `IActionResult`
- Tavsif: Байрам (ишланмайдиган) кунлари ишга жалб этиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `WorkDayOffDelete`
- Return: `IActionResult`
- Tavsif: Байрам (ишланмайдиган) кунлари ишга жалб этиш ҳужжатини ўчириш


## DepartmentController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `DepartmentView`
- Return: `PagedResult<DepartmentListDto>`

### PrintGetListAsync [POST]
- Permission: `DepartmentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DepartmentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DepartmentView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetOrgDepartmentAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DepartmentCreate`
- Return: `IActionResult`
- Tavsif: Бўлим ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DepartmentEdit`
- Return: `IActionResult`
- Tavsif: Бўлим ҳужжатини таҳрирлаш

### GetListForPaymentOrderAsync [POST]
- Permission: `DepartmentView`
- Return: `PagedResult<DepartmentListDto>`

### DeleteAsync [POST]
- Permission: `DepartmentDelete`
- Return: `IActionResult`
- Tavsif: Бўлим ҳужжатини ўчириш


## EducationCategoryController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EducationCategoryView`
- Return: `PagedResult<EducationCategoryListDto>`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Sync [POST]
- Permission: `EducationCategoryCreate`
- Return: `IActionResult`
- Tavsif: Педкадр тизимидан ҳодим тоифасини олиб келиш

### SyncAllAsync [POST]
- Permission: `OrganizationalStructureViewAdmin`
- Return: `IActionResult`
- Tavsif: Педкадр тизимидан ҳодим тоифасини олиб келиш


## EmployeeController
Route: `[Controller]/[action]`

### GetListWithHistoryAsync [POST]
- Permission: `EmployeeView`
- Return: `EmployeeListWithHistoryDto`

### GetListAsync [POST]
- Permission: `EmployeeView`
- Return: `PagedResult<EmployeeListDto>`

### PrintGetListAsync [POST]
- Permission: `EmployeeView`
- Return: `IActionResult`
- Tavsif: Ходим ҳужжатини печать қилиш

### UploadExcel [POST]
- Return: `IActionResult`

### GetPlasticCardNumberAsync [GET]
- Permission: `EmployeeView`
- Return: `string`

### GetAsync [GET]
- Permission: `EmployeeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EmployeeView`
- Return: `IActionResult`

### GetEduStudyCertificateAsync [GET]
- Permission: `EmployeeView`
- Return: `IActionResult`

### SyncWithOldEmployeesAsync [POST]
- Permission: `EmployeeCreate`
- Return: `IActionResult`

### RequestToSyncAllEmployee [GET]
- Permission: `EmployeeCreate`
- Return: `IActionResult`

### TestSyncWithOldEmployees [POST]
- Permission: `EmployeeCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EmployeeCreate`
- Return: `IActionResult`
- Tavsif: Ходим ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EmployeeEdit`
- Return: `IActionResult`
- Tavsif: Ходим ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EmployeeDelete`
- Return: `IActionResult`
- Tavsif: Ходим ҳужжатини ўчириш

### GetPlasticCardsAsync [GET]
- Return: `IActionResult`


## KinderGartenManagementCertificateController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeView`
- Return: `PagedResult<KinderGartenManagementCertificateListDto>`

### Sync [GET]
- Permission: `EmployeeEdit`
- Return: `IActionResult`


## MedicalCategoryController
Route: `[Controller]/[action]`

### GetListWithHistoryAsync [POST]
- Permission: `EmployeeView`
- Return: `MedicalCategoryListWithHistoryDto`

### GetListAsync [POST]
- Permission: `PersonView`
- Return: `PagedResult<MedicalCategoryListDto>`

### GetAsync [GET]
- Permission: `PersonView`
- Return: `IActionResult`

### SyncAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAllEmployeeAsync [POST]
- Permission: `PersonCreate`
- Return: `IActionResult`


## MedicalCertificateController
Route: `[Controller]/[action]`

### GetListWithHistoryAsync [POST]
- Permission: `EmployeeView`
- Return: `MedicalCertificateListWithHistoryDto`

### GetListAsync [POST]
- Permission: `PersonView`
- Return: `PagedResult<MedicalCertificateListDto>`

### GetAsync [GET]
- Permission: `PersonView`
- Return: `IActionResult`

### SyncAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### SyncManagerCertificateAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAllEmployeeAsync [POST]
- Permission: `PersonCreate`
- Return: `IActionResult`


## MoliyachiNotificationController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<MoliyachiNotificationListDto>`

### GetUnreadCount [GET]
- Return: `IActionResult`

### GetEmployeeMessages [GET]
- Return: `IActionResult`

### AddEmployeeMessageSimple [POST]
- Return: `IActionResult`


## PersonController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PersonView`
- Return: `PagedResult<PersonListDto>`

### GetAsync [GET]
- Permission: `PersonView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PersonView`
- Return: `IActionResult`

### GetByDocInfoAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetFromGspAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PersonEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PersonDelete`
- Return: `IActionResult`
- Tavsif: Шахс ҳужжатини ўчириш


## TravelCountyController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Return: `PagedResult<TravelCountyListDto>`

### GetTravelCountData [POST]
- Return: `object`

### SaveChangesCompletedEventData [GET]
- Return: `Task`


## BasicRateTypeController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `BasicRateTypeView`
- Return: `PagedResult<BasicRateTypeListDto>`

### GetAsync [GET]
- Permission: `BasicRateTypeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `BasicRateTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `BasicRateTypeCreate`
- Return: `IActionResult`
- Tavsif: Базавий ставка тури ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `BasicRateTypeEdit`
- Return: `IActionResult`
- Tavsif: Базавий ставка тури ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `BasicRateTypeDelete`
- Return: `IActionResult`
- Tavsif: Базавий ставка тури ҳужжатини ўчириш


## EmployeeTurnikateWarningController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeTurnikateWarningView`
- Return: `PagedResult<EmployeeTurnikateWarningLisDto>`


## FixedMinimumValueController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `FixedMinimumValueView`
- Return: `PagedResult<FixedMinimumValueListDto>`

### GetByDateAsync [GET]
- Permission: `FixedMinimumValueView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FixedMinimumValueView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FixedMinimumValueView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FixedMinimumValueCreate`
- Return: `IActionResult`
- Tavsif: БҲМ, ПҲБМ, МҲЭКМ, ёшга доир пенсия ва нафақалар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FixedMinimumValueEdit`
- Return: `IActionResult`
- Tavsif: БҲМ, ПҲБМ, МҲЭКМ, ёшга доир пенсия ва нафақалар ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `FixedMinimumValueDelete`
- Return: `IActionResult`
- Tavsif: БҲМ, ПҲБМ, МҲЭКМ, ёшга доир пенсия ва нафақалар ҳужжатини ўчириш


## MedicalCategoryTypeController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `MedicalCategoryTypeView`
- Return: `PagedResult<MedicalCategoryTypeListDto>`

### GetAsync [GET]
- Permission: `MedicalCategoryTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### SyncAsync [POST]
- Permission: `MedicalCategoryTypeCreate`
- Return: `IActionResult`
- Tavsif: Тиббиёт тоифа маълумотномасини янгилаш


## MedicalSpecialtyTypeController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `MedicalSpecialtyTypeView`
- Return: `PagedResult<MedicalSpecialtyTypeListDto>`

### Get [GET]
- Permission: `MedicalSpecialtyTypeView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Sync [POST]
- Permission: `MedicalSpecialtyTypeCreate`
- Return: `IActionResult`
- Tavsif: Тиббиёт мутафасислиги турини янгилаш


## PositionClassificationController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PositionClassificationView`
- Return: `PagedResult<PositionClassificationListDto>`

### GetAsync [GET]
- Permission: `PositionClassificationView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PositionClassificationView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PositionClassificationCreate`
- Return: `IActionResult`
- Tavsif: Лавозим таснифи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PositionClassificationEdit`
- Return: `IActionResult`
- Tavsif: Лавозим таснифи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PositionClassificationDelete`
- Return: `IActionResult`
- Tavsif: Лавозим таснифи ҳужжатини ўчириш


## PositionController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PositionView`
- Return: `PagedResult<PositionListDto>`

### GetAsync [GET]
- Permission: `PositionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PositionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### StructurePositionListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PositionCreate`
- Return: `IActionResult`
- Tavsif: Лавозим ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PositionEdit`
- Return: `IActionResult`
- Tavsif: Лавозим ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PositionDelete`
- Return: `IActionResult`
- Tavsif: Лавозим ҳужжатини ўчириш

### GetActivePositionWithOrgStructureAsync [POST]
- Permission: `PositionView`
- Return: `IActionResult`

### GetPositionSpecialtyList [POST]
- Permission: `PositionView`
- Return: `PagedResult<PositionSpecialtyDto>`

### CreatePositionSpecialty [POST]
- Permission: `PositionEdit`
- Return: `IActionResult`
- Tavsif: Лавозимга мутахассислик қўшиш

### DeletePositionSpecialtyAsync [POST]
- Permission: `PositionEdit`
- Return: `IActionResult`
- Tavsif: Лавозимдан мутахассисликни ўчириш


## PositionExpertiseController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PositionExpertisetView`
- Return: `PagedResult<PositionExpertiseListDto>`

### Get [GET]
- Permission: `PositionExpertisetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `PositionExpertisetView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PositionExpertisetCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PositionExpertisetEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PositionExpertisetDelete`
- Return: `IActionResult`


## PositionGroupController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `PositionGrouptView`
- Return: `PagedResult<PositionGroupListDto>`

### Get [GET]
- Permission: `PositionGrouptView`
- Return: `IActionResult`

### Get [GET]
- Permission: `PositionGrouptView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PositionGrouptCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PositionGrouptEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PositionGrouptDelete`
- Return: `IActionResult`


## SchoolSubjectController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolSubjectView`
- Return: `PagedResult<SchoolSubjectListDto>`

### GetAsync [GET]
- Permission: `SchoolSubjectView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SchoolSubjectView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SchoolSubjectCreate`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SchoolSubjectEdit`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SchoolSubjectDelete`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари ҳужжатини ўчириш


## SchoolSubjectGroupController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `SchoolSubjectGroupView`
- Return: `PagedResult<SchoolSubjectGroupListDto>`

### GetAsync [GET]
- Permission: `SchoolSubjectGroupView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `SchoolSubjectGroupView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `SchoolSubjectGroupCreate`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари гуруҳи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `SchoolSubjectGroupEdit`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари гуруҳи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `SchoolSubjectGroupDelete`
- Return: `IActionResult`
- Tavsif: Мактаб фанлари гуруҳи ҳужжатини ўчириш


## StaffTypeBasicTariffController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `StaffTypeBasicTariffView`
- Return: `PagedResult<StaffTypeBasicTariffListDto>`

### GetAsync [GET]
- Permission: `StaffTypeBasicTariffView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StaffTypeBasicTariffView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StaffTypeBasicTariffCreate`
- Return: `IActionResult`
- Tavsif: Асосий ставкалар бўйича ходимлар турлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StaffTypeBasicTariffEdit`
- Return: `IActionResult`
- Tavsif: Асосий ставкалар бўйича ходимлар турлари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `StaffTypeBasicTariffDelete`
- Return: `IActionResult`
- Tavsif: Асосий ставкалар бўйича ходимлар турлари ҳужжатини ўчириш


## StructureDepartmentController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `StructureDepartmentView`
- Return: `PagedResult<StructureDepartmentListDto>`

### Get [GET]
- Permission: `StructureDepartmentView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StructureDepartmentView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StructureDepartmentCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StructureDepartmentEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `StructureDepartmentDelete`
- Return: `IActionResult`


## StructurePositionGroupController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `StructurePositionGrouptView`
- Return: `PagedResult<StructurePositionGroupListDto>`

### Get [GET]
- Permission: `StructurePositionGrouptView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StructurePositionGrouptView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StructurePositionGrouptCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StructurePositionGrouptEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `StructurePositionGrouptDelete`
- Return: `IActionResult`


## StructurePositionSpecialtyController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `StructurePositionSpecialtytView`
- Return: `PagedResult<StructurePositionSpecialtyListDto>`

### Get [GET]
- Permission: `StructurePositionSpecialtytView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StructurePositionSpecialtytView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StructurePositionSpecialtytCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StructurePositionSpecialtytEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `StructurePositionSpecialtytDelete`
- Return: `IActionResult`


## TariffScaleCoefController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TariffScaleCoefView`
- Return: `PagedResult<TariffScaleCoefListDto>`

### GetAsync [GET]
- Permission: `TariffScaleCoefView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TariffScaleCoefView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTableAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TariffScaleCoefCreate`
- Return: `IActionResult`
- Tavsif: Тарифлар шкаласининг даражалари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TariffScaleCoefEdit`
- Return: `IActionResult`
- Tavsif: Тарифлар шкаласининг даражалари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `TariffScaleCoefDelete`
- Return: `IActionResult`
- Tavsif: Тарифлар шкаласининг даражалари ҳужжатини ўчириш


## TariffScaleController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TariffScaleView`
- Return: `PagedResult<TariffScaleListDto>`

### GetAsync [GET]
- Permission: `TariffScaleView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TariffScaleView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTableAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TariffScaleCreate`
- Return: `IActionResult`
- Tavsif: Тариф шкаласи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TariffScaleEdit`
- Return: `IActionResult`
- Tavsif: Тариф шкаласи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `TariffScaleDelete`
- Return: `IActionResult`
- Tavsif: Тариф шкаласи ҳужжатини ўчириш


## TaxBenefitTypeController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `TaxBenefitTypeView`
- Return: `PagedResult<TaxBenefitTypeListDto>`

### GetAsync [GET]
- Permission: `TaxBenefitTypeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `TaxBenefitTypeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `TaxBenefitTypeCreate`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёзлар тури ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `TaxBenefitTypeEdit`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёзлар тури ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `TaxBenefitTypeDelete`
- Return: `IActionResult`
- Tavsif: Даромад солиғи бўйича имтиёзлар тури ҳужжатини ўчириш


## TurnstileDataController
Route: `[Controller]/[action]`

### GetAsync [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Return: `IActionResult`

### AddUsersFromAPIAsync [POST]
- Return: `IActionResult`

### UpdateAsync [POST]
- Return: `IActionResult`

### DeleteAsync [POST]
- Return: `IActionResult`


## WorkScheduleController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `WorkScheduleView`
- Return: `PagedResult<WorkScheduleListDto>`

### GetAsync [GET]
- Permission: `WorkScheduleView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `WorkScheduleView`
- Return: `IActionResult`

### GetForDashboardAsync [GET]
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `WorkScheduleCreate`
- Return: `IActionResult`
- Tavsif: Иш вақти жадвали ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `WorkScheduleEdit`
- Return: `IActionResult`
- Tavsif: Иш вақти жадвали ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `WorkScheduleDelete`
- Return: `IActionResult`
- Tavsif: Иш вақти жадвали ҳужжатини ўчириш


## AccPlanCalculationKindController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeManageView`
- Return: `PagedResult<AccPlanCalculationKindListDto>`

### PrintGetListAsync [POST]
- Permission: `EmployeeManageView`
- Return: `IActionResult`

### PrintAsync [POST]
- Return: `IActionResult`

### PrintGetListByDepartmentAsync [POST]
- Permission: `EmployeeManageView`
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `EmployeeManageView`
- Return: `IActionResult`


## EmployeeManageController
Route: `[Controller]/[action]`

### GetListAsync [POST]
- Permission: `EmployeeManageView`
- Return: `PagedResult<EmployeeManageListDto>`

### GetListForDmbatEmployeeManage [POST]
- Permission: `EmployeeManageViewDmbat`
- Return: `IActionResult`

### GetListForManage [POST]
- Permission: `EmployeeManageView`
- Return: `PagedResult<EmployeeManageListDto>`

### PrintGetListAsync [POST]
- Permission: `EmployeeManageView`
- Return: `IActionResult`

### GetPositionSelectListAsync [GET]
- Return: `IActionResult`

### GetListForCameralAsync [POST]
- Permission: `CameralCreate`
- Return: `PagedResult<EmployeeManageListDto>`


## TypicalStructManageController
Route: `[Controller]/[action]`

### GetTypicalStructManageTurnoverAsync [POST]
- Return: `IActionResult`
