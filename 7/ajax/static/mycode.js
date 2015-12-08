console.log("HELLO");


var demo1 = function demo1(){
		console.log("Calling getstuff");
		$.get("/getslow",function(d){
				console.log("We got: "+d);});
		console.log("back from getstuff\n");
};

var printresult = function printresult(d){
		console.log("We got: "+d);
};

var demo2 = function demo2() {

		console.log("Calling getslow");
		$.get("/getslow",printresult);
		console.log("Back from getslow\n\n");

		
		console.log("Calling Getstuff");
		$.get("/getstuff",printresult);
		console.log("Back from getstuff\n\n");

		console.log("Calling getfast");
		$.get("/getfast",printresult);
		console.log("Back from getfast\n\n");


};
