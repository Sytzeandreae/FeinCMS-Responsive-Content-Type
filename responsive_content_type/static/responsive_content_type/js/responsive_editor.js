'use strict';

$(function() {
    setCols();
    $('.panel').addClass('row');
    $('.panel').on('change', '.cols select', function() {
        setCols();
    });
    $('.panel').on('change', '.type select', function() {
        setCols();
    });
});

function setCols() {
    $('.cols').each(function(){
        var column = this;
        var cols = $(this).find('select').val();
        var type = $(this).parent().find('.type').find('select').val();
        if (cols > 0) {
            var checkExist = setInterval(function() {
                var fieldset = $(column).parents('fieldset').parents('fieldset');
                if (fieldset.length > 0) {
                    var classes = fieldset.attr("class").split(" ").filter(function(item) {
                        return item.lastIndexOf("medium-", 0) !== 0
                            && item.lastIndexOf("small-", 0) !== 0
                            && item.lastIndexOf("large-", 0) !== 0
                            && item.lastIndexOf("columns", 0) !== 0;
                    });
                    fieldset.attr("class", classes.join(" "));
                    fieldset.addClass(type+'-'+cols);
                    fieldset.addClass('columns');
                    clearInterval(checkExist);
                }
            }, 100);
        }
    });
}