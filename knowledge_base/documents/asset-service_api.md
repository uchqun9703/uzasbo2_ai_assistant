# asset-service — API Endpointlar


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

### GetAssetAndTmzDocumentTypeAsync [GET]
- Return: `IActionResult`

### GetCommissionRoleAsync [GET]
- Return: `IActionResult`


## InventoryController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryView`
- Return: `PagedResult<InventoryListDto>`

### GetAsync [GET]
- Permission: `InventoryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryCreate`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси яратиш

### UpdateAsync [POST]
- Permission: `InventoryEdit`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси таҳрирлаш

### DeleteAsync [POST]
- Permission: `InventoryDelete`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InventoryCancel`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини бекор қилиш

### FillTableAsync [POST]
- Permission: `InventoryView`
- Return: `IActionResult`

### ClearTableAsync [POST]
- Permission: `InventoryView`
- Return: `IActionResult`

### GetListInventoryTableAsync [POST]
- Permission: `InventoryView`
- Return: `PagedResult<InventoryTableDto>`

### PrintInventoryAsync [POST]
- Permission: `InventoryView`
- Return: `IActionResult`

### UploadFile [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`

### Register [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`

### GetFile [GET]
- Permission: `InventoryAccept`
- Return: `IActionResult`

### NotAcceptPermanentAsset [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### DeteleFile [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`

### CheckQrCode [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`

### CreatePersonalAsync [POST]
- Permission: `InventoryCreate`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси яратиш

### GetListInventoryPersonalTableAsync [POST]
- Permission: `InventoryView`
- Return: `PagedResult<InventoryPersonalTableDto>`

### DeleteTableAsync [POST]
- Permission: `InventoryCreate`
- Return: `IActionResult`

### ApproveAsync [POST]
- Permission: `InventoryApprove`
- Return: `IActionResult`

### NotApproveAsync [POST]
- Permission: `InventoryNotApprove`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `InventoryApprove`
- Return: `IActionResult`

### GetListInventoryEmployeeAsync [POST]
- Permission: `InventoryView`
- Return: `List<InventoryOrderEmployeeDto>`

### AcceptEmployeeAsync [POST]
- Permission: `InventoryAcceptEmployee`
- Return: `IActionResult`

### CancelEmployeeAsync [POST]
- Permission: `InventoryCancelEmployee`
- Return: `IActionResult`


## InventoryOrderController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `InventoryView`
- Return: `PagedResult<InventoryOrderListDto>`

### GetAsync [GET]
- Permission: `InventoryView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `InventoryView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `InventoryCreate`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси яратиш

### UpdateAsync [POST]
- Permission: `InventoryEdit`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси таҳрирлаш

### DeleteAsync [POST]
- Permission: `InventoryDelete`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `InventoryAccept`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `InventoryCancel`
- Return: `IActionResult`
- Tavsif: Асосий восита инвентаризацияси ҳужжатини бекор қилиш

### ApproveAsync [POST]
- Permission: `InventoryApprove`
- Return: `IActionResult`

### NotApproveAsync [POST]
- Permission: `InventoryNotApprove`
- Return: `IActionResult`

### GetHash [GET]
- Permission: `InventoryApprove`
- Return: `IActionResult`


## PermanentAssetAgeingController
Route: `[controller]/[action]`

### GetList [POST]
- Permission: `PermanentAssetAgeingView`
- Return: `PagedResult<PermanentAssetAgeingListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetAgeingView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetAgeingView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetAgeingCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситанинг эскиришини ҳисоблаш ҳужжатини яратиш

### GetCloneAsync [GET]
- Permission: `PermanentAssetAgeingCanClone`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `PermanentAssetAgeingAccept`
- Return: `IActionResult`
- Tavsif: Асосий воситанинг эскиришини ҳисоблаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PermanentAssetAgeingCancel`
- Return: `IActionResult`
- Tavsif: Асосий воситанинг эскиришини ҳисоблаш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PermanentAssetAgeingDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситанинг эскиришини ҳисоблаш ҳужжатини ўчириш


## PermanentAssetIntakeController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetIntakeView`
- Return: `PagedResult<PermanentAssetIntakeListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetIntakeView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetIntakeView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetIntakeCreate`
- Return: `IActionResult`
- Tavsif: Асосий восита кирими ҳужжатини яратиш

### GetCloneAsync [GET]
- Permission: `PermanentAssetIntakeCanCLone`
- Return: `IActionResult`

