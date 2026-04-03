# edu-service — API Endpointlar


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

### GetEduContractSumTypeSelectList [GET]
- Return: `IActionResult`

### GetEduContractTypeSelectList [GET]
- Return: `IActionResult`

### GetEduFacultyTypeSelectList [GET]
- Return: `IActionResult`

### GetEduPaymentTypeSelectList [GET]
- Return: `IActionResult`

### GetEduFormSelectList [GET]
- Return: `IActionResult`

### GetEduLanguageSelectList [GET]
- Return: `IActionResult`

### GetEduLevelSelectList [GET]
- Return: `IActionResult`

### GetEduTypeSelectList [GET]
- Return: `IActionResult`

### GetScholarshipPenaltyTypeSelectList [GET]
- Return: `IActionResult`

### GetSocialCategorySelectList [GET]
- Return: `IActionResult`

### GetStudentCategorySelectList [GET]
- Return: `IActionResult`

### GetContractCategoryTypeSelectList [GET]
- Return: `IActionResult`


## ContractInvoiceController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `ContractInvoiceView`
- Return: `PagedResult<ContractInvoiceListDto>`

### GetListWithHistory [POST]
- Permission: `ContractInvoiceView`
- Return: `ContractInvoiceListWithHistoryDto`

### Get [GET]
- Permission: `ContractInvoiceView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ContractInvoiceView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ContractInvoiceCreate`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини яратиш

### Update [POST]
- Permission: `ContractInvoiceEdit`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ContractInvoiceAccept`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ContractInvoiceCancel`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ContractInvoiceDelete`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини ўчириш

### PrintGetList [POST]
- Return: `IActionResult`


## ContractOfScholarshipController
Route: `ContractOfScholarship/[action]`

### GetListAsync [POST]
- Permission: `ContractOfScholarshipView`
- Return: `PagedResult<ContractOfScholarshipListDto>`

### GetAsync [GET]
- Permission: `ContractOfScholarshipView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `ContractOfScholarshipCreate`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси  ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `ContractOfScholarshipCreate`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини тозалаш

### UpdateTableAsync [POST]
- Permission: `ContractOfScholarshipEdit`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини таҳрирлаш

### CreateAsync [POST]
- Permission: `ContractOfScholarshipCreate`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ContractOfScholarshipEdit`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ContractOfScholarshipAccept`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ContractOfScholarshipCancel`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `ContractOfScholarshipDelete`
- Return: `IActionResult`
- Tavsif: Стипендия шартномаси ҳужжатини ўчириш


## EduTempCalcKindController
Route: `EduTempCalcKind/[action]`

### GetListAsync [POST]
- Permission: `EduTempCalcKindView`
- Return: `PagedResult<EduTempCalcKindListDto>`

### GetAsync [GET]
- Permission: `EduTempCalcKindView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### FillTableAsync [POST]
- Permission: `EduTempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `EduTempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тозалаш

### CreateAsync [POST]
- Permission: `EduTempCalcKindCreate`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EduTempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `EduTempCalcKindEdit`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `EduTempCalcKindAccept`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `EduTempCalcKindCancel`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `EduTempCalcKindDelete`
- Return: `IActionResult`
- Tavsif: Бир марталик тўловлар бериш тўғрисида буйруқ ҳужжатини ўчириш


## ScholarshipPenaltyController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `ScholarshipPenaltyView`
- Return: `PagedResult<ScholarshipPenaltyListDto>`

### GetAsync [GET]
- Permission: `ScholarshipPenaltyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ScholarshipPenaltyView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ScholarshipPenaltyCreate`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ScholarshipPenaltyEdit`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ScholarshipPenaltyAccept`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ScholarshipPenaltyCancel`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `ScholarshipPenaltyDelete`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини ўчириш


## StudentAdmissionOrderController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StudentAdmissionOrderView`
- Return: `PagedResult<StudentAdmissionOrderListDto>`

### GetAsync [GET]
- Permission: `StudentAdmissionOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentAdmissionOrderView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentAdmissionOrderCreate`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentAdmissionOrderEdit`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StudentAdmissionOrderAccept`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentAdmissionOrderCancel`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentAdmissionOrderDelete`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини ўчириш


## StudentCalcController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StudentCalcView`
- Return: `PagedResult<StudentCalcListDto>`

### GetAsync [GET]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### GetTablesAsync [POST]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentCalcEdit`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StudentCalcAccept`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentCalcCancel`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentCalcDelete`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини ўчириш

