function getData(){
/*
    var data=[
  {
    "Cereal Name": "100%_Bran",
    "Manufacturer": "Nabisco",
    "Calories": 70,
    "Protein (g)": 4,
    "info1":"hi morning",
    "info2":"bye"
  }
];

for(var i = 0; i < 80; i ++){
    var tmp = {"Cereal Name":"test"+i,
                "Manufacturer":"Nabisco",
                "Calories":Math.floor(Math.random() * 100) + 1 ,
                "Protein (g)":Math.floor(Math.random() * 100) + 1 ,
                "info1":"hi",
                "info2":"bye"
            };
    data.push(tmp);
}
*/

var json_query_obj = {
    type: 'data',
    alg:'sailfish',
    x:'TPM',
    y:'NumReads',
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
        
        drawScatter(result, json_query_obj, null);
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

$( document ).ready(function() {
    console.log( "ready!" );
    dropDownList();
    $("#submit_button").click(submit_pic);
    $("#algorithm_type").change(getAxisAttr);
    
});

