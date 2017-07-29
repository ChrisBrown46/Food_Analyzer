$(document).ready(function () {
    let $nutrition = $('#nutrition');
    let nutrition_height = $nutrition.height();
    let nutrition_width = $nutrition.width();
    $('.box__input')
        .width(nutrition_width)
        .height(nutrition_height)
        .css({
            'background-color': 'black',
            'border': '2px dashed dimgrey',
            'text-align': 'center'
        });

    $('.resize_fit_center')
        .css({
            'margin-left': 'auto',
            'margin-top': ((nutrition_height - 200) / 2) + 'px',
            'padding': '0'
        });
});
