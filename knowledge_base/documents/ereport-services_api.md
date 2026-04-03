# ereport-services — API Endpointlar


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

### GetRjReportTypeSelectList [GET]
- Return: `IActionResult`

### GetBrCalcTypeSelectList [GET]
- Return: `IActionResult`

### GetFormaSetTypeSelectList [GET]
- Return: `IActionResult`

### GetFormaSetAppSelectList [GET]
- Return: `IActionResult`

### GetFormaSetOrganizationTypeList [GET]
- Return: `IActionResult`

### GetBudgetProgramTypeSelectList [GET]
- Return: `IActionResult`

### GetTargetIndicatorTypeList [GET]
- Return: `IActionResult`

### GetRjpositionList [GET]
- Return: `IActionResult`

### GetList [POST]
- Permission: `PaymentOrderView`
- Return: `PagedResult<CurrencyTransactionReportListDto`

### PrintGetList [POST]
- Permission: `PaymentOrderView`
- Return: `IActionResult`

### HisobotTopshirmaganTashkilotlarniYopish [POST]
- Return: `IActionResult`

### GetOrganizationReportByDistrict [GET]
- Permission: `PaymentOrderView`
- Return: `IActionResult`


## ReportController
Route: `Report/[action]`

### GetForma2Fill [POST]
- Permission: `Forma2Fill`
- Return: `IActionResult`

### GetReportFormBMMJ [POST]
- Return: `IActionResult`

### PrintForma2Fill [POST]
- Permission: `FormaRjView`
- Return: `IActionResult`

### PrintFormaRjTemplate [POST]
- Permission: `FormaRjView`
- Return: `IActionResult`

### PrintFormaBMMJ [POST]
- Permission: `FormaRjView`
- Return: `IActionResult`

### GetEreportMonitoring [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### GetSubmitForma1OrganizationPrint [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### GetEreportByFinancingMonitoring [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### GetEreportByFinancingMonitoringRecepientType [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### PrintEreportMonitoring [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### PrintEreportByFinancingMonitoring [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### PrintEreportByFinancingMonitoringRecepientType [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### PrintForma1Monitoring [POST]
- Permission: `MonitoringSummary`
- Return: `IActionResult`

### GetRestByPaymentOrder [POST]
- Return: `IActionResult`

### PrintGetRestByPaymentOrder [POST]
- Return: `IActionResult`

### GetRestByAmount [POST]
- Return: `IActionResult`


## BudgetProgramCardController
Route: `BudgetProgramCard/[action]`

### GetList [POST]
- Permission: `BudgetProgramCardView`
- Return: `PagedResult<BudgetProgramCardListDto>`

### Get [GET]
- Permission: `BudgetProgramCardView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetProgramCardView`
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetProgramCardCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetProgramCardEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `BudgetProgramCardAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `BudgetProgramCardCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetProgramCardDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `BudgetProgramCardCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `BudgetProgramCardDelete`
- Return: `IActionResult`

### Print [POST]
- Permission: `BudgetProgramCardView`
- Return: `IActionResult`

### Send [POST]
- Permission: `BudgetProgramCardSend`
- Return: `IActionResult`

### GetListSentToHeader [POST]
- Permission: `BudgetProgramCardViewForReceive`
- Return: `PagedResult<BudgetProgramCardListDto>`

### ReportAccepted [POST]
- Permission: `BudgetProgramCardReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `BudgetProgramCardNotReportAccepted`
- Return: `IActionResult`

### ReportRegistered [POST]
- Permission: `BudgetProgramCardReportRegistered`
- Return: `IActionResult`

### ReportNotRegistered [POST]
- Permission: `BudgetProgramCardCancelReportRegistered`
- Return: `IActionResult`


## BudgetProgramController
Route: `BudgetProgram/[action]`

### GetList [POST]
- Permission: `BudgetProgramView`
- Return: `PagedResult<BudgetProgramListDto>`

