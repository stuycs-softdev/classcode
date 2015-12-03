
var thluffy = document.querySelector("#thluffy");


window.addEventListener('mousemove',function(e){
		if (e.pageX > 525){
				thluffy.src = "thluffy-left.png";
		} else {
				thluffy.src = "thluffy-right.png";
		}
});

var count=1;
var addItem = function addItem(){
		var l = document.getElementById("thelist");
		var n = document.createElement("li");
		n.innerHTML="Item: "+count;
		count=count+1;
		l.appendChild(n);
};

var doStuff = function doStuff(){
		addItem();
		//		setTimeout(doStuff,5000);
};

//var myInterval = setInterval(doStuff,3000);
var start = document.getElementById("start");
var stop = document.getElementById("stop");

var myInterval;
start.addEventListener("click",function(e){
		myInterval = setInterval(doStuff,3000);
});
stop.addEventListener("click",function(e){
		clearInterval(myInterval);
});