### FillAsync [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тозалаш

### StudentCalcReportAsExcelAsync [POST]
- Permission: `StudentCalcPrint`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини печать қилиш

### RefreshAsync [POST]
- Permission: `StudentCalcAccept`
- Return: `IActionResult`


## StudentFixingTransactionController
Route: `StudentFixingTransaction/[action]`

### GetListAsync [POST]
- Permission: `StudentFixingTransactionView`
- Return: `PagedResult<StudentFixingTransactionListDto>`

### Get [GET]
- Permission: `StudentFixingTransactionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentFixingTransactionView`
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentFixingTransactionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `StudentFixingTransactionEdit`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `StudentFixingTransactionDelete`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PaymentOrderAccept`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentOrderCancel`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини бекор қилиш


## StudentLeaveController
Route: `StudentLeave/[action]`

### GetListAsync [POST]
- Permission: `StudentLeaveView`
- Return: `PagedResult<StudentLeaveListDto>`

### GetAsync [GET]
- Permission: `StudentLeaveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentLeaveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentLeaveCreate`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentLeaveEdit`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StudentLeaveAccept`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentLeaveCancel`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentLeaveDelete`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини ўчириш

### FillTableAsync [POST]
- Permission: `StudentLeaveEdit`
- Return: `IActionResult`


## StudentMovementController
Route: `StudentMovement/[action]`

### GetListAsync [POST]
- Permission: `StudentMovementView`
- Return: `PagedResult<StudentMovementListDto>`

### GetAsync [GET]
- Permission: `StudentMovementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentMovementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentMovementCreate`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentMovementEdit`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StudentMovementAccept`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentMovementCancel`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentMovementDelete`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини ўчириш


## StudentPayrollPlasticCardSheetController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `DocumentPagedResult<StudentPayrollPlasticCardSheetListDto>`

### GetPlasticTablesAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `List<StudentPlasticCardDto>`

### GetAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTablesAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `PagedResult<StudentPayrollPlasticCardSheetTableDto>`

### GetTableStipendsAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини яратиш

### ChangeStudentPlasticCardAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини таҳрирлаш

### UpdateTableAsync [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини табел кисмини таҳрирлаш

### FillAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### AcceptAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetAccept`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetDelete`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини ўчириш

### PrintStudentPayrollPlasticCardSheetAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetListForPaymentOrderAsync [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetHashAsync [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetSend`
- Return: `IActionResult`
- Tavsif: Стипендия Пластик карта қайдномаси ҳужжатини жўнатиш

### CancelSendAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetCancelSend`
- Return: `IActionResult`
- Tavsif: Стипендия Пластик карта қайдномаси ҳужжатини жўнатишни бекор қилиш

### ChangeCardAsync [POST]
- Permission: `StudentPayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш


## StudentPayrollSheetController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `StudentPayrollSheetView`
- Return: `DocumentPagedResult<StudentPayrollSheetListDto>`

### GetAsync [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### GetTablesAsync [GET]
- Permission: `StudentPayrollSheetView`
- Return: `PagedResult<StudentPayrollSheetTableDto>`

### GetTableStipendsAsync [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### FillAsync [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси (талабалар) ҳужжатини тўлдириш

### ClearAsync [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси (талабалар) ҳужжатини тозалаш

### CreateAsync [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentPayrollSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `StudentPayrollSheetAccept`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `StudentPayrollSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `StudentPayrollSheetDelete`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини ўчириш

### PrintStudentPayrollSheetAsync [POST]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### GetListForPaymentOrderAsync [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`


## EduSpecialityController
Route: `EduSpeciality/[action]`

### GetListAsync [POST]
- Permission: `EduSpecialityView`
- Return: `PagedResult<EduSpecialityListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `EduSpecialityView`
- Return: `EduSpecialityListWithHistoryDto`

### GetAsync [GET]
- Permission: `EduSpecialityView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EduSpecialityView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EduSpecialityCreate`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EduSpecialityEdit`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EduSpecialityDelete`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини ўчириш

### SyncSpecialityWithBillingAsync [GET]
- Permission: `EduSpecialityCreate`
- Return: `IActionResult`


## FacultyController
Route: `Faculty/[action]`

### GetListAsync [POST]
- Permission: `FacultyView`
- Return: `PagedResult<FacultyListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `FacultyView`
- Return: `FacultyListWithHistoryDto`

