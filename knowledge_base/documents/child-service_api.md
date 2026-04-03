# child-service — API Endpointlar


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

### GetChildGroupTypeSelectList [GET]
- Return: `IActionResult`

### GetChildHoursTypeSelectList [GET]
- Return: `IActionResult`

### GetChildOrganizationTypeSelectList [GET]
- Return: `IActionResult`

### GetChildTimesheetTypeSelectList [GET]
- Return: `IActionResult`

### GetMissedDaysTypeSelectList [GET]
- Return: `IActionResult`

### GetWorkScheduleKindSelectList [GET]
- Return: `IActionResult`


## NewManualController
Route: `New/Manual/[action]`

### GetChildGroupTypeSelectList [GET]
- Return: `IActionResult`

### GetChildHoursTypeSelectList [GET]
- Return: `IActionResult`

### GetChildOrganizationTypeSelectList [GET]
- Return: `IActionResult`

### GetChildTimesheetTypeSelectList [GET]
- Return: `IActionResult`

### GetMissedDaysTypeSelectList [GET]
- Return: `IActionResult`

### GetWorkScheduleKindSelectList [GET]
- Return: `IActionResult`


## ChildComeController
Route: `ChildCome/[action]`

### GetList [POST]
- Permission: `ChildComeView`
- Return: `PagedResult<ChildComeListDto>`

### PrintTable [POST]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildComeView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildComeView`
- Return: `IActionResult`

### AsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildComeCreate`
- Return: `IActionResult`
- Tavsif: Болалар қабул ҳужжатини яратиш

### Update [POST]
- Permission: `ChildComeEdit`
- Return: `IActionResult`
- Tavsif: Болалар қабул ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ChildComeAccept`
- Return: `IActionResult`
- Tavsif: Болалар қабул ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ChildComeCancel`
- Return: `IActionResult`
- Tavsif: Болалар қабул ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ChildComeDelete`
- Return: `IActionResult`
- Tavsif: Болалар қабул ҳужжатини ўчириш


## ChildLeaveController
Route: `ChildLeave/[action]`

### GetList [POST]
- Permission: `ChildLeaveView`
- Return: `PagedResult<ChildLeaveListDto>`

### Get [GET]
- Permission: `ChildLeaveView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildLeaveView`
- Return: `IActionResult`

### AsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildLeaveCreate`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини яратиш

### Update [POST]
- Permission: `ChildLeaveEdit`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ChildLeaveAccept`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ChildLeaveCancel`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ChildLeaveDelete`
- Return: `IActionResult`
- Tavsif: Болани муассасадан чиқариш ҳужжатини ўчириш


## ChildMissedDayController
Route: `ChildMissedDay/[action]`

### GetList [POST]
- Permission: `ChildMissedDayView`
- Return: `PagedResult<ChildMissedDayListDto>`

### Get [GET]
- Permission: `ChildMissedDayView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildMissedDayView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildLeaveCreate`
- Return: `IActionResult`
- Tavsif: Муассасада бўлмаган кунлар маълумотномаси ҳужжатини яратиш

### Update [POST]
- Permission: `ChildMissedDayEdit`
- Return: `IActionResult`
- Tavsif: Муассасада бўлмаган кунлар маълумотномаси ҳужжатини таҳрирлаш

### ChangeDate [POST]
- Permission: `ChildMissedDayChangeDate`
- Return: `IActionResult`

### Accept [POST]
- Permission: `ChildMissedDayAccept`
- Return: `IActionResult`
- Tavsif: Муассасада бўлмаган кунлар маълумотномаси ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ChildMissedDayCancel`
- Return: `IActionResult`
- Tavsif: Муассасада бўлмаган кунлар маълумотномаси ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ChildMissedDayDelete`
- Return: `IActionResult`
- Tavsif: Муассасада бўлмаган кунлар маълумотномаси ҳужжатини ўчириш

### GetMissedDays [POST]
- Return: `IActionResult`


## ChildMovementController
Route: `ChildMovement/[action]`

### GetList [POST]
- Permission: `ChildMovementView`
- Return: `PagedResult<ChildMovementListDto>`

### Get [GET]
- Permission: `ChildMovementView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildMovementView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildMovementCreate`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини яратиш

### Update [POST]
- Permission: `ChildMovementEdit`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ChildMovementAccept`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ChildMovementCancel`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ChildMovementDelete`
- Return: `IActionResult`
- Tavsif: Болаларнинг гуруҳлараро кўчиши ҳужжатини ўчириш


## ChildTimesheetController
Route: `ChildTimesheet/[action]`

### GetList [POST]
- Permission: `ChildTimesheetView`
- Return: `PagedResult<ChildTimesheetListDto>`

### Get [GET]
- Permission: `ChildTimesheetView`
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildTimesheetView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Update [POST]
- Permission: `ChildTimesheetEdit`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини таҳрирлаш

### Accept [POST]
- Permission: `ChildTimesheetAccept`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини тасдиқлаш

