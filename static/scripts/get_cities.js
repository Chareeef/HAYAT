$(document).ready(function() {
  $('#country').change(function() {
    var countryId = $(this).val();
    if (countryId) {
      $.ajax({
        url: '/get_cities/' + countryId,
        type: 'GET',
        success: function(response) {
          var cities = response.cities;
          var options = '<option value="">Select City</option>';
          for (var i = 0; i < cities.length; i++) {
            options += '<option value="' + cities[i].id + '">' + cities[i].name + '</option>';
          }
          $('#city').html(options);
        }
      });
    } else {
      $('#city').html('<option value="">Select City</option>');
    }
  });
});
