
$userName = 'richberedo@gmail.com'
$password = ConvertTo-SecureString -String "pvpt gegc eitb ulsm" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential $userName,$password
Send-MailMessage -UseSsl -To "richberedo@gmail.com" -From "richberedo@gmail.com" -Subject (Get-Date) -Body "Go Cowboys" -Credential $creds -SmtpServer smtp.gmail.com -Port 587 -Attachments .\grocery.txt