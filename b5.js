var ds=["red", "green", "blue"]
ds.push("yellow"); 
ds.unshift("purple");  
console.log( 'thêm màu',ds);

ds.shift(); 
ds.pop(); 
console.log("Sau khi xóa màu:", ds);


ds.sort();
console.log("Sau khi sắp xếp:", ds);


ds.reverse();
console.log("Sau khi đảo ngược:", ds);
