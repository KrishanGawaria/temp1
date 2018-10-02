 var loc;
function loadPages(){
 	
         loc = prompt("Enter URL");
        document.getElementById('preview-frame').setAttribute('src', loc);
		//alert(loc);
		var html1 =  frames["google"].document.body.innerHTML;
		alert(html1);
		return loc;
		
}	
	
	

	
function addRow() {
	
	   document.getElementById('mydata').style.display = "block";
	   
	   //if(!document.getElementById("yes_browser").checked || document.getElementById("no_browser").value === "" ) {alert("You haven't audited Browser Title");}
        
          if(document.getElementById("yes_browser").checked) {
			  var cell2 = "YES";
		  }
		  else {
			 var cell2 = document.getElementById("no_browser").value;
		  }
		  if(document.getElementById("yes_keywords").checked) {
			  var cell3 = "YES";
		  }
		  else {
			 var cell3 = document.getElementById("no_keywords").value;
		  }
		  if(document.getElementById("yes_desc").checked) {
			  var cell4 = "YES";
		  }
		  else {
			 var cell4 = document.getElementById("no_desc").value;
		  }
		  if(document.getElementById("yes_bread").checked) {
			  var cell5 = "YES";
		  }
		  else {
			 var cell5 = document.getElementById("no_bread").value;
		  }
		  if(document.getElementById("yes_page_title").checked) {
			  var cell6 = "YES";
		  }
		  else {
			 var cell6 = document.getElementById("no_pagetitle").value;
		  }
		  if(document.getElementById("yes_s7").checked) {
			  var cell7 = "YES";
		  }
		  else {
			 var cell7 = document.getElementById("no_s7").value;
		  }
		  if(document.getElementById("yes_hot").checked) {
			  var cell8 = "YES";
		  }
		  else {
			 var cell8 = document.getElementById("no_hot").value;
		  }
		  if(document.getElementById("yes_green").checked) {
			  var cell9 = "YES";
		  }
		  else {
			 var cell9 = document.getElementById("no_green").value;
		  }
		  if(document.getElementById("yes_tabname").checked) {
			  var cell10 = "YES";
		  }
		  else {
			 var cell10 = document.getElementById("no_tabname").value;
		  }
		  if(document.getElementById("yes_tabcontent").checked) {
			  var cell11 = "YES";
		  }
		  else {
			 var cell11 = document.getElementById("no_tabcontent").value;
		  }
		  if(document.getElementById("yes_technote").checked) {
			  var cell12 = "YES";
		  }
		  else {
			 var cell12 = document.getElementById("no_technote").value;
		  }
		  if(document.getElementById("yes_alttags").checked) {
			  var cell13 = "YES";
		  }
		  else {
			 var cell13 = document.getElementById("no_alttags").value;
		  }
		  
		  if(document.getElementById("yes_reg").checked) {
			  var cell14 = "YES";
		  }
		  else {
			 var cell14 = document.getElementById("no_reg").value;
		  }
		  if(document.getElementById("yes_right").checked) {
			  var cell15 = "YES";
		  }
		  else {
			 var cell15 = document.getElementById("no_right").value;
		  }
		  if(document.getElementById("yes_franch").checked) {
			  var cell16 = "YES";
		  }
		  else {
			 var cell16 = document.getElementById("no_franch").value;
		  }
		  if(document.getElementById("yes_franchkey").checked) {
			  var cell17 = "YES";
		  }
		  else {
			 var cell17 = document.getElementById("no_franchkey").value;
		  }
		  if(document.getElementById("yes_comppage").checked) {
			  var cell18 = "YES";
		  }
		  else {
			 var cell18 = document.getElementById("no_comppage").value;
		  }
		  
    //var myName = document.getElementById("name");

    var table = document.getElementById("myTableData");
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
 
    row.insertCell(0).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteRow(this)">';
    row.insertCell(1).innerHTML= document.getElementById("preview-frame").src;
	row.insertCell(2).innerHTML= cell2;
    row.insertCell(3).innerHTML= cell3;
	row.insertCell(4).innerHTML= cell4;
	row.insertCell(5).innerHTML= cell5;
	row.insertCell(6).innerHTML= cell6;
	row.insertCell(7).innerHTML= cell7;
	row.insertCell(8).innerHTML= cell8;
	row.insertCell(9).innerHTML= cell9;
	row.insertCell(10).innerHTML= cell10;
	row.insertCell(11).innerHTML= cell11;
	row.insertCell(12).innerHTML= cell12;
	row.insertCell(13).innerHTML= cell13;
	row.insertCell(14).innerHTML= cell14;
	row.insertCell(15).innerHTML= cell15;
	row.insertCell(16).innerHTML= cell16;
	row.insertCell(17).innerHTML= cell17;
	row.insertCell(18).innerHTML= cell18;
	
	
	return loc;
}
 
function deleteRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);
    
}
 