### GetAsync [GET]
- Permission: `FacultyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FacultyView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FacultyCreate`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FacultyEdit`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `FacultyDelete`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини ўчириш

### SyncFacultyWithBillingAsync [GET]
- Permission: `FacultyCreate`
- Return: `IActionResult`

### GetFacultyFromBillingAsync [POST]
- Return: `IActionResult`


## StudentPersonController
Route: `StudentPerson/[action]`

### GetListAsync [POST]
- Return: `PagedResult<StudentPersonListDto>`

### GetAsync [GET]
- Permission: `StudentPersonView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentPersonView`
- Return: `IActionResult`

### GetByDocInfoAsync [GET]
- Permission: `StudentPersonCreate`
- Return: `IActionResult`

### GetFromGspAsync [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `StudentPersonEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `StudentPersonDelete`
- Return: `IActionResult`
- Tavsif: Шахс (талаба) ҳужжатини ўчириш


## StudentController
Route: `Student/[action]`

### GetListAsync [POST]
- Permission: `StudentView`
- Return: `PagedResult<StudentListDto>`

### GetListWithHistoryAsync [POST]
- Permission: `StudentView`
- Return: `StudentListWithHistoryDto`

### GetAsync [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### GetHemisStudentAsync [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `StudentCreate`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `StudentEdit`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `StudentDelete`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини ўчириш

### StudentListSaveAsExcelAsync [POST]
- Return: `IActionResult`

### SyncStudentWithBillingAsync [POST]
- Permission: `StudentCreate`
- Return: `IActionResult`

### AllPlasticCardSentToBillingAsync [POST]
- Permission: `StudentView`
- Return: `IActionResult`


## EduAreaController
Route: `EduArea/[action]`

### GetListAsync [POST]
- Permission: `EduAreaView`
- Return: `PagedResult<EduAreaListDto>`

### GetAsync [GET]
- Permission: `EduAreaView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EduAreaView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EduAreaCreate`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EduAreaEdit`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EduAreaDelete`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини ўчириш


## EduSpecialityClassifierController
Route: `EduSpecialityClassifier/[action]`

### GetListAsync [POST]
- Permission: `EduSpecialityClassifierView`
- Return: `PagedResult<EduSpecialityClassifierListDto>`

### GetListWithHistory [POST]
- Permission: `EduSpecialityView`
- Return: `EduSpecialityClassifierListWithHistoryDto`

### GetAsync [GET]
- Permission: `EduSpecialityClassifierView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EduSpecialityClassifierView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EduSpecialityClassifierCreate`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EduSpecialityClassifierEdit`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EduSpecialityClassifierDelete`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини ўчириш

### SyncSpecialityClassifierWithBillingAsync [GET]
- Permission: `EduSpecialityClassifierCreate`
- Return: `IActionResult`


## EduYearController
Route: `EduYear/[action]`

### GetListAsync [POST]
- Permission: `EduYearView`
- Return: `PagedResult<EduYearListDto>`

### GetAsync [GET]
- Permission: `EduYearView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `EduYearView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `EduYearCreate`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `EduYearEdit`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `EduYearDelete`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини ўчириш


## BillingEduController
Route: `[controller]/[action]`

### CreateContractInvoice [POST]
- Return: `IActionResult`

### CancelContractInvoice [POST]
- Return: `IActionResult`

### DeleteContractInvoice [POST]
- Return: `IActionResult`

### GetStudentCard [POST]
- Return: `IActionResult`

### GetContractInvoice [POST]
- Return: `IActionResult`

### GetList [POST]
- Return: `IActionResult`

### CancelOnTime [POST]
- Return: `IActionResult`

### CheckOrgSettlementAccount [POST]
- Return: `IActionResult`

### StudentVisaPlasticCard [POST]
- Return: `IActionResult`

### TestContractInvoice [POST]
- Return: `IActionResult`

### TestContractInvoice [POST]
- Return: `IActionResult`

### Test2ContractInvoice [POST]
- Return: `IActionResult`


## ManualController
Route: `old/Manual/[action]`

### GetEduContractSumTypeSelectList [GET]
- Return: `IActionResult`

### GetEduContractTypeSelectList [GET]
- Return: `IActionResult`

### GetEduFacultyTypeSelectList [GET]
- Return: `IActionResult`

### GetEduPaymentTypeSelectList [GET]
- Return: `IActionResult`

### GetEduFormSelectList [GET]
- Return: `IActionResult`

### GetEduLanguageSelectList [GET]
- Return: `IActionResult`

