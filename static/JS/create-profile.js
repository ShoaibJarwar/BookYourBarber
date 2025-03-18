// Profile Picture Preview
document.getElementById("profilePic").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            let img = document.getElementById("profilePicPreview");
            if (!img) {
                img = document.createElement("img");
                img.id = "profilePicPreview";
                document.getElementById("profileForm").insertBefore(img, document.getElementById("profilePic").nextSibling);
            }
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

// Google Maps API Initialization
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 31.5204, lng: 74.3587 }, // Default location (Lahore)
        zoom: 13
    });

    var marker = new google.maps.Marker({
        position: { lat: 31.5204, lng: 74.3587 },
        map: map,
        draggable: true
    });

    // Update lat/lng when marker is dragged
    google.maps.event.addListener(marker, 'dragend', function(event) {
        document.getElementById("latitude").value = event.latLng.lat().toFixed(6);
        document.getElementById("longitude").value = event.latLng.lng().toFixed(6);
    });

    // Autocomplete for search
    var input = document.getElementById("location");
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    autocomplete.addListener('place_changed', function() {
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            return;
        }

        map.setCenter(place.geometry.location);
        marker.setPosition(place.geometry.location);

        // Set lat/lng values
        document.getElementById("latitude").value = place.geometry.location.lat().toFixed(6);
        document.getElementById("longitude").value = place.geometry.location.lng().toFixed(6);
    });

    // Ensure lat/lng are set before submitting
    document.getElementById("profileForm").addEventListener("submit", function(event) {
        let lat = document.getElementById("latitude").value;
        let lng = document.getElementById("longitude").value;

        if (!lat || !lng) {
            event.preventDefault(); // Stop form submission
            alert("Please select a location on the map.");
        }
    });
}
function initMap() {
      var map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: 31.5204, lng: 74.3587 }, // Default location (Lahore)
          zoom: 13
      });

      var marker = new google.maps.Marker({
          position: { lat: 31.5204, lng: 74.3587 },
          map: map,
          draggable: true
      });

      // Update lat/lng when marker is dragged
      google.maps.event.addListener(marker, 'dragend', function(event) {
          document.getElementById("latitude").value = event.latLng.lat().toFixed(6);
          document.getElementById("longitude").value = event.latLng.lng().toFixed(6);
      });

      // Autocomplete for search
      var input = document.getElementById("location");
      var autocomplete = new google.maps.places.Autocomplete(input);
      autocomplete.bindTo('bounds', map);

      autocomplete.addListener('place_changed', function() {
          var place = autocomplete.getPlace();
          if (!place.geometry) {
              return;
          }

          map.setCenter(place.geometry.location);
          marker.setPosition(place.geometry.location);

          // Set lat/lng values
          document.getElementById("latitude").value = place.geometry.location.lat().toFixed(6);
          document.getElementById("longitude").value = place.geometry.location.lng().toFixed(6);
      });

      // Ensure lat/lng are set before submitting
      document.getElementById("profileForm").addEventListener("submit", function(event) {
          let lat = document.getElementById("latitude").value;
          let lng = document.getElementById("longitude").value;

          if (!lat || !lng) {
              event.preventDefault(); // Stop form submission
              alert("Please select a location on the map.");
          }
      });
  }