### Get [GET]
- Permission: `BudgetProgramView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetProgramView`
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetProgramCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetProgramEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `BudgetProgramAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `BudgetProgramCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetProgramDelete`
- Return: `IActionResult`

### Print [POST]
- Permission: `BudgetProgramView`
- Return: `IActionResult`


## IndicatorController
Route: `Indicator/[action]`

### GetList [POST]
- Permission: `IndicatorView`
- Return: `PagedResult<IndicatorListDto>`

### Get [GET]
- Permission: `IndicatorView`
- Return: `IActionResult`

### Get [GET]
- Permission: `IndicatorView`
- Return: `IActionResult`

### Create [POST]
- Permission: `IndicatorCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `IndicatorEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `IndicatorAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `IndicatorCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `IndicatorDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `IndicatorCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `IndicatorDelete`
- Return: `IActionResult`

### Print [POST]
- Permission: `IndicatorView`
- Return: `IActionResult`


## IndicatorPositionController
Route: `IndicatorPosition/[action]`

### GetList [POST]
- Permission: `IndicatorPositionView`
- Return: `PagedResult<IndicatorPositionListDto>`

### Get [GET]
- Permission: `IndicatorPositionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `IndicatorPositionView`
- Return: `IActionResult`

### Create [POST]
- Permission: `IndicatorPositionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `IndicatorPositionEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `IndicatorPositionDelete`
- Return: `IActionResult`

### Accept [POST]
- Permission: `IndicatorPositionAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `IndicatorPositionCancel`
- Return: `IActionResult`

### Import [POST]
- Permission: `IndicatorPositionView`
- Return: `IActionResult`


## IndicatorReceiveController
Route: `IndicatorReceive/[action]`

### GetList [POST]
- Permission: `IndicatorReceiveViewForReceive`
- Return: `IActionResult`

### Receive [POST]
- Permission: `IndicatorReceiveReportAccepted`
- Return: `IActionResult`

### NotReceive [POST]
- Permission: `IndicatorReceiveNotReportAccepted`
- Return: `IActionResult`

### Agreed [POST]
- Permission: `IndicatorReceiveAgreed`
- Return: `IActionResult`

### Approved [POST]
- Permission: `IndicatorReceiveApproved`
- Return: `IActionResult`

### NotApproved [POST]
- Permission: `IndicatorReceiveApproved`
- Return: `IActionResult`

### Print [POST]
- Permission: `IndicatorReceiveViewForReceive`
- Return: `IActionResult`

### GetStatuses [GET]
- Return: `IActionResult`


## OldIndicatorController
Route: `OldIndicator/[action]`

### GetList [POST]
- Permission: `OldIndicatorView`
- Return: `PagedResult<OldIndicatorListDto>`

### Get [GET]
- Permission: `OldIndicatorView`
- Return: `IActionResult`

### Get [GET]
- Permission: `OldIndicatorView`
- Return: `IActionResult`

### Create [POST]
- Permission: `OldIndicatorCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `OldIndicatorEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `OldIndicatorAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `OldIndicatorCancel`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `OldIndicatorCreate`
- Return: `IActionResult`

### Delete [POST]
- Permission: `OldIndicatorDelete`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `OldIndicatorDelete`
- Return: `IActionResult`

### SendAsync [POST]
- Permission: `OldIndicatorSend`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `OldIndicatorSend`
- Return: `IActionResult`

### Print [POST]
- Permission: `OldIndicatorView`
- Return: `IActionResult`


## BudgetRequestCalcController
Route: `BudgetRequestCalc/[action]`

### GetList [POST]
- Permission: `BudgetRequestCalcView`
- Return: `PagedResult<BudgetRequestCalcListDto`

### GetListForHeaderOrg [POST]
- Permission: `BudgetRequestCalcViewForReceive`
- Return: `PagedResult<BudgetRequestCalcListDto`

### Get [GET]
- Permission: `BudgetRequestCalcView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetRequestCalcView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `BudgetRequestCalcView`
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetRequestCalcCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetRequestCalcEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `BudgetRequestCalcAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `BudgetRequestCalcCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `BudgetRequestCalcSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `BudgetRequestCalcReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `BudgetRequestCalcNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `BudgetRequestCalcCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetRequestCalcDelete`
- Return: `IActionResult`

