
console.log("HELLO");

var stripe=function stripe(s){
		$(s).each(function(i,item){
				if (i%2==0){
						$(item).addClass('red');
				}else{
						$(item).addClass('green');
				}
		});
		
};
