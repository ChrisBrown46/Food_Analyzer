$(document).ready(function () {
    let $nutrition = $('#nutrition');
    let nutrition_height = $nutrition.height();
    let nutrition_width = $nutrition.width();
    $('.box__input').width(nutrition_width)
        .height(nutrition_height)
        .css({
            'background-color': 'black',
            'border': '2px dashed dimgrey'
        });
});
