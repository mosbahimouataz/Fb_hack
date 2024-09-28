Dim objFSO, objFile, strDesktopPath, strFileName

' الحصول على مسار سطح المكتب
Set objShell = CreateObject("WScript.Shell")
strDesktopPath = objShell.SpecialFolders("Desktop")

' اسم الملف الجديد
strFileName = "mouuuuataaz.txt"

' إنشاء كائن FileSystemObject
Set objFSO = CreateObject("Scripting.FileSystemObject")

' إنشاء الملف الجديد على سطح المكتب
Set objFile = objFSO.CreateTextFile(strDesktopPath & "\" & strFileName, True)

' كتابة نص في الملف (اختياري)
objFile.WriteLine("هذا ملف جديد باسم mouuuuataaz")

' إغلاق الملف
objFile.Close

' تنظيف الكائنات
Set objFile = Nothing
Set objFSO = Nothing
Set objShell = Nothing
