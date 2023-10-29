document.getElementById('backgroundModal').addEventListener('shown.bs.modal', function () {
    console.log("Background selector window opened");
    $.ajax({
        type: 'GET',
        url: '/get_background_images',
        success: function(data) {
            $('#backgroundImagesFill').html(data);
        }
    });
})