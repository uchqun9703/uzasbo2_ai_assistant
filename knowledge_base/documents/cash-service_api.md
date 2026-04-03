# cash-service — API Endpointlar


## DepositedMoneyController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `DepositedMoneyView`
- Return: `PagedResult<DepositedMoneyListDto>`

### GetAsync [GET]
- Permission: `DepositedMoneyView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `DepositedMoneyView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `DepositedMoneyCreate`
- Return: `IActionResult`
- Tavsif: Депозидга кўйилган маблағлар ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `DepositedMoneyEdit`
- Return: `IActionResult`
- Tavsif: Депозидга кўйилган маблағлар ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `DepositedMoneyCanCLone`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `DepositedMoneyAccept`
- Return: `IActionResult`
- Tavsif: Депозидга кўйилган маблағлар ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `DepositedMoneyCancel`
- Return: `IActionResult`
- Tavsif: Депозидга кўйилган маблағлар ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `DepositedMoneyDelete`
- Return: `IActionResult`
- Tavsif: Депозидга кўйилган маблағлар ҳужжатини ўчириш


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## IncomeCashOrderController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `IncomeCashOrderView`
- Return: `PagedResult<IncomeCashOrderListDto>`

### GetAsync [GET]
- Permission: `IncomeCashOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `IncomeCashOrderView`
- Return: `IActionResult`

### GetCloneAsync [GET]
- Permission: `IncomeCashOrderCreate`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `IncomeCashOrderCreate`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `IncomeCashOrderEdit`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини таҳрирлаш

### AcceptAsync [POST]
- Permission: `IncomeCashOrderAccept`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `IncomeCashOrderCancel`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `IncomeCashOrderDelete`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `IncomeCashOrderPrint`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатини печать қилиш

### PrintGetListAsync [POST]
- Permission: `IncomeCashOrderPrint`
- Return: `IActionResult`
- Tavsif: Қабул қилиш ҳужжатларини печат қилиш


## OutcomeCashOrderController
Route: `[controller]/[action]`

### GetListAsync [POST]
- Permission: `OutcomeCashOrderView`
- Return: `PagedResult<OutcomeCashOrderListDto>`

### GetAsync [GET]
- Permission: `OutcomeCashOrderView`
- Return: `IActionResult`

### GetAsync [GET]
- Permission: `OutcomeCashOrderView`
- Return: `IActionResult`

### GetAsSelectListAsync [GET]
- Return: `IActionResult`

### CreateAsync [POST]
- Permission: `OutcomeCashOrderCreate`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини яратиш

### UpdateAsync [POST]
- Permission: `OutcomeCashOrderEdit`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини таҳрирлаш

### GetCloneAsync [GET]
- Permission: `OutcomeCashOrderCanCLone`
- Return: `IActionResult`

### AcceptAsync [POST]
- Permission: `OutcomeCashOrderAccept`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини тасдиқлаш

### CancelAsync [POST]
- Permission: `OutcomeCashOrderCancel`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини бекор қилиш

### DeleteAsync [POST]
- Permission: `OutcomeCashOrderDelete`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини ўчириш

### PrintAsync [POST]
- Permission: `OutcomeCashOrderPrint`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини печать қилиш

### PrintGetListAsync [POST]
- Permission: `OutcomeCashOrderPrint`
- Return: `IActionResult`
- Tavsif: Нақд пул бериш тўғрисидаги буюртма ҳужжатини печать қилиш


## ReportController
Route: `[controller]/[action]`

### GetCashBookAsync [POST]
- Permission: `CashBook`
- Return: `IActionResult`

### PrintGetCashBookAsync [POST]
- Permission: `CashBook`
- Return: `IActionResult`

### GetRegisterCashOrderAsync [POST]
- Permission: `RegisterCashOrder`
- Return: `IActionResult`

### PrintRegisterCashOrderAsync [POST]
- Permission: `CashBook`
- Return: `IActionResult`