### PrintForma2 [POST]
- Permission: `BudgetRequestCalcView`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `BudgetRequestCalcCreate`
- Return: `IActionResult`

### FillOrgs [POST]
- Permission: `BudgetRequestCalcCreate`
- Return: `IActionResult`

### ClearTables [POST]
- Permission: `BudgetRequestCalcCreate`
- Return: `IActionResult`

### ClearOrgs [POST]
- Permission: `BudgetRequestCalcCreate`
- Return: `IActionResult`

### PrintBudgetRequestCalc [POST]
- Return: `IActionResult`


## BudgetRequestController
Route: `BudgetRequest/[action]`

### GetList [POST]
- Permission: `BudgetRequestView`
- Return: `PagedResult<BudgetRequestListDto>`

### Get [GET]
- Permission: `BudgetRequestView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetRequestView`
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetRequestCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetRequestEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `BudgetRequestAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `BudgetRequestCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetRequestDelete`
- Return: `IActionResult`

### PrintBudgetRequest [POST]
- Permission: `BudgetRequestView`
- Return: `IActionResult`


## Forma1Controller
Route: `Forma1/[action]`

### GetList [POST]
- Permission: `Forma1View`
- Return: `PagedResult<Forma1ListDto>`

### GetByAccountList [POST]
- Permission: `Forma1View`
- Return: `PagedResult<Forma1ListDto>`

### GetListForHeaderOrg [POST]
- Permission: `Forma1ViewForReceive`
- Return: `PagedResult<Forma1ListDto>`

### Get [GET]
- Permission: `Forma1View`
- Return: `IActionResult`

### PenalizeForMissingReport [GET]
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma1Send`
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma1Send`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `Forma1Send`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma1Create`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `Forma1Create`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma1Edit`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma1ReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma1NotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma1CancelReportAccepted`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `Forma1Send`
- Return: `IActionResult`

### AdminCancel [POST]
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma1Accept`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `Forma1Accept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma1Cancel`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `Forma1Cancel`
- Return: `IActionResult`

### ExplanatoryNote [POST]
- Permission: `Forma1Cancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma1Delete`
- Return: `IActionResult`

### PrintForma1 [POST]
- Return: `IActionResult`

### PrintForma1ByIdOrg [POST]
- Permission: `Forma1View`
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `Forma1Create`
- Return: `IActionResult`

### FillByAccountTable [POST]
- Permission: `Forma1Create`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma1Create`
- Return: `IActionResult`


## Forma1TotalController
Route: `Forma1Total/[action]`

### GetList [POST]
- Permission: `Forma1TotalView`
- Return: `PagedResult<Forma1TotalListDto>`

### Get [GET]
- Permission: `Forma1TotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `Forma1TotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma1TotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma1TotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma1TotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma1TotalCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma1TotalDelete`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma1TotalSend`
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma1TotalSend`
- Return: `IActionResult`

### PrintForma1Total [POST]
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `Forma1TotalView`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma1TotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma1TotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma1TotalCancelReportAccepted`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma1TotalCreate`
- Return: `IActionResult`


## Forma2Controller
Route: `Forma2/[action]`

### GetListAsync [POST]
- Permission: `Forma2View`
- Return: `PagedResult<Forma2ListDto>`

### GetListForHeaderOrg [POST]
- Permission: `Forma2ViewForReceive`
- Return: `DbPagedModel<GetListByHeaderOrgForma2Dto>`

### Get [GET]
- Permission: `Forma2View`
- Return: `IActionResult`

### GetByOrgSettlementAccountId [GET]
- Permission: `Forma2View`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma2Send`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma2Edit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma2Accept`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `Forma2Accept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma2Cancel`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `Forma2Cancel`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `Forma2Send`
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma2Send`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `Forma2Send`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma2ReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma2NotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma2CancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma2Delete`
- Return: `IActionResult`

### PrintForma2 [POST]
- Return: `IActionResult`

### PrintForma2Totals [POST]
- Permission: `Forma2View`
- Return: `IActionResult`

### PrintForma2ForHeaderOrg [POST]
- Return: `IActionResult`

### PrintForma2Child [POST]
- Return: `IActionResult`

### PrintForma2ChildByOrg [POST]
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`

