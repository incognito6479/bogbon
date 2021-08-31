$(window).on('load', function () {
    if (window.location.pathname.indexOf('/en/') !== -1) {
        let path, new_path;
        path = window.location.pathname;
        new_path = path.replace('/en/', '');
        $('#header_language_en').attr('href', path);
        $('#header_language_uz').attr('href', '/uz/' + new_path);
        $('#header_language_ru').attr('href', '/' + new_path);
    }
    else if (window.location.pathname.indexOf('/uz/') !== -1) {
        let path, new_path;
        path = window.location.pathname;
        new_path = path.replace('/uz/', '');
        $('#header_language_uz').attr('href', path);
        $('#header_language_en').attr('href', '/en/' + new_path);
        $('#header_language_ru').attr('href', '/' + new_path);
    }
    else {
        let path;
        path = window.location.pathname;
        $('#header_language_ru').attr('href', path);
        $('#header_language_en').attr('href', '/en' + path);
        $('#header_language_uz').attr('href', '/uz' + path);
    }
});