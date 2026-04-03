# tmz-service — API Endpointlar


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

### GetInventoryHoldingIncomeTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetInventoryHoldingQuitTypeSelectListAsync [GET]
- Return: `IActionResult`

### GetInventoryHoldingTypeSelectListAsync [POST]
- Return: `IActionResult`

### GetAssetOrTmzSelectListAsync [GET]
- Return: `IActionResult`

### GetTmzDocumentTypeSelectListAsync [GET]
- Return: `IActionResult`


## DrugIntakeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `DrugIntakeView`
- Return: `PagedResult<DrugIntakeListDto>`

### GetAsync [GET]
- Permission: `DrugIntakeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DrugIntakeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DrugIntakeCreate`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кирим қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DrugIntakeEdit`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кирим қилиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `DrugIntakeAccept`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кирим қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `DrugIntakeCancel`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кирим қилиш ҳужжатини бекор қилиш

### GetCloneAsync [GET]
- Permission: `DrugIntakeCreate`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `DrugIntakeDelete`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кирим қилиш ҳужжатини ўчириш


## DrugMoveController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `DrugMoveView`
- Return: `PagedResult<DrugMoveListDto>`

### GetAsync [GET]
- Permission: `DrugMoveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DrugMoveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DrugMoveCreate`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DrugMoveEdit`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `DrugMoveAccept`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `DrugMoveCancel`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `DrugMoveDelete`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `DrugMovePrint`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини печать қилиш


## DrugRetirementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `DrugRetirementView`
- Return: `PagedResult<DrugRetirementListDto>`

### GetAsync [GET]
- Permission: `DrugRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DrugRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DrugRetirementCreate`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DrugRetirementEdit`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `DrugRetirementAccept`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `DrugRetirementCancel`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `DrugRetirementDelete`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `DrugRetirementPrint`
- Return: `IActionResult`
- Tavsif: Дори воситаларини рўйхатдан чиқариш ҳужжатини печать қилиш

### GetDrugIntakeTablesAsync [GET]
- Permission: `DrugIntakeCreate`
- Return: `IActionResult`


## FoodStuffIntakeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `FoodStuffIntakeView`
- Return: `PagedResult<FoodStuffIntakeListDto>`

### GetAsync [GET]
- Permission: `FoodStuffIntakeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FoodStuffIntakeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FoodStuffIntakeCreate`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FoodStuffIntakeEdit`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `FoodStuffIntakeCreate`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `FoodStuffIntakeAccept`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `FoodStuffIntakeCancel`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `FoodStuffIntakeDelete`
- Return: `IActionResult`
- Tavsif: Дори воситаларини кўчириш ҳужжатини ўчириш


## FoodStuffMoveController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `FoodStuffMoveView`
- Return: `PagedResult<FoodStuffMoveListDto>`

### GetAsync [GET]
- Permission: `FoodStuffMoveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FoodStuffMoveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FoodStuffMoveCreate`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FoodStuffMoveEdit`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `FoodStuffMoveAccept`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `FoodStuffMoveCancel`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `FoodStuffMoveDelete`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `FoodStuffMovePrint`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини кўчириш ҳужжатини печать қилиш


## FoodStuffRetirementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `FoodStuffRetirementView`
- Return: `PagedResult<FoodStuffRetirementListDto>`

### GetAsync [GET]
- Permission: `FoodStuffRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FoodStuffRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FoodStuffRetirementCreate`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FoodStuffRetirementEdit`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `FoodStuffRetirementAccept`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `FoodStuffRetirementCancel`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `FoodStuffRetirementDelete`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `FoodStuffRetirementPrint`
- Return: `IActionResult`
- Tavsif: Озиқ-овқат маҳсулотларини чиқариш ҳужжатини печать қилиш

### GetFoodStuffIntakeTablesAsync [GET]
- Permission: `FoodStuffIntakeView`
- Return: `IActionResult`


## GsmIntakeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `GSMIntakeView`
- Return: `PagedResult<GsmIntakeListDto>`

### GetAsync [GET]
- Permission: `GSMIntakeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `GSMIntakeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `GSMIntakeCreate`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `GSMIntakeEdit`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни қилиш ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `GSMIntakeCreate`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `GSMIntakeAccept`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `GSMIntakeCancel`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни қилиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `GSMIntakeDelete`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни қилиш ҳужжатини ўчириш