### Cancel [POST]
- Permission: `ChildTimesheetCancel`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини бекор қилиш

### Delete [POST]
- Permission: `ChildTimesheetDelete`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини ўчириш

### Print [GET]
- Permission: `ChildTimesheetView`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини печать қилиш

### FillTable [POST]
- Permission: `ChildTimesheetCreate`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини толдириш

### ClearTable [POST]
- Permission: `ChildTimesheetCreate`
- Return: `IActionResult`
- Tavsif: Болалар давомати табели ҳужжатини тозалаш


## ChildController
Route: `Child/[action]`

### GetList [POST]
- Permission: `ChildView`
- Return: `PagedResult<ChildListDto>`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildCreate`
- Return: `IActionResult`
- Tavsif: Бола ҳужжатини яратиш

### Update [POST]
- Permission: `ChildEdit`
- Return: `IActionResult`
- Tavsif: Бола ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `ChildDelete`
- Return: `IActionResult`
- Tavsif: Бола ҳужжатини ўчириш

### Print [GET]
- Permission: `ChildView`
- Return: `IActionResult`
- Tavsif: Бола ҳужжатини печать қилиш

### PrintGetList [POST]
- Permission: `ChildView`
- Return: `IActionResult`

### SyncWithOldChildern [POST]
- Permission: `ChildCreate`
- Return: `IActionResult`

### GetListWithHistory [POST]
- Permission: `ChildView`
- Return: `ChildListWithHistoryDto`


## ChildPersonController
Route: `ChildPerson/[action]`

### GetList [POST]
- Permission: `ChildPersonView`
- Return: `PagedResult<ChildPersonListDto>`

### Get [GET]
- Return: `IActionResult`

### GetBySeriaNumber [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildPersonView`
- Return: `IActionResult`

### GetByDocInfo [GET]
- Permission: `ChildPersonCreate`
- Return: `IActionResult`

### GetFromGsp [GET]
- Permission: `PersonCreate`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildPersonCreate`
- Return: `IActionResult`
- Tavsif: Болалар (Шахсий маълумотлари) ҳужжатини яратиш

### Update [POST]
- Permission: `ChildPersonEdit`
- Return: `IActionResult`
- Tavsif: Болалар (Шахсий маълумотлари) ҳужжатини таҳрирлаш

### UpdateForAdmin [POST]
- Permission: `ChildPersonEdit`
- Return: `IActionResult`
- Tavsif: Болалар (Шахсий маълумотлари) ҳужжатини таҳрирлаш adminlar uchun (админлар учун).

### Delete [POST]
- Permission: `ChildPersonDelete`
- Return: `IActionResult`
- Tavsif: Болалар (Шахсий маълумотлари) ҳужжатини ўчириш

### GetChildInfo [GET]
- Return: `IActionResult`


## TrainingGroupController
Route: `TrainingGroup/[action]`

### GetList [POST]
- Permission: `TrainingGroupView`
- Return: `PagedResult<TrainingGroupListDto>`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `TrainingGroupView`
- Return: `IActionResult`

### GetAsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `TrainingGroupCreate`
- Return: `IActionResult`
- Tavsif: Тренинг гуруҳи ҳужжатини яратиш

### Update [POST]
- Permission: `TrainingGroupEdit`
- Return: `IActionResult`
- Tavsif: Тренинг гуруҳи ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `TrainingGroupDelete`
- Return: `IActionResult`
- Tavsif: Тренинг гуруҳи ҳужжатини ўчириш


## ChildPaymentDiscountController
Route: `ChildPaymentDiscount/[action]`

### GetList [POST]
- Permission: `ChildPaymentDiscountView`
- Return: `PagedResult<ChildPaymentDiscountListDto>`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildPaymentDiscountView`
- Return: `IActionResult`

### AsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildPaymentDiscountCreate`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини яратиш

### Update [POST]
- Permission: `ChildPaymentDiscountEdit`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `ChildPaymentDiscountDelete`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини ўчириш


## ChildPriceController
Route: `ChildPrice/[action]`

### GetList [POST]
- Permission: `ChildPriceView`
- Return: `PagedResult<ChildPriceListDto>`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildPriceView`
- Return: `IActionResult`

### AsSelectList [GET]
- Return: `IActionResult`

### Create [POST]
- Permission: `ChildPriceCreate`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини яратиш

### Update [POST]
- Permission: `ChildPriceEdit`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини таҳрирлаш

### Delete [POST]
- Permission: `ChildPriceDelete`
- Return: `IActionResult`
- Tavsif: Болалар тўлови ҳужжатини ўчириш


## ChildManageController
Route: `ChildManage/[action]`

### GetList [POST]
- Permission: `ChildManageView`
- Return: `PagedResult<ChildManageListDto>`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Permission: `ChildManageView`
- Return: `IActionResult`

### GetFirstOrDefault [GET]
- Permission: `ChildManageView`
- Return: `IActionResult`

### PrintGetList [POST]
- Permission: `ChildManageView`
- Return: `IActionResult`
