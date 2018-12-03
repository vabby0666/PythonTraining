    $('#sub_btn').click(function(){
            var n=$('#name').val();
            var e=$('#email').val();
            var p=$('#phone').val();
            $("#success").css("color","red");
            if(n.length<3){
                $("#success").html("Name should be more than 3 characters");
                text=$(dvCSV).html();
                $(dvCSV).css("color","red");
                $(dvCSV).html(text+ "<br> Name should be more than 3 characters where:"+n);

            }
            else if(e.indexOf('@') < 0 || e.indexOf('.') < 0 || e.lastIndexOf('.')<e.indexOf('@') || (e.lastIndexOf('.')+1)>=(e.length)) {
                $("#success").html("invalid Email Address");
                text=$(dvCSV).html();
                $(dvCSV).css("color","red");
                $(dvCSV).html(text+"<br>invalid Email Address where:"+e);
            }
            else if(p.length!=10 || isNaN(p)){
                $("#success").html("Enter a 10-digit Mobile Number");
                text=$(dvCSV).html();
                $(dvCSV).css("color","red");
                $(dvCSV).html(text+" <br> Enter a 10-digit Mobile Number where:"+p);
            }
            else{
                dataadd();
            }
    });

function dataadd(){
        var inputdata = {};
        var flag1=1;
        var myform=$('#myform')[0];
            formdata=new FormData(myform);
            var inputdata={'username':formdata.get('name'),'emailId':formdata.get('email'),'mobileNumber':formdata.get('phone')};
    $.ajax({
        url: '/employeeadd/',
        type: 'POST',
        data: inputdata,
        error: function(){
        $("#success").css("color","red");
        $("#success").html("Duplicate Email-ID. Try another valid one.");
        },
        success: function success(){
        $("#success").css("color","green");
        $("#success").html("Thanks for submission!! will contact you shortly.");
        myform.reset();
        setTimeout(function(){window.location.assign('/employee/')} , 2000);
        }
    });

}



function validate(evt) {
    var key=evt.keyCode;
    key=String.fromCharCode(key);

    if(isNaN(key)){
        evt.returnValue=false;
    }
}

     function updatenow(){
            var n=$('#uname').val();
            var e=$('#uemail').val();
            var p=$('#uphone').val();
            $(dvCSVu).css("color","red");
            if(n.length<3){
                $("#dvCSVu").html("Name should be more than 3 characters");
                text=$(dvCSV).html();
                $(dvCSV).css("color","red");
                $(dvCSV).html(text+ "<br> Name should be more than 3 characters where:"+n);

            }
            else if(p.length!=10 || isNaN(p)){
                $("#dvCSVu").html("Enter a 10-digit Mobile Number");
                text=$(dvCSV).html();
                $(dvCSV).css("color","red");
                $(dvCSV).html(text+" <br> Enter a 10-digit Mobile Number where:"+p);
            }
            else{
                dataupdate();
            }
    }

function dataupdate(){
            var n=$('#uname').val();
            var e=$('#uemail').val();
            var p=$('#uphone').val();
    var updatedata={'updusername':n,'updemailId':e,'updmobileNumber':p};

    $.ajax({
        url: '/employeeupdate/',
        type: 'POST',
        data: updatedata,
        success: function(){
        alert("Update Done Successfully!!");
        window.location.assign('/employee/');
        },
    });
}

function deleterecord(iddata){
$.ajax({
   type: 'DELETE',
   url: '/employee/'+iddata.id+'/delete/',
   success: function(){
   alert("Selected row deleted!!");
   window.location.assign("/employee/");
   }
 });
}

/*$("#delete").click(function(){
$.ajax({
   type: 'DELETE',
   url: '/employee/' + this.attr('data-id') +'/delete/'
 })
})*/


