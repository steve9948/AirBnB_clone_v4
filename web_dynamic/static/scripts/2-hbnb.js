//function is called when the DOM is fully loaded.
$(document).ready(init);

//host url for the api
const HOST = '18.209.224.156';

function init() {
  // Object to store selected amenities
  const amenityObj = {};

  // Event handler for changes in amenities checkboxes
  $('.amenities .popover input').change(function () {
    if ($(this).is(':checked')) {
      // Add amenity to the object if checked
      amenityObj[$(this).attr('data-name')] = $(this).attr('data-id');
    } else if ($(this).is(':not(:checked)')) {
      // Remove amenity from the object if unchecked
      delete amenityObj[$(this).attr('data-name')];
    }
    // Update displayed amenities
    const names = Object.keys(amenityObj);
    $('.amenities h4').text(names.sort().join(', '));
  });

  // Check API status
  apiStatus();
}

function apiStatus() {
  // API endpoint URL
  const API_URL = `http://${HOST}:5001/api/v1/status/`;

  // Send GET request to API endpoint
  $.get(API_URL, (data, textStatus) => {
    // Check if request was successful and status is 'OK'
    if (textStatus === 'success' && data.status === 'OK') {
      // Update status indicator
      $('#api_status').addClass('available');
    } else {
      // Update status indicator
      $('#api_status').removeClass('available');
    }
  });
}
