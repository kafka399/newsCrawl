var a='11, according to the Arabic Sisters Forum for Human Rights in Sana’a. ,To contact the reporter on this story: Donna Abu-Nasr in Dubai at  ,, ,To contact the editor responsible for this story: Andrew J. Barden at  ,barden@bloomberg.net,' 
print( a);
//a=a.replace("\n"," ")
print(a.substring(0,String(a).indexOf("9To contact the reporter on this story")));
a=String(a).replace(/r$/, ".");
print(a);
