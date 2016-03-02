window.onload = function(){
	//Load initial quote and listen for click to change
	loadquote();
	var quote = setInterval(loadquote, 300000);
	document.getElementById("button").addEventListener("click", loadquote);
};

//load quote
function loadquote(){
	var xmlhttp = new XMLHttpRequest();
	var url = "http://54.68.253.162/StudentWork/api-3.0.json";
	//var url = "http://www.twitter.com/somerandomapi.json";

	//state change check.
	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
		var obj = JSON.parse(xmlhttp.responseText);
		document.getElementById("quotes").innerHTML =
		'"' + obj.quote + '"' +  "<br><br>" + obj.author + "<br>"
	    };
	};
	//xmlhttp open and fetched
	xmlhttp.open("GET", url, true);
	xmlhttp.send();
	console.log("fetched!");
};
