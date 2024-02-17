$(document).ready(function() {
  $('#country').change(function() {
    var countryId = $(this).val();
    if (countryId) {
      $.ajax({
        url: '/get_cities/' + countryId,
        type: 'GET',
        success: function(response) {
          var cities = response.cities;
          var options = '<option value="0">Select City</option>';
          for (var i = 0; i < cities.length; i++) {
            options += '<option value="' + cities[i].id + '">' + cities[i].name + '</option>';
          }
          $('#city').html(options);
        }
      });
    } else {
      $('#city').html('<option value="0">Select City</option>');
    }
  });
});

$(document).ready(function() {
  $('#city').change(function() {
    var cityId = $(this).val();
    if (cityId) {
      $.ajax({
        url: '/get_centers/' + cityId,
        type: 'GET',
        success: function(response) {
          var centers = response.centers;
          var options = '<option value="">Select Center</option>';
          for (var i = 0; i < centers.length; i++) {
            options += '<option value="' + centers[i].id + '">' + centers[i].name + '</option>';
          }
          if (centers.length === 0) {
            options = '<option value="">No Centers</option>';
          }
          $('#center').html(options);
        }
      });
    } else {
      $('#center').html('<option value="">Select Center</option>');
    }
  });
});
