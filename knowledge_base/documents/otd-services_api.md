# otd-services — API Endpointlar


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## CalculatingTaxisController
Route: `CalculatingTaxis/[action]`

### GetListAsync [POST]
- Permission: `CalculatingTaxisView`
- Return: `PagedResult<CalculatingTaxisListDto>`

### GetAsync [GET]
- Permission: `CalculatingTaxisView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `CalculatingTaxisView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `CalculatingTaxisView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `CalculatingTaxisCreate`
- Return: `IActionResult`
- Tavsif: Солиқлар ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `CalculatingTaxisEdit`
- Return: `IActionResult`
- Tavsif: Солиқлар ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `CalculatingTaxisAccept`
- Return: `IActionResult`
- Tavsif: Солиқлар ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `CalculatingTaxisCancel`
- Return: `IActionResult`
- Tavsif: Солиқлар ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `CalculatingTaxisDelete`
- Return: `IActionResult`
- Tavsif: Солиқлар ҳисоби ҳужжатини ўчириш


## ClosingTransactionController
Route: `ClosingTransaction/[action]`

### GetListAsync [POST]
- Permission: `ClosingTransactionView`
- Return: `PagedResult<ClosingTransactionListDto>`

### GetAsync [GET]
- Permission: `ClosingTransactionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `ClosingTransactionView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `ClosingTransactionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `ClosingTransactionCreate`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `ClosingTransactionEdit`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `ClosingTransactionAccept`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `ClosingTransactionCancel`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `ClosingTransactionDelete`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини ўчириш

### GetRestBySubAccountPlanAsync [POST]
- Permission: `ClosingTransactionCreate`
- Return: `IActionResult`


## FixingTransactionController
Route: `FixingTransaction/[action]`

### GetListAsync [POST]
- Permission: `FixingTransactionView`
- Return: `PagedResult<FixingTransactionListDto>`

### GetAsync [GET]
- Permission: `FixingTransactionView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `FixingTransactionView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `FixingTransactionView`
- Return: `IActionResult`

### GetCloneListAsync [GET]
- Permission: `FixingTransactionView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `FixingTransactionCreate`
- Return: `IActionResult`
- Tavsif: Тузатиш проводкалари ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `FixingTransactionEdit`
- Return: `IActionResult`
- Tavsif: Тузатиш проводкалари ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `FixingTransactionAccept`
- Return: `IActionResult`
- Tavsif: Тузатиш проводкалари ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `FixingTransactionCancel`
- Return: `IActionResult`
- Tavsif: Тузатиш проводкалари ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `FixingTransactionDelete`
- Return: `IActionResult`
- Tavsif: Тузатиш проводкалари ҳужжатини ўчириш

### PrintGetListAsync [POST]
- Return: `IActionResult`


## PayrollLeaseController
Route: `PayrollLease/[action]`

### GetListAsync [POST]
- Permission: `PayrollLeaseView`
- Return: `PagedResult<PayrollLeaseListDto>`

### GetAsync [GET]
- Permission: `PayrollLeaseView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollLeaseView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `PayrollLeaseView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PayrollLeaseCreate`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollLeaseEdit`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PayrollLeaseAccept`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollLeaseCancel`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PayrollLeaseDelete`
- Return: `IActionResult`
- Tavsif: Пуллик хизматлар ҳисоби ҳужжатини ўчириш


## PayrollParentPaymentController
Route: `PayrollParentPayment/[action]`

### GetListAsync [POST]
- Permission: `PayrollParentPaymentView`
- Return: `PagedResult<PayrollParentPaymentListDto>`

### GetAsync [GET]
- Permission: `PayrollParentPaymentView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `PayrollParentPaymentView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `CalculatingTaxisView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `PayrollParentPaymentCreate`
- Return: `IActionResult`
- Tavsif: Ота-оналар тўлови ҳисоби ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `PayrollParentPaymentEdit`
- Return: `IActionResult`
- Tavsif: Ота-оналар тўлови ҳисоби ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `PayrollParentPaymentAccept`
- Return: `IActionResult`
- Tavsif: Ота-оналар тўлови ҳисоби ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `PayrollParentPaymentCancel`
- Return: `IActionResult`
- Tavsif: Ота-оналар тўлови ҳисоби ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `PayrollParentPaymentDelete`
- Return: `IActionResult`
