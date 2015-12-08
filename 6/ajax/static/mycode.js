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
		$.get("/getslow",printresult);
		console.log("BACK FROM GETSLOW\n");

		console.log("Calling getstuff");
		$.get("/getstuff",printresult);
		console.log("BACK FROM GETSTUFF\n");

		console.log("Calling getfast");
		$.get("/getfast",printresult);
		console.log("BACK FROM GETFAST\n");



		
};
