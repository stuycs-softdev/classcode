
var x = 20;
var l = [1,2,3,4,5];

var d = {'one':1,
				 2:"hello"};

console.log("javascript loaded");
console.log(x);

function f(p) {
		var x = 30;
		console.log("in function f: "+p+x);
}

var fact = function fact(n){
		var prod = 1;
		for ( ; n > 1 ; n--){
				prod = prod * n;
		}
		return prod;
}

var additem = function additem(s){
		var l = document.getElementById("thelist");
		var n = document.createElement("li");
		n.innerHTML=s;
		l.appendChild(n);
};

var removeitem = function(n){
		var items = document.getElementsByTagName("li");
		items[n].remove();

};


var color = function(){
		var items = document.getElementsByTagName("li");
		for (var i = 0; i < items.length; i++){
				items[i].classList.add("red");
		}
};

var stripe = function(){
		var items = document.getElementsByTagName("li");
		for (var i = 0; i < items.length; i++){
				if (i%2==0)
						items[i].classList.add("red");
				else
						items[i].classList.add("green");
		}
};;





