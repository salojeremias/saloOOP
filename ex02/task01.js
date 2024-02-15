<html>
<head>
  <title>Leap Year Checker</title>
  <script>
    function isLeapYear(year) {
      if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
        return true;
      } else {
        return false;
      }
    }

    function checkLeapYear() {
      var year = document.getElementById("yearInput").value;
      var resultDiv = document.getElementById("result");

      if (isLeapYear(year)) {
        resultDiv.textContent = "Year " + year + " is a leap year";
      } else {
        resultDiv.textContent = "Year " + year + " is not a leap year";
      }
    }
  </script>
</head>
<body>
  <label for="yearInput">Enter a year:</label>
  <input type="text" id="yearInput"><input/>
  <button onclick="checkLeapYear()">Check year</button>
  <div id="result"></div>
</body>
</html>