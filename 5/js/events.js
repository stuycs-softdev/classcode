
var thluffy = document.querySelector("#thluffy");

/*
	window.addEventListener('mousemove',function(e){
	//console.log(e.pageX+", "+e.pageY);
	if (e.pageX > 200){
	thluffy.src = "thluffy-left.png";
	} else {
	thluffy.src = "thluffy-right.png";

	}
	});
*/

var doStuff = function doStuff() {
		console.log("Stuff has been done");
};

var myInterval =  setInterval(doStuff,2000);
var b = document.querySelector("#stop");
b.addEventListener('click',function(e){
		clearInterval(myInterval);
});
