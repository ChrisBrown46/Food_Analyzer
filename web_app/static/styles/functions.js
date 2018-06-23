$(document).ready(function () {
    let $nutrition = $("#nutrition");
    let nutrition_height = $nutrition.height();
    let nutrition_width = $nutrition.width();
    $(".box__input")
        .width(nutrition_width)
        .height(nutrition_height)
        .css({
            "background-color": "black",
            "border": "2px dashed dimgrey",
            "text-align": "center"
        });

    $(".resize_fit_center")
        .css({
            "margin-left": "auto",
            "margin-top": ((nutrition_height - 200) / 2) + "px",
            "padding": "0"
        });
});

function stop_event(event) {
    event.stopPropagation();
    event.preventDefault();
}

function upload_file(event) {
    stop_event(event);

    console.log("... file[0].name = " + event.dataTransfer.files[0].name);

    document.getElementById("file-input").files = event.dataTransfer.files;
    document.getElementsByTagName("form")[0].submit();
}

function file_drag_enter(event) {
    document.getElementById('file-label').classList.remove('w3-opacity');
    stop_event(event);
}

function file_drag_leave(event) {
    document.getElementById('file-label').classList.add('w3-opacity');
    stop_event(event);
}
