# Unregister-Event FileCreated
Unregister-Event FileChanged

# Email-settings
$loginuser = 'anvar.big@gmail.com'
$loginpassword = 'P13M27k16a22lvrspctfrvr;'
$smtpserver = 'smtp.gmail.com'
$smtpport = 587
$sendfrom = 'anvar.big@gmail.com'
$sendto = 'add.task.9270372.1523940684.00e376f6308756b9@todoist.net'

# Folder-settings
$folder = 'D:\Google Drive\Other\Obsidian\Nirvana\' # Enter the root path you want to monitor.
$filter = '*.*'  # You can enter a wildcard filter here.
# In the following line, you can change 'IncludeSubdirectories to $true if required.
$fsw = New-Object IO.FileSystemWatcher $folder, $filter -Property @{IncludeSubdirectories = $false; NotifyFilter = [IO.NotifyFilters]'FileName, LastWrite' }

# Trigger-settings
$trigger = '#task'
$lookfor = '#td'
$replaceto = '#intasklist'

Register-ObjectEvent $fsw Changed -SourceIdentifier FileChanged -Action {
    $name = $Event.SourceEventArgs.Name
    $changeType = $Event.SourceEventArgs.ChangeType
    $timeStamp = $Event.TimeGenerated
    $fileContent = (Get-Content $folder$name)
#    Write-Host "The file '$name' was $changeType at $timeStamp" -fore green
   if ($fileContent -match $trigger) {
    $fileContent | Select-String -Pattern ".*$($lookfor)" -AllMatches | ForEach-Object { $_.Matches } | ForEach-Object { $secpasswd = ConvertTo-SecureString $loginpassword -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential ($loginuser, $secpasswd); Send-MailMessage -To $sendto -From $sendfrom  -Subject $_.Value -Body $name -SmtpServer $smtpserver -Port $smtpport -Credential $cred -UseSsl
    $fileContent | ForEach-Object { $_ -replace $lookfor, $replaceto -replace " $($trigger)", '' -replace $trigger, '' } | Set-Content $folder$name }
    }}

# To stop the monitoring, run the following commands:
# Unregister-Event FileChanged
