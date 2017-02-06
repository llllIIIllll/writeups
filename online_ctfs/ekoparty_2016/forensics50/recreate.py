'''
Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub CALCULATE()
	Dim iterator, NOT_ANSWER

	NOT_ANSWER = "NOTNOTNOTNOTNOTNOTNOTNOTNOTNOTNOTNOT"
	
	For iterator = 1 To 16777216
		answer = hash_function(answer)
	Next iterator
	
	Hoja1.NOT_ANSWER.Text = "EKO{" + Replace(answer, "=", "") + "}"

End Sub

Public Function hash_function(ByVal sTextToHash As String)
	Dim hashee As Object, sha1_hasher As Object
	Dim TextToHash() As Byte
	Set hashee = CreateObject("System.Text.UTF8Encoding")
	Set sha1_hasher = CreateObject("System.Security.Cryptography.SHA1CryptoServiceProvider")
	TextToHash = hashee.Getbytes_4(sTextToHash)
	Dim bytes() As Byte
	bytes = sha1_hasher.ComputeHash_2((TextToHash))
	hash_function = bytes_to_string(bytes)
	Set hashee = Nothing
	Set sha1_hasher = Nothing
End Function

Private Function bytes_to_string(ByRef arrData() As Byte) As String
	Dim excel_document
	Dim base64_object
	Set excel_document = CreateObject("MSXML2.DOMDocument")
	Set base64_object = excel_document.createElement("b64")
	base64_object.DataType = "bin.base64"
	base64_object.nodeTypedValue = arrData
	bytes_to_string = base64_object.Text
	Set base64_object = Nothing
	Set excel_document = Nothing
End Function
'''