## GsmMoveController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `GSMMoveView`
- Return: `PagedResult<GsmMoveListDto>`

### GetAsync [GET]
- Permission: `GSMMoveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `GSMMoveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `GSMMoveCreate`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `GSMMoveEdit`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `GSMMoveAccept`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `GSMMoveCancel`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `GSMMoveDelete`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `GSMMovePrint`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш кўчириш ҳужжатини печать қилиш


## GsmRetirementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `GSMRetirementView`
- Return: `PagedResult<GsmRetirementListDto>`

### GetAsync [GET]
- Permission: `GSMRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `GSMRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `GSMRetirementCreate`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `GSMRetirementEdit`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `GSMRetirementAccept`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `GSMRetirementCancel`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `GSMRetirementDelete`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни кўчириш қилиш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `GSMRetirementPrint`
- Return: `IActionResult`
- Tavsif: Ёқилғи мойлаш воситаларни рўйхатдан чиқариш ҳужжатини печать қилиш

### GetGsmIntakeTables [GET]
- Permission: `InventoryHoldingRetirementView`
- Return: `IActionResult`


## IhobRetirementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IhobRetirementView`
- Return: `PagedResult<IhobRetirementListDto>`

### GetAsync [GET]
- Permission: `IhobRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IhobRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IhobRetirementCreate`
- Return: `IActionResult`
- Tavsif: БТ счётдаги ТМЗ чиқими ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `IhobRetirementEdit`
- Return: `IActionResult`
- Tavsif: БТ счётдаги ТМЗ чиқими ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `IhobRetirementAccept`
- Return: `IActionResult`
- Tavsif: БТ счётдаги ТМЗ чиқими ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `IhobRetirementCancel`
- Return: `IActionResult`
- Tavsif: БТ счётдаги ТМЗ чиқими ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `IhobRetirementDelete`
- Return: `IActionResult`
- Tavsif: БТ счётдаги ТМЗ чиқими ҳужжатини ўчириш


## InventoryHoldingIntakeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryHoldingIntakeView`
- Return: `PagedResult<InventoryHoldingIntakeListDto>`

### GetAsync [GET]
- Permission: `InventoryHoldingIntakeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryHoldingIntakeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryHoldingIntakeCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `InventoryHoldingIntakeEdit`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `InventoryHoldingIntakeCanCLone`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `InventoryHoldingIntakeAccept`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InventoryHoldingIntakeCancel`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `InventoryHoldingIntakeDelete`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `InventoryHoldingIntakeView`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар кирим қилиш ҳужжатини печать қилиш


## InventoryHoldingMoveController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryHoldingMoveView`
- Return: `PagedResult<InventoryHoldingMoveListDto>`

### GetAsync [GET]
- Permission: `InventoryHoldingMoveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryHoldingMoveView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryHoldingMoveCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `InventoryHoldingMoveEdit`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `InventoryHoldingMoveAccept`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InventoryHoldingMoveCancel`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `InventoryHoldingMoveDelete`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `InventoryHoldingMovePrint`
- Return: `IActionResult`
- Tavsif: Товар моддий захираларни кўчириш ҳужжатини печать қилиш


## InventoryHoldingRetirementController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryHoldingRetirementView`
- Return: `PagedResult<InventoryHoldingRetirementListDto>`

### GetAsync [GET]
- Permission: `InventoryHoldingRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryHoldingRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryHoldingRetirementCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `InventoryHoldingRetirementEdit`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `InventoryHoldingRetirementAccept`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InventoryHoldingRetirementCancel`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `InventoryHoldingRetirementDelete`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `InventoryHoldingRetirementPrint`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар рўйхатдан чиқариш ҳужжатини печать қилиш

### GetInventoryHoldingIntakeTablesAsync [GET]
- Permission: `InventoryHoldingRetirementView`
- Return: `IActionResult`