### FillOrgs [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`

### ClearOrgs [POST]
- Permission: `Forma2Create`
- Return: `IActionResult`


## Forma2TotalController
Route: `Forma2Total/[action]`

### GetList [POST]
- Permission: `Forma2TotalView`
- Return: `PagedResult<Forma2TotalListDto>`

### Get [GET]
- Permission: `Forma2TotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `Forma2TotalView`
- Return: `IActionResult`

### GetHeaderOrganizationName [GET]
- Permission: `Forma2TotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma2TotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma2TotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma2TotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma2TotalCancel`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma2TotalSend`
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma2TotalSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma2TotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma2TotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma2TotalCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma2TotalDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `Forma2TotalCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma2TotalCreate`
- Return: `IActionResult`

### PrintForma2 [POST]
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `Forma2TotalView`
- Return: `IActionResult`


## Forma5Controller
Route: `Forma5/[action]`

### GetList [POST]
- Permission: `Forma5View`
- Return: `PagedResult<Forma5ListDto>`

### GetByAccountList [POST]
- Permission: `Forma5View`
- Return: `PagedResult<Forma5ListDto>`

### GetListForHeaderOrg [POST]
- Permission: `Forma5ViewForReceive`
- Return: `PagedResult<Forma5ListDto>`

### Get [GET]
- Permission: `Forma5View`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetByAccount [GET]
- Permission: `Forma5View`
- Return: `IActionResult`

### GetByOrgSettlementAccountId [GET]
- Permission: `Forma5View`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma5View`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `Forma5Send`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `Forma5Accept`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `Forma5Cancel`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma5Create`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `Forma5Create`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma5Edit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma5Accept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma5Cancel`
- Return: `IActionResult`

### AdminCancel [POST]
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma5Send`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma5ReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma5NotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma5CancelReportAccepted`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `Forma5Send`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma5ReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma5NotReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma5Delete`
- Return: `IActionResult`

### PrintForma5 [POST]
- Return: `IActionResult`

### PrintForma5ByOrg [POST]
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `Forma5Create`
- Return: `IActionResult`

### FillByAccountTable [POST]
- Permission: `Forma5Create`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma5Create`
- Return: `IActionResult`


## Forma5TotalController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `Forma5TotalView`
- Return: `PagedResult<Forma5TotalListDto>`

### GetListForHeaderOrg [POST]
- Permission: `Forma5TotalViewForReceive`
- Return: `PagedResult<Forma5TotalListDto`

### Get [GET]
- Permission: `Forma5TotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `Forma5TotalView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `Forma5TotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma5TotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma5TotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `Forma5TotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `Forma5TotalCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `Forma5TotalSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `Forma5TotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `Forma5TotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `Forma5TotalCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma5TotalDelete`
- Return: `IActionResult`

### PrintForma5Total [POST]
- Return: `IActionResult`

### PrintForma5TotalByOrg [POST]
- Return: `IActionResult`

### PrintGetList [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `Forma5TotalCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `Forma5TotalCreate`
- Return: `IActionResult`


## FormaAnalizController
Route: `FormaAnaliz/[action]`

### GetListAsync [POST]
- Permission: `FormaAnalizView`
- Return: `PagedResult<FormaAnalizListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaAnalizViewForReceive`
- Return: `PagedResult<FormaAnalizListDto`

### Get [GET]
- Permission: `FormaAnalizView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaAnalizView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaAnalizEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaAnalizAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaAnalizCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaAnalizDelete`
- Return: `IActionResult`

### FillBalans [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### FillVneBalans [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### FillDmj [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### ClearTableBalans [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### ClearTableVneBalans [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### ClearTableDmj [POST]
- Permission: `FormaAnalizCreate`
- Return: `IActionResult`

### Print [POST]
- Return: `IActionResult`

### PrintForma1 [POST]
- Return: `IActionResult`