### GetEduLevelSelectList [GET]
- Return: `IActionResult`

### GetEduTypeSelectList [GET]
- Return: `IActionResult`

### GetScholarshipPenaltyTypeSelectList [GET]
- Return: `IActionResult`

### GetSocialCategorySelectList [GET]
- Return: `IActionResult`

### GetStudentCategorySelectList [GET]
- Return: `IActionResult`

### GetContractCategoryTypeSelectList [GET]
- Return: `IActionResult`


## StudentManageController
Route: `StudentManage/[action]`

### GetListAsync [POST]
- Permission: `StudentManageView`
- Return: `PagedResult<StudentManageListDto>`

### Get [GET]
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `StudentManageView`
- Return: `IActionResult`

### GetFirstOrDefaultAsync [GET]
- Permission: `StudentManageView`
- Return: `IActionResult`


## ContractInvoiceController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `ContractInvoiceView`
- Return: `PagedResult<ContractInvoiceListDto>`

### GetListWithHistory [POST]
- Permission: `ContractInvoiceView`
- Return: `ContractInvoiceListWithHistoryDto`

### Get [GET]
- Permission: `ContractInvoiceView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ContractInvoiceView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ContractInvoiceCreate`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини яратиш

### Update [POST]
- Permission: `ContractInvoiceEdit`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ContractInvoiceAccept`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ContractInvoiceCancel`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ContractInvoiceDelete`
- Return: `IActionResult`
- Tavsif: Шартнома инвойси ҳужжатини ўчириш

### PrintGetList [POST]
- Return: `IActionResult`


## ScholarshipPenaltyController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `ScholarshipPenaltyView`
- Return: `PagedResult<ScholarshipPenaltyListDto`

### Get [GET]
- Permission: `ScholarshipPenaltyView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ScholarshipPenaltyView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ScholarshipPenaltyCreate`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини яратиш

### Update [POST]
- Permission: `ScholarshipPenaltyEdit`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ScholarshipPenaltyAccept`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ScholarshipPenaltyCancel`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ScholarshipPenaltyDelete`
- Return: `IActionResult`
- Tavsif: Стипендия тўлови ҳужжатини ўчириш


## StudentAdmissionOrderController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `StudentAdmissionOrderView`
- Return: `PagedResult<StudentAdmissionOrderListDto`

### Get [GET]
- Permission: `StudentAdmissionOrderView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentAdmissionOrderView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentAdmissionOrderCreate`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини яратиш

### Update [POST]
- Permission: `StudentAdmissionOrderEdit`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StudentAdmissionOrderAccept`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentAdmissionOrderCancel`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentAdmissionOrderDelete`
- Return: `IActionResult`
- Tavsif: Талабаларни рўйҳатга олиш тартиби ҳужжатини ўчириш


## StudentCalcController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `StudentCalcView`
- Return: `PagedResult<StudentCalcListDto>`

### Get [GET]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### GetTables [POST]
- Permission: `StudentCalcView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини яратиш

### Update [POST]
- Permission: `StudentCalcEdit`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StudentCalcAccept`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentCalcCancel`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentCalcDelete`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини ўчириш

### Fill [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тўлдириш

### Clear [POST]
- Permission: `StudentCalcCreate`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини тозалаш

### StudentCalcReportAsExcel [POST]
- Permission: `StudentCalcPrint`
- Return: `IActionResult`
- Tavsif: Стипендия ҳисоби ҳужжатини печать қилиш

### Refresh [POST]
- Permission: `StudentCalcAccept`
- Return: `IActionResult`


## StudentFixingTransactionController
Route: `old/StudentFixingTransaction/[action]`

### GetListAsync [POST]
- Permission: `StudentFixingTransactionView`
- Return: `PagedResult<StudentFixingTransactionListDto>`

### Get [GET]
- Permission: `StudentFixingTransactionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentFixingTransactionView`
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentFixingTransactionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `StudentFixingTransactionEdit`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `StudentFixingTransactionDelete`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PaymentOrderAccept`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PaymentOrderCancel`
- Return: `IActionResult`
- Tavsif: Талабаларни тузатиш транзаксияси ҳужжатини бекор қилиш


## StudentLeaveController
Route: `old/StudentLeave/[action]`

### GetList [POST]
- Permission: `StudentLeaveView`
- Return: `PagedResult<StudentLeaveListDto`

### Get [GET]
- Permission: `StudentLeaveView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentLeaveView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentLeaveCreate`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини яратиш

### Update [POST]
- Permission: `StudentLeaveEdit`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StudentLeaveAccept`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentLeaveCancel`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentLeaveDelete`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини ўчириш