## PermanentAssetQrController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetQrView`
- Return: `PagedResult<PermanentAssetQrListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetQrView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetQrView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetQrCreate`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PermanentAssetQrEdit`
- Return: `IActionResult`

### PrintQRCodesAsync [GET]
- Permission: `PermanentAssetQrView`
- Return: `IActionResult`

### CheckQRCode [POST]
- Permission: `PermanentAssetQrView`
- Return: `bool`

### AcceptAsync [POST]
- Permission: `PermanentAssetQrAccept`
- Return: `IActionResult`

### Cancel [POST]
- Permission: `PermanentAssetQrCancel`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PermanentAssetQrDelete`
- Return: `IActionResult`


## RestByInventoryHoldingController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `RestByInventoryHoldingView`
- Return: `PagedResult<RestByInventoryHoldingListDto>`

### GetAsync [GET]
- Permission: `RestByInventoryHoldingView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestByInventoryHoldingView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestByInventoryHoldingCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestByInventoryHoldingEdit`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `RestByInventoryHoldingAccept`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestByInventoryHoldingCancel`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `RestByInventoryHoldingDelete`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини ўчириш

### FillTableAsync [POST]
- Permission: `RestByInventoryHoldingCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини тўлдириш

### ClearTableAsync [POST]
- Permission: `RestByInventoryHoldingCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғи ҳужжатини тозалаш

### SyncRestByInventoryHoldingImportsAsync [GET]
- Permission: `RestByInventoryHoldingCreate`
- Return: `IActionResult`

### Print [GET]
- Permission: `RestByInventoryHoldingView`
- Return: `IActionResult`
- Tavsif: ТМЗ бўйича қолдиқ ҳужжатини печать қилиш

### InventoryHoldingImportFile [POST]
- Permission: `RestByInventoryHoldingCreate`
- Return: `IActionResult`
- Tavsif: Товар моддий захиралар колдиғини ехcел филедан импорт қилиш

### DownloadTemplate [GET]
- Permission: `InventoryHoldingIntakeView`
- Return: `IActionResult`


## WarrantController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `WarrantView`
- Return: `PagedResult<WarrantListDto>`

### GetAsync [GET]
- Permission: `WarrantView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `WarrantView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `WarrantCreate`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `WarrantAccept`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `WarrantCancel`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини бекор қилиш

### UpdateAsync [POST]
- Permission: `WarrantEdit`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `WarrantDelete`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини бекор қилиш

### SendAsync [POST]
- Permission: `WarrantSend`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини юбориш

### ReadyToSendAsync [POST]
- Permission: `WarrantReadyToSign`
- Return: `IActionResult`
- Tavsif: Ishonchnoma hujjatini jo'natishga tayorlash

### GetHash [GET]
- Permission: `WarrantView`
- Return: `IActionResult`

### ReadyToSendAsync [POST]
- Permission: `WarrantReadyToSign`
- Return: `IActionResult`
- Tavsif: Аризани ҳужжатини имзолаш

### ApprovedAsync [POST]
- Permission: `WarrantApproved`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини тасдиқлаш

### NotApprovedAsync [POST]
- Permission: `WarrantApproved`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини тасдиқлашни бекор қилиш

### ReceivedAsync [POST]
- Permission: `WarrantApproved`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини тасдиқлаш

### NotReceivedAsync [POST]
- Permission: `WarrantApproved`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини тасдиқлашни бекор қилиш

### Print1Async [GET]
- Permission: `WarrantView`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини чоп қилиш

### Print2Async [GET]
- Permission: `WarrantView`
- Return: `IActionResult`
- Tavsif: Моддий қийматлик ва ТМЗлар ишончнома ҳужжатини чоп қилиш


## InventoryHoldingController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryHoldingView`
- Return: `PagedResult<InventoryHoldingListDto>`

### GetAsync [GET]
- Permission: `InventoryHoldingView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryHoldingView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryHoldingCreate`
- Return: `IActionResult`
- Tavsif: Товар-моддий захиралар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `InventoryHoldingEdit`
- Return: `IActionResult`
- Tavsif: Товар-моддий захиралар ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `InventoryHoldingDelete`
- Return: `IActionResult`
- Tavsif: Товар-моддий захиралар ҳужжатини ўчириш


## IntegartionController
Route: `[controller]/[action]`

### CreateFoodStuffRetirement [POST]
- Return: `IActionResult`