### UpdateAsync [POST]
- Permission: `PermanentAssetIntakeEdit`
- Return: `IActionResult`
- Tavsif: Асосий восита кирими ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PermanentAssetIntakeAccept`
- Return: `IActionResult`
- Tavsif: Асосий восита кирими ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PermanentAssetIntakeCancel`
- Return: `IActionResult`
- Tavsif: Асосий восита кирими ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PermanentAssetIntakeDelete`
- Return: `IActionResult`
- Tavsif: Асосий восита кирими ҳужжатини ўчириш

### ImportFileAsync [POST]
- Permission: `PermanentAssetIntakeCreate`
- Return: `IActionResult`
- Tavsif: Aссосий воситаларни колдиғини ехcел филедан импорт қилиш


## PermanentAssetMoveController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetMoveView`
- Return: `PagedResult<PermanentAssetMoveListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetMoveView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetMoveView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetMoveCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситани кўчириш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetMoveEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситани кўчириш ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `PermanentAssetMoveCanCLone`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PermanentAssetMoveDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситани кўчириш ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PermanentAssetMoveAccept`
- Return: `IActionResult`
- Tavsif: Асосий воситани кўчириш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PermanentAssetMoveCancel`
- Return: `IActionResult`
- Tavsif: Асосий воситани кўчириш ҳужжатини бекор қилиш

### PrintAsync [POST]
- Permission: `PermanentAssetMoveView`
- Return: `IActionResult`
- Tavsif: Бюджет ташкилотларида бухгалтерия ҳисоби тўғрисидаги йўриқномага


## PermanentAssetReappraisalController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetReappraisalView`
- Return: `PagedResult<PermanentAssetReappraisalListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetReappraisalView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetReappraisalView`
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetReappraisalCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситани қайта баҳолаш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetReappraisalEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситани қайта баҳолаш ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetReappraisalDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситани қайта баҳолаш ҳужжатини ўчириш

### AcceptAsync [POST]
- Permission: `PermanentAssetReappraisalAccept`
- Return: `IActionResult`
- Tavsif: Асосий воситани қайта баҳолаш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PermanentAssetReappraisalCancel`
- Return: `IActionResult`
- Tavsif: Асосий воситани қайта баҳолаш ҳужжатини бекор қилиш


## PermanentAssetRetirementController
Route: `PermanentAssetRetirement/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetRetirementView`
- Return: `PagedResult<PermanentAssetRetirementListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetRetirementView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetRetirementView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetRetirementCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetRetirementEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PermanentAssetRetirementCancel`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини бекор қилиш

### GetCloneAsync [GET]
- Permission: `PermanentAssetRetirementCanCLone`
- Return: `IActionResult`

### DeleteAsync [POST]
- Permission: `PermanentAssetRetirementDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `PermanentAssetRetirementView`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини печать

### PrintActAsync [POST]
- Permission: `PermanentAssetRetirementView`
- Return: `IActionResult`
- Tavsif: Асосий воситани ҳисобдан чиқариш ҳужжатини печать

### GetPermanentAssetIntakeTablesAsync [GET]
- Permission: `PermanentAssetRetirementView`
- Return: `IActionResult`

### UploadFile [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### Register [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### GetFile [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### NotAcceptPermanentAsset [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### DeteleFile [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`

### CheckQrCode [POST]
- Permission: `PermanentAssetRetirementAccept`
- Return: `IActionResult`


## ReportController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetRetirementView`
- Return: `PagedResult<AssetTmzReportGetListDto>`

### GetDocumentsCountAsync [GET]
- Return: `List<AssetAndTmzDocumentCountDto>`

### Print [POST]
- Return: `IActionResult`


## RestsByPermanentAssetController
Route: `RestByPermanentAsset/[action]`

### GetListAsync [POST]
- Permission: `RestByPermanentAssetView`
- Return: `PagedResult<RestsByPermanentAssetListDto>`

### GetTableListAsync [POST]
- Permission: `RestByPermanentAssetView`
- Return: `PagedResult<RestsByPermanentAssetTableDto>`

### GetAsync [GET]
- Permission: `RestByPermanentAssetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `RestByPermanentAssetView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `RestByPermanentAssetEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `RestByPermanentAssetAccept`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `RestByPermanentAssetCancel`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `RestByPermanentAssetDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини ўчириш

### FillTableAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### ClearTableAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### ClearImportsAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### UpdateTableAsync [POST]
- Permission: `RestByPermanentAssetEdit`
- Return: `IActionResult`

### UpdateAllTableAsync [POST]
- Permission: `RestByPermanentAssetEdit`
- Return: `IActionResult`

### DeleteTableAsync [POST]
- Permission: `RestByPermanentAssetDelete`
- Return: `IActionResult`

### SyncRestsByPermanentAssetImportsAsync [GET]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`

### PrintAsync [GET]
- Permission: `RestByPermanentAssetView`
- Return: `IActionResult`
- Tavsif: Асосий воситалар бўйича қолдиқ ҳужжатини печать қилиш

### AssetImportFileAsync [POST]
- Permission: `RestByPermanentAssetCreate`
- Return: `IActionResult`
- Tavsif: Aссосий воситаларни колдиғини ехcел филедан импорт қилиш

### DownloadTemplateAsync [GET]
- Permission: `PermanentAssetView`
- Return: `IActionResult`


## PermanentAssetController
Route: `PermanentAsset/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetView`
- Return: `PagedResult<PermanentAssetListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `PermanentAssetView`
- Return: `IActionResult`

### GetAsSelectListAsync [POST]
- Return: `PagedResult<PermanentAssetListDto>`

### CreateAsync [POST]
- Permission: `PermanentAssetCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситалар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситалар ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситалар ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `PermanentAssetView`
- Return: `IActionResult`
- Tavsif: Асосий воситалар ҳужжатини чоп этиш


## PermanentAssetAgeingRateController
Route: `PermanentAssetAgeingRate/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetAgeingRateView`
- Return: `PagedResult<PermanentAssetAgeingRateListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetAgeingRateView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetAgeingRateView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetAgeingRateCreate`
- Return: `IActionResult`
- Tavsif: Асосий Воситаларнинг Эскириш Фоизи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetAgeingRateEdit`
- Return: `IActionResult`
- Tavsif: Асосий Воситаларнинг Эскириш Фоизи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetAgeingRateDelete`
- Return: `IActionResult`
- Tavsif: Асосий Воситаларнинг Эскириш Фоизи ҳужжатини ўчириш


## PermanentAssetGroupController
Route: `PermanentAssetGroup/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetGroupView`
- Return: `PagedResult<PermanentAssetGroupListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetGroupView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetGroupView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetGroupCreate`
- Return: `IActionResult`
- Tavsif: Асосий восита гуруҳи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetGroupEdit`
- Return: `IActionResult`
- Tavsif: Асосий восита гуруҳи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetGroupDelete`
- Return: `IActionResult`
- Tavsif: Асосий восита гуруҳи ҳужжатини ўчириш


## PermanentAssetReappraisalIndexController
Route: `PermanentAssetReappraisalIndex/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetReappraisalIndexView`
- Return: `PagedResult<PermanentAssetReappraisalIndexListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetReappraisalIndexView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetReappraisalIndexView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetReappraisalIndexCreate`
- Return: `IActionResult`
- Tavsif: Aсосий воситаларни қайта баҳолаш коеффициентлари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetReappraisalIndexEdit`
- Return: `IActionResult`
- Tavsif: Aсосий воситаларни қайта баҳолаш коеффициентлари ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetReappraisalIndexDelete`
- Return: `IActionResult`
- Tavsif: Aсосий воситаларни қайта баҳолаш коеффициентлари ҳужжатини ўчириш


## PermanentAssetSubGroupController
Route: `PermanentAssetSubGroup/[action]`

### GetListAsync [POST]
- Permission: `PermanentAssetSubGroupView`
- Return: `PagedResult<PermanentAssetSubGroupListDto>`

### GetAsync [GET]
- Permission: `PermanentAssetSubGroupView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PermanentAssetSubGroupView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PermanentAssetSubGroupCreate`
- Return: `IActionResult`
- Tavsif: Асосий воситалар қуйи гуруҳи ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PermanentAssetSubGroupEdit`
- Return: `IActionResult`
- Tavsif: Асосий воситалар қуйи гуруҳи ҳужжатини таҳрирлаш

### DeleteAsync [POST]
- Permission: `PermanentAssetSubGroupDelete`
- Return: `IActionResult`
- Tavsif: Асосий воситалар қуйи гуруҳи ҳужжатини ўчириш
