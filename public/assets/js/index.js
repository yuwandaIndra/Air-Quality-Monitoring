document.addEventListener("DOMContentLoaded", function () {
  var database = firebase.database();

  var statusPath = "web";
  var statusRef = database.ref(statusPath);

  function statusFormat(id, value, units) {
    const status = value.toFixed(2) + " " + units[id];

    document.getElementById(id).innerHTML = status;
  }

  statusRef.on("value", (snapshot) => {
    const statusData = snapshot.val();
    const units = {
      Hum: "%",
      Temp: "&deg;C",
      Voc: "PPM",
    };

    Object.keys(statusData).map(function (key) {
      statusFormat(key, statusData[key], units);
    });
  });

});
