// script.js

document.addEventListener("DOMContentLoaded", function() {
  console.log("JavaScript Loaded");

  


  // Function to handle profile creation
  function createProfile() {
      let name = document.getElementById("name").value;
      let shopName = document.getElementById("shop-name").value;
      let location = document.getElementById("location").value;
      let phone = document.getElementById("phone").value;
      let email = document.getElementById("email").value;
      let services = document.getElementById("services").value;
      let timeSlots = document.getElementById("time-slots").value;
      
      if (name && shopName && location) {
          alert("Profile Created Successfully!");
      } else {
          alert("Please fill in all required fields.");
      }
  }
  
  document.getElementById("create-profile-btn").addEventListener("click", createProfile);
});
