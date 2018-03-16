$(document).ready(function () {
    // $("#headNotify").show();
    $("#envName").empty();

    $.getJSON(userApi + "/users/get_enviroment_key", function (result) {
        $("#envName").text(result.envi);
    });
    if(bAdmin)
    {
         $("#adminManager").show();
    }

});

function dealMenu(o) {
    $(".sidebar-menu li").removeClass("active");
    $(".sidebar-menu treeview-menu li").removeClass("active");
    if (o.id === "messageProduce" || o.id === "messageConsume" || o.id === "queryMessageByMsgKey"
        || o.id === "queryMessageByID" || o.id === "queryMessageByTopic") {
        $("#" + o.id).parent().parent().addClass("active");
    }
    $("#" + o.id).addClass("active");
    $("#mqFrame").attr("src", o.id);

}

