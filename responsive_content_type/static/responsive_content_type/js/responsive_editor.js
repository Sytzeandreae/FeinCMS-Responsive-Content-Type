'use strict';

$(function() {
    $('.panel').addClass('row');
    // Adjust the contenttypes that are set already
    setCols('small');
    setCols('medium');
    setCols('large');

    // Add change listeners for the contenttypes
    $('.panel').on('change', '.small select', function() {
        setCols('small');
    });
    $('.panel').on('change', '.medium select', function() {
        setCols('medium');
    });
    $('.panel').on('change', '.large select', function() {
        setCols('large');
    });
});

function setCols(type) {
    $('.' + type + ' select').each(function() {
        var select = this;
        var cols = $(this).val();
        if (cols > 0) {
            var checkExist = setInterval(function() {
                var fieldset = $(select).parents('fieldset').parents('fieldset');
                if (fieldset.length > 0) {
                    var classes = fieldset.attr("class").split(" ").filter(
                        function(item) {
                            return item.lastIndexOf(type + "-", 0) !== 0;
                        }
                    );
                    fieldset.attr("class", classes.join(" "));
                    fieldset.addClass(type + '-' + cols);
                    fieldset.addClass('columns');
                    clearInterval(checkExist);
                }
            }, 100);
        }
    });
}