## FormaDkByAccountController
Route: `FormaDkByAccount/[action]`

### GetListAsync [POST]
- Permission: `FormaDkByAccountView`
- Return: `PagedResult<FormaDkByAccountListDto>`

### Get [GET]
- Permission: `FormaDkByAccountView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaDkByAccountView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaDkByAccountCreate`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaDkByAccountEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaDkByAccountAccept`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `FormaDkByAccountAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaDkByAccountCancel`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `FormaDkByAccountCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaDkByAccountDelete`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `FormaDkByAccountSend`
- Return: `IActionResult`

### ReturnFromTreasureAll [POST]
- Permission: `FormaDkByAccountSend`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaDkByAccountView`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaDkByAccountSend`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `FormaDkByAccountSend`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaDkByAccountCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaDkByAccountCreate`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaDkByAccountView`
- Return: `IActionResult`


## FormaDkController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `FormaDkView`
- Return: `PagedResult<FormaDkListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaDkViewForReceive`
- Return: `PagedResult<FormaDkListDto>`

### Get [GET]
- Permission: `FormaDkView`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaDkView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaDkCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaDkEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaDkAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaDkCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaDkSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaDkReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaDkNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaDkCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaDkDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaDkCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaDkCreate`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaDkView`
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`


## FormaDkTotalController
Route: `FormaDkTotal/[action]`

### GetList [POST]
- Permission: `FormaDkTotalView`
- Return: `PagedResult<FormaDkTotalListDto>`

### Get [GET]
- Permission: `FormaDkTotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaDkTotalView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaDkTotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaDkTotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaDkTotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaDkTotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaDkTotalCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaDkTotalSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaDkTotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaDkTotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaDkTotalCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaDkTotalDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaDkTotalCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaDkTotalCreate`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaDkTotalView`
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `FormaDkTotalView`
- Return: `IActionResult`


## FormaFinResController
Route: `FormaFinRes/[action]`

### GetList [POST]
- Permission: `FormaFinResView`
- Return: `PagedResult<FormaFinResListDto>`

### GetByAccountList [POST]
- Permission: `FormaFinResView`
- Return: `PagedResult<FormaFinResListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaFinResViewForReceive`
- Return: `PagedResult<FormaFinResListDto>`

### Get [GET]
- Permission: `FormaFinResView`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetByOrgSettlementAccountId [GET]
- Permission: `Forma5View`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaFinResEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaFinResAccept`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaFinResSend`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaFinResView`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaFinResCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaFinResDelete`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `FormaFinResSend`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `FormaFinResAccept`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `FormaFinResCancel`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaFinResView`
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### FillByAccountTable [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaFinResCreate`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `FormaFinResSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaFinResReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaFinResNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaFinResCancelReportAccepted`
- Return: `IActionResult`

### AdminCancel [POST]
- Return: `IActionResult`


## FormaFinResTotalController
Route: `FormaFinResTotal/[action]`

### GetList [POST]
- Permission: `FormaFinResTotalView`
- Return: `PagedResult<FormaFinResTotalListDto>`

### Get [GET]
- Permission: `FormaFinResTotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaFinResTotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaFinResTotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaFinResTotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaFinResTotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaFinResTotalCancel`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaFinResTotalDelete`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaFinResTotalSend`
- Return: `IActionResult`

### GetFormaFinResForma2DeffAmount [GET]
- Permission: `FormaFinResTotalView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaFinResTotalSend`
- Return: `IActionResult`

### GetListForHeaderOrg [POST]
- Permission: `FormaFinResTotalViewForReceive`
- Return: `PagedResult<FormaFinResTotalListDto`

### ReportAccepted [POST]
- Permission: `FormaFinResReportTotalAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaFinResNotReportTotalAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaFinResCancelReportTotalAccepted`
- Return: `IActionResult`

### PrintFormaFinResTotal [POST]
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `FormaFinResTotalView`
- Return: `IActionResult`


## FormaRjController
Route: `FormaRj/[action]`

### GetList [POST]
- Permission: `FormaRjView`
- Return: `PagedResult<FormaRjListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaRjViewForReceive`
- Return: `DbPagedModel<GetListByHeaderOrgFormaRjDto>`