function addTable() {
      
    var myTableDiv = document.getElementById("myDynamicTable");
      
    var table = document.createElement('TABLE');
    table.border='1';
    
    var tableBody = document.createElement('TBODY');
    table.appendChild(tableBody);
      
    for (var i=0; i<3; i++){
       var tr = document.createElement('TR');
       tableBody.appendChild(tr);
       
       for (var j=0; j<4; j++){
           var td = document.createElement('TD');
           td.width='75';
           td.appendChild(document.createTextNode("Cell " + i + "," + j));
           tr.appendChild(td);
       }
    }
    myTableDiv.appendChild(table);
    
}
 
function load() {
    
    console.log("Page load finished");
 
}

var tableToExcel = (function() {
  var uri = 'data:application/vnd.ms-excel;base64,'
    , template = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"/></head><body><table>{table}</table></body></html>'
    , base64 = function(s) { return window.btoa(unescape(encodeURIComponent(s))) }
    , format = function(s, c) { return s.replace(/{(\w+)}/g, function(m, p) { return c[p]; }) }
  return function(table, name) {
    if (!table.nodeType) table = document.getElementById(table)
    var ctx = {worksheet: name || 'Worksheet', table: table.innerHTML}
    window.location.href = uri + base64(format(template, ctx))
  }
})()


function locale() {
   var loc1 = document.getElementById("preview-frame").src
   loc1 = loc1.split("?")[0];
   //alert(loc1);
if ( document.getElementById("menu").value == 'en' ) {
	//Compares if the selected value in the dropdown is English
	var loc = loc1 + '?c=us&l=en&s=bsd';
	//appends EN light e
} else if ( document.getElementById("menu").value == 'ar') {
  loc = loc1 + '?c=ae&l=ar&s=bsd';
  document.getElementById('preview-frame').setAttribute('src', loc);
 
} else if ( document.getElementById("menu").value == 'da') {
  loc = loc1 + '?c=da&l=da&s=bsd';
  document.getElementById('preview-frame').setAttribute('src', loc);
  
} else if ( document.getElementById("menu").value == 'cs') {
  loc = loc1 + '?c=cz&l=cs&s=pad';
 document.getElementById('preview-frame').setAttribute('src', loc);
 
} else if ( document.getElementById("menu").value == 'de') {
  loc = loc1 + '?c=de&l=de&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);

} else if ( document.getElementById("menu").value == 'es') {
  loc = loc1 + '?c=es&l=es&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);
 
}  else if ( document.getElementById("menu").value == 'es') {
  loc = loc1 + '?c=es&l=es&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);
 
}  else if ( document.getElementById("menu").value == 'es-xl') {
  loc = loc1 + '?c=mx&l=es&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);
 
} else if ( document.getElementById("menu").value == 'fr') {
  loc = loc1 + '?c=fr&l=fr&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);
 
} else if ( document.getElementById("menu").value == 'fr-ca') {
  loc = loc1 + '?c=ca&l=fr&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 

} else if ( document.getElementById("menu").value == 'fi') {
  loc = loc1 + '?c=fi&l=fi&s=pad';
document.getElementById('preview-frame').setAttribute('src', loc); 

} else if ( document.getElementById("menu").value == 'gr-el') {
  loc = loc1 + '?c=gr&l=el&s=pad';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'he') {
  loc = loc1 + '?c=il&l=he&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 

 
} else if ( document.getElementById("menu").value == 'hu') {
  loc = loc1 + '?c=hu&l=hu&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'hu') {
  loc = loc1 + '?c=hu&l=hu&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'ja') {
  loc = loc1 + '?c=jp&l=ja&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'ko') {
  loc = loc1 + '?c=kr&l=ko&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'nl') {
  loc = loc1 + '?c=nl&l=nl&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'no') {
  loc = loc1 + '?c=no&l=no&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
}  else if ( document.getElementById("menu").value == 'pl') {
  loc = loc1 + '?c=pl&l=pl&s=pad';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
}  else if ( document.getElementById("menu").value == 'pt') {
  loc = loc1 + '?c=pt&l=pt&s=pad';
  
document.getElementById('preview-frame').setAttribute('src', loc);  

} else if ( document.getElementById("menu").value == 'pt-br') {
  loc = loc1 + '?c=br&l=pt&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'ro') {
  loc = loc1 + '?c=ro&l=ro&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'ru') {
  loc = loc1 + '?c=ru&l=ru&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'sk') {
  loc = loc1 + '?c=sk&l=sk&s=pad';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'sv') {
  loc = loc1 + '?c=sv&l=sv&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'tr') {
  loc = loc1 + '?c=tr&l=tr&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc); 
 
} else if ( document.getElementById("menu").value == 'cn-zh') {
  loc = loc1 + '?c=cn&l=zh&s=bsd';
document.getElementById('preview-frame').setAttribute('src', loc);  

} else if ( document.getElementById("menu").value == 'zh-tw') {
  loc = loc1 + '?c=tw&l=zh&s=bsd';
  document.getElementById('preview-frame').setAttribute('src', loc); 
}

}
 
 
 