### FillTable [POST]
- Permission: `StudentLeaveEdit`
- Return: `IActionResult`


## StudentMovementController
Route: `old/StudentMovement/[action]`

### GetList [POST]
- Permission: `StudentMovementView`
- Return: `PagedResult<StudentMovementListDto`

### Get [GET]
- Permission: `StudentMovementView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentMovementView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentMovementCreate`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини яратиш

### Update [POST]
- Permission: `StudentMovementEdit`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StudentMovementAccept`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentMovementCancel`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentMovementDelete`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини ўчириш


## StudentPayrollPlasticCardSheetController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `DocumentPagedResult<StudentPayrollPlasticCardSheetListDto`

### Get [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### GetTables [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `PagedResult<StudentPayrollPlasticCardSheetTableDto`

### GetTableStipends [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини яратиш

### Update [POST]
- Permission: `StudentPayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини таҳрирлаш

### UpdateTable [POST]
- Permission: `PayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини табел кисмини таҳрирлаш

### Fill [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини тўлдириш

### Clear [POST]
- Permission: `StudentPayrollPlasticCardSheetCreate`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини бекор қилиш

### Accept [POST]
- Permission: `StudentPayrollPlasticCardSheetAccept`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentPayrollPlasticCardSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentPayrollPlasticCardSheetDelete`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости плас.(талабалар) ҳужжатини ўчириш

### PrintStudentPayrollPlasticCardSheet [POST]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### GetListForPaymentOrder [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `StudentPayrollPlasticCardSheetView`
- Return: `IActionResult`

### Send [POST]
- Permission: `StudentPayrollPlasticCardSheetSend`
- Return: `IActionResult`
- Tavsif: Стипендия Пластик карта қайдномаси ҳужжатини жўнатиш

### CancelSend [POST]
- Permission: `StudentPayrollPlasticCardSheetCancelSend`
- Return: `IActionResult`
- Tavsif: Стипендия Пластик карта қайдномаси ҳужжатини жўнатишни бекор қилиш

### ChangeCard [POST]
- Permission: `StudentPayrollPlasticCardSheetEdit`
- Return: `IActionResult`
- Tavsif: Пластик карта қайдномаси ҳужжатини таҳрирлаш


## StudentPayrollSheetController
Route: `old/[controller]/[action]`

### GetList [POST]
- Permission: `StudentPayrollSheetView`
- Return: `DocumentPagedResult<StudentPayrollSheetListDto`

### Get [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### GetTables [GET]
- Permission: `StudentPayrollSheetView`
- Return: `PagedResult<StudentPayrollSheetTableDto`

### GetTableStipends [GET]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### Fill [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси (талабалар) ҳужжатини тўлдириш

### Clear [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов қайдномаси (талабалар) ҳужжатини тозалаш

### Create [POST]
- Permission: `StudentPayrollSheetCreate`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини яратиш

### Update [POST]
- Permission: `StudentPayrollSheetEdit`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `StudentPayrollSheetAccept`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `StudentPayrollSheetCancel`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `StudentPayrollSheetDelete`
- Return: `IActionResult`
- Tavsif: Тўлов ведемости (талабалар) ҳужжатини ўчириш

### PrintStudentPayrollSheet [POST]
- Permission: `StudentPayrollSheetView`
- Return: `IActionResult`

### GetListForPaymentOrder [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`


## EduSpecialityController
Route: `old/EduSpeciality/[action]`

### GetList [POST]
- Permission: `EduSpecialityView`
- Return: `PagedResult<EduSpecialityListDto`

### GetListWithHistory [POST]
- Permission: `EduSpecialityView`
- Return: `EduSpecialityListWithHistoryDto`

### Get [GET]
- Permission: `EduSpecialityView`
- Return: `IActionResult`

### Get [GET]
- Permission: `EduSpecialityView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Permission: `EduSpecialityCreate`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини яратиш

### Update [POST]
- Permission: `EduSpecialityEdit`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `EduSpecialityDelete`
- Return: `IActionResult`
- Tavsif: Мутаҳассислиги ҳужжатини ўчириш

### SyncSpecialityWithBilling [GET]
- Permission: `EduSpecialityCreate`
- Return: `IActionResult`


## FacultyController
Route: `old/Faculty/[action]`

### GetList [POST]
- Permission: `FacultyView`
- Return: `PagedResult<FacultyListDto`

### GetListWithHistory [POST]
- Permission: `FacultyView`
- Return: `FacultyListWithHistoryDto`

### Get [GET]
- Permission: `FacultyView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FacultyView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Permission: `FacultyCreate`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини яратиш

