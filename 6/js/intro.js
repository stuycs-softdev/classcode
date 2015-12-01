
console.log("loaded js");

var x = 20;

var l=[10,20,30,'hello',30.3];

var d = {
		1 : 'the first item',
		'key' :'value',
		3 : [1,2,3]
};

function f(n){
		var x=30;
		console.log("In function f: "+x+n);
}

console.log(x);

var fact = function fact(n){
		var prod=1;
		for (;n>1;n--){
				prod = prod * n;
		}
		return prod;
};

var addItem = function addItem(s){
		var l = document.getElementById("thelist");
		var n = document.createElement("li");
		n.innerHTML=s;
		l.appendChild(n);
};

var removeItem = function removeItem(n) {
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

