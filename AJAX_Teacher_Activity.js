$(document).ready(function () {
    let new_date=new Date()
    only_date=new_date.toLocaleDateString()
    $("#date").text(only_date)

    $("#submit").click(function () {
    let input_data = {
        "text": $("#txt_input").val()
    }
    $.ajax({
        type: 'POST',
        url: "/predict-emotion",
        data: JSON.stringify(input_data),
        dataType: "json",
        contentType: 'application/json',
        success: function (result) {
            predicted_emotion = result.data.predicted_emotion
            $("#prediction").html(result.data.predicted_emotion)
                $('#prediction').css("display", "");
            }