### Get [GET]
- Permission: `FormaRjView`
- Return: `IActionResult`

### GetByOrgSettlementAccountId [GET]
- Permission: `FormaRjView`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`

### AutoCreate [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaRjEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaRjAccept`
- Return: `IActionResult`

### AcceptAll [POST]
- Permission: `FormaRjAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaRjCancel`
- Return: `IActionResult`

### CancelAll [POST]
- Permission: `Forma2Cancel`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `FormaRjSend`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaRjDelete`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaRjSend`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaRjSend`
- Return: `IActionResult`

### SendAll [POST]
- Permission: `FormaRjSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaRjReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaRjNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaRjCancelReportAccepted`
- Return: `IActionResult`

### PrintFormaRj [POST]
- Permission: `FormaRjView`
- Return: `IActionResult`

### PrintFormaRjByOrg [POST]
- Permission: `FormaRjTotalView`
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`

### FillOrgs [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`

### ClearOrgs [POST]
- Permission: `FormaRjCreate`
- Return: `IActionResult`


## FormaRjTotalController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `FormaRjTotalView`
- Return: `PagedResult<FormaRjTotalListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaRjTotalViewForReceive`
- Return: `PagedResult<FormaRjTotalListDto>`

### Get [GET]
- Permission: `FormaRjTotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaRjTotalView`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaRjTotalSend`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaRjTotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaRjTotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaRjTotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaRjTotalCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaRjTotalSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaRjTotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaRjTotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaRjTotalCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaRjTotalDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaRjTotalCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaRjTotalCreate`
- Return: `IActionResult`

### PrintFormaRjTotal [POST]
- Permission: `FormaRjTotalView`
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `FormaRjTotalView`
- Return: `IActionResult`


## FormaSetController
Route: `FormaSet/[action]`

### GetList [POST]
- Permission: `FormaSetView`
- Return: `PagedResult<FormaSetListDto>`

### GetSummList [POST]
- Permission: `FormaSetView`
- Return: `PagedResult<FormaSetListDto>`

### GetListForHeaderOrg [POST]
- Permission: `FormaSetViewForReceive`
- Return: `PagedResult<FormaSetListDto>`

### Get [GET]
- Permission: `FormaSetView`
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetSumm [GET]
- Permission: `FormaSetView`
- Return: `IActionResult`

### GetRegistry [GET]
- Permission: `FormaSetViewForReceive`
- Return: `IActionResult`

### GetRegistry [GET]
- Permission: `FormaSetViewForReceive`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaSetView`
- Return: `IActionResult`

### PrintGetListForHeaderOrg [POST]
- Permission: `Forma2ViewForReceive`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaSetCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaSetEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaSetAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaSetCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaSetSend`
- Return: `IActionResult`

### ReturnFromTreasure [POST]
- Permission: `FormaSetSend`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaSetReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaSetCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaSetDelete`
- Return: `IActionResult`

### PrintFormaSet [POST]
- Permission: `FormaSetView`
- Return: `IActionResult`

### PrintFormaSetRegistry [POST]
- Permission: `FormaSetViewForReceive`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaSetCreate`
- Return: `IActionResult`

### FillSummTable [POST]
- Permission: `FormaSetCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaSetCreate`
- Return: `IActionResult`

### ReadToSend [POST]
- Permission: `FormaSetReadyToSend`
- Return: `IActionResult`

### CancelSendCenter [POST]
- Permission: `FormaSetCancelReadyToSend`
- Return: `IActionResult`

### GetListForCenterOrg [POST]
- Permission: `FormaSetViewForCenter`
- Return: `PagedResult<FormaSetListDto>`

### CancelFromCenter [POST]
- Permission: `FormaSetCenterToCancel`
- Return: `IActionResult`

### GetFormaSetRegistryList [POST]
- Permission: `FormaSetViewForReceive`
- Return: `PagedResult<FormaSetListDto`

### FillRegistryTable [POST]
- Permission: `FormaSetRegistryCreate`
- Return: `IActionResult`

