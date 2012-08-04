//use textmine;
var cursor = db.twentyseven.find();
while (cursor.hasNext()) {
    var x = cursor.next();
    /* replace \\n with \n in x's strings ... */
//x.content=String(x.content).replace(/\\u([0-9A-Za-z]{4})/g, ' ')
//x.date = new Date(ISODate(x.date)); 
//x.content = x.content.toString().replace(/\x27, u\x27/g, "").replace(/u\x27/g, "")
//x.content = x.content.toString().replace(/ u\x22/g, "")
//	x.content=String(x.content).replace(/\n/g,' ');
	x.content=String(x.content).replace(/&amp;/g," "); 
//	ln=x.content.toString().indexOf("To contact Bloom");
//	if(ln>0)
//		x.content=x.content.toString().substring(0,ln);
	db.twentyseven.update({_id : x._id}, x);
}
