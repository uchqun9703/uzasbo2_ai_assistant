# idm-service — API Endpointlar


## AccountController
Route: `Account/[action]`

### GetSessionKeys [GET]
- Return: `IActionResult`

### GetTimestamp [GET]
- Return: `IActionResult`

### TimestampPkcs7 [GET]
- Return: `IActionResult`

### GetChallenge [GET]
- Return: `IActionResult`

### ESignInRequest [POST]
- Return: `IActionResult`

### ESignIn [POST]
- Return: `IActionResult`

### ESignInBySelected [POST]
- Return: `IActionResult`

### SignIn [POST]
- Return: `IActionResult`

### SignInTwoFactor [POST]
- Return: `IActionResult`

### SignOut [GET]
- Return: `new IActionResult`

### ValidateUserSessionAsync [POST]
- Return: `IActionResult`

### RefreshToken [POST]
- Return: `IActionResult`

### ReSendVerificationCode [POST]
- Return: `IActionResult`

### GetUserTrustedDevices [GET]
- Return: `IActionResult`

### DeleteTrustedDevice [DELETE]
- Return: `IActionResult`

### GetUserActiveSessions [GET]
- Return: `IActionResult`

### ResetPassword [POST]
- Return: `IActionResult`

### ConfirmResetPassword [POST]
- Return: `IActionResult`

### ChangePassword [POST]
- Return: `IActionResult`

### SetOrganization [POST]
- Return: `IActionResult`

### SingInWithCameral [POST]
- Return: `IActionResult`

### RefreshCaptcha [GET]
- Return: `IActionResult`


## HealthController
Route: `[controller]`

### Get [GET]
- Return: `IActionResult`


## OrganizationController
Route: `Organization/[action]`

### Get [GET]
- Return: `IActionResult`

### Get [GET]
- Return: `IActionResult`

### GetAsSelectList [POST]
- Return: `IActionResult`

### Create [POST]
- Return: `IActionResult`

### Update [POST]
- Return: `IActionResult`

### Delete [POST]
- Return: `IActionResult`

### ChangeState [POST]
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


## UserController
Route: `User/[action]`

### GetList [POST]
- Permission: `UserView`
- Return: `PagedResult<UserListDto`

### Get [GET]
- Permission: `UserView`
- Return: `IActionResult`

### Get [GET]
- Permission: `UserView`
- Return: `IActionResult`

### GetAsSelectList [POST]
- Permission: `UserView`
- Return: `IActionResult`

### Create [POST]
- Permission: `UserCreate`
- Return: `IActionResult`

### Update [POST]
- Permission: `UserEdit`
- Return: `IActionResult`

### Delete [POST]
- Permission: `UserDelete`
- Return: `IActionResult`

### CheckUserName [POST]
- Return: `IActionResult`

### ChangeState [POST]
- Permission: `UserEdit`
- Return: `IActionResult`

### ChangeLanguage [POST]
- Permission: `UserEdit`
- Return: `IActionResult`


## UserLogController
Route: `UserLog/[action]`

### GetList [POST]
- Return: `IActionResult`


## UserOrganizationController
Route: `UserOrganization/[action]`

### GetUserOrganizations [GET]
- Return: `IActionResult`

### SetUserOrganizations [POST]
- Return: `IActionResult`

### Create [POST]
- Return: `IActionResult`