### ClearRegistryTable [POST]
- Permission: `FormaSetRegistryEdit`
- Return: `IActionResult`


## FormaSetTotalController
Route: `FormaSetTotal/[action]`

### GetList [POST]
- Permission: `FormaSetTotalView`
- Return: `PagedResult<FormaSetTotalListDto>`

### Get [GET]
- Permission: `FormaSetTotalView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaSetTotalView`
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaSetTotalCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaSetTotalEdit`
- Return: `IActionResult`

### Accept [POST]
- Permission: `FormaSetTotalAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `FormaSetTotalCancel`
- Return: `IActionResult`

### Send [POST]
- Permission: `FormaSetTotalSend`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `FormaSetView`
- Return: `IActionResult`

### ReportAccepted [POST]
- Permission: `FormaSetTotalReportAccepted`
- Return: `IActionResult`

### NotReportAccepted [POST]
- Permission: `FormaSetTotalNotReportAccepted`
- Return: `IActionResult`

### CancelReportAccepted [POST]
- Permission: `FormaSetTotalCancelReportAccepted`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaSetTotalDelete`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaSetTotalCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaSetTotalCreate`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaSetTotalView`
- Return: `IActionResult`

### Print [POST]
- Permission: `FormaSetView`
- Return: `IActionResult`


## BudgetProgramTypeController
Route: `BudgetProgramType/[action]`

### GetList [POST]
- Permission: `BudgetProgramTypeView`
- Return: `PagedResult<BudgetProgramTypeListDto`

### Get [GET]
- Permission: `BudgetProgramTypeView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetProgramTypeView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### SubBudgetProgramTypeGetAsSelectList [GET]
- Return: `IActionResult`

### SubBudgetProgramTypeTableGetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetProgramTypeCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetProgramTypeEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetProgramTypeDelete`
- Return: `IActionResult`


## BudgetSectorController
Route: `BudgetSector/[action]`

### GetList [POST]
- Permission: `BudgetSectorView`
- Return: `PagedResult<BudgetSectorListDto`

### Get [GET]
- Permission: `BudgetSectorView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetSectorView`
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetSectorCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetSectorEdit`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Delete [POST]
- Permission: `BudgetSectorDelete`
- Return: `IActionResult`


## BrCoefController
Route: `BrCoef/[action]`

### GetList [POST]
- Permission: `BrCoefView`
- Return: `PagedResult<BrCoefListDto>`

### Get [GET]
- Permission: `BrCoefView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BrCoefView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `BrCoefCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BrCoefEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `BrCoefDelete`
- Return: `IActionResult`


## BudgetRequestEventController
Route: `BudgetRequestEvent/[action]`

### GetList [POST]
- Permission: `BudgetRequestEventView`
- Return: `PagedResult<BudgetRequestEventListDto>`

### Get [GET]
- Permission: `BudgetRequestEventView`
- Return: `IActionResult`

### Get [GET]
- Permission: `BudgetRequestEventView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `BudgetRequestEventCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `BudgetRequestEventEdit`
- Return: `IActionResult`


## EventController
Route: `Event/[action]`

### GetList [POST]
- Permission: `EventView`
- Return: `PagedResult<EventListDto>`

### Get [GET]
- Permission: `EventView`
- Return: `IActionResult`

### Get [GET]
- Permission: `EventView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `EventCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `EventEdit`
- Return: `IActionResult`


## Forma1PositionController
Route: `Forma1Position/[action]`

### GetList [POST]
- Permission: `Forma1PositionView`
- Return: `PagedResult<Forma1PositionListDto`

### Get [GET]
- Permission: `Forma1PositionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `Forma1PositionView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma1PositionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma1PositionEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma1PositionDelete`
- Return: `IActionResult`


## Forma2PositionCanEditController
Route: `Forma2PositionCanEdit/[action]`

### GetList [POST]
- Permission: `FormaDkPositionCanEditView`
- Return: `PagedResult<Forma2PositionCanEditListDto>`

