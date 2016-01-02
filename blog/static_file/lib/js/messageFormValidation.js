
$(function(){

    $('#contactForm').validate({

        rules:{
            Email:{
                required:true,
                email:true
            },
            Subject:{
                required:true
            },
            Content:{
                required:true
            }
        },
        messages:{

            Email:{
                required:'<span style="color:darkred">Bu alan gereklidir.</span><br>',
                email:'<span style="color:darkred">Girilen adres geçerli değil.</span><br>'
            },
            Subject:{
                required:'<span style="color:darkred">Bu alan gereklidir.</span><br>'
            },
            Content:{
                required:'<span style="color:darkred">Bu alan gereklidir.</span>'
            }
        }

    });

});