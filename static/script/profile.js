function frm_s() {
	 if (document.getElementsByTagName('input')[0].value  == "") {
	 	alert("Select your file(s)");
	 } else {
	 	document.getElementsByTagName("form")[0].submit();
	 }
}