### Get [GET]
- Permission: `FormaDkPositionCanEditView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaDkPositionCanEditView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `FormaDkPositionCanEditEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `FormaDkPositionCanEditView`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`


## Forma5PositionController
Route: `Forma5Position/[action]`

### GetList [POST]
- Permission: `Forma5PositionView`
- Return: `PagedResult<Forma5PositionListDto`

### Get [GET]
- Permission: `Forma5PositionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `Forma5PositionView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `Forma5PositionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `Forma5PositionEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `Forma5PositionDelete`
- Return: `IActionResult`


## FormaDkPositionCanEditController
Route: `FormaDkPositionCanEdit/[action]`

### GetList [POST]
- Permission: `FormaDkPositionCanEditView`
- Return: `PagedResult<FormaDkPositionCanEditListDto`

### Get [GET]
- Permission: `FormaDkPositionCanEditView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaDkPositionCanEditView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaDkPositionCanEditEdit`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### CorrectionTable [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaDkPositionCanEditCreate`
- Return: `IActionResult`

### Print [POST]
- Return: `IActionResult`


## FormaDkPositionController
Route: `FormaDkPosition/[action]`

### GetList [POST]
- Permission: `FormaDkPositionView`
- Return: `PagedResult<FormaDkPositionListDto`

### Get [GET]
- Permission: `FormaDkPositionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaDkPositionView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaDkPositionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaDkPositionEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaDkPositionDelete`
- Return: `IActionResult`


## FormaSetAppController
Route: `FormaSetApp/[action]`

### GetList [POST]
- Permission: `FormaSetAppView`
- Return: `PagedResult<FormaSetAppListDto`

### Get [GET]
- Permission: `FormaSetAppView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaSetAppView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaSetAppCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaSetAppEdit`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaSetAppCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaSetAppCreate`
- Return: `IActionResult`


## FormaSetCanEditController
Route: `FormaSetCanEdit/[action]`

### GetList [POST]
- Permission: `FormaSetCanEditView`
- Return: `PagedResult<FormaSetCanEditListDto`

### Get [GET]
- Permission: `FormaSetCanEditView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaSetCanEditView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaSetCanEditCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaSetCanEditEdit`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `FormaSetCanEditCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `FormaSetCanEditCreate`
- Return: `IActionResult`


## FormaSetCommonController
Route: `FormaSetCommon/[action]`

### GetList [POST]
- Permission: `FormaSetCommonView`
- Return: `PagedResult<FormaSetCommonListDto`

### Get [GET]
- Permission: `FormaSetCommonView`
- Return: `IActionResult`

### Get [GET]
- Permission: `FormaSetCommonView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `FormaSetCommonCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `FormaSetCommonEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `FormaSetCommonDelete`
- Return: `IActionResult`


## MinistryController
Route: `Ministry/[action]`

### GetList [POST]
- Return: `PagedResult<MinistryListDto`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Return: `IActionResult`

### Update [POST]
- Return: `IActionResult`


## RjPositionController
Route: `RjPosition/[action]`

### GetList [POST]
- Permission: `RjPositionView`
- Return: `PagedResult<RjPositionListDto`

### Get [GET]
- Permission: `RjPositionView`
- Return: `IActionResult`

### Get [GET]
- Permission: `RjPositionView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `RjPositionCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `RjPositionEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `RjPositionDelete`
- Return: `IActionResult`


## SetCategoryTypeController
Route: `SetCategoryType/[action]`

### GetList [POST]
- Permission: `SetCategoryTypeView`
- Return: `PagedResult<SetCategoryTypeListDto`

### Get [GET]
- Permission: `SetCategoryTypeView`
- Return: `IActionResult`

### Get [GET]
- Permission: `SetCategoryTypeView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `SetCategoryTypeCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `SetCategoryTypeEdit`
- Return: `IActionResult`

### FillTable [POST]
- Permission: `SetCategoryTypeCreate`
- Return: `IActionResult`

### ClearTable [POST]
- Permission: `SetCategoryTypeCreate`
- Return: `IActionResult`


## IntegrationController
Route: `Integration/[action]`

### GetList [POST]
- Return: `PagedResult<BudgetProgramListOBDto>`

### Get [GET]
- Return: `IActionResult`

### GetOrganizationList [GET]
- Return: `List<OrganizationDto>`
