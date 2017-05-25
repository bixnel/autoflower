t_array=[];
l_array=[];
w_array=[];


$(document).ready(function(){
    PopUpHide();
});
function PopUpShow(){
    
    $("#popup").css('opacity', 1);
    $("#popup").css('z-index', 9999999);
    //~ $("#popup").show();
}
function PopUpHide(){
    $("#popup").css('opacity', 0);
    $("#popup").css('z-index', -9);
    //~ $("#popup").hide();
}


            
function getInfo() {
    $.ajax({
        type: 'GET',
        url: 'info',
        cache: false,
        success: function(html) {
                var t = $('#temperature');
                //~ var l = $('#light');
                var w = $('#water');
                var nw = $('#need_water');
                var mydata = JSON.parse(html);
                
                if (t_array.length >= 6) {
                    t_array.shift();
                }
                //~ if (l_array.length >= 6) {
                    //~ l_array.shift();
                //~ }
                if (w_array.length >= 6) {
                    w_array.shift();
                }

                t_array.push([mydata.date, mydata.temperature]);
                //~ l_array.push([mydata.date, mydata.light]);
                w_array.push([mydata.date, mydata.water]);
                
                $(t).html(mydata.temperature);
                //~ $(l).html(mydata.light);
                $(w).html(mydata.water);
                $(nw).html(mydata.need_water);
                
                drawBasic1(t_array);
                //~ drawBasic2(l_array);
                drawBasic3(w_array);
                
                document.img.src="cam.jpg?" + new Date().getTime();
            }
    });
}
            
getInfo();


setInterval(getInfo, 5000);
