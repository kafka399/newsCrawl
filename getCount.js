var i=3;
function mycount(fil) {
//var t = db.twentyseven.find( { date : fil } );
//  return db.eval( function(){
//print( fil);
//return db.twentyseven.find({guid:/bloomberg.com/,date:{$regex:fil}}).count();
return db.twentyseven.find({date:fil},{}).count();
//} );

}
//printjson(mycount(/2011/));
for(var i=1;i<32;i++){
var a;
//a="{$gt:new Date(2012,0,".concat(i).concat("),$lt:new Date(2012,0,").concat(i+1).concat(")}")
a={$gt:new Date(2012,0,i),$lt:new Date(2012,0,i+1)}

//	if(i<10)
//		a = "{$gt:2012-00-0".concat(i).concat("$lt:2012:00:0").concat(i+1);
//	else
//		a = "2012-01-".concat(i)
			print(new Date(2012,0,i));
	printjson(mycount(a));

}

