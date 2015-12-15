function getData(){

var json_query_obj = {
    type: 'data',
    alg:$("#algorithm_type option:selected").val(),
    x:$("#x_attr option:selected").val(),
    y:$("#y_attr option:selected").val(),
    pictype: '1'
};

$.ajax({
    url: 'http://127.0.0.1:8000/get',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(json_query_obj),
    dataType: 'json',
    success: function(result) {
        console.log("start");
        
        drawScatter(result.data, json_query_obj, null);
    },
    error: function(result){
        console.log(result);
    }
});

}



$( document ).ready(function() {
    console.log( "ready!" );
    dropDownList();
    $("#submit_button").click(submit_pic);
    $("#algorithm_type").change(getAxisAttr);
    
});

