if (window.innerHeight > window.innerWidth) {
	document.body.onload = function () {
		document.getElementById('img').remove();
		document.getElementsByTagName('form')[0].style.left="2%";
		document.getElementsByTagName('form')[0].style.width="95%";
	}
}