### Update [POST]
- Permission: `FacultyEdit`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `FacultyDelete`
- Return: `IActionResult`
- Tavsif: Факултет ҳужжатини ўчириш

### SyncFacultyWithBilling [GET]
- Permission: `FacultyCreate`
- Return: `IActionResult`

### GetFacultyFromBilling [POST]
- Return: `IActionResult`


## StudentPersonController
Route: `old/StudentPerson/[action]`

### GetList [POST]
- Return: `PagedResult<StudentPersonListDto`

### Get [GET]
- Permission: `StudentPersonView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentPersonView`
- Return: `IActionResult`

### GetByDocInfo [GET]
- Permission: `StudentPersonCreate`
- Return: `IActionResult`

### GetFromGsp [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Update [POST]
- Permission: `StudentPersonEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `StudentPersonDelete`
- Return: `IActionResult`
- Tavsif: Шахс (талаба) ҳужжатини ўчириш


## StudentController
Route: `old/Student/[action]`

### GetList [POST]
- Permission: `StudentView`
- Return: `PagedResult<StudentListDto`

### GetListWithHistory [POST]
- Permission: `StudentView`
- Return: `StudentListWithHistoryDto`

### Get [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### GetHemisStudent [GET]
- Permission: `StudentView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `StudentCreate`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини яратиш

### Update [POST]
- Permission: `StudentEdit`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `StudentDelete`
- Return: `IActionResult`
- Tavsif: Талаба ҳужжатини ўчириш

### StudentListSaveAsExcel [POST]
- Return: `IActionResult`

### SyncStudentWithBilling [POST]
- Permission: `StudentCreate`
- Return: `IActionResult`

### AllPlasticCardSentToBilling [POST]
- Permission: `StudentView`
- Return: `IActionResult`


## EduAreaController
Route: `old/EduArea/[action]`

### GetList [POST]
- Permission: `EduAreaView`
- Return: `PagedResult<EduAreaListDto`

### Get [GET]
- Permission: `EduAreaView`
- Return: `IActionResult`

### Get [GET]
- Permission: `EduAreaView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Permission: `EduAreaCreate`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини яратиш

### Update [POST]
- Permission: `EduAreaEdit`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `EduAreaDelete`
- Return: `IActionResult`
- Tavsif: Таълим муассасаси ҳужжатини ўчириш


## EduSpecialityClassifierController
Route: `old/EduSpecialityClassifier/[action]`

### GetList [POST]
- Permission: `EduSpecialityClassifierView`
- Return: `PagedResult<EduSpecialityClassifierListDto`

### GetListWithHistory [POST]
- Permission: `EduSpecialityView`
- Return: `EduSpecialityClassifierListWithHistoryDto`

### Get [GET]
- Permission: `EduSpecialityClassifierView`
- Return: `IActionResult`

### Get [GET]
- Permission: `EduSpecialityClassifierView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Permission: `EduSpecialityClassifierCreate`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини яратиш

### Update [POST]
- Permission: `EduSpecialityClassifierEdit`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `EduSpecialityClassifierDelete`
- Return: `IActionResult`
- Tavsif: Таълим мутахассисликлари классификатори ҳужжатини ўчириш

### SyncSpecialityClassifierWithBilling [GET]
- Permission: `EduSpecialityClassifierCreate`
- Return: `IActionResult`


## EduYearController
Route: `old/EduYear/[action]`

### GetList [POST]
- Permission: `EduYearView`
- Return: `PagedResult<EduYearListDto`

### Get [GET]
- Permission: `EduYearView`
- Return: `IActionResult`

### Get [GET]
- Permission: `EduYearView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Permission: `EduYearCreate`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини яратиш

### Update [POST]
- Permission: `EduYearEdit`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `EduYearDelete`
- Return: `IActionResult`
- Tavsif: Ўқув йили ҳужжатини ўчириш


## StudentManageController
Route: `old/StudentManage/[action]`

### GetList [POST]
- Permission: `StudentManageView`
- Return: `PagedResult<StudentManageListDto`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `StudentManageView`
- Return: `IActionResult`

### GetFirstOrDefault [GET]
- Permission: `StudentManageView`
- Return: `IActionResult`
