function dropDownList(){

	var json_query_obj = {
        type: 'algorithm',
		pictype: '1'
	};


$.ajax({
    url: 'http://127.0.0.1:8000/get',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(json_query_obj),
    dataType: 'json',
    success: function(result) {
     /*   console.log(result);
        console.log("The length is:"+result.data.length);
        for(i = 0; i < result.data.length; i ++){
            console.log("This is the " + i + "th, and item is:"+result.data[i].alg);
            console.log("Attr length is:"+ result.data[i].attrs.length);
            for(j = 0; j < result.data[i].attrs.length; j ++){
                console.log("attr " + j + "th: " + result.data[i].attrs[j]);
            }
        }
*/
    	$.each(result, function( nameScope, algoType){
      		$.each(algoType, function(i, algoAttr){
      			$('#algorithm_type').append('<option value="' + algoAttr.alg + '">' + algoAttr.alg + '</option>'); 
      			
      			/*$.each(algoAttr.attrs, function(j, algoAttrItem){
      				console.log("The j is:"+j + " the algoAttrItem is: " + algoAttrItem);
      			});*/
      		});
    	}); 
    },
    error: function(result){
        console.log(result);
    }
});

}

function getAxisAttr(){
	 console.log("Change algorithm");
    var selectAlgo = $( "#algorithm_type option:selected" ).text(); 
    $("#x_attr").empty();
    $("#y_attr").empty();
    $('#x_attr').append('<option value="0">Please choose x attribute</option>'); 
    $('#y_attr').append('<option value="0">Please choose y attribute</option>'); 



    var json_query_obj = {
        type: 'algorithm',
		pictype: '1'
    };
    $.ajax({
    url: 'http://127.0.0.1:8000/get',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(json_query_obj),
    dataType: 'json',
    success: function(result) {
        $.each(result.data, function(i, algoAttr){
            if(algoAttr.alg == selectAlgo){
                $.each(algoAttr.attrs, function(j, algoAttrItem){
                    $('#x_attr').append('<option value="' + algoAttrItem + '">' + algoAttrItem + '</option>'); 
                    $('#y_attr').append('<option value="' + algoAttrItem + '">' + algoAttrItem + '</option>'); 
                });
                
            }       
        });
    },
    error: function(result){
        console.log(result);
    }
});
}

function checkPicInfo(){
    var algo = $( "#algorithm_type option:selected" ).val(); 
    var x_attr = $("#x_attr option:selected").val();
    var y_attr = $("#y_attr option:selected").val();

    if(algo == "0" || x_attr == "0" || y_attr == "0"){
        alert("Selected items should within some value");
        return false;
    }

    if(x_attr == y_attr){
        alert("x axis should be diferent from y axis");
        return false;
    }

    return true;
}

function submit_pic(){
    if(checkPicInfo()){
        getData();
    }
}



