console.log("HELLO");

/*
	$.get("static/datafile",function(d){
	console.log(d);
	});
*/



var demo1 = function demo1(){
		console.log("Calling getstuff");
		$.get("/getfast",function(d){
				console.log("We got: "+d);
		});
		console.log("back from getstuff");
		
};

var printresult = function printresult(d){
		console.log(d);
};

var demo2 = function demo2(){

		console.log("Calling getslow");
		$.get("/getslow",function(){
				console.log("Back from slow");
				console.log("Calling getfast");
				$.get("/getfast",printresult);
				console.log("BACK FROM GETFAST\n");
		});
		console.log("BACK FROM GETSLOW\n");

		console.log("Calling getstuff");
		$.get("/getstuff",printresult);
		console.log("BACK FROM GETSTUFF\n");
};

var testparam = function testparam(){
		$.getJSON("/upcase",{data:'hello'},function(d){
				console.log(d);
				console.log(d.result);
		});
		
};


$("#b").click(function(){
		var input = $("#data");
		var data = input.val();
		input.val("");
		$.getJSON("/upcase",{data:data},function(r){
				$("#result").text(r.result);
				$("#thelist").append("<li>"+r.result+"</li>");
		});
});
