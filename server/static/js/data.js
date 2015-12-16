/*
    Get data from Ajax and draw chart.
*/
function getData(pictype){
    // Query sentence
    var json_query_obj;

    if(pictype == 1){
        json_query_obj  = {
            type: 'data',
            alg: $("#algorithm_type option:selected").val(),
            x:$("#x_attr option:selected").val(),
            y:$("#y_attr option:selected").val(),
            pictype: pictype
        };
    }else if(pictype == 2){
        json_query_obj  = {
            type: 'data',
            alg1: $("#algorithm_type_1 option:selected").val(),
            alg2: $("#algorithm_type_2 option:selected").val(),
            x:$("#x_attr option:selected").val(),
            y:$("#y_attr option:selected").val(),
            pictype: pictype
        };
    }else if(pictype == 3){
        json_query_obj = {
            type: 'data1',
            alg1: $("#algorithm_type_1 option:selected").val(),
            alg2: $("#algorithm_type_2 option:selected").val(),
            attr1: $("#algo_attr option:selected").val(),
            attr2:$("#algo_attr option:selected").val(),
            pictype: pictype
        };
    }

    $.ajax({
        url: 'http://127.0.0.1:8000/get',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(json_query_obj),
        dataType: 'json',
        success: function (result) {
            console.log("Start draw charts");
            if (pictype == 1 || pictype == 2) {
                drawScatter(result.data, json_query_obj, null, pictype);
            } else if (pictype == 3) {
                drawScatter(result.data, json_query_obj, result.regression, pictype);
            }
        },
        error: function (result) {
            console.log(result);
        }
    });
}





